from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import hashlib, json, shutil
work=Path(r'C:\Users\user\AppData\Local\Temp\office-upscale-seoyun')
base=Path(r'C:\Users\user\Desktop\건\오피스')
folder=base/'히로인'/'업스케일_서윤_v1'
if folder.exists():
    n=2
    while (base/'히로인'/f'업스케일_서윤_v{n}').exists(): n+=1
    folder=base/'히로인'/f'업스케일_서윤_v{n}'
folder.mkdir(parents=True)
original=Image.open(work/'source.png').convert('RGBA')
target=(original.width*2,original.height*2)
baseline=original.resize(target,Image.Resampling.LANCZOS)
alpha=baseline.getchannel('A')
general=Image.open(work/'seoyun_general_4x_work.png').convert('RGB').resize(target,Image.Resampling.LANCZOS)
sharp=Image.open(work/'seoyun_detail_4x_work.png').convert('RGB').resize(target,Image.Resampling.LANCZOS)
natural=Image.blend(baseline.convert('RGB'),general,0.40).convert('RGBA')
natural.putalpha(alpha)
sharp=sharp.convert('RGBA'); sharp.putalpha(alpha)
shutil.copy2(work/'source.png',folder/'한서윤_MASTER_업스케일전.png')
natural.save(folder/'한서윤_MASTER_2x_원화보존.png')
sharp.save(folder/'한서윤_MASTER_2x_선명형.png')
shutil.copy2(work/'seoyun_general_4x_work.png',folder/'한서윤_MASTER_4x_작업본.png')
fontpath=base/'RenPy_게임'/'game'/'fonts'/'SourceHanSansLite.ttf'
font=ImageFont.truetype(str(fontpath),28)
small=ImageFont.truetype(str(fontpath),23)
sheet=Image.new('RGB',(1860,1330),'#f0ede7'); draw=ImageDraw.Draw(sheet)
labels=['원본 일반 확대','AI 2배 - 원화 보존형','AI 2배 - 선명형']
for i,(label,im) in enumerate(zip(labels,[baseline,natural,sharp])):
    x=20+i*620
    draw.text((x,15),label,font=font,fill='#26343b')
    for roi,y,size in [((720,0,1320,540),65,(600,540)),((660,520,1460,1200),650,(600,510))]:
        crop=im.crop(roi); crop.thumbnail(size,Image.Resampling.LANCZOS)
        bg=Image.new('RGBA',size,'#ddd8cf')
        bg.alpha_composite(crop,((size[0]-crop.width)//2,(size[1]-crop.height)//2))
        sheet.paste(bg.convert('RGB'),(x,y))
    draw.text((x,1210),'얼굴 / 머리 / 옷감 확대 비교',font=small,fill='#59656b')
draw.text((20,1270),'같은 원본 - 같은 구도 - 원본 투명도 유지 - 원본 MASTER 별도 보관',font=small,fill='#59656b')
sheet.save(folder/'서윤_업스케일_비교.png')
source_hash=hashlib.sha256((work/'source.png').read_bytes()).hexdigest()
current_hash=hashlib.sha256((base/'히로인'/'한서윤_seoyun_MASTER.png').read_bytes()).hexdigest()
assert source_hash==current_hash, 'Master changed during processing'
report={'source_sha256':source_hash,'source_unchanged':True,'original_size':list(original.size),'output_size':list(target),'cost':'local / no cloud credits','device':'RTX 3060 Laptop Vulkan device 1','raw_models':['realesrgan-x4plus','realesrgan-x4plus-anime'],'natural_processing':'general 4x -> Lanczos 2x; original Lanczos RGB 60% + SR RGB 40%; original resized alpha','sharp_processing':'anime 4x -> Lanczos 2x; original resized alpha','checks':{}}
for name in ['한서윤_MASTER_2x_원화보존.png','한서윤_MASTER_2x_선명형.png']:
    im=Image.open(folder/name).convert('RGBA')
    exact=np.array_equal(np.asarray(im.getchannel('A')),np.asarray(alpha))
    assert im.size==target and exact
    report['checks'][name]={'size':list(im.size),'alpha_matches_original_resized':exact,'corner_alpha':im.getpixel((0,0))[3]}
(folder/'검증기록.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(folder/'README.md').write_text('''# 한서윤 MASTER 업스케일 비교

사용자가 선택한 폴더의 MASTER(하이힐 버전)를 기준으로 처리했다. 원본 파일과 게임 실행 에셋은 교체하지 않았다.

- 원본: 1024 x 1535.
- 사용용 2배 확대본: 2048 x 3070 PNG, 원본 투명도 확대 후 그대로 적용.
- 원화 보존형: Real-ESRGAN 일반 모델 4배 결과를 2배로 줄인 뒤 원본 일반 확대 RGB 60%, AI 확대 RGB 40%로 혼합했다. 부드러운 얼굴·머리·옷감 표현 보존을 우선한다.
- 선명형: Real-ESRGAN 애니 모델 4배 결과를 2배로 줄였다. 선이 더 뚜렷하지만 원본보다 그림체가 단순해질 수 있다.
- 4배 작업본: 4096 x 6140. 처리 중간 원본으로 보관하며 기본 게임용 추천은 2배 원화 보존형이다.

무료 로컬 GPU 처리이며 ADetailer, 얼굴 복원 모델, Stable Diffusion 재생성은 사용하지 않았다. 고해상도 디테일은 추정된 결과이므로 비교 이미지를 보고 선택한다.

도구: https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan
배포: https://github.com/xinntao/Real-ESRGAN/releases/tag/v0.2.5.0

원본 보관 사본, 두 확대본, 확대 비교 이미지와 검증 기록을 이 폴더에 저장했다. 원본의 해시 동일, 두 2배 파일의 크기와 원본 대비 투명도 동일을 검증했다.
''',encoding='utf-8')
# Keep the portable upscaler for later characters, with the official license.
tool_src=Path(r'C:\Users\user\AppData\Local\Temp\office-upscale-tools\realesrgan-20220424')
tool_dest=base/'도구'/'realesrgan-ncnn-vulkan-20220424'
if not tool_dest.exists():
    tool_dest.mkdir(parents=True)
    for name in ['realesrgan-ncnn-vulkan.exe','vcomp140.dll','README_windows.md']:
        shutil.copy2(tool_src/name,tool_dest/name)
    shutil.copytree(tool_src/'models',tool_dest/'models')
shutil.copy2(Path(r'C:\Users\user\AppData\Local\Temp\office-upscale-finalize.py'),folder/'비교본_생성기록.py')
print(json.dumps({'output_folder':str(folder),'source_unchanged':True,'dimensions':target,'alpha_check':'passed'},ensure_ascii=False))

from pathlib import Path
import shutil

root=Path(r'C:\Users\user\Desktop\건\오피스')
src=Path(__file__).parent
docs=root/'기획문서_v1'
name='32_첫주스토리와휴대폰연결.md'
shutil.copy2(src/name,docs/name)

p=root/'README.md'; s=p.read_text(encoding='utf-8')
s=s.replace('리아 첫날, 네 인물의 대사 소개','첫 주 1~5일차, 네 인물의 발견 사건·목표 합의')
s=s.replace('현재 플레이는 첫날까지이고, 2일 이후 본편은 제작 예정입니다.','현재 플레이는 5일차까지이고, 6일 이후 본편은 제작 예정입니다. 히로인 루트 선택 계획은 15일차 저녁입니다.')
s=s.replace('캐릭터 사진은 현재 생성하지 않았습니다.','단계 사진은 이번 작업에서 생성하지 않았고, 프로필은 사용자 제공 4개 사진을 적용했습니다.')
s += '\n첫 주 구현: [32 스토리와 휴대폰 연결](기획문서_v1/'+name+'). 실제 화면: [첫 주 실행 미리보기](첫주_실행미리보기/README.md).\n'
p.write_text(s,encoding='utf-8')

p=root/'RenPy_게임/README.md'
p.write_text('''# 퇴근 후, 우리 — Ren’Py 첫 주 버전

상위 폴더의 `RenPy_게임시작.bat`를 실행한다. 무료 공식 SDK가 `도구/renpy-8.5.3-sdk`에 들어 있다. 1920×1080 기준이며 창 크기는 엔진에서 조절한다.

현재 플레이: 첫 출근 → 2일차 서윤 발견 → 3일차 리아 발견 → 4일차 유진 발견 → 5일차 팀 목표 합의. 하루 결과에서 다음 날로 이어 간다. 6~30일 본편과 개별·복수 루트는 제작 예정이다. 히로인 선택은 기획상 15일차 저녁이다.

네 사람의 선택형 문자, 실제 발신자 프로필의 전화, 원자료 약속 이행·변경, 점심 선택과 완료 일정, 저장·불러오기, 기록·자동 진행·롤백을 제공한다. 문자 전송·읽음·타이핑 연출을 유지한다. 자유 입력 채팅이나 음성 통화는 이번 범위에 포함하지 않는다.

사용자 승인 MASTER와 프로필, 배경을 사용한다. 새 표정이나 사진을 만들지 않았다. 현재 전신 표시가 분리 파츠 리깅이나 Live2D 애니메이션은 아니다. 사진 확대·저장표시·숨기기·수신 범위와 단계 조건은 기존 기능을 유지한다.

배경 원본은 상위 `backgrounds`와 `backgrounds_styled`, 실행용은 `game/images/bg`다. 교체 후 `배경동기화.ps1`로 갱신한다.

첫날은 `game/story_day01.rpy`, 2~5일차는 `game/story_week01.rpy`, 새 메시지·일정·사건 처리는 `game/week_phone.rpy`다. 상세 구현·검수는 [32 문서](../기획문서_v1/32_첫주스토리와휴대폰연결.md)를 참조한다.
''',encoding='utf-8')

p=docs/'23_30일사건표와분기제작.md';s=p.read_text(encoding='utf-8').replace('1일만 실제 Ren’Py 플레이로 구현했고 나머지는 제작 설계다.','2026-10-02 기준 1~5일차를 실제 Ren’Py 플레이로 구현했고, 6일차 이후는 제작 설계다. 첫 주의 구체적 선택·문자·전화·일정 연결은 [32](32_첫주스토리와휴대폰연결.md)를 따른다.');p.write_text(s,encoding='utf-8')
p=docs/'09_게임시스템.md';s=p.read_text(encoding='utf-8');s += '\n## 18. 첫 주 구현 현황 — 2026-10-02\n\n현재 1~5일차를 구현했다. SY01·RI01·YJ01의 단계1과 C01, 대상별 답장 보상 상한, 첫 주 점심 보상 2회 상한, 약속 이행·사전 조정·기록을 연결했다. 지현 JH01은 6일차이며, 단계2 이후와 루트·교제 전환은 아직 미구현이다. 위의 첫날 구현 설명은 당시 기록이며 현재 상세 범위는 [32](32_첫주스토리와휴대폰연결.md)를 기준으로 한다.\n';p.write_text(s,encoding='utf-8')
p=docs/'README.md';s=p.read_text(encoding='utf-8');s += '\n- [29_휴대폰_실시간동작](29_휴대폰_실시간동작.md)\n- [30_배경교체_휴대폰정렬](30_배경교체_휴대폰정렬.md)\n- [31_휴대폰외형_메신저](31_휴대폰외형_메신저.md)\n- [32_첫주스토리와휴대폰연결](32_첫주스토리와휴대폰연결.md) — 현재 1~5일차 구현과 다음 날 연결.\n';p.write_text(s,encoding='utf-8')
print('First-week docs and launch guide updated.')

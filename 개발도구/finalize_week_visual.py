from pathlib import Path

g=Path(r'C:\Users\user\Desktop\건\오피스\RenPy_게임\game')
for relative in ['week_phone.rpy','story_week01.rpy','tests/week_test.rpy']:
    p=g/relative
    s=p.read_text(encoding='utf-8').replace(' · ',' / ')
    if relative == 'week_phone.rpy':
        s=s.replace('return promises[0].replace(" / "," / ")','return promises[0].replace(" · "," / ")')
    elif relative == 'story_week01.rpy':
        for who,key in [('seoyun','"d2_sy"'),('ria','"d3_ri"'),('yujin','"d4_yj"')]:
            needle='    call screen phone(mode="story",initial_contact="'+who+'",required_reply='+key+')'
            s=s.replace(needle,needle+'\n    $ clock = "09:30"')
    else:
        s=s.replace('        screenshot ', '        pause 0.6\n        screenshot ')
    p.write_text(s,encoding='utf-8')
print('New labels and timestamps corrected; screenshots wait for phone entrance.')

from pathlib import Path
from datetime import datetime
import shutil

root = Path(r'C:\Users\user\Desktop\건\오피스')
game = root / 'RenPy_게임/game'
source = Path(__file__).parent
backup = root / '변경백업' / ('첫주구현_' + datetime.now().strftime('%Y%m%d_%H%M%S'))
backup.mkdir(parents=True, exist_ok=True)
for name in ['state.rpy','phone_live.rpy','screens.rpy','story_day01.rpy']:
    shutil.copy2(game / name, backup / name)

week = (source / 'week_phone.rpy').read_text(encoding='utf-8').replace(']},\n    message_data[', ']}\n    message_data[')
(game / 'week_phone.rpy').write_text(week,encoding='utf-8')
shutil.copy2(source / 'story_week01.rpy', game / 'story_week01.rpy')

p = game / 'state.rpy'
s = p.read_text(encoding='utf-8')
begin = s.index('    def send_message(key):')
end = s.index('    def photo_allowed(',begin)
s = s[:begin] + '''    def send_message(key):
        if key in phone_events: return
        phone_events.append(key)
        item = message_data[key]
        who = item.get("who", "ria")
        for text in item["texts"]:
            phone_messages.append({"who":who,"out":False,"text":text,"time":item["time"],"event":key,"day":day})
        phone_unread[who] = phone_unread.get(who,0) + len(item["texts"])
        if item.get("photo"):
            if "ria_cafe" not in photo_received: photo_received.append("ria_cafe")
            phone_messages.append({"who":who,"out":False,"text":"카페 사진을 보냈어요.","time":item["time"],"photo":"ria_cafe"})

    def reply_message(key, choice):
        if key in phone_replied or key in phone_expired or phone_pending: return
        phone_replied.append(key)
        who = message_data[key].get("who","ria")
        message_id = "reply:" + key
        phone_messages.append({"who":who,"out":True,"text":choice["text"],"time":clock,"delivery":"sending","id":message_id,"day":day})
        delays = {"ria":(1.2,3.8),"seoyun":(1.8,4.5),"yujin":(2.0,4.8),"jihyun":(1.4,3.6)}
        typing_at, arrive_at = delays[who]
        phone_pending.append({"id":message_id,"who":who,"text":choice["response"],"time":clock,"elapsed":0.0,"typing_at":typing_at,"arrive_at":arrive_at})
        reward_id = "%s:%s" % (day,who)
        if reward_id not in reply_reward_days:
            reply_reward_days.append(reward_id)
            apply_person_effects(who,{"affection":1})
        if choice.get("plan"): flags["lunch_plan"] = choice["plan"]
        flags.update(choice.get("set",{}))
        renpy.retain_after_load()
        renpy.restart_interaction()

''' + s[end:]
# Screen choices and schedule changes must restore together, including daily reward guards.
s = s.replace('global photo_saved, photo_hidden, phone_pending, phone_messages, phone_unread','global photo_saved, photo_hidden, phone_pending, phone_messages, phone_unread\n        global phone_replied, reply_reward_days, flags, people, week_schedule, promises, phone_events, phone_expired, completed_events')
needle = '        photo_hidden = list(saved.get("photo_hidden",photo_hidden))'
s = s.replace(needle,needle + '''
        phone_replied = list(saved.get("phone_replied",phone_replied))
        reply_reward_days = list(saved.get("reply_reward_days",reply_reward_days))
        phone_events = list(saved.get("phone_events",phone_events))
        phone_expired = list(saved.get("phone_expired",[]))
        completed_events = list(saved.get("completed_events",[]))
        flags = dict(saved.get("flags",flags))
        week_schedule = list(saved.get("week_schedule",[]))
        promises = list(saved.get("promises",promises))
        people = saved.get("people",people)
''')
p.write_text(s,encoding='utf-8')

p = game / 'phone_live.rpy'
s = p.read_text(encoding='utf-8').replace('return who == "ria" and any(key not in phone_replied and message_data[key].get("reply") for key in phone_events)','return current_reply_key(who) is not None')
p.write_text(s,encoding='utf-8')

p = game / 'screens.rpy'
s = p.read_text(encoding='utf-8')
s = s.replace('screen phone(mode=None):','screen phone(mode=None, initial_contact=None, required_reply=None):')
s = s.replace('default contact = "ria"','default contact = initial_contact or phone_focus')
s = s.replace('sensitive not phone_pending style "phone_equal_button"','sensitive (not phone_pending and (required_reply is None or required_reply in phone_replied)) style "phone_equal_button"')
old = '''                        for key in phone_events:
                            if contact == "ria" and key not in phone_replied and message_data[key].get("reply"):
                                text "빠른 답장" size 17 color "#899499"
                                for option in message_data[key]["reply"]:
                                    textbutton option["text"] action Function(reply_message,key,option) sensitive not phone_pending style "ui_light_button" text_size 21 xfill True padding (16,14)'''
new = '''                        $ reply_key = current_reply_key(contact)
                        if reply_key:
                            text "빠른 답장" size 17 color "#899499"
                            for option in message_data[reply_key]["reply"]:
                                textbutton option["text"] action Function(reply_message,reply_key,option) sensitive not phone_pending style "ui_light_button" text_size 21 xfill True padding (16,14)
                        elif required_reply and required_reply not in phone_replied:
                            text "답장을 보낼 상대: " + names[message_data[required_reply].get("who","ria")] size 19 color "#28636A"'''
assert old in s
s = s.replace(old,new)
s = s.replace('add ui_phone_avatar("ria",108)','add ui_phone_avatar(ring_who,108)').replace('text "강리아" size 36','text names[ring_who] size 36')
start = s.index('                elif tab == "calls":')
end = s.index('                elif tab == "album":',start)
block = s[start:end]
block = block.replace('                    vbox:\n                        xpos 0 ypos 280 spacing 20 xsize 516','                    viewport:\n                        xpos 0 ypos 280 xsize 516 ysize 500 mousewheel True draggable True\n                        vbox:\n                            spacing 20 xsize 516')
lines = block.splitlines(True)
vbox_index = next(i for i,l in enumerate(lines) if 'spacing 20 xsize' in l)
for i in range(vbox_index+1,len(lines)): lines[i]='    '+lines[i]
s = s[:start] + ''.join(lines) + s[end:]
start = s.index('                elif tab == "calendar":')
end = s.index('                else:',start)
s = s[:start] + '''                elif tab == "calendar":
                    viewport:
                        xpos 0 ypos 280 xsize 516 ysize 500 mousewheel True draggable True
                        vbox:
                            spacing 14 xsize 516
                            text "약속과 기록" size 29 color "#26343B"
                            for item in week_schedule:
                                frame:
                                    background ui_panel("incoming") xsize 516 padding (16,12)
                                    vbox:
                                        spacing 6
                                        text "DAY %02d / %s / %s" % (item["day"],item["time"],item["status"]) size 19 color "#28636A"
                                        text names[item["who"]] + " · " + item["title"] size 22 xmaximum 470
                            for item in promises:
                                frame:
                                    background ui_panel("incoming") xsize 516
                                    text item.replace(" · "," / ") size 22 xmaximum 470
                            if not promises and not week_schedule:
                                text "아직 정한 약속이 없어요.\\n대화에서 다음 만남을 정해 보세요." size 24 color "#899499" line_spacing 8
''' + s[end:]
start = s.index('screen day_result():')
s = s[:start] + '''screen day_result():
    modal True
    zorder 80
    add Solid("#121D24D9")
    frame:
        align (0.5,0.5) xsize 1150 padding (50,40)
        vbox:
            spacing 22
            text "DAY %02d / AFTER HOURS" % day size 24 color "#916641" kerning 2
            text ("첫 주를 마치며" if day == 5 else "내일 이어질 이야기") size 54
            grid 2 2:
                spacing 18 xfill True
                for who in names:
                    text "%s  /  호감 %d · 신뢰 %d" % (names[who],people[who]["affection"],people[who]["trust"]) size 25
            text "프로젝트 " + str(stats["project"]) + " / 스트레스 " + str(stats["stress"]) size 27 color "#899499"
            frame:
                background ui_panel("incoming") xfill True
                text "다음 약속: " + next_meeting_text() size 24 xmaximum 990
            text ("첫 주 플레이는 여기까지입니다. 6일차부터는 제작 예정입니다.\\n히로인 루트는 15일차 저녁에 선택합니다." if day == 5 else "오늘의 선택과 연락은 다음 날에도 이어집니다.") size 24 color "#899499"
            hbox:
                spacing 16
                if day < 5:
                    textbutton "%d일차로 계속" % (day+1) action Return("continue") style "ui_action_button"
                textbutton "휴대폰 확인" action Show("phone") style "ui_light_button"
                textbutton "저장" action ShowMenu("save") style "ui_light_button"
                textbutton "제목으로" action Return("title") style "ui_light_button"
'''
p.write_text(s,encoding='utf-8')

p = game / 'story_day01.rpy'
s = p.read_text(encoding='utf-8').replace('    call screen day_result\n    return','    call screen day_result\n    if _return == "continue":\n        jump day02\n    return')
p.write_text(s,encoding='utf-8')
print('Installed first-week story and phone integration. Backup:', backup)

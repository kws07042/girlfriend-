screen main_menu():
    tag menu
    add office_bg("evening")
    add Solid("#121D24BA")
    add Solid("#121D2466") xsize 1000
    vbox:
        xpos 155 ypos 178 spacing 22
        text "AFTER HOURS / MOMENTWORKS" size 24 color "#D6B18A" kerning 3
        null height 24
        text "퇴근 후,\n우리" size 112 color "#F8F4EE" line_spacing 8
        text "회사에서 시작해, 서로의 일상으로." size 30 color "#D8DEDF"
        null height 45
        textbutton "첫날 시작" action Start() style "ui_action_button" xsize 410
        textbutton "이어하기" action ShowMenu("load") style "ui_light_button" xsize 410
        hbox:
            spacing 24
            textbutton "설정" action ShowMenu("preferences") style "ui_quick_button"
            textbutton "종료" action Quit(confirm=True) style "ui_quick_button"
    text "A STORY ABOUT THE MOMENTS BETWEEN" xpos 158 ypos 988 size 20 color "#B5C1C5" kerning 2

screen say(who, what):
    zorder 20
    window:
        id "window"
        background ui_panel("glass")
        xpos 96 ypos 824 xsize 1728 ysize 232 padding (38,28)
        vbox:
            spacing 12
            hbox:
                spacing 18
                if who:
                    text who id "who" size 30 color ui_colors.get(ui_speaker,"#D6B18A")
                else:
                    text "AFTER HOURS" size 22 color "#9CACB4" kerning 2
            text what id "what" size 31 color "#F8F4EE" line_spacing 5 xmaximum 1600
    add Solid("#D6B18A") xpos 134 ypos 824 xsize 72 ysize 3
    if not renpy.get_screen("choice"):
        text "다음" xpos 1680 ypos 970 size 20 color "#D6B18A"
    use quick_menu

screen choice(items):
    modal True
    zorder 25
    vbox:
        xpos 150 yalign 0.50 spacing 14 xsize 810
        at ui_reveal(duration=0.0 if persistent.reduce_motion else 0.22, distance=0 if persistent.reduce_motion else 10)
        frame:
            background ui_panel("glass") padding (24,15) xsize 810
            vbox:
                spacing 4
                text "YOUR MOMENT" size 20 color "#E2C19E" kerning 3
                text "어떻게 답할까요?" size 30 color "#FFFFFF"
        null height 8
        for item in items:
            button:
                action item.action
                style "ui_light_button" xfill True padding (28,24)
                hbox:
                    spacing 22
                    text "%02d" % (items.index(item)+1) size 23 color "#A47A52" yalign 0.5
                    text item.caption size 27 color "#26343B" xmaximum 690 yalign 0.5

screen quick_menu():
    zorder 30
    hbox:
        xpos 1190 ypos 1024 spacing 5
        textbutton "기록" action ShowMenu("history") style "ui_quick_button"
        textbutton "저장" action ShowMenu("save") style "ui_quick_button"
        textbutton "불러오기" action ShowMenu("load") style "ui_quick_button"
        textbutton "자동" action Preference("auto-forward","toggle") style "ui_quick_button"
        textbutton "설정" action ShowMenu("preferences") style "ui_quick_button"

screen office_hud():
    zorder 35
    if not main_menu and not renpy.get_screen("day_result"):
        frame:
            xpos 66 ypos 36 background ui_panel("glass") padding (24,15)
            hbox:
                spacing 24
                vbox:
                    spacing 2
                    text "DAY [day:02d] / [clock]" size 23 color "#D6B18A"
                    text place.replace(" · "," / ") size 22 color "#F1ECE5"
                add Solid("#60727A88") xsize 1 ysize 48
                vbox:
                    spacing 2
                    text chapter size 23 color "#F1ECE5"
                    text "MOMENTWORKS" size 17 color "#A6B5BB" kerning 1
        hbox:
            xpos 1500 ypos 40 spacing 12
            textbutton "관계" action Show("relationship_panel") style "ui_light_button"
            textbutton "휴대폰" action Show("phone") sensitive not ui_call_contact style "ui_action_button"
        key "K_p" action (NullAction() if ui_call_contact else Show("phone"))

screen phone(mode=None, initial_contact=None, required_reply=None):
    modal True
    zorder 110
    default tab = "calls" if ring_pending else "messages"
    default contact = ring_who if ring_pending else (initial_contact or phone_focus)
    default message_scroll = PhoneChatAdjustment()
    default selected_reply_key = None
    $ message_scroll.select_contact(contact)
    if ring_pending and tab != "calls":
        timer 0.01 action SetScreenVariable("tab", "calls")
    if tab == "messages" and phone_unread.get(contact):
        timer 0.1 action Function(phone_mark_read,contact)
    add Solid("#0D172278")
    key "K_ESCAPE" action (NullAction() if mode else Hide("phone"))
    key "K_p" action (NullAction() if mode else Hide("phone"))
    fixed:
        xpos 644 ypos 20 xsize 632 ysize 1040
        at ui_phone_enter(duration=0.0 if persistent.reduce_motion else 0.42, distance=0 if persistent.reduce_motion else 1100)
        frame:
            xpos 22 ypos 18 xsize 588 ysize 1004
            background Frame("images/ui_v6/screen.png",60,60) padding (36,24)
            fixed:
                text clock xpos 4 ypos 0 size 21 bold True color "#26343B"
                hbox:
                    xpos 516 xanchor 1.0 ypos 0 spacing 8
                    text "LTE" size 18 color "#68757B" yalign 0.5
                    add "images/ui_v2/battery.png" yalign 0.5
                add "images/ui_v2/camera.png" xpos 245 ypos -5
                fixed:
                    xpos 0 ypos 48 xsize 516 ysize 44
                    text "대화" size 22 color "#28636A" ypos 6
                    textbutton "수신 설정" xpos 260 action SetScreenVariable("tab","settings") style "phone_equal_button" xsize 126 ysize 44 text_size 17
                    if mode:
                        textbutton "계속" xpos 430 action Return("continue") sensitive (not ring_pending and not phone_pending and (required_reply is None or required_reply in phone_replied or phone_reply_has_expired(required_reply))) style "phone_equal_button" xsize 86 ysize 44 text_size 21
                    else:
                        textbutton "닫기" xpos 430 action Hide("phone") style "phone_equal_button" xsize 86 ysize 44 text_size 21
                fixed:
                    xpos 0 ypos 102 xsize 516 ysize 96
                    add ui_phone_avatar(contact,96)
                    vbox:
                        xpos 114 ypos 8 spacing 3
                        text (names[contact] if tab=="messages" else {"calls":"통화","album":"사진","calendar":"일정","settings":"수신 설정"}[tab]) size 29 bold True color "#26343B"
                        text phone_roles[contact] size 17 color "#899499"
                        text ("입력 중" if phone_is_typing(contact) else "대화 가능") size 15 color "#28636A"
                    button:
                        xpos 456 ypos 20 xsize 60 ysize 56
                        background ui_panel("incoming") padding (0,0)
                        action SetScreenVariable("tab","calls")
                        add "images/ui_v6/calls_active.png" align (0.5,0.5)
                if tab in ("messages","settings"):
                    grid 4 1:
                        xpos 0 ypos 200 xsize 516 spacing 4
                        for who in names:
                            fixed:
                                xsize 126 ysize 64
                                textbutton names[who][1:] action [SetScreenVariable("contact",who), SetScreenVariable("selected_reply_key",None), Function(phone_mark_read,who)] selected contact==who style "phone_equal_button" xsize 126 ysize 48 ypos 14 text_size 21
                                if tab == "messages":
                                    use phone_contact_marker(who, required_reply)
                add Solid("#D9DCD7") xpos 0 ypos 267 xsize 516 ysize 1
                if tab == "messages":
                    viewport:
                        id "message_view"
                        xpos 0 ypos 280 xsize 516 ysize (330 if phone_has_replies(contact) else 500)
                        mousewheel True draggable True yadjustment message_scroll
                        vbox:
                            spacing 15 xsize 516
                            if not any(msg["who"]==contact for msg in phone_messages):
                                null height 75
                                text "아직 도착한 메시지가 없어요." size 23 color "#899499" xalign 0.5
                            $ contact_messages = [msg for msg in phone_messages if msg["who"] == contact]
                            for index, msg in enumerate(contact_messages):
                                if index == 0 or msg.get("day",1) != contact_messages[index-1].get("day",1):
                                    text "DAY %02d" % msg.get("day",1) size 16 color "#899499" xalign 0.5
                                if msg["who"] == contact:
                                    vbox:
                                        xalign (1.0 if msg["out"] else 0.0)
                                        spacing 5 xmaximum 440
                                        frame:
                                            background ui_panel("outgoing" if msg["out"] else "incoming")
                                            padding (18,14) xmaximum 440
                                            vbox:
                                                spacing 10
                                                text msg["text"] size 24 color ("#FFFFFF" if msg["out"] else "#26343B") xmaximum 400 line_spacing 3
                                                if msg.get("photo") and msg["photo"] not in photo_hidden:
                                                    if renpy.loadable(photo_path(msg["photo"])):
                                                        button:
                                                            action Show("phone_photo",token=msg["photo"])
                                                            background None padding (0,0)
                                                            add Transform(photo_path(msg["photo"]),xysize=(340,172),fit="cover")
                                                    textbutton "사진 열기" action Show("phone_photo",token=msg["photo"]) style "ui_chip_button" text_size 21
                                        text phone_message_status(msg) size 15 color "#929B9B" xalign (1.0 if msg["out"] else 0.0)
                                        if not msg["out"] and msg.get("event") and phone_reply_has_expired(msg["event"]) and msg["text"] == message_data[msg["event"]]["texts"][-1]:
                                            text "답장 시간이 지난 약속이에요" size 15 color "#899499"
                            if phone_is_typing(contact):
                                use phone_typing(contact)
                            null height 14
                    if not message_scroll.follow_latest and message_scroll.range > 0:
                        textbutton "최신 메시지" xpos 360 ypos (574 if phone_has_replies(contact) else 744) action Function(message_scroll.latest) style "ui_light_button" text_size 18 padding (12,8)
                    vbox:
                        xpos 0 ypos 620 spacing 6 xsize 516
                        $ reply_key = phone_selected_reply(contact, selected_reply_key, required_reply)
                        if reply_key:
                            hbox:
                                spacing 12
                                text "DAY %02d 메시지에 답장" % phone_event_day(reply_key) size 17 color "#899499" yalign 0.5
                                if len(phone_reply_keys(contact)) > 1:
                                    textbutton "다른 미답장 (%d)" % len(phone_reply_keys(contact)) action SetScreenVariable("selected_reply_key",phone_next_reply(contact,reply_key)) sensitive not phone_pending style "phone_equal_button" xsize 190 ysize 26 text_size 16
                            for option in phone_reply_options(reply_key):
                                textbutton option["text"] action Function(reply_message,reply_key,option) sensitive not phone_pending style "ui_light_button" text_size 20 xfill True padding (16,10)
                elif tab == "calls":
                    viewport:
                        xpos 0 ypos 280 xsize 516 ysize 500 mousewheel True draggable True
                        vbox:
                            spacing 20 xsize 516
                            if ring_pending:
                                null height 32
                                add ui_phone_avatar(ring_who,108) xalign 0.5
                                text names[ring_who] size 36 color "#26343B" xalign 0.5
                                text "전화가 왔어요" size 23 color "#899499" xalign 0.5
                                null height 30
                                textbutton "받기" action (Return("accept") if mode else Notify("현재 대화를 마친 뒤 전화를 확인하세요.")) style "ui_action_button" xfill True
                                textbutton "지금은 받지 않기" action (Return("missed") if mode else Notify("현재 대화를 마친 뒤 선택하세요.")) style "ui_light_button" xfill True
                            for item in phone_calls:
                                frame:
                                    background ui_panel("incoming")
                                    text item.replace(" · "," / ") size 22
                            if not ring_pending and not phone_calls:
                                text "아직 통화 기록이 없어요." size 24 color "#899499"
                elif tab == "album":
                    viewport:
                        xpos 0 ypos 280 xsize 516 ysize 470 mousewheel True draggable True
                        vbox:
                            spacing 18
                            for token in photo_received:
                                if token not in photo_hidden:
                                    button:
                                        action Show("phone_photo",token=token)
                                        style "ui_light_button" xsize 465
                                        vbox:
                                            spacing 10
                                            if renpy.loadable(photo_path(token)):
                                                add Transform(photo_path(token),xysize=(418,208),fit="cover")
                                            text token size 21
                                            text ("내 앨범에 저장됨" if token in photo_saved else "대화에서만 보관") size 18 color "#899499"
                            if not photo_received:
                                text "함께 나눈 사진이 여기에 모여요." size 24 color "#899499"
                elif tab == "calendar":
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
                                        text names[item["who"]] + " / " + item["title"] size 22 xmaximum 470
                            for item in promises:
                                frame:
                                    background ui_panel("incoming") xsize 516
                                    text item.replace(" · "," / ") size 22 xmaximum 470
                            if not promises and not week_schedule:
                                text "아직 정한 약속이 없어요.\n대화에서 다음 만남을 정해 보세요." size 24 color "#899499" line_spacing 8
                else:
                    vbox:
                        xpos 0 ypos 280 spacing 10 xsize 516
                        text "사진 수신 범위" size 29
                        text "받고 싶은 범위를 선택하세요.\n관계 조건을 충족하면 사진이 도착해요." size 19 color "#899499"
                        null height 8
                        for cap,title in [(0,"사진 받지 않기"),(1,"1 / 일상 셀카"),(2,"2 / 사복 데이트"),(3,"3 / 옷을 입은 가슴골 셀카"),(4,"4 / 연인 드레스 사진")]:
                            textbutton title action Function(set_photo_permission,contact,cap) selected people[contact]["photo_cap"]==cap style "ui_light_button" text_size 20 xfill True padding (18,10)
                        text "현재 허용: " + str(people[contact]["photo_cap"]) + "단계" size 23 color "#916641"
                        text "3단계부터는 사적 사진 수신 동의입니다.\n언제든 범위를 다시 바꿀 수 있어요." size 20 color "#899499"
                if tab == "messages":
                    fixed:
                        xpos 0 ypos 798 xsize 516 ysize 58
                        frame:
                            xpos 0 xsize 448 ysize 54 background ui_panel("incoming") padding (16,12)
                            text ("답장을 기다리는 중…" if phone_pending else "메시지 보내기") size 18 color "#899499" yalign 0.5
                        frame:
                            xpos 462 xsize 54 ysize 54 background ui_panel("outgoing") padding (0,0)
                            add "images/ui_v6/send_white.png" align (0.5,0.5)
                add Solid("#D9DCD7") xpos 0 ypos 870 xsize 516 ysize 1
                grid 4 1:
                    xpos 0 ypos 884 xsize 516 spacing 4
                    for title,key in [("문자","messages"),("통화","calls"),("사진","album"),("일정","calendar")]:
                        button:
                            action SetScreenVariable("tab",key)
                            background None hover_background ui_panel("subtle")
                            padding (0,0) xsize 126 ysize 72
                            fixed:
                                xsize 126 ysize 72
                                if tab == key:
                                    add Solid("#28636A") xpos 28 ypos 0 xsize 70 ysize 3
                                add ("images/ui_v6/" + key + ("_active" if tab==key else "") + ".png") xalign 0.5 ypos 10
                                text title size 19 color ("#28636A" if tab==key else "#899499") xalign 0.5 ypos 46
        add "images/ui_v6/device_frame.png"

screen phone_photo(token):
    modal True
    zorder 130
    add Solid("#121D24F5")
    text "SHARED MOMENTS" xpos 110 ypos 48 size 25 color "#D6B18A" kerning 2
    if renpy.loadable(photo_path(token)):
        add Transform(photo_path(token),xysize=(1540,800),fit="contain") align (0.5,0.47)
    else:
        text "사진 파일이 아직 준비되지 않았어요." align (0.5,0.5) color "#F8F4EE"
    hbox:
        align (0.5,0.92) spacing 16
        textbutton ("저장 취소" if token in photo_saved else "내 앨범에 저장") action Function(toggle_photo_saved,token) style "ui_action_button"
        textbutton "숨기기" action [Function(hide_photo,token),Hide("phone_photo")] style "ui_light_button"
        textbutton "닫기" action Hide("phone_photo") style "ui_light_button"

screen relationship_panel():
    modal True
    zorder 120
    add Solid("#121D24CA")
    frame:
        align (0.5,0.5) xsize 1200 padding (50,38)
        vbox:
            spacing 24
            text "PEOPLE & MOMENTS" size 22 color "#916641" kerning 2
            text "조금씩 가까워지는 사이" size 45
            if day <= 5:
                text "이번 주는 네 사람을 함께 알아가는 시간이에요." size 23 color "#899499"
            elif route_intent == "team":
                text "지금은 팀과 나의 일에 집중하고 있어요." size 23 color "#899499"
            elif route_intent in names:
                text "다음에 더 깊게 알아갈 사람: " + names[route_intent] size 23 color "#899499"
            elif focus_interest in names:
                text "지금 조금 더 알아보고 싶은 사람: " + names[focus_interest] size 23 color "#899499"
            else:
                text "아직 마음을 정하지 않고 이야기하는 중이에요." size 23 color "#899499"
            hbox:
                spacing 22
                for who in names:
                    frame:
                        background ui_panel("incoming") xsize 250
                        vbox:
                            spacing 13
                            add ui_avatar(who,76)
                            text names[who] size 29
                            text "호감 " + str(people[who]["affection"]) + " / 신뢰 " + str(people[who]["trust"]) size 22 color "#899499"
                            bar value people[who]["trust"] range 100 xsize 190
            text "프로젝트 " + str(stats["project"]) + " / 스트레스 " + str(stats["stress"]) size 25 color "#899499"
            textbutton "닫기" action Hide("relationship_panel") style "ui_action_button" xalign 1.0

screen game_menu(title):
    add office_bg("evening")
    add Solid("#121D24EE")
    text "AFTER HOURS" xpos 128 ypos 62 size 22 color "#D6B18A" kerning 2
    text title xpos 128 ypos 105 size 54 color "#F8F4EE"
    textbutton "돌아가기" xpos 1600 ypos 87 action Return() style "ui_light_button"
    transclude

screen save():
    tag menu
    use file_slots("저장")
screen load():
    tag menu
    use file_slots("불러오기")
screen file_slots(title):
    use game_menu(title):
        vbox:
            xpos 140 ypos 210 spacing 25
            hbox:
                spacing 15
                for page in range(1,6):
                    textbutton str(page) action FilePage(page) style "ui_light_button"
            grid 3 2:
                spacing 25
                for number in range(1,7):
                    button:
                        action (FileSave(number) if title=="저장" else OfficeFileLoad(number))
                        style "ui_light_button" xsize 530 ysize 300
                        vbox:
                            spacing 12
                            add FileScreenshot(number) xysize (480,220)
                            text FileTime(number,format="%m/%d %H:%M",empty="빈 슬롯") size 23 color "#26343B"

screen preferences():
    tag menu
    use game_menu("설정"):
        frame:
            xpos 150 ypos 230 xsize 1120 padding (38,30)
            vbox:
                spacing 25 xsize 1000
                text "텍스트 속도"
                bar:
                    value Preference("text speed")
                    xsize 1000 ysize 24
                    left_bar Solid("#28616A")
                    right_bar Solid("#CDD7D2")
                    thumb Transform(Solid("#D6B18A"),xysize=(18,30))
                text "자동 진행 대기"
                bar:
                    value Preference("auto-forward time")
                    xsize 1000 ysize 24
                    left_bar Solid("#28616A")
                    right_bar Solid("#CDD7D2")
                    thumb Transform(Solid("#D6B18A"),xysize=(18,30))
                textbutton "전체 화면 / 창 모드" action Preference("display","toggle") style "ui_light_button"
                textbutton "움직임 줄이기" action ToggleField(persistent,"reduce_motion") style "ui_light_button"
                text "현재 움직임 줄이기: " + ("켜짐" if persistent.reduce_motion else "꺼짐") size 24 color "#899499"
                textbutton "캐릭터 움직임: 준비 중" action NullAction() sensitive False style "ui_light_button"
                text "통화는 대사로 표시됩니다." size 24 color "#899499"

screen history():
    tag menu
    use game_menu("대화 기록"):
        viewport:
            xpos 150 ypos 230 xsize 1620 ysize 740 mousewheel True draggable True
            vbox:
                spacing 20
                for entry in _history_list:
                    frame:
                        xfill True
                        vbox:
                            spacing 8
                            if entry.who:
                                text entry.who color "#916641" size 24
                            text entry.what size 27

screen confirm(message,yes_action,no_action):
    modal True
    zorder 200
    add Solid("#121D24CB")
    frame:
        align (0.5,0.5) xsize 900 padding (45,35)
        vbox:
            spacing 25
            text message xmaximum 800
            hbox:
                spacing 20
                textbutton "확인" action yes_action style "ui_action_button"
                textbutton "취소" action no_action style "ui_light_button"
screen notify(message):
    zorder 210
    frame:
        align (0.5,0.13)
        text message size 25
    timer 3.0 action Hide("notify")
screen day_result():
    modal True
    zorder 80
    add Solid("#121D24D9")
    frame:
        align (0.5,0.5) xsize 1150 padding (50,40)
        vbox:
            spacing 22
            text "DAY %02d / AFTER HOURS" % day size 24 color "#916641" kerning 2
            text ("첫 주를 마치며" if day == 5 else ("다음 이야기의 방향" if day == 11 else "내일 이어질 이야기")) size 54
            grid 2 2:
                spacing 18 xfill True
                for who in names:
                    text "%s  /  호감 %d / 신뢰 %d" % (names[who],people[who]["affection"],people[who]["trust"]) size 25
            text "프로젝트 " + str(stats["project"]) + " / 스트레스 " + str(stats["stress"]) size 27 color "#899499"
            frame:
                background ui_panel("incoming") xfill True
                text "다음 약속: " + next_meeting_text() size 24 xmaximum 990
            text ("다음 주에는 더 알아보고 싶은 사람을 고릅니다.\n대화하면서 마음이 달라지면 다시 정할 수 있어요." if day == 5 else ("이후 본편은 제작 중입니다. 방향 선택은 교제나 후반 루트 진입을 확정하지 않습니다." if day == 11 else "오늘의 선택과 연락은 다음 날에도 이어집니다.")) size 24 color "#899499"
            hbox:
                spacing 16
                if day < 11:
                    textbutton "%d일차로 계속" % (day+1) action Return("continue") style "ui_action_button"
                textbutton "휴대폰 확인" action Show("phone") style "ui_light_button"
                textbutton "저장" action ShowMenu("save") style "ui_light_button"
                textbutton "제목으로" action Return("title") style "ui_light_button"






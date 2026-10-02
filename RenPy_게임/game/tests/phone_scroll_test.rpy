testcase office_phone_scroll:
    pause until screen "main_menu"
    run Preference("text speed",0)
    click "첫날 시작"
    advance until screen "choice"
    click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
    advance until screen "choice"
    click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
    advance until screen "phone"
    pause 0.6
    click "좋아요. 같이 먹으면서 이야기해요."
    pause 4.2
    assert eval not phone_has_replies("ria")
    assert eval not phone_pending
    assert eval abs(renpy.get_screen("phone").scope["message_scroll"].value-renpy.get_screen("phone").scope["message_scroll"].range) < 1
    screenshot "phone_scroll_short_reply"
    $ phone_messages.extend([{"who":"ria","out":False,"text":"지난 대화 %d. 긴 기록도 위로 올려 읽을 수 있어요." % n,"time":"12:31"} for n in range(8)])
    $ renpy.restart_interaction()
    pause 0.4
    assert eval renpy.get_screen("phone").scope["message_scroll"].range > 0
    assert eval abs(renpy.get_screen("phone").scope["message_scroll"].value-renpy.get_screen("phone").scope["message_scroll"].range) < 1
    $ renpy.get_screen("phone").scope["message_scroll"].change(0)
    pause 0.2
    assert eval not renpy.get_screen("phone").scope["message_scroll"].follow_latest
    $ phone_messages.append({"who":"ria","out":False,"text":"기록을 읽는 동안 도착한 새 메시지입니다.","time":"12:32"})
    $ renpy.restart_interaction()
    pause 0.4
    assert eval renpy.get_screen("phone").scope["message_scroll"].value == 0
    screenshot "phone_scroll_history"
    click "최신 메시지"
    pause 0.3
    assert eval abs(renpy.get_screen("phone").scope["message_scroll"].value-renpy.get_screen("phone").scope["message_scroll"].range) < 1
    screenshot "phone_scroll_latest"
    click "유진"
    pause 0.2
    assert eval renpy.get_screen("phone").scope["message_scroll"].value == 0
    click "리아"
    pause 0.2
    assert eval abs(renpy.get_screen("phone").scope["message_scroll"].value-renpy.get_screen("phone").scope["message_scroll"].range) < 1
    exit

testcase office_call_farewells:
    pause until screen "main_menu"
    run Preference("text speed",0)
    click "첫날 시작"
    run Jump("d1_home")
    pause 0.5
    run Function(ui_phone_call_begin, "seoyun", "d1_home")
    pause 0.1
    click "통화 종료"
    assert eval ui_call_closing and not ui_call_ending
    assert eval _last_say_who == "dh"
    advance
    assert eval _last_say_who == "sy" and ui_call_contact == "seoyun"
    assert eval not ui_call_ending
    assert eval renpy.get_displayable("office_portrait", "office_character") is None
    screenshot "call_farewell_seoyun_v6"
    advance
    pause 1.3
    assert eval ui_call_contact is None and not ui_call_closing and not ui_call_ending
    run Function(ui_phone_call_begin, "yujin", "d1_home")
    pause 0.1
    click "통화 종료"
    assert eval ui_call_closing and not ui_call_ending
    assert eval _last_say_who == "dh"
    advance
    assert eval _last_say_who == "yj" and ui_call_contact == "yujin"
    assert eval not ui_call_ending
    assert eval renpy.get_displayable("office_portrait", "office_character") is None
    screenshot "call_farewell_yujin_v6"
    advance
    pause 1.3
    assert eval ui_call_contact is None and not ui_call_closing and not ui_call_ending
    run Function(ui_phone_call_begin, "jihyun", "d1_home")
    pause 0.1
    click "통화 종료"
    assert eval ui_call_closing and not ui_call_ending
    assert eval _last_say_who == "dh"
    advance
    assert eval _last_say_who == "jh" and ui_call_contact == "jihyun"
    assert eval not ui_call_ending
    assert eval renpy.get_displayable("office_portrait", "office_character") is None
    screenshot "call_farewell_jihyun_v6"
    advance
    pause 1.3
    assert eval ui_call_contact is None and not ui_call_closing and not ui_call_ending
    exit


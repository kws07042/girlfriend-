testcase office_call_cleanup:
    pause until screen "main_menu"
    run Preference("text speed",0)
    click "첫날 시작"
    pause 0.5
    assert eval ui_scene_actor is None
    assert eval renpy.get_displayable("office_portrait", "office_character") is None
    advance until screen "choice"
    assert eval ui_scene_actor == "ria"
    assert eval renpy.get_displayable("office_portrait", "office_character") is not None
    run Jump("d1_evening_gate")
    advance until screen "phone"
    pause 0.5
    click "받기"
    pause 0.5
    assert eval ui_call_contact == "ria" and not ui_call_ending
    move pos (20, 20)
    screenshot "call_single_end_button_v6_upscaled_v1"
    click "통화 종료"
    pause 0.15
    assert eval ui_call_closing and not ui_call_ending and ui_call_contact == "ria"
    assert eval _last_say_who == "dh"
    screenshot "call_farewell_request_v6_upscaled_v1"
    advance
    assert eval _last_say_who == "ri" and ui_call_contact == "ria"
    screenshot "call_farewell_ria_v6_upscaled_v1"
    advance
    pause 0.15
    assert eval ui_call_ending and ui_call_contact == "ria"
    assert screen "say"
    screenshot "call_ended_notice_v6_upscaled_v1"
    pause 1.2
    assert eval ui_call_contact is None and not ui_call_ending
    assert eval ui_scene_key == "home" and ui_scene_actor is None
    assert eval renpy.get_displayable("office_portrait", "office_character") is None
    assert eval "사용자 종료" in phone_calls[-1]
    screenshot "call_ended_home_clean_v5_upscaled_v1"
    advance
    advance
    advance
    assert eval ui_scene_key == "home"
    assert eval renpy.get_displayable("office_portrait", "office_character") is None
    run FilePage("call-cleanup-qa")
    run FileSave(1,confirm=False)
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_scene_actor is None
    assert eval renpy.get_displayable("office_portrait", "office_character") is None
    run FileDelete(1,confirm=False)
    run FilePage(1)
    run Jump("d1_cafe")
    advance until screen "choice"
    pause 0.5
    assert eval ui_scene_actor == "ria"
    assert eval renpy.get_displayable("office_portrait", "office_character") is not None
    run SetVariable("ui_scene_actor", None)
    run FilePage("call-cleanup-qa")
    run FileSave(1,confirm=False)
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_scene_actor == "ria"
    run FileDelete(1,confirm=False)
    run FilePage(1)
    exit


testcase office_seoyun_expressions:
    pause until screen "main_menu"
    $ _expression_cps = preferences.text_cps
    run Preference("text speed",0)
    click "첫날 시작"
    run SetVariable("ui_ria_preview_time",0.0)
    run Jump("day02")
    advance until screen "phone"
    click "어디까지 필요한지 듣고 맡을 일을 정할게요."
    pause 5.1
    click "계속"
    assert eval ui_seoyun_expression_current() == "smile"
    pause 0.5
    screenshot "seoyun_smile_ingame_v1_poses_v1_features_v2_ria_pilot_v1"
    advance until screen "choice"
    assert eval ui_seoyun_expression_current() == "sheepish"
    assert eval ui_camera_current() == "C"
    pause 0.5
    screenshot "seoyun_sheepish_ingame_v1_poses_v1_features_v2_ria_pilot_v1"
    run Function(ui_seoyun_expression_set,"normal")
    pause 0.3
    screenshot "seoyun_normal_C_expression_v1_poses_v1_features_v2_ria_pilot_v1"
    run Function(ui_seoyun_expression_set,"smile")
    pause 0.3
    assert eval ui_seoyun_expression_current() == "smile"
    screenshot "seoyun_smile_C_expression_v1_poses_v1_features_v2_ria_pilot_v1"
    run Function(ui_seoyun_expression_set,"serious")
    pause 0.3
    assert eval ui_seoyun_expression_current() == "serious"
    screenshot "seoyun_serious_C_expression_v1_poses_v1_features_v2_ria_pilot_v1"
    run Function(ui_seoyun_expression_set,"surprised")
    pause 0.3
    assert eval ui_seoyun_expression_current() == "surprised"
    screenshot "seoyun_surprised_C_expression_v1_poses_v1_features_v2_ria_pilot_v1"
    run Function(ui_seoyun_expression_set,"sheepish")
    pause 0.3
    assert eval ui_seoyun_expression_current() == "sheepish"
    run FilePage("expressions-qa")
    run FileSave(1,confirm=False)
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_seoyun_expression_current() == "sheepish"
    run FileDelete(1,confirm=False)
    run FilePage(1)
    run Function(ui_seoyun_expression_set,None)
    run SetVariable("ui_expression_context",None)
    run SetVariable("ui_seoyun_expression","normal")
    run FilePage("expressions-qa")
    run FileSave(2,confirm=False)
    run OfficeFileLoad(2,confirm=False)
    assert eval ui_seoyun_expression_current() == "sheepish"
    run FileDelete(2,confirm=False)
    run FilePage(1)
    click "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)"
    advance until eval ui_seoyun_expression_current() == "surprised"
    assert eval _last_say_who == "dh" and ui_speaker == "seoyun"
    advance
    assert eval ui_seoyun_expression_current() == "smile"
    run Jump("d1_home")
    pause 0.5
    assert eval ui_seoyun_expression_current() == "normal"
    assert eval renpy.get_displayable("office_portrait","office_character") is None
    run Preference("text speed",_expression_cps)
    run SetVariable("ui_ria_preview_time",None)
    exit


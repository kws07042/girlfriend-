testcase office_ria_soft_expressions:
    pause until screen "main_menu"
    $ _other_cps = preferences.text_cps
    run Preference("text speed",0)
    click "첫날 시작"
    run SetVariable("ui_ria_preview_time",0.0)
    run Jump("day03")
    advance until screen "phone"
    click "현장에서 어떻게 기록했는지 궁금해요."
    pause 5.2
    click "계속"
    assert eval ui_speaker == "ria" and ui_expression_current("ria") == "smile"
    run Function(ui_camera_set,"C")
    pause 0.6
    move pos (20,20)
    run Function(ui_expression_set,"ria","normal")
    pause 0.3
    assert eval ui_expression_current("ria") == "normal"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_normal_C_expression_soft_v2_poses_v1_features_v2"
    run Function(ui_expression_set,"ria","smile")
    pause 0.3
    assert eval ui_expression_current("ria") == "smile"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_smile_C_expression_soft_v2_poses_v1_features_v2"
    run Function(ui_expression_set,"ria","serious")
    pause 0.3
    assert eval ui_expression_current("ria") == "serious"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_serious_C_expression_soft_v2_poses_v1_features_v2"
    run Function(ui_expression_set,"ria","surprised")
    pause 0.3
    assert eval ui_expression_current("ria") == "surprised"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_surprised_C_expression_soft_v2_poses_v1_features_v2"
    run Function(ui_expression_set,"ria","sheepish")
    pause 0.3
    assert eval ui_expression_current("ria") == "sheepish"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_sheepish_C_expression_soft_v2_poses_v1_features_v2"
    run FilePage("other-expressions-qa")
    run Function(renpy.retain_after_load)
    run FileSave(1,confirm=False)
    run Function(ui_expression_set,"ria","normal")
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_expression_current("ria") == "sheepish"
    run FileDelete(1,confirm=False)
    run FilePage(1)
    run Function(ui_expression_set,"ria",None)
    run Function(ui_camera_set,None)
    advance until eval ui_expression_current("ria") == "sheepish"
    assert eval ui_speaker == "ria"
    run Preference("text speed",_other_cps)
    run SetVariable("ui_ria_preview_time",None)
    exit


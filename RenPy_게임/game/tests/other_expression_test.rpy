testcase office_other_expressions:
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
    screenshot "ria_normal_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"ria","smile")
    pause 0.3
    assert eval ui_expression_current("ria") == "smile"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_smile_C_expression_soft_v2_poses_v1_features_v2"
    run Function(ui_expression_set,"ria","serious")
    pause 0.3
    assert eval ui_expression_current("ria") == "serious"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_serious_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"ria","surprised")
    pause 0.3
    assert eval ui_expression_current("ria") == "surprised"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_surprised_C_expression_soft_v2_poses_v1_features_v2"
    run Function(ui_expression_set,"ria","sheepish")
    pause 0.3
    assert eval ui_expression_current("ria") == "sheepish"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "ria_sheepish_C_expression_v1_poses_v1_features_v2"
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
    run Jump("day04")
    advance until screen "phone"
    click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
    pause 5.2
    click "계속"
    assert eval ui_speaker == "yujin" and ui_expression_current("yujin") == "smile"
    run Function(ui_camera_set,"C")
    pause 0.6
    move pos (20,20)
    run Function(ui_expression_set,"yujin","normal")
    pause 0.3
    assert eval ui_expression_current("yujin") == "normal"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "yujin_normal_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"yujin","smile")
    pause 0.3
    assert eval ui_expression_current("yujin") == "smile"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "yujin_smile_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"yujin","serious")
    pause 0.3
    assert eval ui_expression_current("yujin") == "serious"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "yujin_serious_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"yujin","surprised")
    pause 0.3
    assert eval ui_expression_current("yujin") == "surprised"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "yujin_surprised_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"yujin","sheepish")
    pause 0.3
    assert eval ui_expression_current("yujin") == "sheepish"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "yujin_sheepish_C_expression_v1_poses_v1_features_v2"
    run FilePage("other-expressions-qa")
    run Function(renpy.retain_after_load)
    run FileSave(1,confirm=False)
    run Function(ui_expression_set,"yujin","normal")
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_expression_current("yujin") == "sheepish"
    run FileDelete(1,confirm=False)
    run FilePage(1)
    run Function(ui_expression_set,"yujin",None)
    run Function(ui_camera_set,None)
    advance until eval ui_expression_current("yujin") == "serious"
    assert eval ui_speaker == "yujin"
    run Jump("day05")
    advance until screen "phone"
    click "첫 방문부터 재방문까지 단계별로 정리하겠습니다."
    pause 5.2
    click "계속"
    assert eval ui_speaker == "jihyun" and ui_expression_current("jihyun") == "smile"
    run Function(ui_camera_set,"C")
    pause 0.6
    move pos (20,20)
    run Function(ui_expression_set,"jihyun","normal")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "normal"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "jihyun_normal_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"jihyun","smile")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "smile"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "jihyun_smile_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"jihyun","serious")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "serious"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "jihyun_serious_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"jihyun","surprised")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "surprised"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "jihyun_surprised_C_expression_v1_poses_v1_features_v2"
    run Function(ui_expression_set,"jihyun","sheepish")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "sheepish"
    assert eval renpy.get_displayable("office_portrait","office_character") is not None
    screenshot "jihyun_sheepish_C_expression_v1_poses_v1_features_v2"
    run FilePage("other-expressions-qa")
    run Function(renpy.retain_after_load)
    run FileSave(1,confirm=False)
    run Function(ui_expression_set,"jihyun","normal")
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_expression_current("jihyun") == "sheepish"
    run FileDelete(1,confirm=False)
    run FilePage(1)
    run Function(ui_expression_set,"jihyun",None)
    run Function(ui_camera_set,None)
    advance until eval ui_expression_current("jihyun") == "serious"
    assert eval ui_speaker == "jihyun"
    run Jump("d1_home")
    pause 0.5
    assert eval all(ui_expression_current(w) == "normal" for w in ("ria","yujin","jihyun"))
    assert eval renpy.get_displayable("office_portrait","office_character") is None
    run Preference("text speed",_other_cps)
    run SetVariable("ui_ria_preview_time",None)
    exit



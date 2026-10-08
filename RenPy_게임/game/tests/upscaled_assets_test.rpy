testcase office_upscaled_assets:
    pause until screen "main_menu"
    $ _upscale_cps = preferences.text_cps
    run Preference("text speed",0)
    click "첫날 시작"
    run SetVariable("ui_ria_preview_time",0.0)
    advance until screen "choice"
    assert eval renpy.image_size("images/characters/seoyun_master.png") == (2048,3070)
    assert eval all(renpy.image_size("images/characters/%s_master.png" % who) == (2048,3072) for who in ("ria","yujin","jihyun"))
    assert eval all(ui_master_avatar_box(who) == (770,90,500,500) for who in names)
    assert eval ui_camera_current() == "B"
    pause 0.5
    screenshot "upscaled_ria_B_v1_poses_v1_features_v2"
    run Show("relationship_panel")
    pause 0.3
    assert screen "relationship_panel"
    screenshot "upscaled_relationship_faces_v1_poses_v1_features_v2"
    run Hide("relationship_panel")
    run Jump("d1_cafe")
    advance until screen "choice"
    assert eval ui_camera_current() == "C"
    pause 0.5
    screenshot "upscaled_ria_C_v1_poses_v1_features_v2"
    run Jump("day02")
    advance until screen "phone"
    click "어디까지 필요한지 듣고 맡을 일을 정할게요."
    pause 5.1
    click "계속"
    assert eval ui_scene_actor == "seoyun" and ui_camera_current() == "B"
    pause 0.5
    screenshot "upscaled_seoyun_B_expressions_v1_poses_v1_features_v2"
    advance until screen "choice"
    assert eval ui_scene_actor == "seoyun" and ui_camera_current() == "C"
    pause 0.5
    screenshot "upscaled_seoyun_C_expressions_v1_poses_v1_features_v2"
    run Jump("day04")
    advance until screen "phone"
    click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
    pause 5.1
    click "계속"
    assert eval ui_scene_actor == "yujin" and ui_camera_current() == "B"
    pause 0.5
    screenshot "upscaled_yujin_B_v1_poses_v1_features_v2"
    advance until screen "choice"
    click "각 시안의 목적을 듣고 첫 화면과 후속 화면을 구분한다. (오전 / 호감 +10 / 신뢰 +12)"
    advance until eval ui_camera_current() == "C"
    assert eval ui_speaker == "yujin" and ui_camera_current() == "C"
    pause 0.5
    screenshot "upscaled_yujin_C_v1_poses_v1_features_v2"
    run Jump("day05")
    advance until screen "phone"
    click "첫 방문부터 재방문까지 단계별로 정리하겠습니다."
    pause 4.1
    click "계속"
    assert eval ui_scene_actor == "jihyun" and ui_camera_current() == "B"
    pause 0.5
    screenshot "upscaled_jihyun_B_v1_poses_v1_features_v2"
    run FilePage("upscale-game-qa")
    run FileSave(1,confirm=False)
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_scene_actor == "jihyun"
    assert eval renpy.get_displayable("office_portrait", "office_character") is not None
    run FileDelete(1,confirm=False)
    run FilePage(1)
    run Preference("text speed",_upscale_cps)
    run SetVariable("ui_ria_preview_time",None)
    exit



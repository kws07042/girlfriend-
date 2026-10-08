testcase office_scene_motion:
    pause until screen "main_menu"
    $ _motion_previous = persistent.reduce_motion
    $ _motion_cps = preferences.text_cps
    $ persistent.reduce_motion = False
    run Preference("text speed",0)
    click "첫날 시작"
    advance until screen "choice"
    pause 0.5
    assert eval ui_scene_key == "office"
    assert eval abs(renpy.get_displayable("office_portrait", "office_character").state.zoom - 1.0) < 0.01
    screenshot "motion_normal_B_v2_upscaled_v1"
    run Function(ui_camera_set, "C")
    pause 0.1
    assert eval 1.0 < renpy.get_displayable("office_portrait", "office_character").state.zoom < 1.5
    # Numeric assertion verifies movement without a timing-dependent golden image.
    pause 0.5
    assert eval abs(renpy.get_displayable("office_portrait", "office_character").state.zoom - 1.5) < 0.01
    screenshot "motion_close_C_v2_upscaled_v1"
    run Function(ui_camera_set, "B")
    pause 0.5
    assert eval abs(renpy.get_displayable("office_portrait", "office_character").state.zoom - 1.0) < 0.01
    $ persistent.reduce_motion = True
    run Function(ui_camera_set, "C")
    pause 0.05
    assert eval abs(renpy.get_displayable("office_portrait", "office_character").state.zoom - 1.5) < 0.01
    run Function(ui_camera_set, None)
    run Jump("d1_cafe")
    assert eval ui_scene_key == "cafe"
    assert eval renpy.get_transition("master") is None
    assert eval ui_scene_show("cafe") is False
    $ persistent.reduce_motion = False
    advance until screen "choice"
    pause 0.5
    run FilePage("scene-motion-qa")
    run FileSave(1,confirm=False)
    assert eval renpy.get_save_data("scene-motion-qa-1")["ui_scene_key"] == "cafe"
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_scene_key == "cafe"
    pause 0.5
    assert eval ui_camera_current() == "C"
    run FileDelete(1,confirm=False)
    run FilePage(1)
    run Jump("d1_home")
    pause 0.1
    assert eval ui_scene_key == "home"
    assert eval renpy.get_ongoing_transition() is not None
    assert not screen "say"
    pause 0.45
    assert screen "say"
    run Jump("day02")
    advance until screen "phone"
    assert eval ui_scene_key == "office"
    assert screen "phone"
    assert eval renpy.get_screen("phone").scope["contact"] == "seoyun"
    run Hide("phone")
    $ persistent.reduce_motion = _motion_previous
    run Preference("text speed",_motion_cps)
    exit









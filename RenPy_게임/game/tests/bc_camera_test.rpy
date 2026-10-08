testcase office_bc_camera:
    pause until screen "main_menu"
    $ _bc_cps = preferences.text_cps
    run Preference("text speed",0)
    click "첫날 시작"
    advance until screen "choice"
    assert eval ui_camera_current() == "B"
    pause 0.4
    screenshot "bc_normal_choices_v2_upscaled_v1"
    run Jump("d1_cafe")
    advance until screen "choice"
    assert eval ui_camera_current() == "C"
    pause 0.4
    screenshot "bc_emotional_choices_v2_upscaled_v1"
    click "“현장 판단이 어떻게 나온 건지 더 듣고 싶어요.”"
    assert eval ui_camera_current() == "C"
    pause 0.4
    screenshot "bc_ria_close_v2_upscaled_v1"
    run SetVariable("ui_speaker", "seoyun")
    pause 0.3
    screenshot "bc_seoyun_close_v2_upscaled_v1"
    run SetVariable("ui_speaker", "yujin")
    pause 0.3
    screenshot "bc_yujin_close_v2_upscaled_v1"
    run SetVariable("ui_speaker", "jihyun")
    pause 0.3
    screenshot "bc_jihyun_close_v2_upscaled_v1"
    run Jump("d1_cafe_close")
    pause 0.3
    assert eval ui_camera_current() == "B"
    screenshot "bc_return_normal_v2_upscaled_v1"
    run Show("phone")
    pause 0.6
    screenshot "bc_phone_clean_v3_upscaled_v1"
    run Hide("phone")
    run Preference("text speed",_bc_cps)
    exit




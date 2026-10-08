testcase office_pose_flow:
    pause until screen "main_menu"
    $ _pose_cps = preferences.text_cps
    run Preference("text speed",0)
    click "첫날 시작"
    run SetVariable("ui_ria_preview_time",0.0)
    advance until screen "choice"
    assert eval ui_pose_current("ria") == "master"
    assert eval sum(len(v) for v in ui_pose_files.values()) == 9
    assert eval all(renpy.loadable(p) for d in ui_pose_files.values() for p in d.values())
    $ _pose_old_animation = persistent.ria_animation
    run SetField(persistent,"ria_animation",True)
    run ShowMenu("preferences")
    pause 0.3
    assert screen "preferences"
    screenshot "pose_animation_settings_slider_v2"
    click "캐릭터 움직임: 켜짐"
    assert eval not persistent.ria_animation
    click "캐릭터 움직임: 꺼짐"
    assert eval persistent.ria_animation
    click "돌아가기"
    run SetField(persistent,"ria_animation",_pose_old_animation)
    run Jump("d1_work_intro")
    advance until eval _last_say_who == "ri"
    assert eval ui_pose_current("ria") == "explaining"
    run Function(ui_camera_set,"C")
    pause 0.5
    screenshot "ria_explaining_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run Jump("d1_lunch_talk")
    pause 0.5
    assert eval ui_pose_current("ria") == "casual"
    screenshot "ria_casual_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run SetVariable("clock","19:00")
    run Jump("d1_cafe")
    advance until screen "choice"
    assert eval ui_pose_current("ria") == "listening"
    assert eval ui_camera_current() == "C"
    pause 0.5
    screenshot "ria_listening_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run FilePage("poses-qa")
    run Function(renpy.retain_after_load)
    run FileSave(1,confirm=False)
    run Function(ui_pose_set,"ria","explaining")
    run OfficeFileLoad(1,confirm=False)
    assert eval ui_pose_current("ria") == "listening"
    assert eval not ui_pose_transitions
    run FileDelete(1,confirm=False)
    run SetVariable("ui_pose_version",0)
    run SetVariable("ui_pose_context",None)
    run SetVariable("ui_poses",{})
    run Function(renpy.retain_after_load)
    run FileSave(2,confirm=False)
    run OfficeFileLoad(2,confirm=False)
    assert eval ui_pose_current("ria") == "listening"
    assert eval ui_pose_version == 1
    run FileDelete(2,confirm=False)
    run FilePage(1)
    run Function(ui_camera_set,None)
    run Jump("day02")
    advance until screen "phone"
    click "어디까지 필요한지 듣고 맡을 일을 정할게요."
    pause 5.2
    click "계속"
    assert eval ui_pose_current("seoyun") == "work"
    run Function(ui_camera_set,"C")
    pause 0.5
    screenshot "seoyun_work_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run Function(ui_pose_set,"seoyun","casual")
    pause 0.5
    assert eval ui_pose_current("seoyun") == "casual"
    screenshot "seoyun_casual_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run Function(ui_pose_set,"seoyun",None)
    run Jump("day04")
    advance until screen "phone"
    click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
    pause 5.2
    click "계속"
    assert eval ui_pose_current("yujin") == "work"
    pause 0.5
    screenshot "yujin_work_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run Function(ui_pose_set,"yujin","casual")
    pause 0.5
    assert eval ui_pose_current("yujin") == "casual"
    screenshot "yujin_casual_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run Function(ui_pose_set,"yujin",None)
    run Jump("day05")
    advance until screen "phone"
    click "첫 방문부터 재방문까지 단계별로 정리하겠습니다."
    pause 5.2
    click "계속"
    assert eval ui_pose_current("jihyun") == "work"
    pause 0.5
    screenshot "jihyun_work_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run Function(ui_pose_set,"jihyun","casual")
    pause 0.5
    assert eval ui_pose_current("jihyun") == "casual"
    screenshot "jihyun_casual_C_pose_flow_v1_features_v2_ria_pilot_v1"
    run Function(ui_pose_set,"jihyun",None)
    run Function(ui_camera_set,None)
    run Jump("d1_home")
    pause 0.5
    assert eval renpy.get_displayable("office_portrait","office_character") is None
    run Preference("text speed",_pose_cps)
    run SetVariable("ui_ria_preview_time",None)
    exit


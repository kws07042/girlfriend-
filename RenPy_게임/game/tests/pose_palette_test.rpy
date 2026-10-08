init 90 python:
    def _office_palette_native_render(who,pose):
        folder = "C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007"
        height = 3070 if who == "seoyun" else 3072
        ui_pose_palette["enabled"] = False
        try:
            renpy.render_to_file(ui_character_static_sprite(who,pose=pose),folder+"/native_"+who+"_"+pose+"_before.png",width=2048,height=height,resize=True)
        finally:
            ui_pose_palette["enabled"] = True
        renpy.render_to_file(ui_character_static_sprite(who,pose=pose),folder+"/native_"+who+"_"+pose+"_after.png",width=2048,height=height,resize=True)
        return True

    def _office_palette_enabled(enabled):
        ui_pose_palette["enabled"] = enabled
        renpy.restart_interaction()

testsuite office_pose_palette_20261007:
    setup:
        pause until screen "main_menu"
        run Function(_office_qa_settings)
    teardown:
        run Function(_office_palette_enabled,True)
        run Function(_office_qa_settings,True)
        exit

    testcase palette_frames:
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        assert eval ui_pose_palette["enabled"]
        assert eval not ui_ria_animation_active()
        assert eval sum(len(v) for v in ui_pose_files.values()) == 9
        run SetVariable("ui_speaker","ria")
        run SetVariable("ui_scene_actor","ria")
        run Function(ui_pose_set,"ria","master")
        $ _palette_rendered = _office_palette_native_render("ria","master")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_master_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_master_C_after.png")
        run Function(ui_pose_set,"ria","listening")
        $ _palette_rendered = _office_palette_native_render("ria","listening")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_listening_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_listening_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_listening_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run Function(ui_pose_set,"ria","explaining")
        $ _palette_rendered = _office_palette_native_render("ria","explaining")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_explaining_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_explaining_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_explaining_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run Function(ui_pose_set,"ria","casual")
        $ _palette_rendered = _office_palette_native_render("ria","casual")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_casual_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_casual_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_casual_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run SetVariable("ui_speaker","seoyun")
        run SetVariable("ui_scene_actor","seoyun")
        run Function(ui_pose_set,"seoyun","master")
        $ _palette_rendered = _office_palette_native_render("seoyun","master")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_master_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_master_C_after.png")
        run Function(ui_pose_set,"seoyun","work")
        $ _palette_rendered = _office_palette_native_render("seoyun","work")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_work_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_work_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_work_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run Function(ui_pose_set,"seoyun","casual")
        $ _palette_rendered = _office_palette_native_render("seoyun","casual")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_casual_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_casual_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_casual_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run SetVariable("ui_speaker","yujin")
        run SetVariable("ui_scene_actor","yujin")
        run Function(ui_pose_set,"yujin","master")
        $ _palette_rendered = _office_palette_native_render("yujin","master")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_master_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_master_C_after.png")
        run Function(ui_pose_set,"yujin","work")
        $ _palette_rendered = _office_palette_native_render("yujin","work")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_work_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_work_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_work_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run Function(ui_pose_set,"yujin","casual")
        $ _palette_rendered = _office_palette_native_render("yujin","casual")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_casual_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_casual_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_casual_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run SetVariable("ui_speaker","jihyun")
        run SetVariable("ui_scene_actor","jihyun")
        run Function(ui_pose_set,"jihyun","master")
        $ _palette_rendered = _office_palette_native_render("jihyun","master")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_master_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_master_C_after.png")
        run Function(ui_pose_set,"jihyun","work")
        $ _palette_rendered = _office_palette_native_render("jihyun","work")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_work_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_work_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_work_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run Function(ui_pose_set,"jihyun","casual")
        $ _palette_rendered = _office_palette_native_render("jihyun","casual")
        assert eval _palette_rendered
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_casual_B_after.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_casual_C_after.png")
        run Function(_office_palette_enabled,False)
        pause 0.2
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_casual_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.2
        run Function(ui_pose_set,"yujin","work")
        run SetVariable("ui_speaker","yujin")
        run SetVariable("ui_scene_actor","yujin")
        run Function(ui_camera_set,"C")
        run FilePage("palette-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run Function(ui_pose_set,"yujin","casual")
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_pose_current("yujin") == "work"
        assert eval ui_pose_palette["enabled"]
        assert eval not ui_pose_transitions
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run Function(ui_pose_set,"yujin","casual")
        pause 0.3
        assert eval ui_pose_current("yujin") == "casual"
        run Show("phone",initial_contact="ria")
        pause 0.5
        assert eval renpy.get_displayable("office_portrait","office_character") is None
        run Hide("phone")
        assert eval ui_pose_palette["enabled"]

    testcase fixed_comparison_frames:
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        run SetField(persistent,"reduce_motion",True)
        run Function(ui_camera_set,"C")
        pause 0.1
        run SetVariable("ui_speaker","ria")
        run SetVariable("ui_scene_actor","ria")
        run Function(ui_pose_set,"ria","listening")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_listening_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_listening_C_after.png")
        run Function(ui_pose_set,"ria","explaining")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_explaining_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_explaining_C_after.png")
        run Function(ui_pose_set,"ria","casual")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_casual_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\ria_casual_C_after.png")
        run SetVariable("ui_speaker","seoyun")
        run SetVariable("ui_scene_actor","seoyun")
        run Function(ui_pose_set,"seoyun","work")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_work_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_work_C_after.png")
        run Function(ui_pose_set,"seoyun","casual")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_casual_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\seoyun_casual_C_after.png")
        run SetVariable("ui_speaker","yujin")
        run SetVariable("ui_scene_actor","yujin")
        run Function(ui_pose_set,"yujin","work")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_work_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_work_C_after.png")
        run Function(ui_pose_set,"yujin","casual")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_casual_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\yujin_casual_C_after.png")
        run SetVariable("ui_speaker","jihyun")
        run SetVariable("ui_scene_actor","jihyun")
        run Function(ui_pose_set,"jihyun","work")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_work_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_work_C_after.png")
        run Function(ui_pose_set,"jihyun","casual")
        run Function(_office_palette_enabled,False)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_casual_C_before.png")
        run Function(_office_palette_enabled,True)
        pause 0.15
        assert eval ui_bc_motion_values() == (1.5,480.0)
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\ud3ec\uc988\uc0c9\uac10\ud1b5\uc77c_20261007\\jihyun_casual_C_after.png")
        assert eval ui_pose_palette["enabled"]

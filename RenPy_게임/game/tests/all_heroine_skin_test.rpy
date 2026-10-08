init 90 python:
    def _office_all_skin_render(who,pose):
        folder = "C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007"
        height = 3070 if who == "seoyun" else 3072
        renpy.render_to_file(ui_character_static_sprite(who,pose=pose),folder+"/native_"+who+"_"+pose+".png",width=2048,height=height,resize=True)
        return True

testsuite office_all_skin_20261007:
    setup:
        pause until screen "main_menu"
        run Function(_office_qa_settings)
    teardown:
        run Function(_office_qa_settings,True)
        exit

    testcase capture_current_palettes:
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        run SetField(persistent,"reduce_motion",True)
        assert eval ui_pose_palette["enabled"]
        assert eval not ui_ria_animation_active()
        run SetVariable("ui_speaker","ria")
        run SetVariable("ui_scene_actor","ria")
        run Function(ui_pose_set,"ria","master")
        $ _all_skin_rendered = _office_all_skin_render("ria","master")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\ria_master_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\ria_master_C.png")
        run Function(ui_pose_set,"ria","listening")
        $ _all_skin_rendered = _office_all_skin_render("ria","listening")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\ria_listening_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\ria_listening_C.png")
        run Function(ui_pose_set,"ria","explaining")
        $ _all_skin_rendered = _office_all_skin_render("ria","explaining")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\ria_explaining_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\ria_explaining_C.png")
        run Function(ui_pose_set,"ria","casual")
        $ _all_skin_rendered = _office_all_skin_render("ria","casual")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\ria_casual_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\ria_casual_C.png")
        run SetVariable("ui_speaker","seoyun")
        run SetVariable("ui_scene_actor","seoyun")
        run Function(ui_pose_set,"seoyun","master")
        $ _all_skin_rendered = _office_all_skin_render("seoyun","master")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\seoyun_master_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\seoyun_master_C.png")
        run Function(ui_pose_set,"seoyun","work")
        $ _all_skin_rendered = _office_all_skin_render("seoyun","work")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\seoyun_work_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\seoyun_work_C.png")
        run Function(ui_pose_set,"seoyun","casual")
        $ _all_skin_rendered = _office_all_skin_render("seoyun","casual")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\seoyun_casual_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\seoyun_casual_C.png")
        run SetVariable("ui_speaker","yujin")
        run SetVariable("ui_scene_actor","yujin")
        run Function(ui_pose_set,"yujin","master")
        $ _all_skin_rendered = _office_all_skin_render("yujin","master")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\yujin_master_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\yujin_master_C.png")
        run Function(ui_pose_set,"yujin","work")
        $ _all_skin_rendered = _office_all_skin_render("yujin","work")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\yujin_work_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\yujin_work_C.png")
        run Function(ui_pose_set,"yujin","casual")
        $ _all_skin_rendered = _office_all_skin_render("yujin","casual")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\yujin_casual_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\yujin_casual_C.png")
        run SetVariable("ui_speaker","jihyun")
        run SetVariable("ui_scene_actor","jihyun")
        run Function(ui_pose_set,"jihyun","master")
        $ _all_skin_rendered = _office_all_skin_render("jihyun","master")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\jihyun_master_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\jihyun_master_C.png")
        run Function(ui_pose_set,"jihyun","work")
        $ _all_skin_rendered = _office_all_skin_render("jihyun","work")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\jihyun_work_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\jihyun_work_C.png")
        run Function(ui_pose_set,"jihyun","casual")
        $ _all_skin_rendered = _office_all_skin_render("jihyun","casual")
        assert eval _all_skin_rendered
        run Function(ui_camera_set,"B")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\jihyun_casual_B.png")
        run Function(ui_camera_set,"C")
        pause 0.1
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc804\uccb4\ud788\ub85c\uc778_\ud53c\ubd80\uc0c9\uc7ac\uac80\uc218_20261007\\jihyun_casual_C.png")

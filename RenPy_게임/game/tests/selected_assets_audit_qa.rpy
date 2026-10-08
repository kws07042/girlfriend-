init 90 python:
    def _office_selected_asset_native_same(who,pose):
        import hashlib
        folder = "C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007"
        height = 3070 if who == "seoyun" else 3072
        reference = folder + "/native_" + who + "_" + pose + "_reference.png"
        actual = folder + "/native_" + who + "_" + pose + "_actual.png"
        renpy.render_to_file(Image(ui_character_pose_file(who,pose)),reference,width=2048,height=height,resize=True)
        # Compare authored imagery with the intentional whole-sprite colour stage bypassed.
        _palette_enabled_before = ui_pose_palette["enabled"]
        ui_pose_palette["enabled"] = False
        try:
            renpy.render_to_file(ui_character_static_sprite(who,pose=pose,expression="serious"),actual,width=2048,height=height,resize=True)
        finally:
            ui_pose_palette["enabled"] = _palette_enabled_before
        with open(reference,"rb") as f:
            expected = hashlib.sha256(f.read()).hexdigest()
        with open(actual,"rb") as f:
            return expected == hashlib.sha256(f.read()).hexdigest()

testsuite office_selected_assets_20261007:
    setup:
        pause until screen "main_menu"
        run Function(_office_qa_settings)
    teardown:
        run Function(_office_qa_settings,True)
        exit

    testcase assets_and_frames:
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        assert eval not ui_ria_animation_active()
        assert eval all(renpy.loadable(p) for d in ui_pose_files.values() for p in d.values())
        run SetVariable("ui_speaker","ria")
        run SetVariable("ui_scene_actor","ria")
        run Function(ui_pose_set,"ria","master")
        $ _selected_native_same = _office_selected_asset_native_same("ria","master")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("ria") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\ria_master_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("ria") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\ria_master_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"ria","listening")
        $ _selected_native_same = _office_selected_asset_native_same("ria","listening")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("ria") == "listening"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\ria_listening_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("ria") == "listening"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\ria_listening_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"ria","explaining")
        $ _selected_native_same = _office_selected_asset_native_same("ria","explaining")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("ria") == "explaining"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\ria_explaining_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("ria") == "explaining"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\ria_explaining_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"ria","casual")
        $ _selected_native_same = _office_selected_asset_native_same("ria","casual")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("ria") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\ria_casual_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("ria") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\ria_casual_C_\uc778\uac8c\uc784.png")
        run SetVariable("ui_speaker","seoyun")
        run SetVariable("ui_scene_actor","seoyun")
        run Function(ui_pose_set,"seoyun","master")
        $ _selected_native_same = _office_selected_asset_native_same("seoyun","master")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("seoyun") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\seoyun_master_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("seoyun") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\seoyun_master_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"seoyun","work")
        $ _selected_native_same = _office_selected_asset_native_same("seoyun","work")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("seoyun") == "work"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\seoyun_work_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("seoyun") == "work"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\seoyun_work_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"seoyun","casual")
        $ _selected_native_same = _office_selected_asset_native_same("seoyun","casual")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("seoyun") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\seoyun_casual_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("seoyun") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\seoyun_casual_C_\uc778\uac8c\uc784.png")
        run SetVariable("ui_speaker","yujin")
        run SetVariable("ui_scene_actor","yujin")
        run Function(ui_pose_set,"yujin","master")
        $ _selected_native_same = _office_selected_asset_native_same("yujin","master")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("yujin") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\yujin_master_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("yujin") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\yujin_master_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"yujin","work")
        $ _selected_native_same = _office_selected_asset_native_same("yujin","work")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("yujin") == "work"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\yujin_work_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("yujin") == "work"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\yujin_work_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"yujin","casual")
        $ _selected_native_same = _office_selected_asset_native_same("yujin","casual")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("yujin") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\yujin_casual_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("yujin") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\yujin_casual_C_\uc778\uac8c\uc784.png")
        run SetVariable("ui_speaker","jihyun")
        run SetVariable("ui_scene_actor","jihyun")
        run Function(ui_pose_set,"jihyun","master")
        $ _selected_native_same = _office_selected_asset_native_same("jihyun","master")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("jihyun") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\jihyun_master_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("jihyun") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\jihyun_master_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"jihyun","work")
        $ _selected_native_same = _office_selected_asset_native_same("jihyun","work")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("jihyun") == "work"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\jihyun_work_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("jihyun") == "work"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\jihyun_work_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"jihyun","casual")
        $ _selected_native_same = _office_selected_asset_native_same("jihyun","casual")
        assert eval _selected_native_same
        run Function(ui_camera_set,"B")
        pause 0.4
        assert eval ui_camera_current() == "B" and ui_pose_current("jihyun") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\jihyun_casual_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.4
        assert eval ui_camera_current() == "C" and ui_pose_current("jihyun") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\jihyun_casual_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"yujin","work")
        run SetVariable("ui_speaker","yujin")
        run SetVariable("ui_scene_actor","yujin")
        run FilePage("selected-assets-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run Function(ui_pose_set,"yujin","casual")
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_pose_current("yujin") == "work"
        assert eval not ui_pose_transitions
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run Function(send_message,"cafe_photo")
        assert eval "ria_cafe" in photo_received
        run Show("phone",initial_contact="ria")
        pause 0.6
        assert eval renpy.get_displayable("office_portrait","office_character") is None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\\ub9ac\uc544_A_\ubb38\uc790\uc378\ub124\uc77c.png")
        click "사진"
        pause 0.3
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\\ub9ac\uc544_A_\uc568\ubc94\uc378\ub124\uc77c.png")
        click "ria_cafe"
        pause 0.3
        assert screen "phone_photo"
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc0ac\uc9c4\ud3ec\uc988_\uc0c9\uac10\ud06c\uae30\uac80\uc218_20261007\\\ub9ac\uc544_A_\uc0ac\uc9c4\ud655\ub300.png")
        click "내 앨범에 저장"
        assert eval "ria_cafe" in photo_saved
        click "닫기"
        run Hide("phone")

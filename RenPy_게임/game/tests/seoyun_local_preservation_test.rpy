init 90 python:
    def _office_seoyun_local_preserved_render(pose):
        folder = "C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc11c\uc724_\uc6d0\ud654\ubcf4\uc874\uad6d\uc18c\uc218\uc815_20261007"
        path = ui_character_pose_file("seoyun",pose)
        renpy.render_to_file(Image(path),folder+"/native_"+pose+"_raw.png",width=2048,height=3070,resize=True)
        renpy.render_to_file(ui_character_static_sprite("seoyun",pose=pose,expression="surprised"),folder+"/native_"+pose+"_palette.png",width=2048,height=3070,resize=True)
        import hashlib
        with open(folder+"/native_"+pose+"_raw.png","rb") as f:
            reference = hashlib.sha256(f.read()).digest()
        with open(folder+"/native_"+pose+"_palette.png","rb") as f:
            return reference == hashlib.sha256(f.read()).digest()

testsuite office_seoyun_local_preservation_20261007:
    setup:
        pause until screen "main_menu"
        run Function(_office_qa_settings)
    teardown:
        run Function(_office_qa_settings,True)
        exit

    testcase current_art_and_story:
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        assert eval not ui_ria_animation_active()
        assert eval ui_pose_palette["enabled"]
        run Jump("day02")
        advance until screen "phone"
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        pause 5.2
        click "계속"
        assert eval ui_pose_current("seoyun") == "work"
        assert eval ui_speaker == "seoyun"
        run SetField(persistent,"reduce_motion",True)
        run Function(ui_pose_set,"seoyun","master")
        $ _seoyun_current_rendered = _office_seoyun_local_preserved_render("master")
        assert eval _seoyun_current_rendered
        run Function(ui_camera_set,"B")
        pause 0.2
        assert eval ui_camera_current() == "B" and ui_pose_current("seoyun") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc11c\uc724_\uc6d0\ud654\ubcf4\uc874\uad6d\uc18c\uc218\uc815_20261007\\master_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.2
        assert eval ui_camera_current() == "C" and ui_pose_current("seoyun") == "master"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc11c\uc724_\uc6d0\ud654\ubcf4\uc874\uad6d\uc18c\uc218\uc815_20261007\\master_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"seoyun","work")
        $ _seoyun_current_rendered = _office_seoyun_local_preserved_render("work")
        assert eval _seoyun_current_rendered
        run Function(ui_camera_set,"B")
        pause 0.2
        assert eval ui_camera_current() == "B" and ui_pose_current("seoyun") == "work"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc11c\uc724_\uc6d0\ud654\ubcf4\uc874\uad6d\uc18c\uc218\uc815_20261007\\work_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.2
        assert eval ui_camera_current() == "C" and ui_pose_current("seoyun") == "work"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc11c\uc724_\uc6d0\ud654\ubcf4\uc874\uad6d\uc18c\uc218\uc815_20261007\\work_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"seoyun","casual")
        $ _seoyun_current_rendered = _office_seoyun_local_preserved_render("casual")
        assert eval _seoyun_current_rendered
        run Function(ui_camera_set,"B")
        pause 0.2
        assert eval ui_camera_current() == "B" and ui_pose_current("seoyun") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc11c\uc724_\uc6d0\ud654\ubcf4\uc874\uad6d\uc18c\uc218\uc815_20261007\\casual_B_\uc778\uac8c\uc784.png")
        run Function(ui_camera_set,"C")
        pause 0.2
        assert eval ui_camera_current() == "C" and ui_pose_current("seoyun") == "casual"
        assert eval renpy.get_displayable("office_portrait","office_character") is not None
        $ renpy.screenshot("C:\\Users\\user\\Desktop\\\uac74\\\uc624\ud53c\uc2a4\\RenPy_\uac8c\uc784\\\uc0d8\ud50c\\\uc11c\uc724_\uc6d0\ud654\ubcf4\uc874\uad6d\uc18c\uc218\uc815_20261007\\casual_C_\uc778\uac8c\uc784.png")
        run Function(ui_pose_set,"seoyun","work")
        run FilePage("seoyun-rebuild-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run Function(ui_pose_set,"seoyun","casual")
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_pose_current("seoyun") == "work"
        assert eval not ui_pose_transitions
        assert eval ui_pose_palette["enabled"]
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run Show("phone",initial_contact="seoyun")
        pause 0.3
        assert eval renpy.get_displayable("office_portrait","office_character") is None
        run Hide("phone")
        run SetField(persistent,"reduce_motion",False)
        run Function(ui_pose_set,"seoyun","casual")
        pause 0.3
        assert eval ui_pose_current("seoyun") == "casual"
        assert eval not ui_ria_animation_active("seoyun")
        run Function(ui_pose_set,"seoyun",None)
        assert eval ui_character_pose_file("seoyun") in ui_pose_files["seoyun"].values()

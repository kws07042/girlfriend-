# Background engine verification keeps its timer and save data separate from normal play.
init 95 python:
    import os as _ghost_qa_os
    if _ghost_qa_os.environ.get("OFFICE_GHOST_QA") == "1" or renpy.game.args.command == "test":
        config.performance_test = False
        renpy.test.testsettings._test.force = True
        renpy.test.testsettings._test.timeout = 35.0
        _ghost_shots = _ghost_qa_os.environ.get("OFFICE_GHOST_QA_SHOTS")
        if _ghost_shots:
            renpy.test.testsettings._test.screenshot_directory = _ghost_shots
        def _ghost_qa_redraw():
            renpy.display.interface.force_redraw = True
        def _ghost_qa_interact():
            if not renpy.get_screen("_ghost_qa_tick"):
                renpy.show_screen("_ghost_qa_tick")
        config.interact_callbacks.append(_ghost_qa_interact)
        _ghost_qa_observations = []
        _ghost_qa_results = {}
        _ghost_qa_sequence_done = False
        _ghost_qa_original_render = ui_pose_render
        def _ghost_qa_sprite_path(node):
            for depth in range(5):
                path = getattr(node,"filename",None)
                if path:
                    return str(path).replace("\\","/")
                node = getattr(node,"child",None)
                if node is None:
                    break
            return None
        def _ghost_qa_pose_render(st,at,who):
            result = _ghost_qa_original_render(st,at,who)
            if ui_scene_in_transition:
                _ghost_qa_observations.append((who,ui_scene_key,ui_scene_actor,_ghost_qa_sprite_path(result[0]),ui_bc_motion_values()))
            return result
        ui_pose_render = _ghost_qa_pose_render
        def _ghost_qa_prepare_exit(who):
            store.place = "QA / lounge"
            store.chapter = "QA outgoing"
            store.slot = "lunch"
            ui_scene_show("lounge")
            store.ui_speaker = who
            store.ui_scene_actor = who
            store.ui_poses[who] = "casual"
            store.ui_pose_last_actor = who
            ui_camera_set("C")
        def _ghost_qa_exit():
            store.place = "QA / office"
            store.chapter = "QA incoming"
            ui_scene_show("office")

screen _ghost_qa_tick():
    timer 0.04 repeat True action Function(_ghost_qa_redraw,_update_screens=False)

testsuite office_scene_ghost_20261007:
    setup:
        pause until screen "main_menu"
        run Preference("text speed",0)
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        click "첫날 시작"
        advance until screen "choice"
    teardown:
        exit

    testcase lunch_to_office:
        run Jump("d1_lunch_talk")
        advance until screen "choice"
        click "“조용한 곳에서 걷거나 책을 읽어요.”"
        advance until eval _last_say_what == "그건 좋네요. 꼭 같이 좋아해야 하는 건 아니니까."
        assert eval ui_scene_key == "lounge" and ui_pose_current("ria") == "casual"
        advance
        assert eval ui_scene_key == "office" and ui_scene_actor is None
        assert eval not ui_scene_in_transition and not ui_scene_frozen_sprites
        advance until eval _last_say_who == "jh"
        assert eval ui_scene_actor == "jihyun"
        assert eval ui_pose_current("jihyun") == "casual"

    testcase empty_scene_save_and_call:
        run SetVariable("ui_scene_actor","ria")
        run SetVariable("ui_camera_actor","ria")
        run Function(ui_pose_change,"ria","casual")
        run SetVariable("chapter","next scene")
        run Function(ui_scene_show,"office")
        assert eval ui_scene_actor is None
        assert eval not ui_pose_transitions
        run FilePage("scene-ghost-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run SetVariable("ui_scene_actor","ria")
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_scene_actor is None
        assert eval not ui_scene_in_transition and not ui_scene_frozen_sprites
        run SetVariable("ui_scene_presence_version",0)
        run SetVariable("_last_say_who","ri")
        run SetVariable("ui_camera_actor","ria")
        run Function(ui_scene_restore_actor)
        assert eval ui_scene_actor is None
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run SetVariable("ui_scene_actor","ria")
        run Function(ui_phone_call_begin,"ria","d1_home")
        assert eval ui_scene_actor is None and ui_call_contact == "ria"
        run Function(ui_phone_call_end)
        assert eval ui_call_contact is None and ui_scene_actor is None
        run Function(ui_scene_restore_actor)
        assert eval ui_scene_actor is None
        run SetField(persistent,"reduce_motion",True)
        run Function(ui_scene_show,"home")
        assert eval ui_scene_key == "home" and ui_scene_actor is None
        run SetField(persistent,"reduce_motion",False)

    testcase all_heroine_outgoing_freeze:
        run Jump("_ghost_qa_scene_sequence")
        advance until eval _ghost_qa_sequence_done
        assert eval ui_scene_actor is None and not ui_scene_in_transition
        assert eval all(any(o[0]==who and o[1]=="office" and o[3] and who+"_poses/casual.png" in o[3] for o in _ghost_qa_results[who]) for who in ui_pose_files)
        assert eval all(all(o[3] and who+"_poses/casual.png" in o[3] for o in _ghost_qa_results[who] if o[0]==who) for who in ui_pose_files)
        assert eval all(len(set(o[4] for o in _ghost_qa_results[who]))==1 for who in ui_pose_files)
        assert eval not ui_scene_frozen_sprites and ui_scene_frozen_frame is None
        run Function(ui_camera_set,None)

label _ghost_qa_scene_sequence:
    python:
        for _ghost_who in ui_pose_files:
            _ghost_qa_prepare_exit(_ghost_who)
            renpy.pause(0.5)
            _ghost_qa_observations[:] = []
            _ghost_qa_exit()
            _ghost_qa_results[_ghost_who] = list(_ghost_qa_observations)
        _ghost_qa_sequence_done = True
    "장면 전환 검수가 끝났습니다."
    return

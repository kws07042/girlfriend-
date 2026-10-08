init 90 python:
    import hashlib as _office_face_hash
    def _office_native_face_same(who, pose):
        folder = 'C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007'
        height = 3070 if who == "seoyun" else 3072
        reference = folder + "/" + who + "_" + pose + "_reference.png"
        actual = folder + "/" + who + "_" + pose + "_restored.png"
        renpy.render_to_file(Image(ui_character_pose_file(who,pose)), reference, width=2048, height=height, resize=True)
        # Compare authored imagery with the intentional whole-sprite colour stage bypassed.
        _palette_enabled_before = ui_pose_palette["enabled"]
        ui_pose_palette["enabled"] = False
        try:
            renpy.render_to_file(ui_character_static_sprite(who,pose=pose,expression="serious"), actual, width=2048, height=height, resize=True)
        finally:
            ui_pose_palette["enabled"] = _palette_enabled_before
        with open(reference,"rb") as f:
            expected = _office_face_hash.sha256(f.read()).hexdigest()
        with open(actual,"rb") as f:
            return expected == _office_face_hash.sha256(f.read()).hexdigest()

    def _office_qa_settings(restore=False):
        if not restore:
            _office_qa_settings.previous = (preferences.text_cps or 0, persistent.reduce_motion, renpy.test.testsettings._test.timeout)
            renpy.test.testsettings._test.timeout = 60.0
        else:
            cps, motion, timeout = _office_qa_settings.previous
            Preference("text speed",cps)()
            persistent.reduce_motion = motion
            renpy.test.testsettings._test.timeout = timeout

testsuite office_restore_20261007:
    setup:
        pause until screen "main_menu"
        run Function(_office_qa_settings)
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        run Function(_office_qa_settings,True)
        exit

    testcase original_faces:
        pause until screen "main_menu"
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        assert eval not ui_ria_animation_active()
        $ _restore_pixels_match = _office_native_face_same("ria","master")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("ria","listening")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("ria","explaining")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("ria","casual")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("seoyun","master")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("seoyun","work")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("seoyun","casual")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("yujin","master")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("yujin","work")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("yujin","casual")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("jihyun","master")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("jihyun","work")
        assert eval _restore_pixels_match
        pause 0.05
        $ _restore_pixels_match = _office_native_face_same("jihyun","casual")
        assert eval _restore_pixels_match
        pause 0.05
        run FilePage("face-restore-qa")
        run Function(ui_expression_set,"seoyun","sheepish")
        run Function(ui_pose_set,"seoyun","work")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run Function(ui_expression_set,"seoyun","surprised")
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_expression_current("seoyun") == "sheepish" and ui_pose_current("seoyun") == "work"
        $ _restore_pixels_match = _office_native_face_same("seoyun","work")
        assert eval _restore_pixels_match
        pause 0.05
        run FileDelete(1,confirm=False)
        run FilePage(1)

    testcase office_phone_live:
        pause until screen "main_menu"
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "phone"
        pause 0.6
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_v4_idle_message_policy_v1") + ".png")
        $ _phone_before = len(phone_messages)
        $ _affection_before = people["ria"]["affection"]
        click "좋아요. 같이 먹으면서 이야기해요."
        assert eval len(phone_pending) == 1
        assert eval len(phone_messages) == _phone_before + 1
        assert eval phone_messages[-1]["delivery"] == "sending"
        pause 0.8
        assert eval phone_messages[-1]["delivery"] == "sent"
        pause 0.7
        assert eval phone_is_typing("ria")
        assert eval phone_messages[-1]["delivery"] == "read"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_v4_typing_message_policy_v1") + ".png")
        run FilePage("phoneqa")
        $ renpy.retain_after_load()
        run FileSave(1,confirm=False)
        assert eval len(renpy.get_save_data("phoneqa-1")["phone_pending"]) == 1
        click "유진"
        assert eval phone_is_typing("ria")
        run Hide("phone")
        pause 2.8
        assert eval len(phone_pending) == 0
        assert eval len(phone_messages) == _phone_before + 2
        assert eval phone_unread["ria"] == 1
        assert eval people["ria"]["affection"] == _affection_before + 1
        $ reply_message(phone_replied[-1], message_data[phone_replied[-1]]["reply"][0])
        assert eval len(phone_messages) == _phone_before + 2
        assert eval people["ria"]["affection"] == _affection_before + 1
        run OfficeFileLoad(1,confirm=False)
        pause 0.2
        assert eval len(phone_pending) == 1
        assert eval len(phone_messages) == len(renpy.get_save_data("phoneqa-1")["phone_messages"])
        run Hide("phone")
        pause 2.8
        assert eval len(phone_pending) == 0
        assert eval len(phone_messages) == len(renpy.get_save_data("phoneqa-1")["phone_messages"]) + 1
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run Show("phone")
        pause 0.6
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_v4_received_message_policy_v1") + ".png")

    testcase office_phone_scroll:
        pause until screen "main_menu"
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "phone"
        pause 0.6
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 4.2
        assert eval not phone_has_replies("ria")
        assert eval not phone_pending
        assert eval abs(renpy.get_screen("phone").scope["message_scroll"].value-renpy.get_screen("phone").scope["message_scroll"].range) < 1
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_scroll_short_reply_message_policy_v1") + ".png")
        $ phone_messages.extend([{"who":"ria","out":False,"text":"지난 대화 %d. 긴 기록도 위로 올려 읽을 수 있어요." % n,"time":"12:31"} for n in range(8)])
        $ renpy.restart_interaction()
        pause 0.4
        assert eval renpy.get_screen("phone").scope["message_scroll"].range > 0
        assert eval abs(renpy.get_screen("phone").scope["message_scroll"].value-renpy.get_screen("phone").scope["message_scroll"].range) < 1
        $ renpy.get_screen("phone").scope["message_scroll"].change(0)
        pause 0.2
        assert eval not renpy.get_screen("phone").scope["message_scroll"].follow_latest
        $ phone_messages.append({"who":"ria","out":False,"text":"기록을 읽는 동안 도착한 새 메시지입니다.","time":"12:32"})
        $ renpy.restart_interaction()
        pause 0.4
        assert eval renpy.get_screen("phone").scope["message_scroll"].value == 0
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_scroll_history_message_policy_v1") + ".png")
        click "최신 메시지"
        pause 0.3
        assert eval abs(renpy.get_screen("phone").scope["message_scroll"].value-renpy.get_screen("phone").scope["message_scroll"].range) < 1
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_scroll_latest_message_policy_v1") + ".png")
        click "유진"
        pause 0.2
        assert eval renpy.get_screen("phone").scope["message_scroll"].value == 0
        click "리아"
        pause 0.2
        assert eval abs(renpy.get_screen("phone").scope["message_scroll"].value-renpy.get_screen("phone").scope["message_scroll"].range) < 1

    testcase office_reply_marker:
        pause until screen "main_menu"
        run Preference("text speed",0)
        click "첫날 시작"
        run Jump("day02")
        advance until screen "phone"
        assert eval phone_contact_attention("seoyun", "d2_sy") == "reply"
        click "유진"
        assert eval renpy.get_screen("phone").scope["contact"] == "yujin"
        assert eval phone_contact_attention("seoyun", "d2_sy") == "reply"
        pause 0.6
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_reply_marker_other_red_v4_message_policy_v1") + ".png")
        click "서윤"
        assert eval phone_unread["seoyun"] == 0
        assert eval phone_contact_attention("seoyun", "d2_sy") == "reply"
        $ _marker_previous_motion = persistent.reduce_motion
        $ persistent.reduce_motion = True
        pause 0.4
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_reply_marker_still_red_v4_message_policy_v1") + ".png")
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        assert eval phone_contact_attention("seoyun", "d2_sy") is None
        pause 5.1
        assert eval not phone_pending
        $ persistent.reduce_motion = _marker_previous_motion
        click "계속"
        assert screen "say"





    testcase office_message_day_boundary:
        pause until screen "main_menu"
        $ _policy_cps = preferences.text_cps
        run Preference("text speed",0)
        click "첫날 시작"
        run Jump("d1_ending_home")
        advance until screen "day_result"
        assert eval day == 1 and clock == "21:30"
        assert eval all(phone_time_minutes(msg["time"]) <= phone_time_minutes(clock) for msg in phone_messages if msg.get("day") == day)
        $ _policy_events_before = list(phone_events)
        click "휴대폰 확인"
        pause 0.5
        assert eval phone_events == _policy_events_before
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_night_clock_policy_v1") + ".png")
        click "닫기"
        click "2일차로 계속"
        advance until screen "phone"
        pause 0.5
        assert eval day == 2 and clock == "09:05"
        assert eval "goodnight" not in phone_expired and phone_reply_available("goodnight")
        assert eval any(msg.get("event") == "goodnight" and msg.get("day") == 1 for msg in phone_messages)
        click "리아"
        assert eval phone_selected_reply("ria",None,"d2_sy") == "goodnight"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_next_day_reply_policy_v1") + ".png")
        click "어제 이야기 좋았어요. 다음에도 이어서 이야기해요."
        assert eval "goodnight" in phone_replied
        assert eval phone_messages[-1]["day"] == 2 and phone_messages[-1]["time"] == "09:05"
        run Function(start_week_day, 3, "다음 날 답장 도착 검수")
        pause 4.3
        assert eval not phone_pending
        assert eval phone_messages[-1]["day"] == 3 and phone_messages[-1]["time"] == "09:00"
        run FilePage("message-policy-qa")
        run FileSave(1,confirm=False)
        run OfficeFileLoad(1,confirm=False)
        assert eval phone_messages[-1]["day"] == 3 and phone_messages[-1]["time"] == clock
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run Preference("text speed",_policy_cps)

    testcase office_message_backlog:
        pause until screen "main_menu"
        $ _policy_cps = preferences.text_cps
        run Preference("text speed",0)
        click "첫날 시작"
        run Jump("_phone_policy_test_wait")
        run Function(send_message,"lunch_invite")
        run SetVariable("clock","12:30")
        assert eval phone_reply_available("lunch_invite")
        run SetVariable("clock","12:31")
        assert eval phone_reply_has_expired("lunch_invite")
        run Function(reply_message,"lunch_invite",message_data["lunch_invite"]["reply"][0])
        assert eval "lunch_invite" not in phone_replied and "lunch_plan" not in flags
        run Function(send_message,"goodnight")
        assert eval clock == "21:10"
        run Function(start_week_day,2,"안부 유지 검수")
        assert eval phone_reply_available("goodnight") and "lunch_invite" in phone_expired
        run Function(send_message,"d2_sy")
        run SetVariable("clock","09:31")
        assert eval not phone_reply_available("d2_sy")
        run Function(send_message,"d2_sy_night")
        assert eval clock == "20:40"
        run Function(start_week_day,3,"기한 만료 검수")
        run Function(send_message,"d3_ri")
        run Function(send_message,"d3_ri_night")
        assert eval clock == "21:00"
        run Function(start_week_day,4,"이전 미답장 검수")
        assert eval phone_reply_keys("ria") == ["d3_ri_night","goodnight"]
        assert eval phone_reply_available("d2_sy_night")
        assert eval all(key in phone_expired for key in ("lunch_invite","d2_sy","d3_ri"))
        $ _policy_history_count = len(phone_messages)
        run Show("phone",initial_contact="ria")
        pause 0.5
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_reply_backlog_latest_policy_v1") + ".png")
        click "다른 미답장 (2)"
        assert eval renpy.get_screen("phone").scope["selected_reply_key"] == "goodnight"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("phone_reply_backlog_older_policy_v1") + ".png")
        click "첫날 이야기 좋았어요. 다음에도 이어서 이야기해요."
        pause 4.3
        assert eval len(phone_messages) == _policy_history_count + 2
        assert eval phone_reply_keys("ria") == ["d3_ri_night"]
        $ _policy_affection_after = people["ria"]["affection"]
        click "수정 이유까지 남겨 두니 다시 보기도 편하겠어요."
        pause 4.3
        assert eval not phone_reply_keys("ria")
        assert eval people["ria"]["affection"] == _policy_affection_after
        assert eval "ri_analysis" not in flags
        assert eval phone_messages[-1]["day"] == 4 and phone_messages[-1]["time"] == "09:00"
        assert eval any(msg.get("event") == "lunch_invite" for msg in phone_messages)
        run Function(phone_expired.append,"d2_sy_night")
        run SetVariable("phone_event_days",{})
        run SetVariable("clock","08:00")
        run FilePage("message-policy-qa")
        run FileSave(2,confirm=False)
        run OfficeFileLoad(2,confirm=False)
        assert eval "d2_sy_night" not in phone_expired and phone_reply_available("d2_sy_night")
        assert eval phone_event_day("d2_sy_night") == 2
        assert eval clock == "09:00"
        assert eval "lunch_invite" in phone_expired
        run FileDelete(2,confirm=False)
        run FilePage(1)
        run Hide("phone")
        run Preference("text speed",_policy_cps)

    testcase office_message_legacy_times:
        pause until screen "main_menu"
        click "첫날 시작"
        run Jump("_phone_policy_test_wait")
        run SetVariable("day",2)
        run SetVariable("clock","09:05")
        run SetVariable("phone_events",["goodnight","d2_sy"])
        run SetVariable("phone_event_days",{})
        run SetVariable("phone_replied",["goodnight"])
        run SetVariable("phone_messages",[{"who":"ria","out":False,"text":"밤의 안부","time":"21:10","day":1,"event":"goodnight"},{"who":"ria","out":True,"text":"밤의 답장","time":"19:00","day":1,"id":"reply:goodnight"},{"who":"seoyun","out":False,"text":"아침 연락","time":"09:05","day":2,"event":"d2_sy"},{"who":"ria","out":False,"text":"다음 날 도착한 답장","time":"19:00","id":"reply:goodnight:response"}])
        run Function(phone_restore_message_policy)
        assert eval phone_messages[1]["time"] == "21:10"
        assert eval phone_messages[-1]["day"] == 2 and phone_messages[-1]["time"] == "09:05"
        assert eval clock == "09:05"
        assert eval phone_reply_available("d2_sy")

    testcase office_active_call:
        pause until screen "main_menu"
        run Preference("text speed",0)
        click "첫날 시작"
        run Jump("d1_evening_gate")
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        pause 0.45
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("incoming_auto_%s_v1" % ring_who) + ".png")
        click "받기"
        assert eval ui_call_contact == "ria"
        assert screen "say"
        assert not screen "phone"
        pause 0.5
        move pos (20, 20)
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("active_call_ria_auto_v5") + ".png")
        run FilePage("active-call-qa")
        run FileSave(1,confirm=False)
        assert eval renpy.get_save_data("active-call-qa-1")["ui_call_contact"] == "ria"
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_call_contact == "ria"
        run FileDelete(1,confirm=False)
        run FilePage(1)
        advance until screen "choice"
        assert eval ui_call_contact == "ria"
        pause 0.3
        move pos (20, 20)
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("active_call_choices_auto_v5") + ".png")
        click "카페에 들른다."
        assert eval ui_call_contact is None
        run Jump("day02")
        advance until screen "phone"
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        pause 5.1
        click "계속"
        advance until screen "choice"
        click "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "phone"
        click "오늘 점심은 쉬고 내일 오전에 같이 볼게요."
        pause 4.2
        click "계속"
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        pause 0.45
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("incoming_auto_%s_v1" % ring_who) + ".png")
        click "받기"
        assert eval ui_call_contact == "seoyun"
        pause 0.4
        move pos (20, 20)
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("active_call_seoyun_auto_v5") + ".png")
        advance until screen "day_result"
        assert eval ui_call_contact is None and flags["d2_sy_call"] == "answered"
        run Jump("day04")
        advance until screen "phone"
        click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
        pause 5.1
        click "계속"
        advance until screen "choice"
        click "각 시안의 목적을 듣고 첫 화면과 후속 화면을 구분한다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "choice"
        click "유진과 점심을 먹는다. (점심 / 호감 +5 / 스트레스 -5)"
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        pause 0.45
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("incoming_auto_%s_v1" % ring_who) + ".png")
        click "받기"
        assert eval ui_call_contact == "yujin"
        pause 0.4
        move pos (20, 20)
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("active_call_yujin_auto_v5") + ".png")
        click "통화 종료"
        advance
        advance
        pause 1.0
        assert eval ui_call_contact is None and flags["d4_yj_call"] == "answered"




    testcase office_call_cleanup:
        pause until screen "main_menu"
        run Preference("text speed",0)
        click "첫날 시작"
        pause 0.5
        assert eval ui_scene_actor is None
        assert eval renpy.get_displayable("office_portrait", "office_character") is None
        advance until screen "choice"
        assert eval ui_scene_actor == "ria"
        assert eval renpy.get_displayable("office_portrait", "office_character") is not None
        run Jump("d1_evening_gate")
        advance until screen "phone"
        pause 0.5
        click "받기"
        pause 0.5
        assert eval ui_call_contact == "ria" and not ui_call_ending
        move pos (20, 20)
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("call_single_end_button_v6_upscaled_v1") + ".png")
        click "통화 종료"
        pause 0.15
        assert eval ui_call_closing and not ui_call_ending and ui_call_contact == "ria"
        assert eval _last_say_who == "dh"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("call_farewell_request_v6_upscaled_v1") + ".png")
        advance
        assert eval _last_say_who == "ri" and ui_call_contact == "ria"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("call_farewell_ria_v6_upscaled_v1") + ".png")
        advance
        pause 0.15
        assert eval ui_call_ending and ui_call_contact == "ria"
        assert screen "say"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("call_ended_notice_v6_upscaled_v1") + ".png")
        pause 1.2
        assert eval ui_call_contact is None and not ui_call_ending
        assert eval ui_scene_key == "home" and ui_scene_actor is None
        assert eval renpy.get_displayable("office_portrait", "office_character") is None
        assert eval "사용자 종료" in phone_calls[-1]
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("call_ended_home_clean_v5_upscaled_v1") + ".png")
        advance
        advance
        advance
        assert eval ui_scene_key == "home"
        assert eval renpy.get_displayable("office_portrait", "office_character") is None
        run FilePage("call-cleanup-qa")
        run FileSave(1,confirm=False)
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_scene_actor is None
        assert eval renpy.get_displayable("office_portrait", "office_character") is None
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run Jump("d1_cafe")
        advance until screen "choice"
        pause 0.5
        assert eval ui_scene_actor == "ria"
        assert eval renpy.get_displayable("office_portrait", "office_character") is not None
        run SetVariable("ui_scene_actor", None)
        run FilePage("call-cleanup-qa")
        run FileSave(1,confirm=False)
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_scene_actor == "ria"
        run FileDelete(1,confirm=False)
        run FilePage(1)


    testcase office_call_farewells:
        pause until screen "main_menu"
        run Preference("text speed",0)
        click "첫날 시작"
        run Jump("d1_home")
        pause 0.5
        run Function(ui_phone_call_begin, "seoyun", "d1_home")
        pause 0.1
        click "통화 종료"
        assert eval ui_call_closing and not ui_call_ending
        assert eval _last_say_who == "dh"
        advance
        assert eval _last_say_who == "sy" and ui_call_contact == "seoyun"
        assert eval not ui_call_ending
        assert eval renpy.get_displayable("office_portrait", "office_character") is None
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("call_farewell_seoyun_v6") + ".png")
        advance
        pause 1.3
        assert eval ui_call_contact is None and not ui_call_closing and not ui_call_ending
        run Function(ui_phone_call_begin, "yujin", "d1_home")
        pause 0.1
        click "통화 종료"
        assert eval ui_call_closing and not ui_call_ending
        assert eval _last_say_who == "dh"
        advance
        assert eval _last_say_who == "yj" and ui_call_contact == "yujin"
        assert eval not ui_call_ending
        assert eval renpy.get_displayable("office_portrait", "office_character") is None
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("call_farewell_yujin_v6") + ".png")
        advance
        pause 1.3
        assert eval ui_call_contact is None and not ui_call_closing and not ui_call_ending
        run Function(ui_phone_call_begin, "jihyun", "d1_home")
        pause 0.1
        click "통화 종료"
        assert eval ui_call_closing and not ui_call_ending
        assert eval _last_say_who == "dh"
        advance
        assert eval _last_say_who == "jh" and ui_call_contact == "jihyun"
        assert eval not ui_call_ending
        assert eval renpy.get_displayable("office_portrait", "office_character") is None
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("call_farewell_jihyun_v6") + ".png")
        advance
        pause 1.3
        assert eval ui_call_contact is None and not ui_call_closing and not ui_call_ending


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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("motion_normal_B_v2_upscaled_v1") + ".png")
        run Function(ui_camera_set, "C")
        pause 0.1
        assert eval 1.0 < renpy.get_displayable("office_portrait", "office_character").state.zoom < 1.5
        # Numeric assertion verifies movement without a timing-dependent golden image.
        pause 0.5
        assert eval abs(renpy.get_displayable("office_portrait", "office_character").state.zoom - 1.5) < 0.01
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("motion_close_C_v2_upscaled_v1") + ".png")
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









    testcase office_bc_camera:
        pause until screen "main_menu"
        $ _bc_cps = preferences.text_cps
        run Preference("text speed",0)
        click "첫날 시작"
        advance until screen "choice"
        assert eval ui_camera_current() == "B"
        pause 0.4
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("bc_normal_choices_v2_upscaled_v1") + ".png")
        run Jump("d1_cafe")
        advance until screen "choice"
        assert eval ui_camera_current() == "C"
        pause 0.4
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("bc_emotional_choices_v2_upscaled_v1") + ".png")
        click "“현장 판단이 어떻게 나온 건지 더 듣고 싶어요.”"
        assert eval ui_camera_current() == "C"
        pause 0.4
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("bc_ria_close_v2_upscaled_v1") + ".png")
        run SetVariable("ui_speaker", "seoyun")
        pause 0.3
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("bc_seoyun_close_v2_upscaled_v1") + ".png")
        run SetVariable("ui_speaker", "yujin")
        pause 0.3
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("bc_yujin_close_v2_upscaled_v1") + ".png")
        run SetVariable("ui_speaker", "jihyun")
        pause 0.3
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("bc_jihyun_close_v2_upscaled_v1") + ".png")
        run Jump("d1_cafe_close")
        pause 0.3
        assert eval ui_camera_current() == "B"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("bc_return_normal_v2_upscaled_v1") + ".png")
        run Show("phone")
        pause 0.6
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\원화얼굴복구_검수_20261007\\' + ("bc_phone_clean_v3_upscaled_v1") + ".png")
        run Hide("phone")
        run Preference("text speed",_bc_cps)




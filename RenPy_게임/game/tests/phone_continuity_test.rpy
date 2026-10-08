testsuite office_phone_continuity_20261007:
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

    testcase late_personality:
        run Preference("text speed",0)
        click "첫날 시작"
        run Jump("_phone_policy_test_wait")
        run SetVariable("day",1)
        run Function(send_message,"goodnight")
        assert eval phone_reply_options("goodnight") == message_data["goodnight"]["reply"]
        run SetVariable("day",2)
        run SetVariable("clock","09:00")
        assert eval phone_reply_available("goodnight")
        $ _continuity_choice = phone_reply_options("goodnight")[0]
        assert eval _continuity_choice["response"] == phone_late_personality_responses["goodnight"][0]
        assert eval "set" not in _continuity_choice and "plan" not in _continuity_choice
        $ _continuity_flags_before = dict(flags)
        run Function(reply_message,"goodnight",_continuity_choice)
        assert eval flags == _continuity_flags_before
        assert eval phone_pending[-1]["text"] == _continuity_choice["response"]
        pause 5.2
        assert eval not phone_pending and phone_messages[-1]["text"] == _continuity_choice["response"]
        run SetVariable("day",2)
        run Function(send_message,"d2_sy_night")
        assert eval phone_reply_options("d2_sy_night") == message_data["d2_sy_night"]["reply"]
        run SetVariable("day",3)
        run SetVariable("clock","09:00")
        assert eval phone_reply_available("d2_sy_night")
        $ _continuity_choice = phone_reply_options("d2_sy_night")[0]
        assert eval _continuity_choice["response"] == phone_late_personality_responses["d2_sy_night"][0]
        assert eval "set" not in _continuity_choice and "plan" not in _continuity_choice
        $ _continuity_flags_before = dict(flags)
        run Function(reply_message,"d2_sy_night",_continuity_choice)
        assert eval flags == _continuity_flags_before
        assert eval phone_pending[-1]["text"] == _continuity_choice["response"]
        pause 5.2
        assert eval not phone_pending and phone_messages[-1]["text"] == _continuity_choice["response"]
        run SetVariable("day",3)
        run Function(send_message,"d3_ri_night")
        assert eval phone_reply_options("d3_ri_night") == message_data["d3_ri_night"]["reply"]
        run SetVariable("day",4)
        run SetVariable("clock","09:00")
        assert eval phone_reply_available("d3_ri_night")
        $ _continuity_choice = phone_reply_options("d3_ri_night")[0]
        assert eval _continuity_choice["response"] == phone_late_personality_responses["d3_ri_night"][0]
        assert eval "set" not in _continuity_choice and "plan" not in _continuity_choice
        $ _continuity_flags_before = dict(flags)
        run Function(reply_message,"d3_ri_night",_continuity_choice)
        assert eval flags == _continuity_flags_before
        assert eval phone_pending[-1]["text"] == _continuity_choice["response"]
        pause 5.2
        assert eval not phone_pending and phone_messages[-1]["text"] == _continuity_choice["response"]
        run SetVariable("day",4)
        run Function(send_message,"d4_yj_night")
        assert eval phone_reply_options("d4_yj_night") == message_data["d4_yj_night"]["reply"]
        run SetVariable("day",5)
        run SetVariable("clock","09:00")
        assert eval phone_reply_available("d4_yj_night")
        $ _continuity_choice = phone_reply_options("d4_yj_night")[0]
        assert eval _continuity_choice["response"] == phone_late_personality_responses["d4_yj_night"][0]
        assert eval "set" not in _continuity_choice and "plan" not in _continuity_choice
        $ _continuity_flags_before = dict(flags)
        run Function(reply_message,"d4_yj_night",_continuity_choice)
        assert eval flags == _continuity_flags_before
        assert eval phone_pending[-1]["text"] == _continuity_choice["response"]
        pause 5.2
        assert eval not phone_pending and phone_messages[-1]["text"] == _continuity_choice["response"]
        run SetVariable("day",5)
        run Function(send_message,"d5_jh_night")
        assert eval phone_reply_options("d5_jh_night") == message_data["d5_jh_night"]["reply"]
        run SetVariable("day",6)
        run SetVariable("clock","09:00")
        assert eval phone_reply_available("d5_jh_night")
        $ _continuity_choice = phone_reply_options("d5_jh_night")[0]
        assert eval _continuity_choice["response"] == phone_late_personality_responses["d5_jh_night"][0]
        assert eval "set" not in _continuity_choice and "plan" not in _continuity_choice
        $ _continuity_flags_before = dict(flags)
        run Function(reply_message,"d5_jh_night",_continuity_choice)
        assert eval flags == _continuity_flags_before
        assert eval phone_pending[-1]["text"] == _continuity_choice["response"]
        pause 5.2
        assert eval not phone_pending and phone_messages[-1]["text"] == _continuity_choice["response"]
        run SetVariable("day",5)
        assert eval phone_reply_options("d2_sy_night")[0]["text"] == "그때 나눠 맡으니 진행 상황도 정리하기 편했어요."
        assert eval phone_reply_options("goodnight")[0]["text"] == "첫날 이야기 좋았어요. 다음에도 이어서 이야기해요."

    testcase followup_state:
        run Preference("text speed",0)
        click "첫날 시작"
        run Jump("day02")
        advance until screen "phone"
        run Hide("phone")
        run Jump("_phone_policy_test_wait")
        run SetVariable("clock","18:30")
        $ renpy.session["phone_continuity_qa"] = {"affection":{who:person["affection"] for who,person in people.items()},"flags":dict(flags),"schedule":list(week_schedule)}
        run Function(phone_interrupted_call_followup,"seoyun","ui_d2_call_done")
        assert eval "계정 알림" in phone_messages[-1]["text"] and phone_messages[-1]["day"] == 2 and phone_messages[-1]["time"] == "18:30"
        assert eval phone_contact_attention("seoyun") == "unread"
        assert eval not phone_has_replies("seoyun")
        $ renpy.session["phone_continuity_qa"]["count"] = len(phone_messages)
        run Function(phone_interrupted_call_followup,"seoyun","ui_d2_call_done")
        assert eval len(phone_messages) == renpy.session["phone_continuity_qa"]["count"]
        run FilePage("phone-continuity-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run OfficeFileLoad(1,confirm=False)
        assert eval day == 2 and phone_messages[-1]["id"] == "hangup:2:seoyun:ui_d2_call_done"
        run Function(phone_interrupted_call_followup,"seoyun","ui_d2_call_done")
        assert eval len(phone_messages) == renpy.session["phone_continuity_qa"]["count"]
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run SetVariable("day",4)
        run SetVariable("clock","18:40")
        run Function(phone_interrupted_call_followup,"yujin","ui_d4_call_done")
        assert eval "자료 제목" in phone_messages[-1]["text"]
        assert eval phone_messages[-1]["day"] == 4 and phone_messages[-1]["time"] == "18:40"
        assert eval flags == renpy.session["phone_continuity_qa"]["flags"] and week_schedule == renpy.session["phone_continuity_qa"]["schedule"]
        assert eval {who:person["affection"] for who,person in people.items()} == renpy.session["phone_continuity_qa"]["affection"]
        run Show("phone",initial_contact="yujin")
        pause 0.5
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\통화후_용건문자.png')
        run Hide("phone")
        $ renpy.session["phone_continuity_qa"]["normal_count"] = len(phone_messages)
        run Function(ui_phone_call_begin,"ria","d1_home")
        run Function(ui_phone_call_end)
        assert eval len(phone_messages) == renpy.session["phone_continuity_qa"]["normal_count"]
        $ renpy.session.pop("phone_continuity_qa",None)

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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("call_farewell_seoyun_v6") + ".png")
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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("call_farewell_yujin_v6") + ".png")
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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("call_farewell_jihyun_v6") + ".png")
        advance
        pause 1.3
        assert eval ui_call_contact is None and not ui_call_closing and not ui_call_ending


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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("call_single_end_button_v6_upscaled_v1") + ".png")
        click "통화 종료"
        pause 0.15
        assert eval ui_call_closing and not ui_call_ending and ui_call_contact == "ria"
        assert eval _last_say_who == "dh"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("call_farewell_request_v6_upscaled_v1") + ".png")
        advance
        assert eval _last_say_who == "ri" and ui_call_contact == "ria"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("call_farewell_ria_v6_upscaled_v1") + ".png")
        advance
        pause 0.15
        assert eval ui_call_ending and ui_call_contact == "ria"
        assert screen "say"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("call_ended_notice_v6_upscaled_v1") + ".png")
        pause 1.2
        assert eval ui_call_contact is None and not ui_call_ending
        assert eval ui_scene_key == "home" and ui_scene_actor is None
        assert eval renpy.get_displayable("office_portrait", "office_character") is None
        assert eval "사용자 종료" in phone_calls[-1]
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("call_ended_home_clean_v5_upscaled_v1") + ".png")
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


    testcase office_active_call:
        pause until screen "main_menu"
        run Preference("text speed",0)
        click "첫날 시작"
        run Jump("d1_evening_gate")
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        pause 0.45
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("incoming_auto_%s_v1" % ring_who) + ".png")
        click "받기"
        assert eval ui_call_contact == "ria"
        assert screen "say"
        assert not screen "phone"
        pause 0.5
        move pos (20, 20)
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("active_call_ria_auto_v5") + ".png")
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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("active_call_choices_auto_v5") + ".png")
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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("incoming_auto_%s_v1" % ring_who) + ".png")
        click "받기"
        assert eval ui_call_contact == "seoyun"
        pause 0.4
        move pos (20, 20)
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("active_call_seoyun_auto_v5") + ".png")
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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("incoming_auto_%s_v1" % ring_who) + ".png")
        click "받기"
        assert eval ui_call_contact == "yujin"
        pause 0.4
        move pos (20, 20)
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("active_call_yujin_auto_v5") + ".png")
        click "통화 종료"
        advance
        advance
        pause 1.0
        assert eval ui_call_contact is None and flags["d4_yj_call"] == "answered"




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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("phone_night_clock_policy_v1") + ".png")
        click "닫기"
        click "2일차로 계속"
        advance until screen "phone"
        pause 0.5
        assert eval day == 2 and clock == "09:05"
        assert eval "goodnight" not in phone_expired and phone_reply_available("goodnight")
        assert eval any(msg.get("event") == "goodnight" and msg.get("day") == 1 for msg in phone_messages)
        click "리아"
        assert eval phone_selected_reply("ria",None,"d2_sy") == "goodnight"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("phone_next_day_reply_policy_v1") + ".png")
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
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("phone_reply_backlog_latest_policy_v1") + ".png")
        click "다른 미답장 (2)"
        assert eval renpy.get_screen("phone").scope["selected_reply_key"] == "goodnight"
        $ renpy.screenshot('C:\\Users\\user\\Desktop\\건\\오피스\\RenPy_게임\\샘플\\휴대폰대화연결_20261007\\' + ("phone_reply_backlog_older_policy_v1") + ".png")
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


label _phone_policy_test_wait:
    "휴대폰 기능 검수 중."
    jump _phone_policy_test_wait

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
    screenshot "phone_night_clock_policy_v1" max_pixel_difference 200
    click "닫기"
    click "2일차로 계속"
    advance until screen "phone"
    pause 0.5
    assert eval day == 2 and clock == "09:05"
    assert eval "goodnight" not in phone_expired and phone_reply_available("goodnight")
    assert eval any(msg.get("event") == "goodnight" and msg.get("day") == 1 for msg in phone_messages)
    click "리아"
    assert eval phone_selected_reply("ria",None,"d2_sy") == "goodnight"
    screenshot "phone_next_day_reply_policy_v1" max_pixel_difference 200
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
    exit

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
    screenshot "phone_reply_backlog_latest_policy_v1" max_pixel_difference 200
    click "다른 미답장 (2)"
    assert eval renpy.get_screen("phone").scope["selected_reply_key"] == "goodnight"
    screenshot "phone_reply_backlog_older_policy_v1" max_pixel_difference 200
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
    exit

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
    exit

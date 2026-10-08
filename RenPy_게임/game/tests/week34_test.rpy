init 98 python:
    def _w34_qa_seed(who):
        for key in names:
            people[key]["episode_stage"] = 1
            people[key]["affection"] = 32 if key == who else 10
            people[key]["trust"] = 33 if key == who else 12
        store.route_intent = who
        store.focus_interest = who if who in names else None
        store.focus_locked = True
        store.week2_finished = True
        store.day = 11

testsuite office_week34:
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

    testcase seoyun_full_week34:
        run Function(_w34_qa_seed,"seoyun")
        run Jump("week34_start")
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 11
        click "12일차로 계속"
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 12
        click "13일차로 계속"
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 13
        click "14일차로 계속"
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 14
        click "15일차로 계속"
        advance until screen "choice"
        click "체험과 예약을 나누고 추가 인력 조건을 함께 제안한다."
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "choice"
        assert eval w34_eligible("seoyun")
        click "서윤에게 개인적인 마음을 말한다."
        advance until screen "day_result"
        assert eval day == 15
        click "16일차로 계속"
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until eval ui_pose_current("seoyun") == "daily_a" and ui_scene_actor == "seoyun"
        pause 0.4
        screenshot "week34_seoyun_daily"
        advance until screen "day_result"
        assert eval w34_route == "seoyun" and people["seoyun"]["relationship"] == "none"
        assert eval ui_pose_overrides.get("seoyun") is None
        assert eval day == 16
        click "17일차로 계속"
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "choice"
        click "개인적인 약속이라고 짧게 말하고 자세한 이야기는 둘이 정한다."
        advance until screen "day_result"
        assert eval day == 17
        click "18일차로 계속"
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "choice"
        click "연인으로 만나고 싶다고 답한다."
        advance until screen "choice"
        click "서로 원하는지 확인하고 오늘은 시간을 더 함께 보낸다."
        advance until screen "w34_placeholder"
        assert eval ui_scene_actor is None and ui_camera_override is None and w34_outfit is None
        assert eval any(h.what == "(거사중)" for h in _history_list)
        assert eval not w34_seen_gaps and people["seoyun"]["photo_cap"] == 0
        screenshot "week34_seoyun_dialogue_gap" max_pixel_difference 200
        run FilePage("week34-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run SetVariable("w34_answer","friends")
        run OfficeFileLoad(1,confirm=False)
        pause until screen "w34_placeholder"
        assert eval w34_answer == "dating" and not w34_seen_gaps
        run FileDelete(1,confirm=False)
        run FilePage(1)
        click "(거사중)"
        advance until screen "day_result"
        assert eval w34_seen_gaps == ["seoyun_first"]
        assert eval day == 18
        click "19일차로 계속"
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "day_result"
        assert eval day == 19
        click "20일차로 계속"
        advance until screen "choice"
        click "서윤과 점심을 먹는다."
        advance until screen "choice"
        click "오늘도 서로의 뜻을 확인하고 함께 시간을 보낸다."
        advance until screen "w34_placeholder"
        assert eval ui_scene_actor is None and w34_outfit is None
        click "(거사중)"
        advance until screen "day_result"
        assert eval w34_seen_gaps == ["seoyun_first","seoyun_followup"]
        assert eval w34_finished and day == 20 and "C03" in completed_events and "C04" in completed_events
        assert eval all(people[x]["relationship"] == ("dating" if x == "seoyun" else "none") for x in names)
        assert eval all(people[x]["photo_cap"] == 0 for x in names)
        assert eval all(ui_pose_overrides.get(x) is None for x in names)

    testcase ria_full_week34:
        run Function(_w34_qa_seed,"ria")
        run Jump("week34_start")
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 11
        click "12일차로 계속"
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 12
        click "13일차로 계속"
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 13
        click "14일차로 계속"
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 14
        click "15일차로 계속"
        advance until screen "choice"
        click "체험과 예약을 나누고 추가 인력 조건을 함께 제안한다."
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "choice"
        assert eval w34_eligible("ria")
        click "리아에게 개인적인 마음을 말한다."
        advance until screen "day_result"
        assert eval day == 15
        click "16일차로 계속"
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until eval ui_pose_current("ria") == "daily_a" and ui_scene_actor == "ria"
        pause 0.4
        screenshot "week34_ria_daily"
        advance until screen "day_result"
        assert eval w34_route == "ria" and people["ria"]["relationship"] == "none"
        assert eval ui_pose_overrides.get("ria") is None
        assert eval day == 16
        click "17일차로 계속"
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "choice"
        click "개인적인 약속이라고 짧게 말하고 자세한 이야기는 둘이 정한다."
        advance until screen "day_result"
        assert eval day == 17
        click "18일차로 계속"
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "choice"
        click "연인으로 만나고 싶다고 답한다."
        advance until screen "choice"
        click "서로 원하는지 확인하고 오늘은 시간을 더 함께 보낸다."
        advance until screen "w34_placeholder"
        assert eval ui_scene_actor is None and ui_camera_override is None and w34_outfit is None
        assert eval any(h.what == "(거사중)" for h in _history_list)
        assert eval not w34_seen_gaps and people["ria"]["photo_cap"] == 0
        screenshot "week34_ria_dialogue_gap" max_pixel_difference 200
        click "(거사중)"
        advance until screen "day_result"
        assert eval w34_seen_gaps == ["ria_first"]
        assert eval day == 18
        click "19일차로 계속"
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "day_result"
        assert eval day == 19
        click "20일차로 계속"
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "choice"
        click "오늘도 서로의 뜻을 확인하고 함께 시간을 보낸다."
        advance until screen "w34_placeholder"
        assert eval ui_scene_actor is None and w34_outfit is None
        click "(거사중)"
        advance until screen "day_result"
        assert eval w34_seen_gaps == ["ria_first","ria_followup"]
        assert eval w34_finished and day == 20 and "C03" in completed_events and "C04" in completed_events
        assert eval all(people[x]["relationship"] == ("dating" if x == "ria" else "none") for x in names)
        assert eval all(people[x]["photo_cap"] == 0 for x in names)
        assert eval all(ui_pose_overrides.get(x) is None for x in names)

    testcase yujin_full_week34:
        run Function(_w34_qa_seed,"yujin")
        run Jump("week34_start")
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 11
        click "12일차로 계속"
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 12
        click "13일차로 계속"
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 13
        click "14일차로 계속"
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 14
        click "15일차로 계속"
        advance until screen "choice"
        click "체험과 예약을 나누고 추가 인력 조건을 함께 제안한다."
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "choice"
        assert eval w34_eligible("yujin")
        click "유진에게 개인적인 마음을 말한다."
        advance until screen "day_result"
        assert eval day == 15
        click "16일차로 계속"
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until eval ui_pose_current("yujin") == "daily_a" and ui_scene_actor == "yujin"
        pause 0.4
        screenshot "week34_yujin_daily"
        advance until screen "day_result"
        assert eval w34_route == "yujin" and people["yujin"]["relationship"] == "none"
        assert eval ui_pose_overrides.get("yujin") is None
        assert eval day == 16
        click "17일차로 계속"
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "choice"
        click "개인적인 약속이라고 짧게 말하고 자세한 이야기는 둘이 정한다."
        advance until screen "day_result"
        assert eval day == 17
        click "18일차로 계속"
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "choice"
        click "연인으로 만나고 싶다고 답한다."
        advance until screen "choice"
        click "서로 원하는지 확인하고 오늘은 시간을 더 함께 보낸다."
        advance until screen "w34_placeholder"
        assert eval ui_scene_actor is None and ui_camera_override is None and w34_outfit is None
        assert eval any(h.what == "(거사중)" for h in _history_list)
        assert eval not w34_seen_gaps and people["yujin"]["photo_cap"] == 0
        screenshot "week34_yujin_dialogue_gap" max_pixel_difference 200
        click "(거사중)"
        advance until screen "day_result"
        assert eval w34_seen_gaps == ["yujin_first"]
        assert eval day == 18
        click "19일차로 계속"
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "day_result"
        assert eval day == 19
        click "20일차로 계속"
        advance until screen "choice"
        click "유진과 점심을 먹는다."
        advance until screen "choice"
        click "오늘도 서로의 뜻을 확인하고 함께 시간을 보낸다."
        advance until screen "w34_placeholder"
        assert eval ui_scene_actor is None and w34_outfit is None
        click "(거사중)"
        advance until screen "day_result"
        assert eval w34_seen_gaps == ["yujin_first","yujin_followup"]
        assert eval w34_finished and day == 20 and "C03" in completed_events and "C04" in completed_events
        assert eval all(people[x]["relationship"] == ("dating" if x == "yujin" else "none") for x in names)
        assert eval all(people[x]["photo_cap"] == 0 for x in names)
        assert eval all(ui_pose_overrides.get(x) is None for x in names)

    testcase jihyun_full_week34:
        run Function(_w34_qa_seed,"jihyun")
        run Jump("week34_start")
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 11
        click "12일차로 계속"
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 12
        click "13일차로 계속"
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 13
        click "14일차로 계속"
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "choice"
        click "상대가 말한 범위를 존중하고 구체적인 확인 방법을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 14
        click "15일차로 계속"
        advance until screen "choice"
        click "체험과 예약을 나누고 추가 인력 조건을 함께 제안한다."
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "choice"
        assert eval w34_eligible("jihyun")
        click "지현에게 개인적인 마음을 말한다."
        advance until screen "day_result"
        assert eval day == 15
        click "16일차로 계속"
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until eval ui_pose_current("jihyun") == "daily_a" and ui_scene_actor == "jihyun"
        pause 0.4
        screenshot "week34_jihyun_daily"
        advance until screen "day_result"
        assert eval w34_route == "jihyun" and people["jihyun"]["relationship"] == "none"
        assert eval ui_pose_overrides.get("jihyun") is None
        assert eval day == 16
        click "17일차로 계속"
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "choice"
        click "개인적인 약속이라고 짧게 말하고 자세한 이야기는 둘이 정한다."
        advance until screen "day_result"
        assert eval day == 17
        click "18일차로 계속"
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "choice"
        click "연인으로 만나고 싶다고 답한다."
        advance until screen "choice"
        click "서로 원하는지 확인하고 오늘은 시간을 더 함께 보낸다."
        advance until screen "w34_placeholder"
        assert eval ui_scene_actor is None and ui_camera_override is None and w34_outfit is None
        assert eval any(h.what == "(거사중)" for h in _history_list)
        assert eval not w34_seen_gaps and people["jihyun"]["photo_cap"] == 0
        screenshot "week34_jihyun_dialogue_gap" max_pixel_difference 200
        click "(거사중)"
        advance until screen "day_result"
        assert eval w34_seen_gaps == ["jihyun_first"]
        assert eval day == 18
        click "19일차로 계속"
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "day_result"
        assert eval day == 19
        click "20일차로 계속"
        advance until screen "choice"
        click "지현과 점심을 먹는다."
        advance until screen "choice"
        click "오늘도 서로의 뜻을 확인하고 함께 시간을 보낸다."
        advance until screen "w34_placeholder"
        assert eval ui_scene_actor is None and w34_outfit is None
        click "(거사중)"
        advance until screen "day_result"
        assert eval w34_seen_gaps == ["jihyun_first","jihyun_followup"]
        assert eval w34_finished and day == 20 and "C03" in completed_events and "C04" in completed_events
        assert eval all(people[x]["relationship"] == ("dating" if x == "jihyun" else "none") for x in names)
        assert eval all(people[x]["photo_cap"] == 0 for x in names)
        assert eval all(ui_pose_overrides.get(x) is None for x in names)

    testcase defer_without_gap:
        run Function(_w34_qa_seed,"ria")
        run SetDict(people["ria"],"affection",50)
        run SetDict(people["ria"],"trust",55)
        run Function(w34_resolve_core,"ria")
        run Function(w34_set_route,"ria")
        run Function(start_week_day,18,"약속이 되는 마음")
        run Jump("week34_workday")
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        click "좋아하지만 관계를 정하는 데 시간이 더 필요하다고 말한다."
        advance until screen "day_result"
        assert eval not w34_seen_gaps and day == 18
        assert eval w34_answer == "defer"
        click "19일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        assert eval not w34_seen_gaps
        click "20일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        assert eval w34_finished and not w34_seen_gaps

    testcase friends_without_gap:
        run Function(_w34_qa_seed,"ria")
        run SetDict(people["ria"],"affection",50)
        run SetDict(people["ria"],"trust",55)
        run Function(w34_resolve_core,"ria")
        run Function(w34_set_route,"ria")
        run Function(start_week_day,18,"약속이 되는 마음")
        run Jump("week34_workday")
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        click "친구와 동료로 이어가고 싶다고 솔직히 말한다."
        advance until screen "day_result"
        assert eval not w34_seen_gaps and day == 18
        assert eval w34_answer == "friends"
        click "19일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        assert eval not w34_seen_gaps
        click "20일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        assert eval w34_finished and not w34_seen_gaps

    testcase slow_without_gap:
        run Function(_w34_qa_seed,"ria")
        run SetDict(people["ria"],"affection",50)
        run SetDict(people["ria"],"trust",55)
        run Function(w34_resolve_core,"ria")
        run Function(w34_set_route,"ria")
        run Function(start_week_day,18,"약속이 되는 마음")
        run Jump("week34_workday")
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        click "연인으로 만나고 싶다고 답한다."
        advance until screen "choice"
        click "오늘은 돌아가고 다음 만남을 잡는다."
        advance until screen "day_result"
        assert eval not w34_seen_gaps and day == 18
        assert eval w34_answer == "dating"
        click "19일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        assert eval not w34_seen_gaps
        click "20일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        click "이번 주는 여기까지 하고 다음 약속을 잡는다."
        advance until screen "day_result"
        assert eval w34_finished and not w34_seen_gaps

    testcase team_and_unresolved_core:
        run Function(_w34_qa_seed,"team")
        run Jump("week34_start")
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        click "오늘은 답을 미루고 핵심 문제를 보류한다."
        advance until screen "day_result"
        click "12일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        click "오늘은 답을 미루고 핵심 문제를 보류한다."
        advance until screen "day_result"
        click "13일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        click "오늘은 답을 미루고 핵심 문제를 보류한다."
        advance until screen "day_result"
        click "14일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        click "오늘은 답을 미루고 핵심 문제를 보류한다."
        advance until screen "day_result"
        click "15일차로 계속"
        advance until screen "choice"
        click "현 규모를 지키고 다음 공개 일정으로 확대를 제안한다."
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "choice"
        assert eval not any(w34_eligible(x) for x in names)
        click "이번에는 팀과 내 일상에 집중한다."
        advance until screen "day_result"
        click "16일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        click "17일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        click "18일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        click "19일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        click "20일차로 계속"
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        assert eval w34_finished and w34_route == "team" and not w34_seen_gaps
        assert eval all(p["relationship"] == "none" and not p["core_resolved"] for p in people.values())

    testcase day11_existing_checkpoint_continues:
        run Function(_w34_qa_seed,"team")
        run Jump("week3_direction_start")
        advance until screen "choice"
        click "지금은 팀과 나의 일에 집중한다."
        advance until screen "day_result"
        assert eval day == 11 and not w34_started
        click "11일차 이야기 계속"
        advance until screen "choice"
        assert eval w34_started and day == 11

init 98 python:
    def _w56_qa_seed(who,answer="dating",trust=70,project=40,old_breach=False):
        store.w34_route = who
        store.w34_answer = answer
        store.w34_finished = True
        stats["project"] = project
        if who in names:
            people[who].update(affection=75,trust=trust,episode_stage=4,core_resolved=True,relationship="dating" if answer == "dating" else "none",breach=old_breach)
            flags[w34_core_flags[who]] = True
            complete_week_event(w34_codes[who]+"04",who,stage=4)

testsuite office_week56:
    setup:
        pause until screen "main_menu"
        run Preference("text speed",0)
        run Preference("auto-forward","disable")
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        click "첫날 시작"
        advance until screen "choice"
    teardown:
        exit

    testcase seoyun_good:
        run Function(_w56_qa_seed,"seoyun","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "seoyun" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        run FilePage("week56-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run SetVariable("w56_focus","team")
        run SetDict(stats,"project",0)
        run OfficeFileLoad(1,confirm=False)
        pause until screen "day_result"
        assert eval w56_focus == "seoyun" and stats["project"] == 59 and w56_commitment == "together"
        run FileDelete(1,confirm=False)
        run FilePage(1)
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "choice"
        assert eval w56_ending_kind == "good" and w56_can_final_gap()
        click "서로의 뜻을 확인하고 프로젝트 이후의 시간을 함께 보낸다."
        pause until eval _last_say_what == "상대도 지금 함께 있고 싶다고 답했다. 다음 만남의 대답까지 먼저 정하지는 않았다."
        keysym "K_SPACE"
        pause until screen "w34_placeholder"
        assert eval w34_gap_page == 1 and w34_gap_token == "seoyun_final" and ui_scene_actor is None
        click "(거사중)"
        pause 0.1
        assert eval w34_gap_page == 2 and w34_gap_token == "seoyun_final" and ui_scene_actor is None
        click "(거사중)"
        pause 0.1
        assert eval w34_gap_page == 3 and w34_gap_token == "seoyun_final" and ui_scene_actor is None
        click "(거사중)"
        pause 0.1
        assert eval w34_gap_page == 4 and w34_gap_token == "seoyun_final" and ui_scene_actor is None
        click "(거사중)"
        pause 0.1
        assert eval w34_gap_page == 5 and w34_gap_token == "seoyun_final" and ui_scene_actor is None
        click "(거사중)"
        pause 0.1
        assert eval w56_final_gap and "seoyun_final" in w34_seen_gaps
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "good"
        assert eval w56_ending_id == "seoyun_good" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        screenshot "week56_seoyun_good_endcard" max_pixel_difference 200
        click "제목으로"
        pause until screen "main_menu"

    testcase seoyun_open:
        run Function(_w56_qa_seed,"seoyun","defer",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "seoyun" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval people["seoyun"]["relationship"] == "none"
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "open"
        assert eval w56_ending_id == "seoyun_open" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase seoyun_distance:
        run Function(_w56_qa_seed,"seoyun","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "일이 끝날 때까지 연락을 미루고 뒤늦게 설명한다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["19:20","19:21"]
        assert eval all(m["day"] == 22 and m["who"] == "seoyun" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "업무 밖의 약속은 없었다고 부정한다."
        advance until screen "day_result"
        assert eval day == 24
        assert eval people["seoyun"]["breach"] and people["seoyun"]["relationship"] == "paused"
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "답을 더 미루고 지금은 거리를 두겠다고 말한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval w56_commitment == "apart" and not w34_can_gap()
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "distance"
        assert eval w56_ending_id == "seoyun_distance" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase ria_good:
        run Function(_w56_qa_seed,"ria","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "ria" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "choice"
        assert eval w56_ending_kind == "good" and w56_can_final_gap()
        click "오늘은 돌아가고 다음 약속을 남긴다."
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "good"
        assert eval w56_ending_id == "ria_good" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        screenshot "week56_ria_good_endcard" max_pixel_difference 200
        click "제목으로"
        pause until screen "main_menu"

    testcase ria_open:
        run Function(_w56_qa_seed,"ria","defer",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "ria" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval people["ria"]["relationship"] == "none"
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "open"
        assert eval w56_ending_id == "ria_open" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase ria_distance:
        run Function(_w56_qa_seed,"ria","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "일이 끝날 때까지 연락을 미루고 뒤늦게 설명한다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["19:20","19:21"]
        assert eval all(m["day"] == 22 and m["who"] == "ria" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "업무 밖의 약속은 없었다고 부정한다."
        advance until screen "day_result"
        assert eval day == 24
        assert eval people["ria"]["breach"] and people["ria"]["relationship"] == "paused"
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "답을 더 미루고 지금은 거리를 두겠다고 말한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval w56_commitment == "apart" and not w34_can_gap()
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "distance"
        assert eval w56_ending_id == "ria_distance" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase yujin_good:
        run Function(_w56_qa_seed,"yujin","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "yujin" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "choice"
        assert eval w56_ending_kind == "good" and w56_can_final_gap()
        click "오늘은 돌아가고 다음 약속을 남긴다."
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "good"
        assert eval w56_ending_id == "yujin_good" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        click "제목으로"
        pause until screen "main_menu"

    testcase yujin_open:
        run Function(_w56_qa_seed,"yujin","defer",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "yujin" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval people["yujin"]["relationship"] == "none"
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "open"
        assert eval w56_ending_id == "yujin_open" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase yujin_distance:
        run Function(_w56_qa_seed,"yujin","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "일이 끝날 때까지 연락을 미루고 뒤늦게 설명한다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["19:20","19:21"]
        assert eval all(m["day"] == 22 and m["who"] == "yujin" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "업무 밖의 약속은 없었다고 부정한다."
        advance until screen "day_result"
        assert eval day == 24
        assert eval people["yujin"]["breach"] and people["yujin"]["relationship"] == "paused"
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "답을 더 미루고 지금은 거리를 두겠다고 말한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval w56_commitment == "apart" and not w34_can_gap()
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "distance"
        assert eval w56_ending_id == "yujin_distance" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase jihyun_good:
        run Function(_w56_qa_seed,"jihyun","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "jihyun" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "choice"
        assert eval w56_ending_kind == "good" and w56_can_final_gap()
        click "오늘은 돌아가고 다음 약속을 남긴다."
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "good"
        assert eval w56_ending_id == "jihyun_good" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        click "제목으로"
        pause until screen "main_menu"

    testcase jihyun_open:
        run Function(_w56_qa_seed,"jihyun","defer",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "jihyun" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval people["jihyun"]["relationship"] == "none"
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "open"
        assert eval w56_ending_id == "jihyun_open" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase jihyun_distance:
        run Function(_w56_qa_seed,"jihyun","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "일이 끝날 때까지 연락을 미루고 뒤늦게 설명한다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["19:20","19:21"]
        assert eval all(m["day"] == 22 and m["who"] == "jihyun" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "업무 밖의 약속은 없었다고 부정한다."
        advance until screen "day_result"
        assert eval day == 24
        assert eval people["jihyun"]["breach"] and people["jihyun"]["relationship"] == "paused"
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "답을 더 미루고 지금은 거리를 두겠다고 말한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval w56_commitment == "apart" and not w34_can_gap()
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "distance"
        assert eval w56_ending_id == "jihyun_distance" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase quality_open:
        run Function(_w56_qa_seed,"ria","dating",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "ria" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        click "27일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "open"
        assert eval w56_ending_id == "ria_open" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 60
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase repaired_return:
        run Function(_w56_qa_seed,"ria","dating",80,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "일이 끝날 때까지 연락을 미루고 뒤늦게 설명한다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["19:20","19:21"]
        assert eval all(m["day"] == 22 and m["who"] == "ria" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "업무 밖의 약속은 없었다고 부정한다."
        advance until screen "day_result"
        assert eval day == 24
        assert eval people["ria"]["breach"] and people["ria"]["relationship"] == "paused"
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "choice"
        assert eval not w56_breaks and not people["ria"]["breach"] and people["ria"]["relationship"] == "paused"
        run Function(w56_break,"w56_late_contact")
        assert eval not w56_breaks and not people["ria"]["breach"]
        click "서로 뜻을 확인하고 관계를 다시 이어간다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval not people["ria"]["breach"] and people["ria"]["relationship"] == "dating"
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "choice"
        assert eval w56_ending_kind == "good" and w56_can_final_gap()
        click "오늘은 돌아가고 다음 약속을 남긴다."
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "good"
        assert eval w56_ending_id == "ria_good" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        screenshot "week56_ria_good_endcard" max_pixel_difference 200
        click "제목으로"
        pause until screen "main_menu"

    testcase friend_stays_friend:
        run Function(_w56_qa_seed,"yujin","friends",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "yujin" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval people["yujin"]["relationship"] == "none"
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "distance"
        assert eval w56_ending_id == "yujin_distance" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        assert eval w34_answer == "friends" and people["yujin"]["relationship"] == "none"
        click "제목으로"
        pause until screen "main_menu"

    testcase old_breach_preserved:
        run Function(_w56_qa_seed,"jihyun","dating",70,40,True)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        advance until screen "day_result"
        assert eval day == 22
        assert eval [m["time"] for m in phone_messages if m.get("id","").startswith("w56_" )] == ["16:30","16:31"]
        assert eval all(m["day"] == 22 and m["who"] == "jihyun" for m in phone_messages if m.get("id","").startswith("w56_"))
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "개인적인 약속이 있었다고만 말하고 자세한 내용은 공개하지 않는다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "choice"
        click "미룬 말까지 솔직히 꺼내고 다음 약속을 함께 정한다."
        advance until screen "day_result"
        assert eval day == 26
        assert eval people["jihyun"]["breach"]
        click "27일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "프로젝트가 끝나도 개인적으로 계속 만나고 싶다고 말한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "distance"
        assert eval w56_ending_id == "jihyun_distance" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 72
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase team_40:
        run Function(_w56_qa_seed,"team","friends",70,40,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 22
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "day_result"
        assert eval day == 26
        click "27일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "team"
        assert eval w56_ending_id == "team" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 60
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase team_10:
        run Function(_w56_qa_seed,"team","friends",70,10,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 22
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "day_result"
        assert eval day == 26
        click "27일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "team"
        assert eval w56_ending_id == "team" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 30
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase team_0:
        run Function(_w56_qa_seed,"team","friends",70,0,False)
        run Jump("week56_start")
        advance until screen "day_result"
        assert eval day == 21
        click "22일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 22
        click "23일차로 계속"
        advance until screen "day_result"
        assert eval day == 23
        click "24일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 24
        click "25일차로 계속"
        advance until screen "day_result"
        assert eval day == 25
        click "26일차로 계속"
        advance until screen "day_result"
        assert eval day == 26
        click "27일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 27
        click "28일차로 계속"
        advance until screen "day_result"
        assert eval day == 28
        click "29일차로 계속"
        advance until screen "choice"
        click "추가 확인 없이 지금 추측한 안으로 진행한다."
        advance until screen "day_result"
        assert eval day == 29
        click "30일차로 계속"
        advance until screen "w56_endcard"
        assert eval day == 30 and w56_finished and w56_ending_kind == "team"
        assert eval w56_ending_id == "team" and w56_ending_id in persistent.office_endings
        assert eval "C05" in completed_events and "C06" in completed_events
        assert eval stats["project"] == 20
        assert eval not any(ui_pose_overrides.get(x) for x in names) and ui_scene_actor is None
        assert eval all(p["photo_cap"] == 0 for p in people.values())
        assert eval not w56_final_gap and not w56_can_final_gap()
        click "제목으로"
        pause until screen "main_menu"

    testcase existing_day20_checkpoint:
        run Function(_w56_qa_seed,"team","friends")
        run Function(start_week_day,20,"약속이 되는 마음")
        run Jump("week34_workday")
        advance until screen "choice"
        click "혼자 쉬며 오늘의 생각을 정리한다."
        advance until screen "day_result"
        assert eval day == 20 and not w56_started
        click "21일차로 계속"
        advance until screen "day_result"
        assert eval day == 21 and w56_started and w56_focus == "team"

    testcase early_phone_time:
        run Function(_w56_qa_seed,"ria")
        run Function(w56_begin)
        run Function(start_week_day,22,"미뤄지는 시간")
        run Jump("week56_workday")
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "지금 연락하고 만날 시간을 함께 바꾼다."
        pause until eval clock == "16:31"
        assert eval phone_messages[-1]["time"] == clock and phone_messages[-1]["day"] == day == 22
        assert eval phone_messages[-1]["who"] == "ria" and not phone_messages[-1]["out"]
        run Show("phone",initial_contact="ria")
        pause until screen "phone"
        pause 0.4
        screenshot "week56_early_phone_time" max_pixel_difference 200
        run Hide("phone")
        advance until screen "day_result"
        assert eval clock == "21:30" and day == 22

    testcase late_phone_time:
        run Function(_w56_qa_seed,"ria")
        run Function(w56_begin)
        run Function(start_week_day,22,"미뤄지는 시간")
        run Jump("week56_workday")
        advance until screen "choice"
        click "확인한 근거와 가능한 범위를 적고 수정한다."
        advance until screen "choice"
        click "일이 끝날 때까지 연락을 미루고 뒤늦게 설명한다."
        pause until eval clock == "19:21"
        assert eval phone_messages[-1]["time"] == clock and phone_messages[-1]["day"] == day == 22
        assert eval phone_messages[-1]["who"] == "ria" and not phone_messages[-1]["out"]
        run Show("phone",initial_contact="ria")
        pause until screen "phone"
        pause 0.4
        screenshot "week56_late_phone_time" max_pixel_difference 200
        run Hide("phone")
        advance until screen "day_result"
        assert eval clock == "21:30" and day == 22

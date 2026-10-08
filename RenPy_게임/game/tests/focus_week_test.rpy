init 98 python:
    def _focus_qa_common_minimum():
        # A real common first week awards at least +2 trust to each person at shared lunch.
        for who in names:
            people[who]["trust"] = max(12,people[who]["trust"])
            intro_seen[who] = 5

testsuite office_focus_week_20261007:
    setup:
        pause until screen "main_menu"
        run Preference("text speed",0)
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        pause 0.3
        click "첫날 시작"
        advance until screen "choice"
        run Function(_focus_qa_common_minimum)
        run Jump("day06")
    teardown:
        exit

    testcase earned_switch_and_save:
        advance until screen "choice"
        pause 0.25
        screenshot "week2_initial_interest_20261007" max_pixel_difference 200
        click "서윤을 조금 더 알아본다."
        assert eval focus_interest == "seoyun" and route_intent is None
        advance until screen "choice"
        pause 0.25
        click "리아와 조금 더 이야기한다."
        advance until screen "phone"
        pause 0.65
        assert eval renpy.get_screen("phone").scope["contact"] == "ria"
        click "저도 비슷한 경험이 있어요. 같이 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "day_result"
        assert eval day == 6 and focus_interest == "seoyun"
        assert eval focus_days["ria"] == [6] and not focus_eligible("ria")
        assert eval focus_open["ria"] and not focus_candidates()
        $ _focus_saved_trust = people["ria"]["trust"]
        run SetDict(people["ria"],"trust",100)
        assert eval not focus_eligible("ria")
        run SetDict(people["ria"],"trust",_focus_saved_trust)
        click "7일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "리아와 조금 더 이야기한다."
        advance until screen "phone"
        pause 0.65
        assert eval renpy.get_screen("phone").scope["contact"] == "ria"
        click "저도 비슷한 경험이 있어요. 같이 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        assert eval day == 7 and focus_interest == "seoyun"
        assert eval ui_scene_key == "home" and ui_scene_actor is None
        assert eval focus_eligible("ria") and focus_days["ria"] == [6,7]
        screenshot "week2_earned_change_20261007" max_pixel_difference 200
        run FilePage("focus-week-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run SetVariable("focus_interest","jihyun")
        run SetDict(focus_open,"ria",False)
        run OfficeFileLoad(1,confirm=False)
        assert eval focus_interest == "seoyun" and focus_eligible("ria")
        assert eval len(focus_history) == 1 and focus_days["ria"] == [6,7]
        run FileDelete(1,confirm=False)
        run FilePage(1)
        run Show("relationship_panel")
        pause 0.5
        screenshot "week2_relationship_interest_20261007" max_pixel_difference 200
        run Hide("relationship_panel")
        click "리아에게 조금 더 시간을 쓰고 싶다."
        advance until screen "day_result"
        assert eval focus_interest == "ria" and len(focus_history) == 2
        assert eval focus_history[-1]["from"] == "seoyun" and focus_history[-1]["reason"] == "shared_time"
        assert eval all(p["relationship"] == "none" and not p["core_resolved"] for p in people.values())
        $ _focus_affection_before = people["ria"]["affection"]
        run Function(focus_record,"ria","lunch",True)
        assert eval people["ria"]["affection"] == _focus_affection_before and focus_days["ria"] == [6,7]
        click "8일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "지현과 조금 더 이야기한다."
        advance until screen "phone"
        pause 0.65
        assert eval renpy.get_screen("phone").scope["contact"] == "jihyun"
        click "저도 비슷한 경험이 있어요. 같이 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "day_result"
        assert eval day == 8 and focus_interest == "ria" and not focus_eligible("jihyun")
        click "9일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "지현과 조금 더 이야기한다."
        advance until screen "phone"
        pause 0.65
        assert eval renpy.get_screen("phone").scope["contact"] == "jihyun"
        click "저도 비슷한 경험이 있어요. 같이 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        assert eval focus_interest == "ria" and focus_eligible("jihyun")
        click "지현에게 조금 더 시간을 쓰고 싶다."
        advance until screen "day_result"
        assert eval focus_interest == "jihyun" and len(focus_history) == 3
        click "10일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "확인된 첫 흐름부터 짧게 시험한다."
        advance until screen "choice"
        pause 0.25
        click "오늘은 혼자 쉬며 생각을 정리한다."
        advance until screen "day_result"
        assert eval week2_finished and "C02" in completed_events and stats["project"] == 10
        assert eval not focus_locked and route_intent is None and focus_interest == "jihyun"
        click "11일차로 계속"
        advance until screen "choice"
        pause 0.25
        assert eval not focus_eligible("yujin") and focus_eligible("jihyun")
        click "지현과 더 깊게 알아가는 방향으로 간다."
        advance until screen "day_result"
        assert eval day == 11 and focus_locked and route_intent == "jihyun"
        assert eval not focus_candidates()
        assert eval all(p["relationship"] == "none" and not p["core_resolved"] and p["photo_cap"] == 0 for p in people.values())

    testcase undecided_and_team:
        advance until screen "choice"
        pause 0.25
        click "아직 정하지 않고 더 이야기해 본다."
        advance until screen "choice"
        pause 0.25
        click "오늘은 혼자 쉬며 생각을 정리한다."
        advance until screen "day_result"
        assert eval day == 6 and focus_interest is None and not focus_candidates()
        click "7일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "오늘은 혼자 쉬며 생각을 정리한다."
        advance until screen "day_result"
        assert eval focus_interest is None
        click "8일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "오늘은 혼자 쉬며 생각을 정리한다."
        advance until screen "day_result"
        click "9일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "오늘은 혼자 쉬며 생각을 정리한다."
        advance until screen "day_result"
        click "10일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "흐름이 끊긴 곳을 먼저 재현한다."
        advance until screen "choice"
        pause 0.25
        click "오늘은 혼자 쉬며 생각을 정리한다."
        advance until screen "day_result"
        assert eval week2_finished and focus_interest is None and not focus_candidates()
        assert eval all(not focus_days[w] for w in names)
        click "11일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "지금은 팀과 나의 일에 집중한다."
        advance until screen "day_result"
        assert eval route_intent == "team" and focus_locked
        assert eval all(p["relationship"] == "none" for p in people.values())


    testcase undecided_to_yujin:
        advance until screen "choice"
        pause 0.25
        click "아직 정하지 않고 더 이야기해 본다."
        advance until screen "choice"
        pause 0.25
        click "유진과 조금 더 이야기한다."
        advance until screen "phone"
        pause 0.65
        click "저도 비슷한 경험이 있어요. 같이 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "day_result"
        assert eval focus_interest is None and not focus_eligible("yujin")
        click "7일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "유진과 조금 더 이야기한다."
        advance until screen "phone"
        pause 0.65
        click "저도 비슷한 경험이 있어요. 같이 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        assert eval focus_interest is None and focus_eligible("yujin")
        assert eval ui_scene_key == "home" and ui_scene_actor is None
        click "유진에게 조금 더 시간을 쓰고 싶다."
        advance until screen "day_result"
        assert eval focus_interest == "yujin" and focus_days["yujin"] == [6,7]
        assert eval focus_history[-1]["from"] is None and focus_history[-1]["to"] == "yujin"
        click "8일차로 계속"
        advance until screen "choice"
        pause 0.25
        click "유진과 조금 더 이야기한다."
        advance until screen "phone"
        pause 0.65
        click "그 이야기를 조금 더 듣고 싶어요."
        pause 5.2
        click "계속"
        advance until screen "day_result"
        assert eval day == 8 and focus_interest == "yujin" and focus_days["yujin"] == [6,7,8]
        assert eval not focus_locked and route_intent is None

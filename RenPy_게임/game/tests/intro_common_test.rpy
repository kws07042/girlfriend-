testsuite office_week:
    setup:
        pause until screen "main_menu"
        run Preference("text speed",0)
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        pause 0.3
        click "첫날 시작"
    teardown:
        exit

    testcase shared_and_answers:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "phone"
        pause 0.25
        click "좋아요. 다 같이 먹으면서 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "“작은 공연 보러 가는 걸 좋아해요.”"
        advance until screen "phone"
        pause 0.25
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "“현장 판단이 어떻게 나온 건지 더 듣고 싶어요.”"
        advance until screen "day_result"
        pause 0.25
        assert eval day == 1 and focus_interest is None and not focus_history
        assert eval all(intro_seen[w] == 1 for w in names)
        assert eval flags["first_lunch"] == "group" and flags["first_evening"] == "group"
        assert eval all("w1_night_"+w in phone_events for w in names)
        click "2일차로 계속"
        advance until screen "phone"
        pause 0.25
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "phone"
        pause 0.25
        click "약속대로 갈게요. 밥부터 먹어요."
        pause 5.2
        click "계속"
        advance until screen "phone"
        pause 0.25
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "“사람들 이야기를 듣고 나서 제 속도를 찾아요.”"
        advance until screen "day_result"
        pause 0.25
        assert eval all(intro_seen[w] == 2 for w in names) and focus_interest is None
        assert eval not ui_call_contact and not ring_pending
        click "3일차로 계속"
        advance until screen "phone"
        pause 0.25
        click "예상과 달랐던 반응부터 같이 볼까요?"
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "관찰과 가설을 구분하고 리아에게 기록법을 설명해 달라고 한다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "choice"
        pause 0.25
        assert eval flags["jh_private_movie"] and week_lunch == "jihyun"
        click "회사 앞 카페에서 잠깐 혼자 쉰다. (저녁 / 감각 +3 / 스트레스 -8)"
        advance until screen "day_result"
        pause 0.25
        assert eval all(intro_seen[w] == 3 for w in names) and focus_interest is None
        click "4일차로 계속"
        advance until screen "phone"
        pause 0.25
        click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "각 시안의 목적을 듣고 첫 화면과 후속 화면을 구분한다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "phone"
        pause 0.25
        assert eval week_lunch == "yujin"
        click "지금은 받지 않기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "“손에 익으면 바꿀 때도 망설여져요.”"
        advance until screen "day_result"
        pause 0.25
        assert eval all(intro_seen[w] == 4 for w in names) and focus_interest is None
        click "5일차로 계속"
        advance until screen "phone"
        pause 0.25
        click "첫 방문부터 재방문까지 단계별로 정리하겠습니다."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "경험을 단계별로 적고 각 단계의 담당과 확인 방법을 정한다. (오전 / 프로젝트 +10)"
        advance until screen "choice"
        pause 0.25
        click "“한 말을 되짚다가 못 한 말까지 생각해요.”"
        advance until screen "day_result"
        pause 0.25
        assert eval day == 5 and week_finished and all(intro_seen[w] == 5 for w in names)
        assert eval not focus_history and focus_interest is None and route_intent is None
        assert eval all(p["relationship"] == "none" and not p["core_resolved"] for p in people.values())
        assert eval all("intro_lunch_"+w in completed_events for w in names)
        assert eval flags["sy_private_book"] and flags["jh_private_movie"] and flags["yj_private_cup"]
        assert eval not ui_call_contact and not ring_pending
        screenshot "week1_all_common_result_20261007" max_pixel_difference 200
        click "6일차로 계속"
        advance until screen "choice"
        pause 0.25
        assert eval day == 6 and focus_interest is None and not focus_history

    testcase shared_and_boundaries:
        advance until screen "choice"
        pause 0.25
        click "“앞으로 잘 부탁드립니다. 자료부터 확인할게요.”"
        advance until screen "choice"
        pause 0.25
        click "자료를 받아 혼자 요구사항 초안을 먼저 작성한다."
        advance until screen "phone"
        pause 0.25
        click "물 한 잔 마시고 갈게요. 자리에서 뵈어요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "“조용한 곳에서 걷거나 책을 읽어요.”"
        advance until screen "phone"
        pause 0.25
        click "지금은 받지 않기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "“오늘은 일 얘기 쉬어도 돼요. 다음에 이어서 듣죠.”"
        advance until screen "day_result"
        pause 0.25
        assert eval day == 1 and focus_interest is None and not focus_history
        assert eval all(intro_seen[w] == 1 for w in names)
        assert eval flags["first_lunch"] == "group" and flags["first_evening"] == "group"
        assert eval all("w1_night_"+w in phone_events for w in names)
        click "2일차로 계속"
        advance until screen "phone"
        pause 0.25
        click "전체 흐름부터 보고 궁금한 부분을 물어볼게요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "제가 전부 정리하겠다고 제안한 뒤 담당 권한을 다시 묻는다. (오전 / 호감 +5 / 신뢰 +6)"
        advance until screen "phone"
        pause 0.25
        click "오늘은 밥만 먹고, 자료는 내일 오전에 볼까요?"
        pause 5.2
        click "계속"
        advance until screen "phone"
        pause 0.25
        click "지금은 받지 않기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "“직접 걸어 봐야 익숙해지는 편이에요.”"
        advance until screen "day_result"
        pause 0.25
        assert eval all(intro_seen[w] == 2 for w in names) and focus_interest is None
        assert eval not ui_call_contact and not ring_pending
        click "3일차로 계속"
        advance until screen "phone"
        pause 0.25
        click "현장에서 어떻게 기록했는지 궁금해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "성공한 숫자부터 쓰자고 했다가 실패한 기록도 함께 남긴다. (오전 / 호감 +5 / 신뢰 +6)"
        advance until screen "choice"
        pause 0.25
        assert eval flags["jh_private_movie"] and week_lunch == "jihyun"
        click "집에 돌아가 충분히 쉰다. (저녁 / 스트레스 -15)"
        advance until screen "day_result"
        pause 0.25
        assert eval all(intro_seen[w] == 3 for w in names) and focus_interest is None
        click "4일차로 계속"
        advance until screen "phone"
        pause 0.25
        click "사용자가 처음 보는 순서부터 함께 읽어 볼게요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "취향으로 A를 고른 뒤 첫 사용자의 목적을 다시 확인한다. (오전 / 호감 +5 / 신뢰 +6)"
        advance until screen "phone"
        pause 0.25
        assert eval week_lunch == "yujin"
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "“처음 보는 물건이 있으면 써 보고 싶어요.”"
        advance until screen "day_result"
        pause 0.25
        assert eval all(intro_seen[w] == 4 for w in names) and focus_interest is None
        click "5일차로 계속"
        advance until screen "phone"
        pause 0.25
        click "지금 확정할 내용과 검증할 내용을 나눠 가져갈게요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "이번 주 확정한 것과 다음 주 검증할 것을 나눈다. (오전 / 프로젝트 +10)"
        advance until screen "choice"
        pause 0.25
        click "“좋았던 것 하나를 떠올리고 끝내려고 해요.”"
        advance until screen "day_result"
        pause 0.25
        assert eval day == 5 and week_finished and all(intro_seen[w] == 5 for w in names)
        assert eval not focus_history and focus_interest is None and route_intent is None
        assert eval all(p["relationship"] == "none" and not p["core_resolved"] for p in people.values())
        assert eval all("intro_lunch_"+w in completed_events for w in names)
        assert eval flags["sy_private_book"] and flags["jh_private_movie"] and flags["yj_private_cup"]
        assert eval not ui_call_contact and not ring_pending
        click "6일차로 계속"
        advance until screen "choice"
        pause 0.25
        assert eval day == 6 and focus_interest is None and not focus_history

    testcase shared_call_interrupt:
        run Jump("intro_evening_gate")
        advance until screen "phone"
        click "받기"
        pause 0.5
        move pos (20,20)
        assert eval ui_call_contact == "ria"
        click "통화 종료"
        advance until screen "choice"
        pause 0.25
        click "“오늘은 일 얘기 쉬어도 돼요. 다음에 이어서 듣죠.”"
        advance until screen "day_result"
        assert eval not ui_call_contact and not ring_pending
        assert eval all(intro_seen[w] == 1 for w in names)
        assert eval any("사용자 종료" in c for c in phone_calls)
        assert eval any(m.get("id", "").startswith("hangup:") for m in phone_messages)

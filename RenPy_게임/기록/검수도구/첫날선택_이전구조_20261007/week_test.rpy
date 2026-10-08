testsuite office_week:
    setup:
        pause until screen "main_menu"
        run Preference("text speed",0)
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        click "첫날 시작"
    teardown:
        exit

    testcase continuous_week:
        advance until screen "choice"
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "choice"
        click "리아와 점심을 먹는다."
        advance until screen "phone"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 4.2
        click "계속"
        advance until screen "choice"
        click "“작은 공연 보러 가는 걸 좋아해요.”"
        advance until screen "choice"
        click "리아에게 퇴근 후 시간을 물어본다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20, 20)
        advance until screen "choice"
        click "카페에 들른다."
        advance until screen "choice"
        click "“현장 판단이 어떻게 나온 건지 더 듣고 싶어요.”"
        advance until screen "day_result"
        click "2일차로 계속"
        advance until screen "phone"
        assert eval day == 2
        assert eval renpy.get_screen("phone").scope["contact"] == "seoyun"
        pause 0.6
        screenshot "week_sy_options_message_policy_v1_upscaled_v1" max_pixel_difference 200
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        pause 2.4
        assert eval phone_is_typing("seoyun")
        pause 0.6
        screenshot "week_sy_typing_message_policy_v1_upscaled_v1" max_pixel_difference 200
        pause 2.7
        click "계속"
        advance until screen "choice"
        click "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "phone"
        assert eval flags["d2_had_promise"]
        click "약속대로 갈게요. 밥부터 먹어요."
        pause 4.2
        click "계속"
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        pause 0.6
        screenshot "week_sy_call_message_policy_v1_upscaled_v1" max_pixel_difference 200
        click "받기"
        pause 0.5
        move pos (20, 20)
        advance until screen "day_result"
        assert eval flags["d2_review_done"]
        assert eval flags["d2_sy_call"] == "answered"
        assert eval not promises
        assert eval next(p for p in week_schedule if p["id"]=="d2_ria_review")["status"] == "완료"
        click "휴대폰 확인"
        click "오늘은 체크리스트 닫고 편히 쉬세요."
        pause 5.1
        assert eval people["seoyun"]["affection"] == 21
        click "닫기"
        click "3일차로 계속"
        advance until screen "phone"
        click "예상과 달랐던 반응부터 같이 볼까요?"
        pause 4.2
        click "계속"
        advance until screen "choice"
        click "관찰과 가설을 구분하고 리아에게 기록법을 설명해 달라고 한다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "choice"
        click "서윤과 점심을 먹는다. (점심 / 호감 +5 / 스트레스 -5)"
        advance until screen "choice"
        click "회사 앞 카페에서 잠깐 혼자 쉰다. (저녁 / 감각 +3 / 스트레스 -8)"
        advance until screen "day_result"
        click "4일차로 계속"
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["contact"] == "yujin"
        click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
        pause 5.1
        pause 0.6
        screenshot "week_yj_messages_message_policy_v1_upscaled_v1" max_pixel_difference 200
        click "계속"
        advance until screen "choice"
        pause 0.6
        screenshot "week_yj_choices_message_policy_v1_upscaled_v1" max_pixel_difference 200
        click "각 시안의 목적을 듣고 첫 화면과 후속 화면을 구분한다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "choice"
        click "유진과 점심을 먹는다. (점심 / 호감 +5 / 스트레스 -5)"
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        click "지금은 받지 않기"
        advance until screen "day_result"
        assert eval flags["d4_yj_call"] == "deferred"
        click "5일차로 계속"
        advance until screen "phone"
        click "첫 방문부터 재방문까지 단계별로 정리하겠습니다."
        pause 4.1
        click "계속"
        advance until screen "choice"
        click "경험을 단계별로 적고 각 단계의 담당과 확인 방법을 정한다. (오전 / 프로젝트 +10)"
        advance until screen "choice"
        click "지현과 점심을 먹는다. (점심 / 호감 +5 / 스트레스 -5)"
        advance until screen "choice"
        click "리아와 카페에서 한 주 이야기를 나눈다. (저녁 / 감각 +3 / 스트레스 -8)"
        advance until screen "day_result"
        assert eval day == 5 and week_finished
        assert eval stats["project"] == 13
        assert eval [people[w]["episode_stage"] for w in names] == [1,1,1,0]
        assert eval all(not p["core_resolved"] and p["relationship"]=="none" for p in people.values())
        assert eval [people[w]["affection"] for w in names] == [26,33,26,16]
        assert eval all(p["status"] == "완료" for p in week_schedule)
        $ complete_week_event("C01",effects={"project":10})
        assert eval stats["project"] == 13
        pause 0.6
        screenshot "week_result_message_policy_v1_upscaled_v1" max_pixel_difference 200
        click "휴대폰 확인"
        click "일정"
        pause 0.6
        screenshot "week_calendar_message_policy_v1_upscaled_v1" max_pixel_difference 200
        click "닫기"
        run FilePage("weekqa")
        $ renpy.retain_after_load()
        run FileSave(1,confirm=False)
        $ flags["c01_method"] = "tampered"
        $ week_schedule[0]["status"] = "tampered"
        run OfficeFileLoad(1,confirm=False)
        pause 0.3
        assert eval flags["c01_method"] == "steps"
        assert eval week_schedule[0]["status"] == "완료"
        assert eval day == 5 and week_finished
        run FileDelete(1,confirm=False)
        run FilePage(1)

    testcase adjusted_and_rest:
        run Jump("day02")
        advance until screen "phone"
        click "전체 흐름부터 보고 궁금한 부분을 물어볼게요."
        pause 5.1
        click "계속"
        advance until screen "choice"
        click "제가 전부 정리하겠다고 제안한 뒤 담당 권한을 다시 묻는다. (오전 / 호감 +5 / 신뢰 +6)"
        advance until screen "choice"
        click "오늘 점심은 혼자 쉰다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        click "지금은 받지 않기"
        advance until screen "day_result"
        assert eval flags["d2_sy_call"] == "deferred"
        assert eval next(p for p in week_schedule if p["id"]=="d3_ria_review")["status"] == "예정"
        assert eval people["ria"]["trust"] == 10
        click "3일차로 계속"
        advance until screen "phone"
        click "현장에서 어떻게 기록했는지 궁금해요."
        pause 4.2
        click "계속"
        advance until screen "choice"
        click "성공한 숫자부터 쓰자고 했다가 실패한 기록도 함께 남긴다. (오전 / 호감 +5 / 신뢰 +6)"
        advance until screen "choice"
        assert eval next(p for p in week_schedule if p["id"]=="d3_ria_review")["status"] == "완료"
        click "리아와 점심을 먹는다. (점심 / 호감 +5 / 스트레스 -5)"
        advance until screen "choice"
        click "집에 돌아가 충분히 쉰다. (저녁 / 스트레스 -15)"
        advance until screen "day_result"
        click "4일차로 계속"
        advance until screen "phone"
        click "사용자가 처음 보는 순서부터 함께 읽어 볼게요."
        pause 5.1
        click "계속"
        advance until screen "choice"
        click "취향으로 A를 고른 뒤 첫 사용자의 목적을 다시 확인한다. (오전 / 호감 +5 / 신뢰 +6)"
        advance until screen "choice"
        click "테라스에서 혼자 쉰다. (점심 / 스트레스 -15)"
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20, 20)
        advance until screen "day_result"
        assert eval flags["d4_yj_call"] == "answered"
        click "5일차로 계속"
        advance until screen "phone"
        click "지금 확정할 내용과 검증할 내용을 나눠 가져갈게요."
        pause 4.1
        click "계속"
        advance until screen "choice"
        click "이번 주 확정한 것과 다음 주 검증할 것을 나눈다. (오전 / 프로젝트 +10)"
        advance until screen "choice"
        click "테라스에서 혼자 쉰다. (점심 / 스트레스 -15)"
        advance until screen "choice"
        click "집에 돌아가 약속 없는 저녁을 보낸다. (저녁 / 스트레스 -15)"
        advance until screen "day_result"
        assert eval stats["project"] == 10 and stats["stress"] == 0
        assert eval flags["c01_method"] == "verify"
        assert eval people["seoyun"]["trust"] == 16
        assert eval people["ria"]["trust"] == 16
        assert eval people["yujin"]["trust"] == 16
        assert eval "goodnight" not in phone_events
        assert eval not phone_pending
        $ lunch_before = people["ria"]["affection"]
        $ reward_week_lunch("ria")
        assert eval people["ria"]["affection"] == lunch_before
        $ week_lunch_rewards["ria"] = 2
        assert eval "호감 +0" in lunch_caption("ria")


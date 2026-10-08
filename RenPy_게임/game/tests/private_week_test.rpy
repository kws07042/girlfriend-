testsuite office_private_week_20261007:
    setup:
        pause until screen "main_menu"
        run Function(_office_qa_settings)
        run Preference("text speed",0)
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        click "첫날 시작"
        advance until screen "choice"
    teardown:
        run Function(_office_qa_settings,True)
        exit

    testcase seoyun_book:
        run Jump("day02")
        advance until screen "phone"
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        pause 5.2
        click "계속"
        assert eval ui_pose_current("seoyun") == "work"
        advance until screen "choice"
        click "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until eval _last_say_what == "이건 제가 읽던 책이에요. 점심 전에 한 장만 보려고 가져왔는데, 아직 그대로네요."
        assert eval clock == "11:55" and ui_speaker == "seoyun"
        assert eval ui_pose_current("seoyun") == "master"
        $ _private_affection_before = people["seoyun"]["affection"]
        pause 0.5
        screenshot "week_private_seoyun_master_20261007"
        advance until eval _last_say_what == "궁금하죠. 그런데 끝내고 나면 이 사람들이랑 헤어지는 것 같아서, 마지막은 좀 아껴요."
        assert eval ui_pose_current("seoyun") == "casual"
        assert eval ui_camera_current() == "C"
        pause 0.5
        screenshot "week_private_seoyun_casual_20261007"
        advance until screen "phone"
        assert eval flags["sy_private_book"] and "d2_sy_private" in completed_events
        assert eval people["seoyun"]["affection"] == _private_affection_before and people["seoyun"]["episode_stage"] == 1
        assert eval clock == "12:20" and not ui_pose_overrides

    testcase yujin_cup:
        run Jump("day04")
        advance until screen "phone"
        click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
        pause 5.2
        click "계속"
        assert eval ui_pose_current("yujin") == "work"
        advance until screen "choice"
        click "각 시안의 목적을 듣고 첫 화면과 후속 화면을 구분한다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until eval _last_say_what == "그 컵은 제가 만들었어요. 처음 도예 배울 때요."
        assert eval clock == "11:50" and ui_speaker == "yujin"
        assert eval ui_pose_current("yujin") == "master"
        $ _private_affection_before = people["yujin"]["affection"]
        pause 0.5
        screenshot "week_private_yujin_master_20261007"
        advance until eval _last_say_what == "네. 쥐어 보면 제 손에는 잘 맞아요. 처음엔 삐뚤어진 것만 보였는데, 쓰다 보니 좋아졌어요."
        assert eval ui_pose_current("yujin") == "casual" and ui_camera_current() == "C"
        pause 0.5
        screenshot "week_private_yujin_casual_20261007"
        advance until screen "choice"
        assert eval flags["yj_private_cup"] and "d4_yj_private" in completed_events
        assert eval people["yujin"]["affection"] == _private_affection_before and people["yujin"]["episode_stage"] == 1
        click "테라스에서 혼자 쉰다. (점심 / 스트레스 -15)"
        advance until eval _last_say_who == "yj" and clock == "17:30"
        assert eval ui_pose_current("yujin") == "work" and not ui_pose_overrides

    testcase jihyun_movie_save:
        run Jump("day03")
        advance until screen "phone"
        click "예상과 달랐던 반응부터 같이 볼까요?"
        pause 5.2
        click "계속"
        advance until screen "choice"
        click "관찰과 가설을 구분하고 리아에게 기록법을 설명해 달라고 한다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "choice"
        click "테라스에서 혼자 쉰다. (점심 / 스트레스 -15)"
        advance until eval _last_say_what == "일 얘기는 아니에요. 예전에 봤던 영화 장면이 떠서요."
        assert eval ui_pose_current("jihyun") == "master" and clock == "18:15"
        pause 0.5
        screenshot "week_private_jihyun_master_20261007"
        advance until eval _last_say_what == "네. 매번 그 장면까지 보고도 웃어요. 오늘은 줄거리 설명하면서도 웃네요."
        assert eval ui_pose_current("jihyun") == "casual" and ui_camera_current() == "C"
        pause 0.5
        screenshot "week_private_jihyun_casual_20261007"
        run FilePage("private-week-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run Function(ui_pose_change,"jihyun","work")
        run OfficeFileLoad(1,confirm=False)
        assert eval ui_pose_current("jihyun") == "casual" and clock == "18:15"
        assert eval not ui_pose_transitions
        run FileDelete(1,confirm=False)
        run FilePage(1)
        advance until screen "choice"
        assert eval flags["jh_private_movie"] and "d3_jh_private" in completed_events
        assert eval clock == "18:30" and people["jihyun"]["episode_stage"] == 0
        assert eval people["jihyun"]["affection"] == 10
        click "집에 돌아가 충분히 쉰다. (저녁 / 스트레스 -15)"
        advance until screen "day_result"
        assert eval not ui_pose_overrides and not ui_call_contact

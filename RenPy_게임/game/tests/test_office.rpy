testsuite office_qa:
    setup:
        pause until screen "main_menu"
        pause 0.4
        screenshot "title"
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        click "첫날 시작"
    teardown:
        exit

    testcase cafe_path:
        advance until screen "choice"
        pause 0.4
        screenshot "start"
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "phone"
        pause 0.4
        screenshot "phone"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 4.2
        click "계속"
        advance until screen "choice"
        click "“조용한 곳에서 걷거나 책을 읽어요.”"
        advance until screen "phone"
        click "통화"
        click "받기"
        advance until screen "choice"
        click "카페에 들른다."
        advance until screen "choice"
        click "“현장 판단이 어떻게 나온 건지 더 듣고 싶어요.”"
        advance until screen "day_result"
        assert eval people["ria"]["affection"] == 16
        assert eval people["ria"]["trust"] == 15
        assert eval stats["project"] == 3
        assert eval stats["stress"] == 11
        assert eval len(promises) == 1
        pause 0.4
        screenshot "cafe_result"
        click "휴대폰 확인"
        pause 0.6
        click "사진"
        click "ria_cafe"
        pause 0.4
        screenshot "photo"
        click "내 앨범에 저장"
        assert eval "ria_cafe" in photo_saved
        click "닫기"
        click "닫기"
        run FilePage("qa")
        $ renpy.retain_after_load()
        run FileSave(1)
        assert eval "ria_cafe" in renpy.get_save_data("qa-1")["photo_saved"]
        $ stats["project"] = 99
        run OfficeFileLoad(1,confirm=False)
        pause 0.2
        assert eval stats["project"] == 3
        assert eval "ria_cafe" in photo_saved
        run FileDelete(1,confirm=False)
        run FilePage(1)

    testcase home_path:
        advance until screen "choice"
        click "“앞으로 잘 부탁드립니다. 자료부터 확인할게요.”"
        advance until screen "choice"
        click "자료를 받아 혼자 요구사항 초안을 먼저 작성한다."
        advance until screen "phone"
        click "오늘은 잠깐 쉬고 싶어요. 오후에 이야기해요."
        pause 4.2
        click "계속"
        advance until screen "phone"
        click "통화"
        click "지금은 받지 않기"
        advance until screen "choice"
        click "오늘은 쉰다고 문자를 보낸다."
        advance until screen "day_result"
        assert eval people["ria"]["affection"] == 11
        assert eval people["ria"]["trust"] == 10
        assert eval stats["project"] == 4
        assert eval stats["stress"] == 0
        assert eval len(promises) == 0
        pause 0.4
        screenshot "home_result"

    testcase photo_permissions:
        $ person = dict(affection=100,trust=100,episode_stage=4,relationship="dating",photo_cap=4,private_photo_ok=True,core_resolved=True,breach=False)
        assert eval photo_allowed(person,photo_tiers[2])
        $ person["private_photo_ok"] = False
        assert eval not photo_allowed(person,photo_tiers[2])
        $ person["private_photo_ok"] = True
        $ person["trust"] = 54
        assert eval not photo_allowed(person,photo_tiers[2])
        $ person["trust"] = 100
        $ person["relationship"] = "none"
        assert eval not photo_allowed(person,photo_tiers[2])
        $ person["relationship"] = "paused"
        assert eval not photo_allowed(person,photo_tiers[0])
        $ person["relationship"] = "dating"
        $ person["core_resolved"] = False
        assert eval not photo_allowed(person,photo_tiers[2])
        $ people["ria"].update(affection=100,trust=100,episode_stage=4,relationship="dating",photo_cap=4,private_photo_ok=True,core_resolved=True)
        $ queue_photo_rewards()
        assert eval len(photo_received) == 0

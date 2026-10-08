# Native first-day route regression and read-volume observations.
init 96 python:
    import json as _day1_json
    import os as _day1_os
    def _day1_qa_reset():
        _day1_qa_record.rows = []
    def _day1_qa_record(event, **kwargs):
        if event == "begin" and renpy.game.args.command == "test" and day == 1:
            rows = getattr(_day1_qa_record,"rows",[])
            rows.append((getattr(store,"_last_say_who",None),getattr(store,"_last_say_what","")))
            _day1_qa_record.rows = rows
    config.all_character_callbacks.append(_day1_qa_record)
    def _day1_qa_finish(key):
        rows = getattr(_day1_qa_record,"rows",[])
        result = {"blocks":len(rows),"characters":sum(len(t) for w,t in rows),"heroines":{w:sum(a==w for a,t in rows) for w in ("sy","ri","yj","jh")},"flags":dict(flags)}
        _day1_qa_finish.last = result
        results = getattr(_day1_qa_finish,"results",{})
        results[key] = result
        _day1_qa_finish.results = results
        path = _day1_os.environ.get("OFFICE_DAY1_QA_LOG")
        if path:
            with open(path,"w",encoding="utf-8") as stream:
                _day1_json.dump(results,stream,ensure_ascii=False,indent=2)

testsuite office_day1_choices_20261007:
    setup:
        pause until screen "main_menu"
        run Preference("text speed",0)
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Function(_day1_qa_reset)
        pause 0.3
        click "첫날 시작"
    teardown:
        exit

    testcase seoyun_full:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "choice"
        pause 0.25
        screenshot "day1_lunch_choices_20261007" max_pixel_difference 200
        click "서윤과 점심을 먹는다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["contact"] == "seoyun"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "서윤에게 퇴근 후 시간을 물어본다."
        advance until screen "phone"
        assert eval ring_who == "seoyun" and renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "잠깐 카페에 들러 이야기를 이어간다."
        advance until screen "choice"
        pause 0.25
        screenshot "day1_seoyun_cafe_choices_20261007" max_pixel_difference 200
        click "“사람들 이야기를 듣고 나서 제 속도를 찾아요.”"
        advance until screen "day_result"
        run Function(_day1_qa_finish,"seoyun")
        assert eval _day1_qa_finish.last["blocks"] >= 89
        assert eval _day1_qa_finish.last["characters"] >= 3757
        assert eval all(n >= 10 for n in _day1_qa_finish.last["heroines"].values())
        assert eval flags["first_lunch"] == "seoyun" and flags["first_evening"] == "seoyun"
        assert eval ui_call_contact is None and not ring_pending
        assert eval "d1_seoyun_night" in phone_events
        assert eval "cafe_photo" not in phone_events and "ria_cafe" not in photo_received
        assert eval not flags.get("nextLunch")
        click "2일차로 계속"
        advance until screen "phone"
        assert eval day == 2
        assert eval week_lunch_rewards.get("seoyun") == 1
        assert eval phone_reply_available("d1_seoyun_night") and "그날" in phone_reply_options("d1_seoyun_night")[0]["text"]
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "choice"
        pause 0.25
        click "유진과 점심을 먹는다."
        advance until screen "phone"
        assert eval week_lunch == "yujin" and not flags.get("d2_review_done")
        assert eval next(p for p in week_schedule if p["id"] == "d3_ria_review")["status"] == "예정"

    testcase ria_full:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "choice"
        pause 0.25
        click "리아와 점심을 먹는다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["contact"] == "ria"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "“작은 공연 보러 가는 걸 좋아해요.”"
        advance until screen "choice"
        pause 0.25
        click "리아에게 퇴근 후 시간을 물어본다."
        advance until screen "phone"
        assert eval ring_who == "ria" and renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "카페에 들른다."
        advance until screen "choice"
        pause 0.25
        click "“현장 판단이 어떻게 나온 건지 더 듣고 싶어요.”"
        advance until screen "day_result"
        run Function(_day1_qa_finish,"ria")
        assert eval _day1_qa_finish.last["blocks"] >= 89
        assert eval _day1_qa_finish.last["characters"] >= 3757
        assert eval all(n >= 10 for n in _day1_qa_finish.last["heroines"].values())
        assert eval flags["first_lunch"] == "ria" and flags["first_evening"] == "ria"
        assert eval ui_call_contact is None and not ring_pending
        assert eval "goodnight" in phone_events
        click "2일차로 계속"
        advance until screen "phone"
        assert eval day == 2
        assert eval week_lunch_rewards.get("ria") == 1

    testcase yujin_full:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "choice"
        pause 0.25
        click "유진과 점심을 먹는다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["contact"] == "yujin"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "유진에게 퇴근 후 시간을 물어본다."
        advance until screen "phone"
        assert eval ring_who == "yujin" and renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "잠깐 카페에 들러 이야기를 이어간다."
        advance until screen "choice"
        pause 0.25
        click "“손에 익으면 바꿀 때도 망설여져요.”"
        advance until screen "day_result"
        run Function(_day1_qa_finish,"yujin")
        assert eval _day1_qa_finish.last["blocks"] >= 89
        assert eval _day1_qa_finish.last["characters"] >= 3757
        assert eval all(n >= 10 for n in _day1_qa_finish.last["heroines"].values())
        assert eval flags["first_lunch"] == "yujin" and flags["first_evening"] == "yujin"
        assert eval ui_call_contact is None and not ring_pending
        assert eval "d1_yujin_night" in phone_events
        assert eval "cafe_photo" not in phone_events and "ria_cafe" not in photo_received
        assert eval not flags.get("nextLunch")
        click "2일차로 계속"
        advance until screen "phone"
        assert eval day == 2
        assert eval week_lunch_rewards.get("yujin") == 1
        assert eval phone_reply_available("d1_yujin_night") and "그날" in phone_reply_options("d1_yujin_night")[0]["text"]
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "choice"
        pause 0.25
        click "지현과 점심을 먹는다."
        advance until screen "phone"
        assert eval week_lunch == "jihyun" and not flags.get("d2_review_done")
        assert eval next(p for p in week_schedule if p["id"] == "d3_ria_review")["status"] == "예정"

    testcase jihyun_full:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "자료를 받아 혼자 요구사항 초안을 먼저 작성한다."
        advance until screen "choice"
        pause 0.25
        click "지현과 점심을 먹는다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["contact"] == "jihyun"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "지현에게 퇴근 후 시간을 물어본다."
        advance until screen "phone"
        assert eval ring_who == "jihyun" and renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "잠깐 카페에 들러 이야기를 이어간다."
        advance until screen "choice"
        pause 0.25
        click "“한 말을 되짚다가 못 한 말까지 생각해요.”"
        advance until screen "day_result"
        run Function(_day1_qa_finish,"jihyun")
        assert eval _day1_qa_finish.last["blocks"] >= 89
        assert eval _day1_qa_finish.last["characters"] >= 3757
        assert eval all(n >= 10 for n in _day1_qa_finish.last["heroines"].values())
        assert eval flags["first_lunch"] == "jihyun" and flags["first_evening"] == "jihyun"
        assert eval ui_call_contact is None and not ring_pending
        assert eval "d1_jihyun_night" in phone_events
        assert eval "cafe_photo" not in phone_events and "ria_cafe" not in photo_received
        assert eval not flags.get("nextLunch")
        click "2일차로 계속"
        advance until screen "phone"
        assert eval day == 2
        assert eval week_lunch_rewards.get("jihyun") == 1
        assert eval phone_reply_available("d1_jihyun_night") and "그날" in phone_reply_options("d1_jihyun_night")[0]["text"]
        click "어디까지 필요한지 듣고 맡을 일을 정할게요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)"
        advance until screen "choice"
        pause 0.25
        click "서윤과 점심을 먹는다."
        advance until screen "phone"
        assert eval week_lunch == "seoyun" and not flags.get("d2_review_done")
        assert eval next(p for p in week_schedule if p["id"] == "d3_ria_review")["status"] == "예정"

    testcase rest_full:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "자료를 받아 혼자 요구사항 초안을 먼저 작성한다."
        advance until screen "choice"
        pause 0.25
        click "테라스에서 혼자 쉰다."
        advance until screen "choice"
        pause 0.25
        click "오늘은 연락하지 않고 집에서 쉰다."
        advance until screen "day_result"
        run Function(_day1_qa_finish,"rest")
        assert eval _day1_qa_finish.last["blocks"] >= 59
        assert eval _day1_qa_finish.last["characters"] >= 2674
        assert eval not phone_calls and "cafe_photo" not in phone_events and "goodnight" not in phone_events
        assert eval flags["first_lunch"] == "rest" and flags["first_evening"] == "rest"

    testcase mixed_contacts_and_save:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "choice"
        pause 0.25
        click "유진과 점심을 먹는다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["contact"] == "yujin"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "서윤에게 퇴근 후 시간을 물어본다."
        advance until screen "phone"
        assert eval ring_who == "seoyun" and renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "잠깐 카페에 들러 이야기를 이어간다."
        advance until screen "choice"
        pause 0.25
        run FilePage("day1-choices-qa")
        run Function(renpy.retain_after_load)
        run FileSave(1,confirm=False)
        run SetDict(flags,"first_evening","ria")
        run OfficeFileLoad(1,confirm=False)
        assert eval flags["first_lunch"] == "yujin" and flags["first_evening"] == "seoyun"
        run FileDelete(1,confirm=False)
        run FilePage(1)
        click "“직접 걸어 봐야 익숙해지는 편이에요.”"
        advance until screen "day_result"
        assert eval "d1_seoyun_night" in phone_events and "d1_yujin_night" not in phone_events
        assert eval "cafe_photo" not in phone_events and not flags.get("nextLunch")

    testcase decline_invitation:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "choice"
        pause 0.25
        click "지현과 점심을 먹는다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["contact"] == "jihyun"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "유진에게 퇴근 후 시간을 물어본다."
        advance until screen "phone"
        assert eval ring_who == "yujin" and renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        click "오늘은 집에서 쉬고 다음에 이야기한다."
        advance until screen "day_result"
        assert eval not flags.get("d1_private_met") and "d1_yujin_night" not in phone_events
        assert eval any(m.get("id") == "d1_yujin_night:rest" for m in phone_messages)
        assert eval ui_call_contact is None and "cafe_photo" not in phone_events

    testcase interrupt_call:
        advance until screen "choice"
        pause 0.25
        click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
        advance until screen "choice"
        pause 0.25
        click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
        advance until screen "choice"
        pause 0.25
        click "서윤과 점심을 먹는다."
        advance until screen "phone"
        assert eval renpy.get_screen("phone").scope["contact"] == "seoyun"
        click "좋아요. 같이 먹으면서 이야기해요."
        pause 5.2
        click "계속"
        advance until screen "choice"
        pause 0.25
        click "지현에게 퇴근 후 시간을 물어본다."
        advance until screen "phone"
        assert eval ring_who == "jihyun" and renpy.get_screen("phone").scope["tab"] == "calls"
        click "받기"
        pause 0.5
        move pos (20,20)
        advance until screen "choice"
        pause 0.25
        run Jump("ui_phone_hangup")
        advance until screen "day_result"
        assert eval ui_call_contact is None and not flags.get("d1_private_met")
        assert eval any(m.get("who") == "jihyun" and m.get("id", "").startswith("hangup:") for m in phone_messages)
        assert eval "d1_jihyun_night" not in phone_events and "cafe_photo" not in phone_events


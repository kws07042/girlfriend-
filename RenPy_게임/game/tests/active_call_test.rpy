testcase office_active_call:
    pause until screen "main_menu"
    run Preference("text speed",0)
    click "첫날 시작"
    run Jump("d1_evening_gate")
    advance until screen "phone"
    assert eval renpy.get_screen("phone").scope["tab"] == "calls"
    pause 0.45
    screenshot "incoming_auto_%s_v1" % ring_who
    click "받기"
    assert eval ui_call_contact == "ria"
    assert screen "say"
    assert not screen "phone"
    pause 0.5
    move pos (20, 20)
    screenshot "active_call_ria_auto_v5"
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
    screenshot "active_call_choices_auto_v5"
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
    screenshot "incoming_auto_%s_v1" % ring_who
    click "받기"
    assert eval ui_call_contact == "seoyun"
    pause 0.4
    move pos (20, 20)
    screenshot "active_call_seoyun_auto_v5"
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
    screenshot "incoming_auto_%s_v1" % ring_who
    click "받기"
    assert eval ui_call_contact == "yujin"
    pause 0.4
    move pos (20, 20)
    screenshot "active_call_yujin_auto_v5"
    click "통화 종료"
    advance
    advance
    pause 1.0
    assert eval ui_call_contact is None and flags["d4_yj_call"] == "answered"
    exit




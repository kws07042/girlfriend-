testcase office_phone_live:
    pause until screen "main_menu"
    run Preference("text speed",0)
    click "첫날 시작"
    advance until screen "choice"
    click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
    advance until screen "choice"
    click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
    advance until screen "phone"
    pause 0.6
    screenshot "phone_v4_idle"
    $ _phone_before = len(phone_messages)
    $ _affection_before = people["ria"]["affection"]
    click "좋아요. 같이 먹으면서 이야기해요."
    assert eval len(phone_pending) == 1
    assert eval len(phone_messages) == _phone_before + 1
    assert eval phone_messages[-1]["delivery"] == "sending"
    pause 0.8
    assert eval phone_messages[-1]["delivery"] == "sent"
    pause 0.7
    assert eval phone_is_typing("ria")
    assert eval phone_messages[-1]["delivery"] == "read"
    screenshot "phone_v4_typing"
    run FilePage("phoneqa")
    $ renpy.retain_after_load()
    run FileSave(1,confirm=False)
    assert eval len(renpy.get_save_data("phoneqa-1")["phone_pending"]) == 1
    click "유진"
    assert eval phone_is_typing("ria")
    run Hide("phone")
    pause 2.8
    assert eval len(phone_pending) == 0
    assert eval len(phone_messages) == _phone_before + 2
    assert eval phone_unread["ria"] == 1
    assert eval people["ria"]["affection"] == _affection_before + 1
    $ reply_message(phone_replied[-1], message_data[phone_replied[-1]]["reply"][0])
    assert eval len(phone_messages) == _phone_before + 2
    assert eval people["ria"]["affection"] == _affection_before + 1
    run OfficeFileLoad(1,confirm=False)
    pause 0.2
    assert eval len(phone_pending) == 1
    assert eval len(phone_messages) == len(renpy.get_save_data("phoneqa-1")["phone_messages"])
    run Hide("phone")
    pause 2.8
    assert eval len(phone_pending) == 0
    assert eval len(phone_messages) == len(renpy.get_save_data("phoneqa-1")["phone_messages"]) + 1
    run FileDelete(1,confirm=False)
    run FilePage(1)
    run Show("phone")
    pause 0.6
    screenshot "phone_v4_received"
    exit

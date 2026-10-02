testcase office_reply_marker:
    pause until screen "main_menu"
    run Preference("text speed",0)
    click "첫날 시작"
    run Jump("day02")
    advance until screen "phone"
    assert eval phone_contact_attention("seoyun", "d2_sy") == "reply"
    click "유진"
    assert eval renpy.get_screen("phone").scope["contact"] == "yujin"
    assert eval phone_contact_attention("seoyun", "d2_sy") == "reply"
    pause 0.6
    screenshot "phone_reply_marker_other_red_v4"
    click "서윤"
    assert eval phone_unread["seoyun"] == 0
    assert eval phone_contact_attention("seoyun", "d2_sy") == "reply"
    $ _marker_previous_motion = persistent.reduce_motion
    $ persistent.reduce_motion = True
    pause 0.4
    screenshot "phone_reply_marker_still_red_v4"
    click "어디까지 필요한지 듣고 맡을 일을 정할게요."
    assert eval phone_contact_attention("seoyun", "d2_sy") is None
    pause 5.1
    assert eval not phone_pending
    $ persistent.reduce_motion = _marker_previous_motion
    click "계속"
    assert screen "say"
    exit





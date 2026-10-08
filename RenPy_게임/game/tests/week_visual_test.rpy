testcase office_week_visual:
    pause until screen "main_menu"
    $ _week_preview_cps = preferences.text_cps
    run Preference("text speed",0)
    click "첫날 시작"
    run Jump("day04")
    advance until screen "phone"
    pause 0.7
    screenshot "week_yj_messages_upscaled_v1"
    click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
    pause 5.1
    click "계속"
    advance until screen "choice"
    pause 0.6
    assert eval ui_speaker == "yujin"
    assert eval day == 4 and clock == "09:30"
    screenshot "week_yj_choices_upscaled_v1"
    run Preference("text speed",_week_preview_cps)
    exit

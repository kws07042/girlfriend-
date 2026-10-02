testcase office_ui_preview:
    pause until screen "main_menu"
    pause 0.6
    screenshot "ui_title"
    $ _ui_old_cps = preferences.text_cps
    run Preference("text speed",0)
    click "첫날 시작"
    advance until screen "choice"
    pause 0.6
    screenshot "ui_choices"
    click "“선택할 수 있게 챙겨 주셨네요. 고마워요.”"
    pause 0.6
    screenshot "ui_dialogue"
    advance until screen "choice"
    click "리아와 자료를 함께 읽고 고객 흐름을 정리한다."
    advance until screen "phone"
    pause 0.6
    screenshot "ui_messages"
    click "서윤"
    pause 0.3
    screenshot "profile_seoyun"
    click "리아"
    pause 0.3
    screenshot "profile_ria"
    click "유진"
    pause 0.3
    screenshot "profile_yujin"
    click "지현"
    pause 0.3
    screenshot "profile_jihyun"
    click "리아"
    click "통화"
    pause 0.6
    screenshot "ui_calls_empty"
    click "수신 설정"
    pause 0.6
    screenshot "ui_permissions"
    click "문자"
    click "좋아요. 같이 먹으면서 이야기해요."
    pause 4.2
    click "계속"
    advance until screen "choice"
    click "“조용한 곳에서 걷거나 책을 읽어요.”"
    advance until screen "phone"
    click "통화"
    pause 0.6
    screenshot "ui_incoming"
    click "받기"
    advance until screen "choice"
    click "카페에 들른다."
    advance until screen "choice"
    click "“현장 판단이 어떻게 나온 건지 더 듣고 싶어요.”"
    advance until screen "day_result"
    pause 0.6
    screenshot "ui_result"
    click "저장"
    pause 0.6
    screenshot "ui_save"
    run Preference("text speed",_ui_old_cps)
    exit

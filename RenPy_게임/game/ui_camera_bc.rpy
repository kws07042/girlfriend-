# B/C conversation framing. Independent of story and phone implementation.
init offset = 20
default ui_camera_mode = "B"
default ui_camera_override = None
default ui_camera_place = None
default ui_camera_actor = None

init python:
    # Exact authored beats; ordinary discussion and all unspecified scenes use B.
    ui_camera_close_beats = (
        "지금도 모르는 건 많죠. 사람들 앞에서는 웃는 게 먼저 나와서 그렇지.",
        "아까 유진 씨가 제 기록 이야기했을 때… 조금 좋았어요. 제가 만든 거라고 들리니까.",
        "그렇게 물어보면 길어지는데. 괜찮아요?",
        "그렇게 말해 주니까 좀 편해지네요. 자꾸 설명해야 인정받을 것 같아서.",
        "담당이 정해지지 않으면 일단 제 이름을 넣어 둬요. 기다리다가 빠뜨리는 것보다는 나으니까요.",
        "그걸 구분하지 않고 계속해 온 것 같네요. 매번 금방 끝날 줄 알았거든요.",
        "사진 찍은 뒤 뭘 해야 할지 몰랐대요. 재밌게 해 준 사람은 됐는데, 안내한 사람은 못 된 거죠.",
        "그래서 함께 남기고 싶었어요. 나중에 제가 봐도 왜 바꿨는지 알 수 있게요.",
    )
    ui_camera_who = {"sy": "seoyun", "ri": "ria", "yj": "yujin", "jh": "jihyun"}

    def ui_camera_set(mode=None):
        # Story authors can opt into explicit B/C without changing the UI.
        if mode not in (None, "B", "C"):
            raise ValueError("Camera mode must be B, C, or None (automatic).")
        store.ui_camera_override = mode
        ui_bc_motion_schedule()

    def ui_camera_reset(label=None, abnormal=False):
        # Engine save/load and menu labels must preserve the restored framing.
        if label and label.startswith('_'):
            return
        store.ui_camera_mode = "B"
        store.ui_camera_actor = None
        ui_bc_motion_schedule()

    def ui_camera_update(who, what, location):
        if store.ui_camera_place != location:
            ui_camera_reset()
            store.ui_camera_place = location
        actor = ui_camera_who.get(who)
        if actor:
            if actor != store.ui_camera_actor:
                store.ui_camera_mode = "B"
            store.ui_camera_actor = actor
            if what in ui_camera_close_beats:
                store.ui_camera_mode = "C"
        ui_bc_motion_schedule()
        # Preserve a close-up through the protagonist's reply and its choices.

    def ui_camera_callback(event, **kwargs):
        if event == "begin":
            ui_camera_update(getattr(store, "_last_say_who", None),
                             getattr(store, "_last_say_what", ""),
                             getattr(store, "place", None))

    def ui_camera_current():
        return store.ui_camera_override or store.ui_camera_mode

    config.all_character_callbacks.append(ui_camera_callback)
    config.label_callbacks.append(ui_camera_reset)

screen office_portrait():
    zorder -5
    if ui_scene_actor and ui_scene_key != "home" and not main_menu and not renpy.get_screen("day_result") and not renpy.get_screen("phone") and not ui_call_contact:
        add Solid("#101A2418") at ui_bc_tint
        add ui_bc_frame(Transform(ui_character_present(ui_speaker), xysize=(1024,1536), fit="contain")) id "office_character"

screen say(who, what):
    zorder 20
    window:
        id "window"
        background ui_panel("glass")
        xpos 80 ypos 850 xsize 1760 ysize 220 padding (36,20)
        vbox:
            spacing 8
            if who:
                text who id "who" size 28 color ui_colors.get(ui_speaker,"#D6B18A")
            else:
                text "AFTER HOURS" size 20 color "#9CACB4" kerning 2
            text what id "what" size 31 color "#F8F4EE" line_spacing 5 xmaximum 1660
    add Solid("#D6B18A") xpos 116 ypos 850 xsize 72 ysize 3
    use quick_menu

screen choice(items):
    modal True
    zorder 25
    vbox:
        xpos 80 yalign 0.49 spacing 12 xsize 650
        at ui_reveal(duration=0.0 if persistent.reduce_motion else 0.22, distance=0 if persistent.reduce_motion else 10)
        frame:
            background ui_panel("glass") padding (24,14) xsize 650
            vbox:
                spacing 4
                text "YOUR MOMENT" size 18 color "#E2C19E" kerning 3
                text "어떻게 답할까요?" size 28 color "#FFFFFF"
        for item in items:
            button:
                action item.action
                style "ui_light_button" xfill True padding (24,20)
                hbox:
                    spacing 18
                    text "%02d" % (items.index(item)+1) size 21 color "#A47A52" yalign 0.5
                    text item.caption size 25 color "#26343B" xmaximum 540 yalign 0.5

screen quick_menu():
    zorder 30
    hbox:
        xpos 1210 ypos 1028 spacing 3
        textbutton "기록" action ShowMenu("history") style "ui_quick_button" text_size 20
        textbutton "저장" action ShowMenu("save") style "ui_quick_button" text_size 20
        textbutton "불러오기" action ShowMenu("load") style "ui_quick_button" text_size 20
        textbutton "자동" action Preference("auto-forward","toggle") style "ui_quick_button" text_size 20
        textbutton "설정" action ShowMenu("preferences") style "ui_quick_button" text_size 20







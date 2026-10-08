# Active voice-call presentation, independent of character art.
default ui_call_contact = None
default ui_call_elapsed = 0
default ui_call_end_target = None
default ui_call_ending = False
default ui_call_closing = False
default ui_call_hangup_target = None

init -4 python:
    def ui_phone_call_begin(who, end_target):
        store.ui_scene_presence_version = 1
        store.ui_pose_transitions = {}
        store.ui_call_ending = False
        store.ui_call_closing = False
        store.ui_scene_actor = None
        store.ui_call_contact = who
        store.ui_call_elapsed = 0
        store.ui_call_end_target = end_target
        store.ui_speaker = who

    def ui_phone_call_end():
        store.ui_scene_presence_version = 1
        store.ui_pose_transitions = {}
        store.ui_call_ending = False
        store.ui_call_closing = False
        store.ui_scene_actor = None
        store.ui_call_contact = None
        store.ui_call_end_target = None

    def ui_phone_call_tick():
        store.ui_call_elapsed += 1
        renpy.restart_interaction()

    def ui_phone_call_time():
        return "%02d:%02d" % (store.ui_call_elapsed // 60, store.ui_call_elapsed % 60)

    config.overlay_screens.append("phone_active_call")

screen phone_active_call():
    zorder 15
    if ui_call_contact and not main_menu and not renpy.get_screen("phone") and not renpy.get_screen("save") and not renpy.get_screen("load") and not renpy.get_screen("preferences") and not renpy.get_screen("history") and not renpy.get_screen("day_result"):
        add Solid("#0D17224D")
        if not ui_call_ending:
            timer 1.0 repeat True action Function(ui_phone_call_tick)
        fixed:
            xpos 732 ypos 40 xsize 632 ysize 1040
            at Transform(zoom=0.72)
            frame:
                xpos 22 ypos 18 xsize 588 ysize 1004
                background Frame("images/ui_v6/screen.png",60,60) padding (36,24)
                fixed:
                    xsize 516 ysize 956
                    text clock xpos 4 ypos 0 size 21 bold True color "#26343B"
                    hbox:
                        xpos 516 xanchor 1.0 ypos 0 spacing 8
                        text "LTE" size 18 color "#68757B" yalign 0.5
                        add "images/ui_v2/battery.png" yalign 0.5
                    add "images/ui_v2/camera.png" xpos 245 ypos -5
                    add ui_phone_avatar(ui_call_contact,160) xalign 0.5 ypos 150
                    text names[ui_call_contact] size 40 bold True color "#26343B" xalign 0.5 ypos 344
                    text ("통화 종료" if ui_call_ending else ("마무리 중" if ui_call_closing else "통화 중")) size 27 color "#899499" xalign 0.5 ypos 408
                    text ui_phone_call_time() size 34 color "#28636A" xalign 0.5 ypos 460
                    textbutton "대화 기록" action ShowMenu("history") style "phone_equal_button" xsize 200 ysize 64 xalign 0.5 ypos 594 text_size 25
                    if not ui_call_ending and not ui_call_closing:
                        textbutton "통화 종료":
                            action Jump("ui_phone_hangup")
                            xalign 0.5 ypos 800 xsize 240 ysize 80 padding (0,0)
                            background AlphaMask(Solid("#C84B4B"),Frame("images/ui_v2/paper.png",32,32))
                            hover_background AlphaMask(Solid("#DC6060"),Frame("images/ui_v2/paper.png",32,32))
                            text_size 26 text_color "#FFFFFF" text_hover_color "#FFFFFF" text_align 0.5 text_xalign 0.5 text_yalign 0.5
            add "images/ui_v6/device_frame.png"


# A brief end state acknowledges the tap before the authored continuation.
label ui_phone_hangup:
    if not ui_call_contact or not ui_call_end_target:
        return
    $ ui_call_hangup_target = ui_call_end_target
    $ ui_call_closing = True
    dh "지금은 통화를 마쳐야 할 것 같아요. 다음에 이어서 이야기해요."
    if ui_call_contact == "seoyun":
        sy "네. 남은 얘기는 다음에 해요. 저도 오늘은 여기서 멈출게요. 편히 쉬세요."
    elif ui_call_contact == "ria":
        ri "네, 그럼 오늘은 여기까지! 푹 쉬어요. 남은 얘기는 다음에 해요."
    elif ui_call_contact == "yujin":
        yj "알겠어요. 지금 답을 정하지 않아도 괜찮아요. 다음에 이어서 이야기해요."
    elif ui_call_contact == "jihyun":
        jh "네. 여기까지 하죠. 남은 내용은 나중에 확인해요."
    $ ui_call_closing = False
    $ ui_call_ending = True
    if phone_calls and "통화 완료" in phone_calls[-1]:
        $ phone_calls[-1] = phone_calls[-1].replace("통화 완료", "사용자 종료")
    $ renpy.say(None, "통화를 마쳤다.", interact=False)
    $ renpy.pause(0.8)
    $ _ui_hangup_contact = ui_call_contact
    $ ui_phone_call_end()
    $ phone_interrupted_call_followup(_ui_hangup_contact,ui_call_hangup_target)
    $ renpy.jump(ui_call_hangup_target)


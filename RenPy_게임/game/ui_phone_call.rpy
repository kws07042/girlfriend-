# Active voice-call presentation, independent of character art.
default ui_call_contact = None
default ui_call_elapsed = 0
default ui_call_end_target = None

init -4 python:
    def ui_phone_call_begin(who, end_target):
        store.ui_call_contact = who
        store.ui_call_elapsed = 0
        store.ui_call_end_target = end_target
        store.ui_speaker = who

    def ui_phone_call_end():
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
                    text "통화 중" size 27 color "#899499" xalign 0.5 ypos 408
                    text ui_phone_call_time() size 34 color "#28636A" xalign 0.5 ypos 460
                    textbutton "대화 기록" action ShowMenu("history") style "phone_equal_button" xsize 200 ysize 64 xalign 0.5 ypos 594 text_size 25
                    button:
                        action Jump(ui_call_end_target)
                        xalign 0.5 ypos 780 xsize 104 ysize 104 padding (0,0)
                        background AlphaMask(Solid("#C84B4B"),Transform("images/ui_v2/circle.png",xysize=(104,104)))
                        hover_background AlphaMask(Solid("#DC6060"),Transform("images/ui_v2/circle.png",xysize=(104,104)))
                        text "종료" align (0.5,0.5) size 26 color "#FFFFFF"
                    text "통화 종료" xalign 0.5 ypos 901 size 24 color "#B64646"
            add "images/ui_v6/device_frame.png"


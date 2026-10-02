# Native Ren'Py UI prototype. No character artwork is edited.
default ui_speaker = "ria"
init -5 python:
    def ui_panel(name):
        return Frame("images/ui_v2/" + name + ".png", 32, 32)
    def ui_speaker_callback(who):
        def callback(event, **kwargs):
            if event == "begin":
                store.ui_speaker = who
        return callback
    phone_profile_boxes = {'yujin': (269, 15, 759, 759), 'jihyun': (234, 0, 759, 759), 'ria': (249, 15, 759, 759), 'seoyun': (219, 30, 759, 759)}
    def ui_avatar(who, size=56, profile=False):
        path = "images/phone/%s_profile_v001.png" % who
        if profile and renpy.loadable(path):
            portrait = Crop(phone_profile_boxes[who],path)
        else:
            portrait = Crop((385,45,250,250),"images/characters/%s_master.png" % who)
        return AlphaMask(Transform(portrait,xysize=(size,size)),
                         Transform("images/ui_v2/circle.png",xysize=(size,size)))
    def ui_phone_avatar(who, size=56):
        return ui_avatar(who,size,profile=True)
    ui_roles = {"seoyun":"SERVICE PLANNING", "ria":"CAMPAIGN MANAGER", "yujin":"BRAND DESIGN", "jihyun":"BUSINESS STRATEGY"}
    ui_colors = {"seoyun":"#AAD0CB", "ria":"#D6B18A", "yujin":"#D3A9BA", "jihyun":"#B7C4D4"}
    config.overlay_screens.append("office_portrait")

transform ui_reveal(duration=0.22, distance=10):
    alpha 0.0 yoffset distance
    ease duration alpha 1.0 yoffset 0
transform ui_phone_enter(duration=0.42, distance=1100):
    on show:
        alpha 0.0 yoffset distance
        easeout duration alpha 1.0 yoffset 0
    on hide:
        easein duration alpha 0.0 yoffset distance

transform phone_typing_dot(delay=0.0):
    alpha 0.35 yoffset 0
    pause delay
    block:
        ease 0.22 alpha 1.0 yoffset -4
        ease 0.22 alpha 0.35 yoffset 0
        pause 0.40
        repeat

transform phone_message_arrive:
    alpha 0.0 yoffset 8
    easeout 0.20 alpha 1.0 yoffset 0

screen office_portrait():
    zorder -5
    if not main_menu and not renpy.get_screen("day_result"):
        add Transform("images/characters/%s_master.png" % ui_speaker, xysize=(740,1110),fit="contain") xpos 1010 ypos 2

style default:
    font "fonts/SourceHanSansLite.ttf"
    size 28
    color "#26343B"
style button:
    background ui_panel("glass")
    hover_background ui_panel("glass_hover")
    padding (22,14)
style button_text:
    color "#F7F2EB"
    hover_color "#EDD0AC"
    size 26
style frame:
    background ui_panel("paper")
    padding (28,24)
style input:
    color "#26343B"
style bar:
    left_bar Solid("#D6B18A")
    right_bar Solid("#D9DEE0")
    ysize 8
style ui_light_button is button:
    background ui_panel("paper")
    hover_background ui_panel("paper_hover")
style ui_light_button_text is button_text:
    color "#26343B"
    hover_color "#916641"
style ui_chip_button is button:
    background None
    selected_background ui_panel("subtle")
    hover_background ui_panel("subtle")
    padding (14,9)
style ui_chip_button_text is button_text:
    color "#68757B"
    hover_color "#26343B"
    selected_color "#916641"
    size 23
style ui_action_button is button:
    background ui_panel("gold")
    hover_background ui_panel("gold_hover")
style ui_action_button_text is button_text:
    color "#202A30"
    hover_color "#202A30"
style ui_quick_button is button:
    background None
    hover_background None
    padding (12,4)
style ui_quick_button_text is button_text:
    size 22
    color "#B2BFC5"
    hover_color "#EDD0AC"

# Fixed equal cells; label and hit area share the same center.
style phone_equal_button is ui_chip_button:
    padding (0,0)
style phone_equal_button_text is ui_chip_button_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    selected_color "#28636A"

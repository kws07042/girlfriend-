init python:
    bg_files = {"office":"BG_OFFICE_DAY_001.png","evening":"BG_OFFICE_NIGHT_001.png","lounge":"BG_LOUNGE_DAY_001.png","terrace":"BG_TERRACE_DAY_001.png","cafe":"BG_CAFE_001.png","home":"BG_HOME_NIGHT_001.png","meeting":"BG_MEETING_ROOM_001.png","meeting_night":"BG_MEETING_ROOM_NIGHT_001.png","studio":"BG_DESIGN_STUDIO_001.png","development":"BG_DEVELOPMENT_SPACE_001.png","marketing":"BG_MARKETING_PROJECT_001.png","elevator":"BG_ELEVATOR_001.png","hotel":"BG_HOTEL_LOBBY_001.png","restaurant":"BG_RESTAURANT_001.png","rooftop":"BG_ROOFTOP_NIGHT_001.png","rain":"BG_STREET_RAIN_001.png","bar":"BG_BAR_001.png"}
    def office_bg(key):
        filename = "images/bg/" + bg_files.get(key,bg_files["office"])
        if renpy.loadable(filename): return Transform(filename, xysize=(1920,1080),fit="cover")
        return Solid("#23353f")

transform ria_idle:
    subpixel True
    align (0.77, 0.50)
    zoom 0.93
    block:
        ease 2.4 yoffset -3 rotate 0.25
        ease 2.4 yoffset 0 rotate -0.25
        repeat

transform ria_still:
    align (0.77, 0.50)
    zoom 0.93

# Equal panels remain a draft. Crop and ATL use existing images, no paid rig.
image ria open = Crop((0,0,682,768), "images/cg/ria_expression_sheet_v001.png")
image ria blink = Crop((683,0,682,768), "images/cg/ria_expression_sheet_v001.png")
image ria quiet = Crop((1366,0,682,768), "images/cg/ria_expression_sheet_v001.png")
image ria animated:
    "ria open"
    3.6
    "ria blink"
    0.12
    "ria open"
    2.8
    "ria blink"
    0.12
    repeat

define config.name = "퇴근 후, 우리"
define config.version = "0.3.0-first-week"
define config.screen_width = 1920
define config.screen_height = 1080
define config.save_directory = "MomentWorksOffice-20261001"
define config.window_title = "퇴근 후, 우리 · Ren'Py 첫 주"
define config.rollback_enabled = True
define config.default_text_cps = 35
define config.default_afm_time = 15
define config.has_sound = False
define config.has_music = False
define config.has_voice = False
define build.name = "AfterWorkOffice"
init python:
    config.overlay_screens.append("office_hud")
    build.classify("**/saves/**", None)
    build.classify("**/tests/**", None)
    build.classify("**/*.md", None)

init -2 python:
    gui.init(1920,1080)

define _game_menu_screen = "save"

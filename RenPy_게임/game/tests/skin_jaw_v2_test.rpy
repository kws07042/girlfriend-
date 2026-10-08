testcase office_skin_jaw_v2:
    pause until screen "main_menu"
    $ _skin_cps = preferences.text_cps
    run Preference("text speed",0)
    click "첫날 시작"
    advance until screen "choice"
    run SetVariable("ui_ria_preview_time",0.0)
    assert eval not persistent.ria_animation
    run SetField(persistent,"ria_animation",True)
    assert eval not ui_ria_animation_active("ria")
    run SetField(persistent,"ria_animation",False)
    run Jump("day02")
    advance until screen "phone"
    click "어디까지 필요한지 듣고 맡을 일을 정할게요."
    pause 5.2
    click "계속"
    run Function(ui_camera_set,"C")
    run Function(ui_expression_set,"seoyun","normal")
    pause 0.3
    assert eval ui_expression_current("seoyun") == "normal"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\seoyun_normal_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("seoyun"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\seoyun_normal.png",width=2048,height=3070,resize=True)
    run Function(ui_expression_set,"seoyun","smile")
    pause 0.3
    assert eval ui_expression_current("seoyun") == "smile"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\seoyun_smile_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("seoyun"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\seoyun_smile.png",width=2048,height=3070,resize=True)
    run Function(ui_expression_set,"seoyun","serious")
    pause 0.3
    assert eval ui_expression_current("seoyun") == "serious"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\seoyun_serious_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("seoyun"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\seoyun_serious.png",width=2048,height=3070,resize=True)
    run Function(ui_expression_set,"seoyun","sheepish")
    pause 0.3
    assert eval ui_expression_current("seoyun") == "sheepish"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\seoyun_sheepish_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("seoyun"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\seoyun_sheepish.png",width=2048,height=3070,resize=True)
    run Function(ui_expression_set,"seoyun",None)
    run Jump("day04")
    advance until screen "phone"
    click "각 시안에서 지키고 싶은 부분을 듣고 싶어요."
    pause 5.2
    click "계속"
    run Function(ui_camera_set,"C")
    run Function(ui_expression_set,"yujin","normal")
    pause 0.3
    assert eval ui_expression_current("yujin") == "normal"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\yujin_normal_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("yujin"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\yujin_normal.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"yujin","smile")
    pause 0.3
    assert eval ui_expression_current("yujin") == "smile"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\yujin_smile_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("yujin"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\yujin_smile.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"yujin","serious")
    pause 0.3
    assert eval ui_expression_current("yujin") == "serious"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\yujin_serious_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("yujin"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\yujin_serious.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"yujin","sheepish")
    pause 0.3
    assert eval ui_expression_current("yujin") == "sheepish"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\yujin_sheepish_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("yujin"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\yujin_sheepish.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"yujin",None)
    run Jump("day05")
    advance until screen "phone"
    click "첫 방문부터 재방문까지 단계별로 정리하겠습니다."
    pause 5.2
    click "계속"
    run Function(ui_camera_set,"C")
    run Function(ui_expression_set,"jihyun","normal")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "normal"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\jihyun_normal_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("jihyun"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\jihyun_normal.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"jihyun","smile")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "smile"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\jihyun_smile_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("jihyun"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\jihyun_smile.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"jihyun","serious")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "serious"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\jihyun_serious_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("jihyun"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\jihyun_serious.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"jihyun","sheepish")
    pause 0.3
    assert eval ui_expression_current("jihyun") == "sheepish"
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\jihyun_sheepish_skin_v2.png")
    $ renpy.render_to_file(ui_character_static_sprite("jihyun"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\jihyun_sheepish.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"jihyun",None)
    run Jump("d1_work_intro")
    advance until eval _last_say_who == "ri"
    advance
    assert eval ui_pose_current("ria") == "explaining"
    run Function(ui_camera_set,"B")
    run Function(ui_expression_set,"ria","serious")
    pause 0.5
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2\ria_work_jaw_static_v2.png")
    run SetVariable("ui_ria_preview_time",0.0)
    pause 0.05
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2/ria_static_0.png")
    run SetVariable("ui_ria_preview_time",1.0)
    pause 0.05
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2/ria_static_1.png")
    run SetVariable("ui_ria_preview_time",3.0)
    pause 0.05
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2/ria_static_3.png")
    run SetVariable("ui_ria_preview_time",5.0)
    pause 0.05
    $ renpy.screenshot(r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2/ria_static_5.png")
    $ renpy.render_to_file(ui_character_static_sprite("ria",pose="casual",expression="smile"),r"C:\Users\user\Desktop\건\오피스\RenPy_게임\샘플\피부턱수정_v2/ria_live2d_base.png",width=2048,height=3072,resize=True)
    run Function(ui_expression_set,"ria",None)
    run Function(ui_camera_set,None)
    run SetVariable("ui_ria_preview_time",None)
    run Preference("text speed",_skin_cps)
    exit

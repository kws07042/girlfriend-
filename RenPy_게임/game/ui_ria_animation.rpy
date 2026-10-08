# Legacy PNG pilot is suspended while the actual Live2D model is prepared.
default persistent.ria_animation = True
default ui_ria_preview_time = None
default ui_ria_eye_override = None
default persistent.ria_animation_review_version = 0

init 40 python:
    import math as ui_ria_math
    import time as ui_ria_clock
    if (persistent.ria_animation_review_version or 0) < 2:
        persistent.ria_animation = False
        persistent.ria_animation_review_version = 2

    renpy.register_shader("office.ria_head", variables="""
        uniform mat4 u_transform;
        attribute vec4 a_position;
        uniform vec2 u_model_size;
        uniform float u_ria_angle;
        uniform vec2 u_ria_shift;
    """, vertex_300="""
        float ria_weight = 1.0 - smoothstep(0.13, 0.22, a_position.y / u_model_size.y);
        vec2 ria_pivot = vec2(u_model_size.x * 0.5, u_model_size.y * 0.155);
        vec2 ria_local = a_position.xy - ria_pivot;
        float ria_angle = u_ria_angle * ria_weight;
        float ria_c = cos(ria_angle);
        float ria_s = sin(ria_angle);
        vec2 ria_rotated = vec2(ria_c * ria_local.x - ria_s * ria_local.y,
                               ria_s * ria_local.x + ria_c * ria_local.y);
        vec2 ria_delta = ria_rotated - ria_local + u_ria_shift * ria_weight;
        gl_Position = u_transform * (a_position + vec4(ria_delta, 0.0, 0.0));
    """)

    UI_RIA_LEGACY_ANIMATION_APPROVED = False
    def ui_ria_animation_active(who="ria"):
        return (UI_RIA_LEGACY_ANIMATION_APPROVED and who == "ria" and persistent.ria_animation and not persistent.reduce_motion
                and not renpy.is_skipping() and getattr(store,"ui_scene_actor",None)=="ria"
                and not getattr(store,"ui_call_contact",None)
                and not any(renpy.get_screen(s) for s in ("phone","save","load","preferences","history")))

    def ui_ria_phase():
        if store.ui_ria_preview_time is not None:
            return float(store.ui_ria_preview_time)
        return ui_ria_clock.time() - ui_ria_phase.epoch
    ui_ria_phase.epoch = ui_ria_clock.time()

    def ui_ria_eye_state(t=None):
        if store.ui_ria_eye_override in ("open","half","closed"):
            return store.ui_ria_eye_override
        t = ui_ria_phase() if t is None else float(t)
        t %= 13.0
        for start in (2.35,8.0):
            d = t-start
            if 0.0 <= d < 0.04 or 0.11 <= d < 0.16:
                return "half"
            if 0.04 <= d < 0.11:
                return "closed"
        return "open"

    def ui_ria_blink_draw(st, at):
        base = ui_character_sprite("ria")
        if not ui_ria_animation_active():
            return base, None
        state = ui_ria_eye_state()
        if state == "open":
            return base, 0.016
        path = "images/characters/ria_animation/%s.png" % state
        if not renpy.loadable(path):
            return base, 0.016
        eyes = AlphaMask(path,"images/characters/ria_animation/eyes_mask.svg")
        return Composite((2048,3072),(0,0),base,(740,40),eyes), 0.016

    def ui_ria_head_update(trans,st,at):
        # Old saves may still reference this transform. Keep it strictly static.
        trans.u_ria_angle = 0.0
        trans.u_ria_shift = (0.0,0.0)
        return None

    def ui_character_present(who):
        if not ui_ria_animation_active(who):
            return ui_character_sprite(who)
        cached = getattr(ui_character_present,"blink_only",None)
        if cached is None:
            cached = DynamicDisplayable(ui_ria_blink_draw)
            ui_character_present.blink_only = cached
        return cached

transform ui_ria_head:
    mesh (32,48)
    shader "office.ria_head"
    u_ria_angle 0.0
    u_ria_shift (0.0,0.0)
    function ui_ria_head_update

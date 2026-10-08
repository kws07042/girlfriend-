# Scene exits freeze their outgoing portrait before location-dependent state changes.
default ui_scene_key = None
default ui_scene_actor = None
default ui_scene_context = None
default ui_scene_presence_version = 0
default ui_scene_in_transition = False
default ui_scene_frozen_sprites = {}
default ui_scene_frozen_frame = None

init 25 python:
    config.overlay_during_with = True

    def ui_scene_restore_actor():
        # A transition snapshot belongs to one render pass, never to a loaded save.
        store.ui_scene_in_transition = False
        store.ui_scene_frozen_sprites = {}
        store.ui_scene_frozen_frame = None
        if store.ui_scene_key == "home" or "집" in getattr(store,"place","") or store.ui_call_contact:
            store.ui_scene_actor = None
        # Preserve an intentional absence even in older saves. A missing legacy
        # portrait is shown by the next real character line, never guessed from
        # the preceding call or camera actor.
        store.ui_scene_presence_version = 1

    config.after_load_callbacks.append(ui_scene_restore_actor)

    def ui_scene_show(key):
        changed = key != store.ui_scene_key
        context = (getattr(store,"day",1),getattr(store,"place",None),getattr(store,"slot",None),getattr(store,"chapter",None))
        new_context = context != store.ui_scene_context
        animated = changed and not persistent.reduce_motion and not renpy.is_skipping()
        store.ui_scene_presence_version = 1
        if animated:
            # Freeze while ui_scene_key still names the outgoing location.
            store.ui_scene_frozen_sprites = {who:ui_character_static_sprite(who,pose=ui_pose_current(who)) for who in ui_pose_files}
            store.ui_scene_frozen_frame = ui_bc_motion_values()
            store.ui_scene_in_transition = True
        try:
            if animated:
                renpy.with_statement(None)
            if changed or new_context or key == "home":
                store.ui_scene_actor = None
                store.ui_pose_transitions = {}
                store.ui_poses = {}
                store.ui_pose_last_actor = None
                store.ui_pose_context = None
            renpy.scene()
            renpy.show("background",what=office_bg(key))
            store.ui_scene_key = key
            store.ui_scene_context = context
            if animated:
                renpy.with_statement(Dissolve(0.4))
        finally:
            store.ui_scene_in_transition = False
            store.ui_scene_frozen_sprites = {}
            store.ui_scene_frozen_frame = None
        if changed or new_context:
            # The next portrait enters with the next scene's frame; the outgoing
            # portrait never zooms towards a future character's camera setting.
            store.ui_camera_mode = "B"
            store.ui_camera_actor = None
            store.ui_camera_place = getattr(store,"place",None)
            zoom,x = (1.5,480.0) if ui_camera_current()=="C" else (1.0,610.0)
            store.ui_bc_motion_from_zoom = store.ui_bc_motion_to_zoom = zoom
            store.ui_bc_motion_from_x = store.ui_bc_motion_to_x = x
            store.ui_bc_motion_start = ui_motion_clock.time()
        return changed

default ui_bc_motion_start = 0.0
default ui_bc_motion_from_zoom = 1.0
default ui_bc_motion_from_x = 610.0
default ui_bc_motion_to_zoom = 1.0
default ui_bc_motion_to_x = 610.0

init 25 python:
    import time as ui_motion_clock

    def ui_bc_motion_values():
        if store.ui_scene_in_transition and store.ui_scene_frozen_frame is not None:
            return store.ui_scene_frozen_frame
        if persistent.reduce_motion or renpy.is_skipping():
            return store.ui_bc_motion_to_zoom, store.ui_bc_motion_to_x
        fraction = min(1.0, max(0.0, (ui_motion_clock.time() - store.ui_bc_motion_start) / 0.3))
        weight = fraction * fraction * (3.0 - 2.0 * fraction)
        zoom = store.ui_bc_motion_from_zoom + (store.ui_bc_motion_to_zoom - store.ui_bc_motion_from_zoom) * weight
        x = store.ui_bc_motion_from_x + (store.ui_bc_motion_to_x - store.ui_bc_motion_from_x) * weight
        return zoom, x

    def ui_bc_motion_schedule():
        if not hasattr(store, 'ui_camera_override') or not hasattr(store, 'ui_bc_motion_start'):
            return
        target_zoom, target_x = (1.5, 480.0) if ui_camera_current() == "C" else (1.0, 610.0)
        if target_zoom == store.ui_bc_motion_to_zoom and target_x == store.ui_bc_motion_to_x:
            return
        store.ui_bc_motion_from_zoom, store.ui_bc_motion_from_x = ui_bc_motion_values()
        store.ui_bc_motion_to_zoom, store.ui_bc_motion_to_x = target_zoom, target_x
        store.ui_bc_motion_start = ui_motion_clock.time()

    def ui_bc_frame_update(trans, st, at):
        zoom, x = ui_bc_motion_values()
        trans.zoom, trans.xpos = zoom, absolute(x)
        trans.ypos = 0
        return 0.02

    def ui_bc_tint_update(trans, st, at):
        zoom, x = ui_bc_motion_values()
        trans.alpha = min(1.0, max(0.0, (zoom - 1.0) * 2.0))
        return 0.02

transform ui_bc_frame:
    subpixel True
    function ui_bc_frame_update

transform ui_bc_tint:
    function ui_bc_tint_update







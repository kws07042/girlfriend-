# Authored pose changes with the original face of each accepted pose.
default ui_poses = {}
default ui_pose_overrides = {}
default ui_pose_context = None
default ui_pose_last_actor = None
default ui_pose_transitions = {}
default ui_pose_version = 0

init 30 python:
    import time as ui_pose_clock
    ui_pose_files = {'ria': {'listening': 'images/characters/ria_poses/listening.png', 'explaining': 'images/characters/ria_poses/explaining.png', 'casual': 'images/characters/ria_poses/casual.png'}, 'seoyun': {'work': 'images/characters/seoyun_poses/work.png', 'casual': 'images/characters/seoyun_poses/casual.png'}, 'yujin': {'work': 'images/characters/yujin_poses/work.png', 'casual': 'images/characters/yujin_poses/casual.png'}, 'jihyun': {'work': 'images/characters/jihyun_poses/work.png', 'casual': 'images/characters/jihyun_poses/casual.png'}}
    ui_pose_beats = {'ria': {'새로 오신 기획자 맞죠? 강리아예요. 캠페인 쪽 맡고 있어요. 커피는 아직 주문 안 하셨을 것 같아서.': 'master', '제가 현장 반응 자료를 가져왔어요. 숫자는 작지만, 사람들이 어느 지점에서 멈추는지는 보여요.': 'explaining', '지금도 모르는 건 많죠. 사람들 앞에서는 웃는 게 먼저 나와서 그렇지.': 'listening', '아까 유진 씨가 제 기록 이야기했을 때… 조금 좋았어요. 제가 만든 거라고 들리니까.': 'listening', '그렇게 물어보면 길어지는데. 괜찮아요?': 'listening', '그렇게 말해 주니까 좀 편해지네요. 자꾸 설명해야 인정받을 것 같아서.': 'listening', '그럼 카페 이야기. 여기 창가 빛이 오후에 예쁜데, 주말에는 너무 붐벼요.': 'casual', '이제 커피 마셔도 되겠네요. 숫자 먼저 보여 드렸으니까.': 'casual'}, 'jihyun': {'오늘은 여기까지 합시다. 내일 첫 화면 흐름을 보고 방향을 정하죠.': 'casual', '오늘의 결정은 여기까지입니다. 첫 주 수고했어요.': 'casual'}, 'yujin': {'이 폴더까지만 정리하고 갈게요. 기다려 주실 필요는 없어요.': 'casual'}, 'seoyun': {}}
    ui_pose_aliases = {"sy":"seoyun", "ri":"ria", "yj":"yujin", "jh":"jihyun"}

    def ui_pose_default(who):
        scene = getattr(store,"ui_scene_key",None)
        if who == "ria":
            return "casual" if scene in ("cafe","lounge","terrace") else "explaining"
        if who == "yujin":
            return "casual" if scene in ("cafe","lounge","terrace","elevator") or (scene == "studio" and getattr(store,"slot",None)=="evening") else "work"
        return "casual" if scene in ("cafe","lounge","terrace","elevator") else "work"

    def ui_pose_current(who):
        return store.ui_pose_overrides.get(who) or store.ui_poses.get(who, ui_pose_default(who))

    def ui_character_pose_file(who, pose=None):
        pose = pose or ui_pose_current(who)
        return ui_pose_files.get(who,{}).get(pose,"images/characters/%s_master.png" % who)

    def ui_pose_change(who, pose):
        old = ui_pose_current(who)
        store.ui_poses[who] = pose
        if old != pose and store.ui_pose_last_actor == who:
            store.ui_pose_transitions[who] = (old, pose, ui_pose_clock.time())

    def ui_pose_set(who, pose=None):
        if who not in ui_pose_files or pose not in (None,"master") and pose not in ui_pose_files[who]:
            raise ValueError("Unknown character pose")
        old = ui_pose_current(who)
        store.ui_pose_overrides[who] = pose
        new = ui_pose_current(who)
        if old != new:
            store.ui_pose_transitions[who] = (old,new,ui_pose_clock.time())

    def ui_pose_callback(event, **kwargs):
        if event != "begin":
            return
        context = (getattr(store,"day",1),getattr(store,"place",None),getattr(store,"slot",None),getattr(store,"chapter",None))
        if store.ui_pose_context != context:
            store.ui_poses = {}
            store.ui_pose_transitions = {}
            store.ui_pose_last_actor = None
            store.ui_pose_context = context
        if getattr(store,"ui_call_contact",None) or getattr(store,"ui_scene_key",None)=="home":
            return
        who = ui_pose_aliases.get(getattr(store,"_last_say_who",None))
        if who:
            what = getattr(store,"_last_say_what","")
            pose = ui_pose_beats.get(who,{}).get(what)
            if pose:
                ui_pose_change(who,pose)
            store.ui_pose_last_actor = who
            store.ui_pose_version = 1

    class UIPoseDissolve(renpy.Displayable):
        def __init__(self, previous, current, started):
            super(UIPoseDissolve,self).__init__()
            self.started = started
            self.transition = renpy.display.transition.Dissolve(0.18,old_widget=previous,new_widget=current,alpha=True)

        def render(self,width,height,st,at):
            elapsed = max(0.0,ui_pose_clock.time()-self.started)
            result = renpy.render(self.transition,width,height,elapsed,at)
            if elapsed < 0.18:
                renpy.redraw(self,0.02)
            return result

        def visit(self):
            return [self.transition]

    def ui_pose_render(st, at, who):
        if getattr(store,"ui_scene_in_transition",False):
            frozen = store.ui_scene_frozen_sprites.get(who)
            if frozen is not None:
                return frozen,None
        current = ui_character_static_sprite(who)
        transition = store.ui_pose_transitions.get(who)
        if transition and not persistent.reduce_motion and not renpy.is_skipping():
            old, new, start = transition
            if ui_pose_clock.time()-start < 0.18 and new == ui_pose_current(who):
                cache = getattr(ui_pose_render,"blend_cache",None)
                if cache is None:
                    ui_pose_render.blend_cache = cache = {}
                key = (old,new,start)
                if who not in cache or cache[who][0] != key:
                    previous = ui_character_static_sprite(who,pose=old)
                    cache[who] = (key,UIPoseDissolve(previous,current,start))
                return cache[who][1],0.02
        return current,None

    def ui_character_sprite(who):
        cache = getattr(ui_character_sprite,"cache",None)
        if cache is None:
            ui_character_sprite.cache = cache = {}
        if who not in cache:
            cache[who] = DynamicDisplayable(ui_pose_render,who)
        return cache[who]

    def ui_pose_after_load():
        store.ui_pose_transitions = {}
        if not store.ui_pose_version:
            ui_pose_callback("begin")
            if getattr(store,"ui_speaker",None)=="ria" and getattr(store,"ui_scene_key",None)=="cafe" and ui_camera_current()=="C":
                store.ui_poses["ria"] = "listening"
            store.ui_pose_version = 1

    config.all_character_callbacks.append(ui_pose_callback)
    config.after_load_callbacks.append(ui_pose_after_load)

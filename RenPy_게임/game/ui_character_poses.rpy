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
    ui_pose_files["ria"].update({
        "greeting": "images/characters/ria_poses/greeting.png",
        "honest": "images/characters/ria_poses/honest.png",
    })
    for _who in ("seoyun", "yujin", "jihyun"):
        ui_pose_files[_who]["listening"] = "images/characters/%s_poses/listening.png" % _who
    ui_pose_beats["ria"].update({
        "새로 오신 기획자 맞죠? 강리아예요. 캠페인 쪽 맡고 있어요. 커피는 아직 주문 안 하셨을 것 같아서.": "greeting",
        "몰랐어요. 그래서 설탕이랑 우유를 따로 챙겼죠. 실패할 때 빠져나갈 길은 있어야 하니까.": "casual",
        "어, 왔어요? 이 자리 비어 있어요. 첫날이라 혼자 메뉴 고르기 애매할까 봐 물어봤어요.": "greeting",
        "지도에 없는 정보가 중요하죠. 이 집은 줄이 길어도 빨리 나오고, 저 집은 한가해 보여도 오래 걸려요.": "casual",
        "어, 왔어요? 이쪽이에요. 자료 열어 놨어요.": "greeting",
        "어제 같이 찾은 빈 분류부터 볼까요? 그 질문이 나오기 전 행동도 붙여 봤어요.": "explaining",
        "어제 옮긴 약속, 오늘 자료 시간에 같이 보면 돼요. 쉬고 와서 질문해 주는 편이 더 좋아요.": "explaining",
        "제가 처음엔 제일 마음에 들어 했던 문구예요. 시선만 잡으면 됐다고 생각했거든요.": "honest",
        "사진 찍은 뒤 뭘 해야 할지 몰랐대요. 재밌게 해 준 사람은 됐는데, 안내한 사람은 못 된 거죠.": "honest",
        "네. 다음에는 처음부터 그 부분을 같이 봐 주세요. 실패를 꺼내는 데도 시간이 좀 들거든요.": "honest",
        "그렇게 말해 주니까 좀 편해지네요. 자꾸 설명해야 인정받을 것 같아서.": "honest",
        "좋아요. 하나로 다 하려다 둘 다 애매해졌을 수도 있겠네요.": "explaining",
        "맞아요. 같은 사람도 설명 듣고 바로 들어갔을 수 있으니까. 기록법부터 같이 바꿔 봐요.": "explaining",
    })
    ui_pose_beats["seoyun"]["그걸 구분하지 않고 계속해 온 것 같네요. 매번 금방 끝날 줄 알았거든요."] = "listening"
    ui_pose_beats["seoyun"].update({
        "계정 세 개가 같은 화면에 들어가는지만 확인해 주세요. 오류가 나면 고치기보다 상태를 남겨 주시면 돼요.": "work",
        "고마워요. 다만 각 담당자에게 먼저 확인해야 해요. 목록만 보고 나누면 실제 업무와 다를 수 있거든요.": "work",
        "테스트 계정 상태를 확인해 주세요. 담당자 칸은 제가 당사자들과 먼저 이야기할게요.": "work",
    })
    ui_pose_beats["yujin"]["그 감상은 고마워요. 다만 처음 보는 사람도 다음 행동을 찾을 수 있을까요?"] = "listening"
    ui_pose_beats["yujin"]["화면은 첫 행동과 후속 경험으로 나눠 설명할 수 있어요."] = "work"
    ui_pose_beats["jihyun"]["도현 씨도 그래요? 저는 비 오는 날이면 자꾸 같은 걸 틀게 돼요."] = "listening"
    ui_pose_beats["jihyun"]["그럼 나중에 제목 알려 드릴게요. 보고 나서 재미없었다고 해도 괜찮고요."] = "casual"
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

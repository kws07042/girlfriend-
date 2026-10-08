# Original pose faces are displayed without eye/mouth/skin overlays.
default ui_seoyun_expression = "normal"
default ui_seoyun_expression_override = None
default ui_expression_context = None
default ui_other_expressions = {}
default ui_other_expression_overrides = {}
default ui_other_expression_version = 0

init 25 python:
    import json as ui_skin_json
    with renpy.file("ui_face_tones.json") as ui_skin_file:
        ui_face_tones = ui_skin_json.load(ui_skin_file)
    renpy.register_shader("office.skin_match", variables="""
        uniform vec3 u_face_tone;
    """, fragment_300="""
        float skin_a = gl_FragColor.a;
        vec3 skin_c = gl_FragColor.rgb / max(skin_a,0.001);
        float skin_max = max(skin_c.r,max(skin_c.g,skin_c.b));
        float skin_min = min(skin_c.r,min(skin_c.g,skin_c.b));
        float skin_sat = (skin_max-skin_min)/max(skin_max,0.001);
        float skin_weight = smoothstep(0.72,0.84,skin_c.r) * smoothstep(0.45,0.56,skin_c.g);
        skin_weight *= smoothstep(0.025,0.065,skin_c.g-skin_c.b);
        skin_weight *= 1.0-smoothstep(0.43,0.52,skin_sat);
        skin_weight *= 1.0-smoothstep(0.28,0.40,skin_c.r-skin_c.g);
        gl_FragColor.rgb = clamp(skin_c + u_face_tone*skin_weight,0.0,1.0)*skin_a;
    """)
    ui_seoyun_expression_files = {
        "smile": "images/characters/seoyun_expressions/smile.png",
        "serious": "images/characters/seoyun_expressions/serious.png",
        "surprised": "images/characters/seoyun_expressions/surprised.png",
        "sheepish": "images/characters/seoyun_expressions/sheepish.png",
    }
    ui_seoyun_expression_beats = {
        "도현 씨? 한서윤이에요. 서비스 기획 쪽은 저한테 물어보시면 돼요. 첫날이니까 오늘은 방향부터 같이 보죠.": "smile",
        "루멘은 조명과 루틴 기록 서비스를 같이 보여 주려는 브랜드예요. 행사와 웹페이지가 동시에 열릴 거고요.": "serious",
        "좋아요. 오늘은 그 빈칸을 찾는 게 중요한 일이에요.": "smile",
        "자료 위치는 메신저에 남겨 둘게요. 첫날에 전부 외우려고 하지 않아도 돼요.": "smile",
        "도현 씨, 오셨어요? 여기 앉으시면 같이 보기 편해요.": "smile",
        "이건 서비스 흐름이고, 이쪽 작은 칸들은 그 흐름이 멈추지 않게 하는 일들이에요.": "serious",
        "담당이 정해지지 않으면 일단 제 이름을 넣어 둬요. 기다리다가 빠뜨리는 것보다는 나으니까요.": "serious",
        "그걸 구분하지 않고 계속해 온 것 같네요. 매번 금방 끝날 줄 알았거든요.": "sheepish",
        "계정 세 개가 같은 화면에 들어가는지만 확인해 주세요. 오류가 나면 고치기보다 상태를 남겨 주시면 돼요.": "serious",
        "고마워요. 다만 각 담당자에게 먼저 확인해야 해요. 목록만 보고 나누면 실제 업무와 다를 수 있거든요.": "serious",
        "테스트 계정 상태를 확인해 주세요. 담당자 칸은 제가 당사자들과 먼저 이야기할게요.": "serious",
        "이렇게 남겨 주면 제가 같은 확인을 또 하지 않아도 되겠네요.": "smile",
        "좋아요. 도현 씨가 해 준 일을 제 체크 표시로만 남기지 않을게요.": "smile",
        "도움이 안 되는 책을 고르려니까 더 어려운데요. 그냥 재미있는 걸로 해도 될까요?": "sheepish",
    }

    def ui_seoyun_expression_set(expression=None):
        if expression not in (None, "normal", "smile", "serious", "surprised", "sheepish"):
            raise ValueError("Unknown Seoyun expression")
        store.ui_seoyun_expression_override = expression

    def ui_seoyun_expression_current():
        return store.ui_seoyun_expression_override or store.ui_seoyun_expression

    # Separate saved state per heroine. Unknown/normal expressions use the approved MASTER.
    ui_other_expression_beats = {
        "ria": {
            "새로 오신 기획자 맞죠? 강리아예요. 캠페인 쪽 맡고 있어요. 커피는 아직 주문 안 하셨을 것 같아서.": "smile",
            "몰랐어요. 그래서 설탕이랑 우유를 따로 챙겼죠. 실패할 때 빠져나갈 길은 있어야 하니까.": "smile",
            "어, 왔어요? 이 자리 비어 있어요. 첫날이라 혼자 메뉴 고르기 애매할까 봐 물어봤어요.": "smile",
            "어, 왔어요? 이쪽이에요. 자료 열어 놨어요.": "smile",
            "네. 약속 지켰으니까, 이제는 진짜 점심 끝!": "smile",
            "좋아요. 하나로 다 하려다 둘 다 애매해졌을 수도 있겠네요.": "smile",
            "이제 커피 마셔도 되겠네요. 숫자 먼저 보여 드렸으니까.": "smile",
            "그건 오늘 가장 중요한 성과일지도요.": "smile",
            "좋아요. 그럼 이번 주 제일 웃겼던 일부터 말할게요.": "smile",
            "그거면 금요일 저녁은 성공이죠.": "smile",
            "제가 현장 반응 자료를 가져왔어요. 숫자는 작지만, 사람들이 어느 지점에서 멈추는지는 보여요.": "serious",
            "네. 사람들한테 말 거는 건 빠른데, 말만 걸고 끝내면 남는 게 없잖아요.": "serious",
            "둘 다요. 어떤 질문인지 나누면 달라요. 기능을 묻는 사람은 관심이 있고, 어디부터 해야 하냐고 묻는 사람은 길을 잃은 거예요.": "serious",
            "잘된 것도 필요하죠. 다만 그 숫자만 남기면 제가 왜 문구를 바꾸자는지 사라져요.": "serious",
            "제가 만든 방법이니까 제가 쓸게요. 도현 씨는 처음 보는 사람 입장에서 빠진 곳을 찾아 주세요.": "serious",
            "오늘 정리한 질문은 자료 폴더에 두었어요. 현장에서 또 물어볼 때 같은 방법으로 기록해 볼게요.": "serious",
            "아, 진짜네. 누가 기억해 주니까 이제 마시겠다.": "surprised",
            "진짜요? 저는 큰 공연보다 관객 가까이 있는 작은 무대가 좋더라.": "surprised",
            "지금도 모르는 건 많죠. 사람들 앞에서는 웃는 게 먼저 나와서 그렇지.": "sheepish",
            "아까 유진 씨가 제 기록 이야기했을 때… 조금 좋았어요. 제가 만든 거라고 들리니까.": "sheepish",
            "그렇게 물어보면 길어지는데. 괜찮아요?": "sheepish",
            "그렇게 말해 주니까 좀 편해지네요. 자꾸 설명해야 인정받을 것 같아서.": "sheepish",
            "제가 처음엔 제일 마음에 들어 했던 문구예요. 시선만 잡으면 됐다고 생각했거든요.": "sheepish",
            "사진 찍은 뒤 뭘 해야 할지 몰랐대요. 재밌게 해 준 사람은 됐는데, 안내한 사람은 못 된 거죠.": "sheepish",
            "네. 다음에는 처음부터 그 부분을 같이 봐 주세요. 실패를 꺼내는 데도 시간이 좀 들거든요.": "sheepish"
        },
        "yujin": {
            "오셨네요. 시안은 여기 나란히 놓아뒀어요.": "smile",
            "그 차이를 느꼈다면 두 개를 만든 이유가 전달된 거네요.": "smile",
            "좋아요. A를 좋아했다는 말까지 취소하지는 않아도 돼요. 어디에 쓸지 찾으면 되니까요.": "smile",
            "네. 제가 찾을 수 있으면 되는 자리도 있으니까요.": "smile",
            "두 시안은 같이 보관했어요. 고르지 않은 쪽도 쓰일 곳을 찾을 수 있겠죠.": "smile",
            "브랜드 자료는 공유 폴더에 있어요. 먼저 보시고, 이해가 안 되는 부분이 있으면 이야기해 주세요.": "serious",
            "A는 조명이 만드는 분위기, B는 오늘 할 행동을 먼저 보여 줘요. 어느 쪽이 더 예쁜지만 고르려는 회의는 아니에요.": "serious",
            "가능해요. 다만 A를 장식으로만 붙이지 말고, 조명을 켠 다음의 경험으로 이어 주세요.": "serious",
            "네. 남길 이유와 바꿀 이유를 같이 적어 봐요.": "serious",
            "그 감상은 고마워요. 다만 처음 보는 사람도 다음 행동을 찾을 수 있을까요?": "serious",
            "화면은 첫 행동과 후속 경험으로 나눠 설명할 수 있어요.": "serious",
            "제품이 왜 필요한지와 어떤 느낌을 주는지가 같이 남았으면 해요. 클릭 수만으로는 그 부분을 설명하기 어렵죠.": "serious",
            "그래서 함께 남기고 싶었어요. 나중에 제가 봐도 왜 바꿨는지 알 수 있게요.": "sheepish",
            "이 폴더까지만 정리하고 갈게요. 기다려 주실 필요는 없어요.": "sheepish"
        },
        "jihyun": {
            "오셨군요. 다들 모였으니 시작할까요?": "smile",
            "좋아요. 제가 전달할 내용과 팀에서 검증할 내용을 구분할 수 있겠어요.": "smile",
            "오늘의 결정은 여기까지입니다. 첫 주 수고했어요.": "smile",
            "다섯 번 출근하니 길은 익숙해졌나요?": "smile",
            "오늘 목표는 완성본이 아니에요. 역할과 모르는 부분을 확인하는 것부터 합시다.": "serious",
            "맞아요. 오늘은 고객이 기대하는 경험과 우리가 준비한 경험의 차이를 정리해 주세요.": "serious",
            "오늘 무엇을 결정해야 하죠? 먼저 각자 성공이라고 부르는 결과부터 이야기해 주세요.": "serious",
            "행사 반응과 서비스 재방문을 한 숫자로 적으면, 잘된 부분 뒤에 빠진 부분이 가려지겠네요.": "serious",
            "역할표 수정본을 기준으로 갑시다. 다만 아직 확인하지 못한 항목은 확정이라고 외부에 말하지 않을게요.": "serious",
            "다음 주 발표 전까지 무엇을 검증할지 정합시다. 오늘 안에 전부 답하려고 하진 말고요.": "serious",
            "모르는 것을 숨기면 제가 판단할 정보도 줄어들죠. 앞으로도 분명하게 말해 주세요.": "serious",
            "저도 이름보다 어디 있는지로 기억해요. 그건 오래 다닌다고 다르지 않네요.": "sheepish"
        }
    }
    ui_expression_aliases = {"ri":"ria", "yj":"yujin", "jh":"jihyun"}
    ui_other_reaction_beats = {
        ("ria", "분류 근거도 리아 씨 설명으로 남길게요."): "surprised",
        ("yujin", "설명 없이 시안을 바꾸면 이 메모들은 다 사라지겠네요."): "surprised",
        ("jihyun", "행사에서 시작한 기록이 집에서도 이어지는지 확인할 접점이 비어 있어요. 첫날 종료 화면과 다음 날 안내를 먼저 검증해 봅시다."): "surprised",
        ("yujin", "정리된 책상과 마음에 드는 책상은 같지 않을 수도 있겠네요."): "smile",
    }

    def ui_expression_set(who, expression=None):
        if who == "seoyun":
            return ui_seoyun_expression_set(expression)
        if who not in ui_other_expression_beats or expression not in (None,"normal","smile","serious","surprised","sheepish"):
            raise ValueError("Unknown heroine or expression")
        store.ui_other_expression_overrides[who] = expression

    def ui_expression_current(who):
        if who == "seoyun":
            return ui_seoyun_expression_current()
        return store.ui_other_expression_overrides.get(who) or store.ui_other_expressions.get(who,"normal")

    def ui_expression_callback(event, **kwargs):
        if event != "begin" or not hasattr(store, "ui_seoyun_expression"):
            return
        context = (getattr(store,"day",1), getattr(store,"place",None))
        if store.ui_expression_context != context:
            store.ui_seoyun_expression = "normal"
            store.ui_other_expressions = {}
            store.ui_expression_context = context
        if getattr(store,"ui_call_contact",None) or getattr(store,"ui_scene_key",None) == "home":
            return
        who = getattr(store,"_last_say_who",None)
        what = getattr(store,"_last_say_what","")
        actor = ui_expression_aliases.get(who)
        store.ui_other_expression_version = 1
        if actor:
            store.ui_other_expressions[actor] = ui_other_expression_beats[actor].get(what,"normal")
        elif who == "dh":
            actor = getattr(store,"ui_speaker",None)
            reaction = ui_other_reaction_beats.get((actor,what))
            if reaction:
                store.ui_other_expressions[actor] = reaction
        if who == "sy" and what in ui_seoyun_expression_beats:
            store.ui_seoyun_expression = ui_seoyun_expression_beats[what]
        elif who is None and getattr(store,"ui_speaker",None) == "seoyun" and what == "서윤이 펜을 들었다가 내려놓았다. 목록을 발견했다는 이유로 내가 모두 다시 정할 수는 없다.":
            store.ui_seoyun_expression = "sheepish"
        elif who == "dh" and getattr(store,"ui_speaker",None) == "seoyun" and what == "목록에 제 이름도 적어 주세요. 임시로 맡았는지 계속 맡는지도 같이요.":
            store.ui_seoyun_expression = "surprised"

    def ui_character_static_sprite(who, pose=None, expression=None):
        # Keep authored geometry and facial features. The whole sprite receives
        # smooth colour calibration to its MASTER; no eye/mouth overlay is used.
        return ui_character_palette_sprite(who, pose)

    def ui_expression_after_load():
        if store.ui_expression_context is None or not store.ui_other_expression_version:
            ui_expression_callback("begin")

    ui_other_expression_beats["ria"].update({
        "좋아요. 처음에는 제가 좋아하는 걸 사람들이 좋아할 줄 알았어요. 그런데 반응을 보다 보니 반대일 때도 있더라고요.": "serious",
        "그걸 인정하는 게 조금 어려웠는데, 틀린 걸 확인해도 다음 걸 만들 수 있다는 게 좋았어요.": "sheepish",
        "그 문장은 마음에 드는데. 다음 발표에 써도 돼요?": "smile",
        "그럼 카페 이야기. 여기 창가 빛이 오후에 예쁜데, 주말에는 너무 붐벼요.": "smile",
        "그건 순수하게 제 취향입니다. 숫자 안 붙일래요.": "smile",
    })
    config.all_character_callbacks.append(ui_expression_callback)
    config.after_load_callbacks.append(ui_expression_after_load)


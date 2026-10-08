define dh = Character("도현", color="#cbdbe5")
define sy = Character("서윤", color="#c8deca", callback=ui_speaker_callback("seoyun"))
define ri = Character("리아", color="#edc28c", callback=ui_speaker_callback("ria"))
define yj = Character("유진", color="#d9b4c4", callback=ui_speaker_callback("yujin"))
define jh = Character("지현", color="#c6cbd4", callback=ui_speaker_callback("jihyun"))
define message_data = {'lunch_invite': {'time': '12:20', 'texts': ['첫날이라 메뉴 고르기 애매하죠?', '점심 같이 먹을래요? 라운지 쪽에 있어요.'], 'reply': [{'id': 'talk', 'text': '좋아요. 같이 먹으면서 이야기해요.', 'response': '좋아요! 창가 쪽 자리 비워 둘게요.', 'plan': 'talk'}, {'id': 'rest', 'text': '오늘은 잠깐 쉬고 싶어요. 오후에 이야기해요.', 'response': '네, 편하게 쉬어요. 오후에 봐요.', 'plan': 'rest'}]}, 'cafe_photo': {'time': '18:55', 'texts': ['회사 앞 카페예요. 저는 잠깐 들러서 쉬는 중!', '시간 괜찮으면 전화로 이야기할래요?'], 'photo': True}, 'goodnight': {'time': '21:10', 'texts': ['오늘 수고했어요. 첫날인데 질문 잘 받아 줘서 고마워요.', '내일 회사에서 봐요.'], 'reply': [{'id': 'warm', 'text': '오늘 이야기 좋았어요. 내일 봐요.', 'response': '저도요. 잘 쉬어요!'}, {'id': 'brief', 'text': '수고하셨어요. 내일 봬요.', 'response': '네! 편하게 쉬어요.'}]}}

label start:
    $ chapter = "첫 출근"
    $ slot = "morning"
    $ clock = "09:00"
    $ place = "모멘트웍스 · 오픈 오피스"
    $ place = "모멘트웍스 · 엘리베이터"
    $ ui_scene_show("elevator")
    "엘리베이터 문이 열리자 커피 향과 키보드 소리가 먼저 들어왔다. 유리문 너머로 아직 낯선 회사의 이름이 보인다."
    $ place = "모멘트웍스 · 오픈 오피스"
    $ ui_scene_show("office")
    "모멘트웍스. 오늘부터 나는 이곳의 통합 기획자다. 책상 위에는 사원증과 새 노트, 그리고 여섯 주짜리 일정표가 놓여 있었다."
    dh "여섯 주 뒤 런칭이라… 첫날부터 여유 있는 일정은 아니네."
    sy "도현 씨? 한서윤이에요. 서비스 기획 쪽은 저한테 물어보시면 돼요. 첫날이니까 오늘은 방향부터 같이 보죠."
    "태블릿을 든 서윤이 빈 자리를 가리켰다. 맞은편에서는 유진이 두 장의 시안을 나란히 놓고 있었다."
    yj "브랜드 자료는 공유 폴더에 있어요. 먼저 보시고, 이해가 안 되는 부분이 있으면 이야기해 주세요."
    jh "오늘 목표는 완성본이 아니에요. 역할과 모르는 부분을 확인하는 것부터 합시다."
    "세 사람의 설명을 노트에 옮기고 있을 때, 책상 모서리에 커피 한 잔이 놓였다."
    ri "새로 오신 기획자 맞죠? 강리아예요. 캠페인 쪽 맡고 있어요. 커피는 아직 주문 안 하셨을 것 같아서."
    dh "감사합니다. 그런데 제가 뭘 마시는지 어떻게 아셨어요?"
    ri "몰랐어요. 그래서 설탕이랑 우유를 따로 챙겼죠. 실패할 때 빠져나갈 길은 있어야 하니까."
    "금발 포니테일이 어깨 뒤로 가볍게 흔들렸다. 리아는 농담을 했지만, 컵을 놓을 때는 노트가 젖지 않는 자리를 골랐다."
    menu:
        "“선택할 수 있게 챙겨 주셨네요. 고마워요.”":
            $ flags.update({'firstImpression': 'observant'})
            jump d1_greeting_notice
        "“그럼 오늘 제 첫 결정은 커피 취향 공개네요.”":
            $ flags.update({'firstImpression': 'humor'})
            jump d1_greeting_joke
        "“앞으로 잘 부탁드립니다. 자료부터 확인할게요.”":
            $ flags.update({'firstImpression': 'formal'})
            jump d1_greeting_formal

label d1_greeting_notice:
    $ ui_scene_show("office")
    ri "그걸 알아봐 주는 사람은 별로 없는데. 보통은 그냥 아메리카노인지만 보거든요."
    dh "첫날부터 제 취향을 맞히실 필요는 없죠. 제가 알려 드리면 되니까."
    ri "좋아요. 커피 취향은 천천히 알아가는 걸로. 일하는 취향은 오늘 좀 봐야겠고요."
    call d1_team_round
    jump d1_work_intro

label d1_greeting_joke:
    $ ui_scene_show("office")
    ri "중요하죠. 나중에 회의가 길어지면 생존에 관련된 정보예요."
    dh "저는 우유 조금 넣는 쪽입니다. 생존 정보 등록해 주세요."
    ri "접수 완료. 대신 제가 커피 들고만 있고 안 마시면, 한 번쯤 알려 주세요."
    call d1_team_round
    jump d1_work_intro

label d1_greeting_formal:
    $ ui_scene_show("office")
    ri "네, 잘 부탁해요. 그런데 지금은 입사 면접 아니니까 어깨는 조금 내려도 돼요."
    dh "그렇게 긴장한 티가 났나요?"
    ri "조금요. 괜찮아요. 여기 있는 사람들도 처음엔 다 그랬을걸요."
    call d1_team_round
    jump d1_work_intro

label d1_work_intro:
    $ ui_scene_show("office")
    sy "루멘은 조명과 루틴 기록 서비스를 같이 보여 주려는 브랜드예요. 행사와 웹페이지가 동시에 열릴 거고요."
    dh "제가 맡는 건 두 흐름이 서로 어긋나지 않게 연결하는 일인가요?"
    jh "맞아요. 오늘은 고객이 기대하는 경험과 우리가 준비한 경험의 차이를 정리해 주세요."
    ri "제가 현장 반응 자료를 가져왔어요. 숫자는 작지만, 사람들이 어느 지점에서 멈추는지는 보여요."
    "리아가 화면을 돌렸다. 행사 사진 아래에는 방문객이 머문 시간과 물어본 질문이 정리되어 있었다."
    dh "이 자료도 직접 정리하신 거예요?"
    ri "네. 사람들한테 말 거는 건 빠른데, 말만 걸고 끝내면 남는 게 없잖아요."
    yj "그 기록 덕분에 안내 문구를 바꿨죠. 이번에도 먼저 보시면 좋겠어요."
    "리아는 잠깐 유진을 보더니 화면을 조금 더 가까이 밀었다. 오늘 오전에 할 일을 정할 시간이다."
    menu:
        "리아와 자료를 함께 읽고 고객 흐름을 정리한다.":
            $ apply_effects({'project': 3, 'trust': 5, 'communication': 2, 'stress': 4})
            $ flags.update({'work': 'collaborate'})
            jump d1_work_together
        "자료를 받아 혼자 요구사항 초안을 먼저 작성한다.":
            $ apply_effects({'project': 4, 'planning': 2, 'stress': 8})
            $ flags.update({'work': 'focus'})
            jump d1_work_focus

label d1_work_together:
    $ ui_scene_show("office")
    dh "입장 직후보다 설명을 듣고 나서 질문이 많아지네요. 설명이 부족한 걸까요, 관심이 생긴 걸까요?"
    ri "둘 다요. 어떤 질문인지 나누면 달라요. 기능을 묻는 사람은 관심이 있고, 어디부터 해야 하냐고 묻는 사람은 길을 잃은 거예요."
    dh "그럼 첫 화면에서는 기능보다 다음 행동을 먼저 보여 주는 게 좋겠네요."
    ri "맞아요. 제가 말로만 설명했을 때보다 그 문장이 더 명확해요."
    "리아가 자신의 자료 옆에 내가 쓴 문장을 붙였다. 한 사람이 모든 답을 낸 것이 아니라 서로의 설명이 조금씩 이어졌다."
    dh "현장 기록은 리아 씨 자료라고 적어 둘게요. 제가 정리한 건 흐름 제안이고요."
    ri "좋아요. 다음에 반응을 더 모으면 그 문장도 같이 확인해 봐요."
    "첫 작업이 끝났을 때, 오전은 생각보다 빠르게 지나가 있었다."
    jump d1_lunch_gate

label d1_work_focus:
    $ ui_scene_show("office")
    dh "먼저 초안을 만들어 볼게요. 현장 기록에서 판단이 어려운 건 따로 표시해 두겠습니다."
    ri "좋아요. 숫자만 보면 오해할 수 있는 부분이 있어서, 거긴 제가 메모 붙여 둘게요."
    "혼자 읽어 보니 설명되지 않은 요구사항이 눈에 들어왔다. 질문과 가정을 다른 칸에 쓰자 문서가 조금 단순해졌다."
    dh "이건 확정 요구가 아니라 제 가정이라고 표시했습니다. 점심 이후에 한 번 확인 부탁드려도 될까요?"
    ri "그렇게 나누면 보기 편하죠. 빈칸이 있다고 바로 틀린 문서는 아니니까."
    sy "좋아요. 오늘은 그 빈칸을 찾는 게 중요한 일이에요."
    "초안을 저장하고 나서야 커피가 식어 있다는 걸 알았다. 아직 첫날인데 벌써 어깨가 조금 무겁다."
    jump d1_lunch_gate

label d1_lunch_gate:
    $ chapter = "같은 테이블"
    $ slot = "lunch"
    $ clock = "12:30"
    $ place = "모멘트웍스 · 라운지"
    $ ui_scene_show("lounge")
    $ flags["intro_common"] = True
    $ flags["first_lunch"] = "group"
    $ send_message("w1_lunch_group")
    $ phone_focus = "ria"
    "점심 자리를 맡은 리아에게 연락이 왔다. 오늘은 네 사람과 같은 테이블에서 밥을 먹기로 했다."
    $ renpy.retain_after_load()
    call screen phone(mode="story",initial_contact="ria",required_reply="w1_lunch_group")
    call intro_group_lunch
    jump d1_afternoon

label d1_lunch_talk:
    $ place = "모멘트웍스 · 라운지"
    $ ui_scene_show("lounge")
    $ apply_effects({'affection': 5, 'stress': -5})
    ri "어, 왔어요? 이 자리 비어 있어요. 첫날이라 혼자 메뉴 고르기 애매할까 봐 물어봤어요."
    dh "잘 물어보셨어요. 회사 주변은 지도만 봤거든요."
    ri "지도에 없는 정보가 중요하죠. 이 집은 줄이 길어도 빨리 나오고, 저 집은 한가해 보여도 오래 걸려요."
    dh "점심에도 현장 분석이네요."
    ri "직업병인가? 그래도 지금은 보고서 쓰지 않을 거예요."
    "노트북을 닫고 앉으니 오전에는 보이지 않던 것들이 눈에 들어온다. 리아의 컵에는 아직 커피가 절반이나 남아 있었다."
    dh "커피 들고만 있으면 알려 달라고 하셨죠. 지금 그런 상태 같은데요."
    ri "아, 진짜네. 누가 기억해 주니까 이제 마시겠다."
    ri "도현 씨는 쉬는 날에 뭐 해요? 일 얘기 말고."
    menu:
        "“조용한 곳에서 걷거나 책을 읽어요.”":
            $ flags.update({'hobby': 'quiet'})
            jump d1_hobby_quiet
        "“작은 공연 보러 가는 걸 좋아해요.”":
            $ flags.update({'hobby': 'music'})
            jump d1_hobby_music
        "“요즘은 쉬는 방법부터 다시 찾고 있어요.”":
            $ flags.update({'hobby': 'rest'})
            jump d1_hobby_rest

label d1_hobby_quiet:
    ri "저는 조용한 곳에서도 결국 플레이리스트를 켜요. 취향이 조금 다르네요."
    dh "같은 장소에 가서 다르게 쉬어도 괜찮지 않을까요?"
    ri "그건 좋네요. 꼭 같이 좋아해야 하는 건 아니니까."
    jump d1_afternoon

label d1_hobby_music:
    ri "진짜요? 저는 큰 공연보다 관객 가까이 있는 작은 무대가 좋더라."
    dh "무대 끝나고 동네를 걷는 시간까지 좋아합니다."
    ri "그럼 공연만 보고 바로 집에 가는 사람은 아니네요. 다음에 괜찮은 곳 있으면 알려 줄게요."
    jump d1_afternoon

label d1_hobby_rest:
    ri "그 말, 생각보다 공감돼요. 쉬려고 약속 잡았다가 더 피곤해질 때도 있죠."
    dh "아무것도 안 해도 괜찮은 시간을 조금 만들어 보려고요."
    ri "좋네요. 저도 웃고 떠들지 않아도 괜찮은 시간이 가끔 필요해요."
    jump d1_afternoon

label d1_lunch_rest:
    $ place = "모멘트웍스 · 테라스"
    $ ui_scene_show("terrace")
    $ apply_effects({'stress': -15})
    "점심은 혼자 먹기로 했다. 첫날에 모든 사람과 한꺼번에 친해질 필요는 없다는 생각이 들었다."
    dh "일단 숨 좀 돌리자."
    "난간 너머로 점심을 먹으러 가는 사람들이 보인다. 휴대전화에는 짧은 답장이 도착해 있다."
    if flags.get("first_lunch", "ria") != "rest":
        "문자를 나눈 상대도 편하게 쉬라는 답을 남겼다. 오후에 회사에서 다시 만나면 된다."
    else:
        "오전에 나눈 대화를 천천히 떠올렸다. 누구와 시간을 보낼지 오늘 안에 전부 결정할 필요는 없다."
    "거절했다는 이유로 분위기가 어색해지지는 않았다. 오히려 오후에는 조금 더 집중할 수 있을 것 같다."
    jump d1_afternoon

label d1_afternoon:
    $ chapter = "퇴근을 앞두고"
    $ clock = "17:50"
    $ place = "모멘트웍스 · 오픈 오피스"
    $ ui_scene_show("office")
    "오후에는 초안에 표시한 빈칸을 함께 확인했다. 새로운 업무를 추가하기보다 오전 작업을 마무리하는 시간이었다."
    jh "오늘은 여기까지 합시다. 내일 첫 화면 흐름을 보고 방향을 정하죠."
    sy "자료 위치는 메신저에 남겨 둘게요. 첫날에 전부 외우려고 하지 않아도 돼요."
    yj "현장 기록과 비주얼이 같이 보이니까 판단하기 편하네요. 내일은 두 시안 중 하나를 좁혀 봅시다."
    ri "오늘 질문했던 부분, 제가 원자료 링크 붙여 놨어요. 해석이 달라지면 내일 같이 보죠."
    dh "감사합니다. 첫날인데 혼자 헤매는 시간은 많이 줄었네요."
    ri "그럼 성공이네요. 혼자 헤매면 빨리 끝난 것 같아도 나중에 더 오래 걸리거든요."
    "리아는 자기 자리로 돌아갔다. 정리한 문서의 제목 아래에 오늘 함께 작업한 사람들의 이름이 보였다."
    "컴퓨터를 끄고 나서야 조금 긴장이 풀렸다. 현관으로 가기 전에 오늘 나눈 이야기가 떠올랐다."
    call d1_before_leaving
    jump intro_evening_gate

label d1_evening_gate:
    $ flags["first_evening"] = "ria"
    $ chapter = "회사 밖의 연락"
    $ slot = "evening"
    $ clock = "19:00"
    $ place = "모멘트웍스 · 엘리베이터"
    $ ui_scene_show("elevator")
    $ send_message("cafe_photo")
    "화면에 강리아라는 이름이 떠 있다. 회사 밖에서 받는 첫 연락이다."
    dh "지금은 통화할 수 있겠다. 아니면 나중에 문자로 이야기해도 되고."
    $ ring_who = "ria"
    $ phone_focus = "ria"
    $ ring_pending = True
    "리아에게 전화가 왔다. 휴대폰의 통화 탭에서 확인할 수 있다."
    $ renpy.retain_after_load()
    call screen phone(mode="evening")
    $ ring_pending = False
    if _return != "accept":
        $ phone_calls.append("19:00 · 강리아 · 부재중")
        menu:
            "다시 전화한다.":
                jump d1_phone_call
            "오늘은 쉰다고 문자를 보낸다.":
                $ phone_messages.append({"who":"ria","out":True,"text":"오늘은 집에서 쉬려고 해요. 내일 봐요.","time":clock,"day":day})
                jump d1_home
    jump d1_phone_call

label d1_cafe:
    $ ui_phone_call_end()
    $ chapter = "창가의 커피"
    $ place = "회사 앞 · 카페"
    $ ui_scene_show("cafe")
    $ apply_effects({'sensitivity': 3, 'stress': -8})
    "회사 앞 카페에는 노트북보다 책을 펼친 사람이 많았다. 창가에서 리아가 손을 들어 보였다."
    ri "어, 도현 씨! 여기예요. 사진이랑 같은 자리죠? 제가 약속 장소 설명은 잘해요."
    dh "네. 찾기 쉬웠습니다. 오늘은 커피도 바로 마시고 계시네요."
    ri "이제 급한 화면이 없으니까요. 아까는 생각하면서 들고만 있었나 봐요."
    "같은 커피인데 사무실에서 마셨을 때보다 향이 선명하다. 리아도 업무 자료를 펼치지 않았다."
    ri "첫날 어땠어요? 잘할 수 있을 것 같은지 말고, 그냥 어땠는지."
    dh "계속 평가받을 줄 알았는데, 모르는 걸 말해도 되는 분위기라 좋았습니다."
    ri "다행이다. 저도 첫날에는 아는 척하느라 더 힘들었거든요."
    dh "리아 씨는 오늘 그렇게 안 보였는데요."
    ri "지금도 모르는 건 많죠. 사람들 앞에서는 웃는 게 먼저 나와서 그렇지."
    "농담 뒤에 짧은 침묵이 생겼다. 이번에는 그 침묵을 급하게 채우지 않았다."
    ri "아까 유진 씨가 제 기록 이야기했을 때… 조금 좋았어요. 제가 만든 거라고 들리니까."
    menu:
        "“현장 판단이 어떻게 나온 건지 더 듣고 싶어요.”":
            $ flags.update({'cafeTone': 'heard'})
            jump d1_cafe_listen
        "“오늘은 일 얘기 쉬어도 돼요. 다음에 이어서 듣죠.”":
            $ flags.update({'cafeTone': 'space'})
            jump d1_cafe_light

label d1_cafe_listen:
    $ ui_scene_show("cafe")
    ri "그렇게 물어보면 길어지는데. 괜찮아요?"
    dh "지금은 급한 다음 회의가 없잖아요."
    ri "좋아요. 처음에는 제가 좋아하는 걸 사람들이 좋아할 줄 알았어요. 그런데 반응을 보다 보니 반대일 때도 있더라고요."
    ri "그걸 인정하는 게 조금 어려웠는데, 틀린 걸 확인해도 다음 걸 만들 수 있다는 게 좋았어요."
    dh "직관을 버린 게 아니라 확인하는 방법을 만든 거네요."
    ri "그 문장은 마음에 드는데. 다음 발표에 써도 돼요?"
    "리아가 웃었다. 커피가 식을 때까지 이야기는 이어졌지만, 이번에는 컵을 잊어버리지는 않았다."
    jump d1_cafe_close

label d1_cafe_light:
    $ ui_scene_show("cafe")
    ri "그렇게 말해 주니까 좀 편해지네요. 자꾸 설명해야 인정받을 것 같아서."
    dh "오늘 만든 자료는 이미 남아 있잖아요. 지금은 다른 이야기를 해도 괜찮죠."
    ri "그럼 카페 이야기. 여기 창가 빛이 오후에 예쁜데, 주말에는 너무 붐벼요."
    dh "그 정보도 현장에서 모은 건가요?"
    ri "그건 순수하게 제 취향입니다. 숫자 안 붙일래요."
    "편한 농담이 다시 돌아왔다. 중요한 말을 피한 것이 아니라, 오늘은 설명하지 않아도 괜찮다는 자리를 만든 것 같았다."
    jump d1_cafe_close

label d1_cafe_close:
    $ ui_scene_show("cafe")
    $ flags.update({'nextLunch': True})
    $ promises.append("DAY 02 · 12:30 라운지 원자료 검토")
    ri "내일 점심에 원자료 같이 볼까요? 오늘은 반쯤 쉬면서 이야기했으니까."
    dh "좋아요. 12시 30분, 라운지로 잡아 두죠."
    ri "시간까지 정확하네. 좋아요. 제가 공유 링크 보내 둘게요."
    "휴대전화 일정에 내일의 짧은 약속이 하나 생겼다. 연애라고 부를 일은 아직 없지만, 내일 다시 이야기할 이유는 생겼다."
    jump d1_ending_cafe

label d1_home:
    $ ui_phone_call_end()
    $ chapter = "오늘은 여기까지"
    $ place = "도현의 집"
    $ ui_scene_show("home")
    $ apply_effects({'stress': -15})
    "오늘은 집으로 돌아왔다. 새로운 이름과 업무를 기억하느라 생각보다 많이 지친 하루였다."
    dh "첫날부터 무리해서 가까워질 필요는 없겠지. 내일도 같은 사무실에서 만나니까."
    if flags.get("first_evening", "ria") == "ria":
        "휴대전화에는 리아가 보낸 카페 사진이 남아 있다. 사진은 저장할 수 있지만, 저장하지 않아도 대화가 사라지는 것은 아니다."
        ri "오늘은 편하게 쉬어요. 자료 링크만 남겨 둘게요. 내일 필요하면 같이 봐요."
    elif flags.get("first_evening") in ("seoyun", "yujin", "jihyun"):
        "문자를 나눈 상대에게 오늘은 쉬겠다고 알렸다. 내일 회사에서 이어가면 된다는 답이 돌아왔다."
    else:
        "휴대폰을 뒤집어 놓고 물을 끓였다. 오전에 들었던 네 사람의 목소리가 조금씩 구분되어 떠올랐다."
        dh "서윤 씨는 설명할 시간을 줬고, 유진 씨는 제가 어디서 멈추는지 봤지."
        "지현은 질문을 미루지 않아도 된다고 했다. 리아는 모르는 취향을 맞히는 대신 선택할 여지를 남겼다."
        dh "내일은 도움받은 만큼 제가 찾은 것도 이야기해 봐야겠다."
        "노트의 마지막 장에 기억나는 질문을 적었다. 답을 얻어야만 기록할 수 있는 것은 아니었다."
        "샤워를 마치고 돌아오니 차는 마시기 좋은 온도가 되어 있었다. 하루를 뒤늦게 따라잡는 기분이다."
        "잘한 말보다 못 한 말이 먼저 떠오르곤 했다. 오늘은 그 사이에 다시 이야기할 사람들의 이름도 있었다."
        dh "다음에는 어느 자리에서 점심을 먹을지도 조금 더 쉽게 정할 수 있겠지."
        "알람을 맞추고 회사 메신저를 닫았다. 혼자 보낸 저녁도 오늘의 한 부분으로 남았다."
    "처음 만난 동료에게 내 컨디션을 말해도 괜찮았다. 좋은 시작은 꼭 많은 약속을 만드는 것만은 아닐 것이다."
    jump d1_ending_home

label d1_ending_cafe:
    $ chapter = "첫날의 기록"
    $ place = "DAY 01 · 하루 마무리"
    $ ui_scene_show("cafe")
    $ clock = "21:30"
    $ d1_send_night()
    "낯선 회사가 조금 익숙해졌다. 리아의 웃음 뒤에 있는 생각도 아주 조금 알게 되었다."
    "아직 서로의 모든 것을 아는 사이는 아니다. 다만 다음 이야기를 기다릴 수 있는 동료가 되었다."
    $ queue_photo_rewards()
    $ renpy.retain_after_load()
    call screen day_result
    if _return == "continue":
        jump day02
    return

label d1_ending_home:
    $ chapter = "첫날의 기록"
    $ place = "DAY 01 · 하루 마무리"
    $ ui_scene_show("home")
    $ clock = "21:30"
    $ d1_send_night()
    "새로운 회사에서 해야 할 일과 쉬어도 되는 시간을 조금 알게 되었다."
    "오늘 만난 사람들과의 이야기는 내일도 이어질 수 있다. 오늘 관계를 서두르지 않았다는 이유로 문이 닫히지는 않았다."
    $ queue_photo_rewards()
    $ renpy.retain_after_load()
    call screen day_result
    if _return == "continue":
        jump day02
    return

label d1_phone_call:
    $ ui_phone_call_begin("ria", "d1_home")
    $ phone_calls.append("19:00 · 강리아 · 통화 완료")
    ri "퇴근하셨어요? 지금 통화 잠깐 괜찮아요?"
    ri "첫날인데 질문 많이 받아 주셔서 고마워요. 기록 보여 주는 건 좋아해도, 상대가 바쁘면 좀 눈치 보이거든요."
    ri "저는 회사 앞 카페에서 잠깐 쉬고 있어요. 사진 보냈는데 찾기 쉬울 거예요."
    ri "시간 괜찮으면 커피 한 잔 더 할래요? 피곤하면 오늘은 쉬어도 되고요."
    menu:
        "카페에 들른다.":
            jump d1_cafe
        "오늘은 집에서 쉰다.":
            jump d1_home




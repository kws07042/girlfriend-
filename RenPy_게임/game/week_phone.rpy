# First-week events share the existing native phone delivery/save pipeline.
default completed_events = []
default phone_expired = []
default phone_focus = "ria"
default ring_who = "ria"
default week_schedule = []
default week_lunch = "rest"
default week_evening = "rest"
default week_finished = False
default week_lunch_rewards = {}

init 10 python:
    # Authored conversation choices, not a free-text chatbot.
    message_data["d2_sy"] = {"who":"seoyun", "time":"09:05", "texts":["좋은 아침이에요. 오늘은 체크리스트부터 같이 볼까요?", "회의실 예약과 테스트 계정 확인이 빠져 있어서요. 9시 30분에 제 자리에서 봐요."], "reply":[
        {"text":"어디까지 필요한지 듣고 맡을 일을 정할게요.", "response":"고마워요. 설명할 때는 잠깐 기다려 주셔도 돼요. 제가 필요한 범위를 정리해 둘게요.", "set":{"sy_help_tone":"scope"}},
        {"text":"전체 흐름부터 보고 궁금한 부분을 물어볼게요.", "response":"좋아요. 누가 무엇을 기다리고 있는지부터 보여 드릴게요.", "set":{"sy_help_tone":"overview"}}]}
    message_data["d2_ri_plan"] = {"who":"ria", "time":"12:20", "texts":["어제 잡은 원자료 검토, 12시 30분 라운지 맞죠?", "먼저 밥 먹고 짧게 봐요. 점심까지 회의로 만들면 억울하니까."], "reply":[
        {"text":"약속대로 갈게요. 밥부터 먹어요.", "response":"좋아요. 원자료는 식판 치운 다음에 꺼낼게요!", "set":{"d2_lunch":"ria"}},
        {"text":"오늘은 쉬고 싶어요. 내일 자료 시간으로 옮길까요?", "response":"네. 내일 오전에 같이 보기로 해요. 미리 알려 줘서 고마워요.", "set":{"d2_lunch":"rest"}}]}
    message_data["d2_ri_free"] = {"who":"ria", "time":"12:20", "texts":["어제는 잘 쉬었어요? 오늘 점심은 여유 좀 있어요?", "라운지에서 밥 먹고 원자료 잠깐 같이 봐도 좋고요."], "reply":[
        {"text":"라운지에서 만나요. 밥 먹고 같이 볼게요.", "response":"네! 자료는 짧게, 점심은 천천히 먹어요.", "set":{"d2_lunch":"ria"}},
        {"text":"오늘 점심은 쉬고 내일 오전에 같이 볼게요.", "response":"좋아요. 내일 업무 시간으로 잡아 둬요. 점심은 편하게 쉬세요.", "set":{"d2_lunch":"rest"}}]}
    message_data["d2_sy_night"] = {"who":"seoyun", "time":"20:40", "texts":["오늘 정리한 담당자 칸을 다시 봤어요.", "제 이름이 줄었는데, 이상하게 빈칸이 생긴 기분은 아니네요."], "reply":[
        {"text":"내일 맡은 부분 진행 상황도 알려 드릴게요.", "response":"좋아요. 제가 먼저 확인하러 가지 않고 기다려 볼게요."},
        {"text":"오늘은 체크리스트 닫고 편히 쉬세요.", "response":"방금 닫았어요. 차를 끓였는데 이번에는 식기 전에 마시려고요."}]}
    message_data["d3_ri"] = {"who":"ria", "time":"09:00", "texts":["오늘은 커피보다 숫자부터 보여 드릴게요.", "지난 행사에서 반응이 적었던 문구도 같이 가져왔어요. 잘된 것만 보면 다음에 또 헷갈리거든요."], "reply":[
        {"text":"예상과 달랐던 반응부터 같이 볼까요?", "response":"그 질문 좋아요. 제가 찍은 가설이 틀린 곳부터 꺼낼게요.", "set":{"ri_analysis":"hypothesis"}},
        {"text":"현장에서 어떻게 기록했는지 궁금해요.", "response":"사람이 몰릴 때와 한산할 때 기록법이 달라요. 그 부분부터 설명할게요.", "set":{"ri_analysis":"method"}}]}
    message_data["d3_ri_night"] = {"who":"ria", "time":"21:00", "texts":["오늘 자료에는 실패한 문구까지 남겼어요.", "안 된 걸 꺼냈는데도 일이 앞으로 가는 느낌, 꽤 좋네요."], "reply":[
        {"text":"왜 바꿨는지까지 남아서 다음 사람이 이해할 거예요.", "response":"맞아요. 나중에 제가 다시 볼 때도 덜 부끄러울 것 같아요."},
        {"text":"오늘은 숫자 쉬게 두고 커피는 다 마셨어요?", "response":"다 마셨어요. 컵만 들고 퇴근할 뻔했지만요. 잘 쉬어요!"}]}
    message_data["d4_yj"] = {"who":"yujin", "time":"09:00", "texts":["시안 두 개를 디자인 작업실에 놓아 두었어요.", "좋아 보이는 쪽을 바로 정하기보다, 각각 무엇을 먼저 보여 주는지 이야기하고 싶어요."], "reply":[
        {"text":"사용자가 처음 보는 순서부터 함께 읽어 볼게요.", "response":"좋아요. 화면에 없는 설명을 덧붙이지 않고 먼저 보죠.", "set":{"yj_view":"flow"}},
        {"text":"각 시안에서 지키고 싶은 부분을 듣고 싶어요.", "response":"그 부분은 제가 설명할 수 있어요. 다른 의견도 같이 적어 주세요.", "set":{"yj_view":"intent"}}]}
    message_data["d4_yj_night"] = {"who":"yujin", "time":"20:50", "texts":["오늘 비교한 두 시안, 수정 이유와 함께 보관했어요.", "고르지 않은 쪽도 어디에 쓸 수 있는지 남겨 놓으니 덜 아쉽네요."], "reply":[
        {"text":"제 취향과 첫 화면의 목적이 다를 수도 있더라고요.", "response":"다른 감상을 지울 필요는 없죠. 기준을 함께 정하면 돼요."},
        {"text":"오늘 설명해 주신 여백이 기억에 남아요.", "response":"무엇이 남았는지 알려 주셔서 고마워요. 다음에는 그 부분을 더 살펴보죠."}]}
    message_data["d5_jh"] = {"who":"jihyun", "time":"09:00", "texts":["10시에 첫 주 목표를 확정하겠습니다.", "행사 유입과 서비스 재방문을 같은 성공 지표로 묶지 말고, 각각 확인할 항목을 준비해 주세요."], "reply":[
        {"text":"첫 방문부터 재방문까지 단계별로 정리하겠습니다.", "response":"좋아요. 담당자가 빠진 접점도 표시해 주세요."},
        {"text":"지금 확정할 내용과 검증할 내용을 나눠 가져갈게요.", "response":"그 구분이 필요해요. 확실하지 않은 내용은 확실하지 않다고 적어 주세요."}]}
    message_data["d5_jh_night"] = {"who":"jihyun", "time":"21:10", "texts":["역할표 수정본을 확인했어요. 다음 주에는 가정부터 검증하죠.", "오늘은 더 수정하지 않아도 됩니다. 저도 파일을 닫았어요."], "reply":[
        {"text":"네. 다음 주 검증 순서만 메모하고 쉬겠습니다.", "response":"좋아요. 업무 연락은 여기까지 할게요. 편히 쉬세요."},
        {"text":"첫 주 동안 방향 잡아 주셔서 고마웠어요.", "response":"질문을 분명하게 해 주셔서 저도 판단하기 편했어요. 다음 주에 봐요."}]}
    message_data["d5_sy_roles"] = {"who":"seoyun", "time":"17:50", "texts":["역할표 수정본을 올렸어요. 빈 담당자 칸은 다음 주 회의 안건으로 남겼어요.", "예전 같으면 제 이름을 넣었을 텐데, 이번에는 먼저 묻기로 했어요."]}

    def apply_person_effects(who, effects):
        for key, value in effects.items():
            target = people[who] if key in ("affection", "trust") else stats
            if key in target:
                target[key] = max(0, min(100, target[key] + value))

    def complete_week_event(token, who=None, effects=None, stage=None):
        if token in completed_events: return
        completed_events.append(token)
        if effects: apply_person_effects(who or "ria", effects)
        if stage is not None:
            people[who]["episode_stage"] = max(people[who]["episode_stage"], stage)

    def start_week_day(number, title):
        global day, chapter, slot, clock, place, ring_pending, week_lunch, week_evening
        day, chapter, slot, clock = number, title, "morning", "09:00"
        place, ring_pending, week_lunch, week_evening = "모멘트웍스 / 오픈 오피스", False, "rest", "rest"
        store.ui_speaker = {2:"seoyun",3:"ria",4:"yujin",5:"jihyun"}.get(number,"jihyun")
        if number == 2 and flags.get("lunch_plan") == "talk":
            first_who = flags.get("first_lunch", "ria")
            if first_who in names and first_who not in week_lunch_rewards:
                week_lunch_rewards[first_who] = 1
        phone_sync_reply_policy()

    def week_scene(background, location, time, period, title=None):
        global place, clock, slot, chapter
        place, clock, slot = location, time, period
        if title: chapter = title
        phone_sync_reply_policy()
        ui_scene_show(background)

    def schedule_meeting(token, who, number, period, time, title, status="예정"):
        if any(p["id"] == token for p in week_schedule): return
        if status == "예정" and any(p["day"] == number and p["slot"] == period and p["status"] == "예정" for p in week_schedule):
            raise Exception("Duplicate scheduled slot: %s %s" % (number,period))
        week_schedule.append({"id":token,"who":who,"day":number,"slot":period,"time":time,"title":title,"status":status})

    def finish_meeting(token, status="완료"):
        for item in week_schedule:
            if item["id"] == token: item["status"] = status

    def current_reply_key(who):
        keys = phone_reply_keys(who)
        return keys[0] if keys else None

    def choose_week_lunch(who):
        global week_lunch
        week_lunch = who
        if who != "rest": schedule_meeting("d%d_lunch" % day,who,day,"lunch","12:30","점심 대화")

    def next_meeting_text():
        next_item = next((p for p in week_schedule if p["status"]=="예정" and p["day"] >= day),None)
        if next_item:
            return "DAY %02d / %s / %s / %s" % (next_item["day"],next_item["time"],names[next_item["who"]],next_item["title"])
        return promises[0].replace(" · "," / ") if promises else "아직 정하지 않았어요."

    def lunch_caption(who):
        reward = 5 if week_lunch_rewards.get(who,0) < 2 else 0
        particle = "와" if who == "ria" else "과"
        return "%s%s 점심을 먹는다. (점심 / 호감 +%d / 스트레스 -5)" % (names[who][1:],particle,reward)

    def reward_week_lunch(who):
        token = "d%d_lunch" % day
        if token in completed_events: return
        reward = 5 if week_lunch_rewards.get(who,0) < 2 else 0
        complete_week_event(token,who,{"affection":reward,"stress":-5})
        week_lunch_rewards[who] = week_lunch_rewards.get(who,0) + 1

label week_lunch_scene:
    $ week_scene("terrace" if week_lunch == "rest" else "lounge", "모멘트웍스 / 테라스" if week_lunch == "rest" else "모멘트웍스 / 라운지", "12:30", "lunch", "점심의 여유")
    if week_lunch == "rest":
        $ complete_week_event("d%d_lunch" % day,effects={"stress":-15})
        "휴대폰을 잠시 뒤집어 놓았다. 다음 이야기를 이어 가려면 지금 쉬는 시간도 필요하다."
        dh "점심 한 번 조용히 먹는다고 하루가 멈추는 건 아니니까."
        "바람을 쐬고 들어가기 전에 오늘 오후 일정만 확인했다. 아직 네 사람과의 대화에는 시간이 충분하다."
    elif week_lunch == "seoyun":
        $ reward_week_lunch("seoyun")
        sy "오셨어요? 옆자리 비워 뒀어요."
        sy "오늘은 메뉴를 먼저 고르셨네요. 저는 두 개 사이에서 아직 고민 중이에요."
        dh "업무 우선순위보다 점심 결정이 어려울 때도 있죠."
        sy "업무에는 기준이 있는데, 오늘은 둘 다 먹고 싶어서요. 기준이 없네요."
        if flags.get("sy_approach") == "scope":
            sy "오전에는 먼저 범위를 물어봐 주셔서 좋았어요. 제가 설명할 시간도 생겼고요."
        else:
            sy "도움을 주겠다는 말은 고마웠어요. 다음엔 필요한 부분부터 제가 이야기해 볼게요."
        dh "점심은 대신 골라 드리지 않을게요. 기다리는 건 할 수 있습니다."
        sy "그럼 오늘은 조금 기다려 주세요. 메뉴 앞에서는 제가 선배가 아닌 것 같네요."
    elif week_lunch == "ria":
        $ reward_week_lunch("ria")
        ri "어, 왔어요? 여기 앉아요. 저도 방금 왔어요."
        ri "오늘은 밥 먹는 동안 자료 안 꺼낼게요. 제가 먼저 약속했습니다."
        if flags.get("hobby") == "music":
            ri "첫날 작은 공연 좋아한다고 하셨죠? 어제 새 공연표가 떴는데, 아직 제 일정부터 확인 중이에요."
            dh "갈 수 있는지 정해지면 알려 주세요. 급하게 답하지 않아도 됩니다."
        elif flags.get("hobby") == "quiet":
            ri "조용한 곳에서 걷는다고 하셨죠? 회사 뒤 길은 점심시간이 지나면 꽤 한산해요."
            dh "퇴근하고 한번 걸어 볼게요. 회사 주변 정보가 계속 늘어나네요."
        else:
            ri "요즘은 약속 없는 저녁도 일정표에 써 두려고요. 안 쓰면 자꾸 일을 넣게 되더라."
            dh "비워 두는 것도 정해 놓을 필요가 있겠네요."
        ri "제가 연락했다고 매번 같이 놀아야 하는 건 아니에요. 답을 분명하게 해 주면 그걸로 좋아요."
    elif week_lunch == "yujin":
        $ reward_week_lunch("yujin")
        yj "오셨네요. 자리 같이 찾을까요?"
        yj "창가보다는 안쪽이 덜 눈부시네요. 여기 앉아도 괜찮아요?"
        dh "네. 화면 안 봐도 되는 점심이면 어느 자리든 좋습니다."
        yj "그럼 오늘은 색 이야기 말고 맛 이야기로 해요."
        dh "유진 씨는 음식 고를 때도 기준이 분명한 편인가요?"
        yj "메뉴 설명이 길면 오히려 다른 걸 고를 때도 있어요. 읽는 일까지 점심에 하고 싶지 않아서요."
        "유진이 작게 웃었다. 업무에서 신중한 사람이 점심까지 무거운 대화를 원하는 것은 아니었다."
    else:
        $ reward_week_lunch("jihyun")
        jh "오셨군요. 이쪽에 앉으세요."
        jh "점심에 업무 보고까지 할 필요는 없어요. 편하게 드세요."
        dh "팀장님이 먼저 말씀해 주시니 노트를 꺼내려던 손이 멈췄네요."
        jh "저도 가끔 그래요. 밥을 먹으러 왔는데 다음 일정부터 보죠."
        dh "오늘은 시계 한 번 덜 보는 걸 목표로 하면 어떨까요?"
        jh "달성 가능한 목표네요. 다만 오후 회의에는 제시간에 돌아갑시다."
        "지현은 화면을 껐다. 다음 결정을 잠시 기다리게 해도 점심은 이어졌다."
    $ finish_meeting("d%d_lunch" % day)
    return

label week_choose_lunch:
    if day <= 5:
        call intro_fixed_lunch
        return
    "점심에는 한 사람과 이야기하거나 혼자 쉴 수 있다. 점심 슬롯 하나를 사용한다."
    menu:
        "[lunch_caption('seoyun')]":
            $ choose_week_lunch("seoyun")
        "[lunch_caption('ria')]":
            $ choose_week_lunch("ria")
        "[lunch_caption('yujin')]":
            $ choose_week_lunch("yujin")
        "[lunch_caption('jihyun')]":
            $ choose_week_lunch("jihyun")
        "테라스에서 혼자 쉰다. (점심 / 스트레스 -15)":
            $ choose_week_lunch("rest")
    call week_lunch_scene
    return

label week_close_day:
    $ week_scene("home","도현의 집","21:30","evening","하루의 기록")
    "집에 돌아와 오늘 나눈 이야기를 떠올렸다. 회사의 역할표보다 조금 더 많은 것이 네 사람의 이름 옆에 남아 있다."
    $ queue_photo_rewards()
    $ renpy.retain_after_load()
    call screen day_result
    if _return != "continue":
        return "title"
    return "continue"


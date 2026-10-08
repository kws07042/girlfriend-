# Day 2–5: discovery episodes precede the day-15 route choice.
label day02:
    $ start_week_day(2,"남겨진 체크리스트")
    $ week_scene("office","모멘트웍스 / 오픈 오피스","09:05","morning")
    "두 번째 출근에는 유리문 앞에서 사원증을 찾느라 멈추지 않았다. 책상까지 가는 길도 어제보다 짧게 느껴졌다."
    dh "어제는 회사 이름부터 낯설었는데, 오늘은 해야 할 일이 먼저 보이네."
    $ phone_focus = "seoyun"
    $ send_message("d2_sy")
    "서윤이 체크리스트를 함께 보자는 연락을 남겼다. 답장을 정한 뒤 오전 일을 시작하자."
    call screen phone(mode="story",initial_contact="seoyun",required_reply="d2_sy")
    $ clock = "09:30"
    sy "도현 씨, 오셨어요? 여기 앉으시면 같이 보기 편해요."
    dh "네. 문자 보고 왔어요."
    sy "이건 서비스 흐름이고, 이쪽 작은 칸들은 그 흐름이 멈추지 않게 하는 일들이에요."
    "태블릿에는 테스트 계정, 회의실, 샘플 수령, 고객 질문 정리까지 서로 다른 일이 한 목록에 있었다."
    dh "본문보다 체크 표시할 칸이 더 많네요. 이것도 전부 서윤 씨가 맡으신 건가요?"
    sy "담당이 정해지지 않으면 일단 제 이름을 넣어 둬요. 기다리다가 빠뜨리는 것보다는 나으니까요."
    dh "오늘만 하는 임시 처리인가요, 계속 맡아야 하는 일인가요?"
    sy "그걸 구분하지 않고 계속해 온 것 같네요. 매번 금방 끝날 줄 알았거든요."
    "서윤이 펜을 들었다가 내려놓았다. 목록을 발견했다는 이유로 내가 모두 다시 정할 수는 없다."
    menu:
        "오늘 필요한 범위를 묻고 테스트 계정 확인을 맡는다. (오전 / 호감 +10 / 신뢰 +12)":
            $ flags["sy_approach"] = "scope"
            dh "오늘 어디까지 끝나야 하나요? 제가 테스트 계정을 확인하고 결과를 남기는 건 어떨까요?"
            sy "계정 세 개가 같은 화면에 들어가는지만 확인해 주세요. 오류가 나면 고치기보다 상태를 남겨 주시면 돼요."
            dh "네. 수정 여부는 확인한 다음에 같이 정하죠."
            $ complete_week_event("SY01","seoyun",{"affection":10,"trust":12},stage=1)
        "제가 전부 정리하겠다고 제안한 뒤 담당 권한을 다시 묻는다. (오전 / 호감 +5 / 신뢰 +6)":
            $ flags["sy_approach"] = "takeover"
            dh "그럼 제가 한 번에 정리해서 나눠 드릴게요."
            sy "고마워요. 다만 각 담당자에게 먼저 확인해야 해요. 목록만 보고 나누면 실제 업무와 다를 수 있거든요."
            dh "제가 너무 빨리 결정했네요. 오늘 맡아도 되는 한 가지부터 알려 주세요."
            sy "테스트 계정 상태를 확인해 주세요. 담당자 칸은 제가 당사자들과 먼저 이야기할게요."
            $ complete_week_event("SY01","seoyun",{"affection":5,"trust":6},stage=1)
    "확인한 계정의 상태와 다음 확인 시각을 남겼다. 서윤은 결과를 다시 검사하기 전에 메모를 먼저 읽었다."
    sy "이렇게 남겨 주면 제가 같은 확인을 또 하지 않아도 되겠네요."
    dh "목록에 제 이름도 적어 주세요. 임시로 맡았는지 계속 맡는지도 같이요."
    sy "좋아요. 도현 씨가 해 준 일을 제 체크 표시로만 남기지 않을게요."
    "서윤의 목록에 내 이름이 한 줄 들어갔다. 도움은 커다란 선언보다 필요한 만큼의 일을 남기는 쪽에 가까웠다."
    call week_sy_private
    $ week_scene("lounge","모멘트웍스 / 라운지","12:20","lunch","일하다 남긴 질문")
    $ promises[:] = [p for p in promises if not p.startswith("DAY 02")]
    $ schedule_meeting("d2_ria_review","ria",2,"lunch","12:30","공동 원자료 검토")
    $ send_message("d2_ri_plan")
    $ phone_focus = "ria"
    "원자료를 보기 전에 네 사람이 함께 점심을 먹기로 했다. 오늘은 한 사람과의 사적 약속이 아니라 어제 남긴 업무 질문을 함께 확인하는 자리다."
    call screen phone(mode="story",initial_contact="ria",required_reply="d2_ri_plan")
    $ week_lunch = "ria"
    call week_lunch_scene
    ri "그럼 약속한 자료는 여기 두 줄만 볼까요? 밥 먹는 시간보다 길게 잡진 않을게요."
    dh "분류에 없는 질문들이 있네요."
    ri "억지로 기존 칸에 넣지 않았어요. 새 종류인지 단순한 표현 차이인지는 내일 같이 확인해요."
    sy "사용자 다음 행동과도 붙여 둘게요. 계정 확인만으로 끝나지 않는 부분이네요."
    yj "그 질문이 나오는 화면도 같은 위치에 놓아 보겠습니다."
    jh "오늘은 모르는 칸을 찾았으면 충분해요. 답은 내일 확인하고요."
    if flags.get("d2_lunch") == "rest":
        "집중해서 검토할 부분은 내일 오전으로 옮겼다. 모두의 일정에서 확인할 시간을 남기고 점심 이야기를 이어갔다."
        $ finish_meeting("d2_ria_review","조정")
        $ schedule_meeting("d3_ria_review","ria",3,"morning","09:30","원자료 검토 / 변경한 약속")
    else:
        dh "오늘은 이상한 칸이 있다는 걸 찾은 것으로 충분하겠네요."
        ri "네. 약속 지켰으니까, 이제는 진짜 점심 끝!"
        $ finish_meeting("d2_ria_review")
        $ flags["d2_review_done"] = True
    $ week_scene("office","모멘트웍스 / 오픈 오피스","17:50","lunch","한 칸의 담당자")
    jh "테스트 상태가 남아 있으니 내일 확인할 항목을 좁힐 수 있겠어요."
    sy "담당이 없는 일은 먼저 물어보고 정하려고요. 일단 제 이름을 쓰는 건 잠깐 멈춰 볼게요."
    ri "질문 자료에도 담당 칸 넣어 둬요. 제가 만든 분류는 제가 설명할게요."
    yj "화면 비교 자료는 제 쪽에서 준비할게요. 서윤 씨 목록에는 링크만 남겨 주세요."
    "책임이 사라진 것이 아니라 이름이 나뉘었다. 서윤은 목록을 닫기 전에 네 사람을 한 번씩 바라봤다."
    sy "퇴근길에 잠깐 차 한 잔 하실래요? 카페에서 책 이야기를 조금 이어가고 싶어요."
    dh "네. 계정은 내일 보고 오늘은 다른 이야기로요."
    $ week_scene("elevator","모멘트웍스 / 엘리베이터","18:30","evening","퇴근길의 짧은 통화")
    $ ring_who = "seoyun"
    $ phone_focus = "seoyun"
    $ ring_pending = True
    "엘리베이터를 기다리는데 서윤에게 전화가 왔다. 통화 탭에서 받거나 지금은 어렵다고 알릴 수 있다."
    call screen phone(mode="call",initial_contact="seoyun")
    $ ring_pending = False
    if _return == "accept":
        $ phone_calls.append("DAY 02 / 18:30 / 한서윤 / 통화 완료")
        $ ui_phone_call_begin("seoyun", "ui_d2_call_done")
        sy "퇴근하셨어요? 맡아 주신 계정 중 하나가 로그아웃됐다는 알림이 와서요."
        dh "상태 메모에 적어 두었습니다. 내일 재현 확인부터 하면 돼요."
        sy "지금 다시 접속하라는 뜻은 아니었어요. 내일 할 일인지 확인하고 싶었어요."
        dh "그럼 오늘은 둘 다 다시 열지 않는 걸로 하죠."
        sy "좋아요. 이렇게 말하고 끊는 것도 연습이 필요하네요. 편히 들어가세요."
        label ui_d2_call_done:
            $ ui_phone_call_end()
        $ flags["d2_sy_call"] = "answered"
    else:
        $ phone_calls.append("DAY 02 / 18:30 / 한서윤 / 부재중")
        $ phone_messages.append({"who":"seoyun","out":True,"text":"지금은 통화가 어려워요. 필요한 내용은 문자로 남겨 주세요.","time":clock,"day":day})
        $ phone_messages.append({"who":"seoyun","out":False,"text":"계정 알림은 내일 확인하기로 했어요. 오늘 다시 접속하지 않아도 돼요. 편히 쉬세요.","time":clock,"day":day})
        $ flags["d2_sy_call"] = "deferred"
        "필요한 내용은 문자로 받았다. 다시 일할 필요가 없다는 답을 확인하고 휴대폰을 넣었다."
    call intro_seoyun_evening
    $ intro_mark_day()
    $ complete_week_event("d2_evening",effects={"stress":-15})
    $ send_message("d2_sy_night")
    call week_close_day
    if _return == "continue":
        jump day03
    return

label day03:
    $ start_week_day(3,"커피 뒤의 숫자")
    $ week_scene("marketing","모멘트웍스 / 마케팅 프로젝트실","09:00","morning")
    "리아의 화면에는 행사 사진보다 작은 표가 먼저 떠 있었다. 웃는 방문객 뒤에 멈춘 시간과 질문의 순서가 남아 있었다."
    $ send_message("d3_ri")
    $ phone_focus = "ria"
    call screen phone(mode="story",initial_contact="ria",required_reply="d3_ri")
    $ clock = "09:30"
    ri "어, 왔어요? 이쪽이에요. 자료 열어 놨어요."
    if flags.get("d2_review_done"):
        ri "어제 같이 찾은 빈 분류부터 볼까요? 그 질문이 나오기 전 행동도 붙여 봤어요."
    else:
        ri "어제 옮긴 약속, 오늘 자료 시간에 같이 보면 돼요. 쉬고 와서 질문해 주는 편이 더 좋아요."
        $ finish_meeting("d3_ria_review")
    dh "이 문구는 사람들이 많이 쳐다봤는데, 다음 단계로 간 사람은 적네요."
    ri "제가 처음엔 제일 마음에 들어 했던 문구예요. 시선만 잡으면 됐다고 생각했거든요."
    dh "어디서 예상과 달라졌나요?"
    ri "사진 찍은 뒤 뭘 해야 할지 몰랐대요. 재밌게 해 준 사람은 됐는데, 안내한 사람은 못 된 거죠."
    "리아는 실패한 칸을 접지 않았다. 틀린 가설 옆에 새로 물어볼 질문을 적었다."
    yj "시선을 잡은 역할은 남기고, 행동을 알려 주는 문장을 분리하면 어떨까요?"
    ri "좋아요. 하나로 다 하려다 둘 다 애매해졌을 수도 있겠네요."
    menu:
        "관찰과 가설을 구분하고 리아에게 기록법을 설명해 달라고 한다. (오전 / 호감 +10 / 신뢰 +12)":
            dh "'머뭇거렸다'는 관찰과 '관심이 없었다'는 판단을 나눠 보면 어떨까요?"
            ri "맞아요. 같은 사람도 설명 듣고 바로 들어갔을 수 있으니까. 기록법부터 같이 바꿔 봐요."
            dh "분류 근거도 리아 씨 설명으로 남길게요."
            ri "제가 만든 방법이니까 제가 쓸게요. 도현 씨는 처음 보는 사람 입장에서 빠진 곳을 찾아 주세요."
            $ flags["ri01_method"] = "separate"
            $ complete_week_event("RI01","ria",{"affection":10,"trust":12},stage=1)
        "성공한 숫자부터 쓰자고 했다가 실패한 기록도 함께 남긴다. (오전 / 호감 +5 / 신뢰 +6)":
            dh "발표에서는 잘된 숫자부터 보여 주는 게 낫지 않을까요?"
            ri "잘된 것도 필요하죠. 다만 그 숫자만 남기면 제가 왜 문구를 바꾸자는지 사라져요."
            dh "그럼 바꿀 이유가 되는 기록도 같은 페이지에 넣죠."
            ri "네. 다음에는 처음부터 그 부분을 같이 봐 주세요. 실패를 꺼내는 데도 시간이 좀 들거든요."
            $ flags["ri01_method"] = "results"
            $ complete_week_event("RI01","ria",{"affection":5,"trust":6},stage=1)
    "표에 확인된 사실과 아직 물어봐야 할 내용이 나뉘었다. 리아의 빠른 판단은 이유 없는 감이 아니었다."
    ri "이제 커피 마셔도 되겠네요. 숫자 먼저 보여 드렸으니까."
    dh "커피가 식기 전에 끝내는 것도 기록에 넣으시죠."
    ri "그건 오늘 가장 중요한 성과일지도요."
    call week_choose_lunch
    $ week_scene("office","모멘트웍스 / 오픈 오피스","17:40","lunch","첫 화면의 질문")
    sy "첫 화면에서 사용자가 뭘 기다리는지 좀 더 분명해졌어요."
    yj "내일은 같은 문장을 두 화면에 놓고 비교해 볼게요. 문장만 좋아도 순서가 바뀌면 다르게 읽히니까요."
    ri "오늘 정리한 질문은 자료 폴더에 두었어요. 현장에서 또 물어볼 때 같은 방법으로 기록해 볼게요."
    jh "다음 주 발표 전까지 무엇을 검증할지 정합시다. 오늘 안에 전부 답하려고 하진 말고요."
    ri "오늘은 커피도 다 마셨어요. 표부터 보여 주느라 컵을 잊을 줄 알았는데요."
    dh "숫자 먼저 보여 준 뒤에는 조금 편해 보이셨습니다."
    ri "설명할 사람이 있다는 건 좋네요. 제가 만든 건 제가 이야기하고 싶으니까요."
    call week_jh_private
    jh "같은 영화를 여러 번 보면 그때마다 놓쳤던 장면이 하나씩 보여요."
    dh "지난주에 같은 길을 다시 걸으면 다르게 보인다고 하신 것과 비슷하네요."
    jh "그러네요. 취향에도 기준은 있는데, 꼭 그대로 지킬 필요는 없겠죠."
    "지현은 영화 제목을 메모해 내 쪽으로 돌렸다. 업무와 무관한 제목이 오늘의 마지막 메모가 되었다."
    $ week_scene("elevator","모멘트웍스 / 엘리베이터","18:30","evening","약속 없는 저녁")
    menu:
        "회사 앞 카페에서 잠깐 혼자 쉰다. (저녁 / 감각 +3 / 스트레스 -8)":
            $ week_scene("cafe","회사 앞 / 카페","19:00","evening")
            $ complete_week_event("d3_evening",effects={"sensitivity":3,"stress":-8})
            "회사 앞 카페의 창가에 앉았다. 오늘은 약속 상대 없이, 창밖을 보는 사람들의 다른 속도를 바라봤다."
            if flags.get("nextLunch"):
                "리아가 장소를 설명하며 웃던 모습이 떠올랐다. 같은 자리에 혼자 앉아도 그 대화는 남아 있었다."
            dh "모든 만남을 다음 만남으로 채울 필요는 없겠지."
        "집에 돌아가 충분히 쉰다. (저녁 / 스트레스 -15)":
            $ complete_week_event("d3_evening",effects={"stress":-15})
            $ week_scene("home","도현의 집","19:00","evening")
            "오늘은 지도에서 새 장소를 찾지 않았다. 신발을 벗고 앉으니 오전에 들었던 이야기가 천천히 정리됐다."
    $ intro_mark_day()
    $ send_message("d3_ri_night")
    call week_close_day
    if _return == "continue":
        jump day04
    return

label day04:
    $ start_week_day(4,"두 개의 시안")
    $ week_scene("studio","모멘트웍스 / 디자인 작업실","09:00","morning")
    "작업실 책상에 같은 문장을 쓰는 두 시안이 놓여 있었다. 한쪽은 제품의 빛이 먼저 보이고, 다른 쪽은 시작 버튼이 먼저 읽혔다."
    $ send_message("d4_yj")
    $ phone_focus = "yujin"
    call screen phone(mode="story",initial_contact="yujin",required_reply="d4_yj")
    $ clock = "09:30"
    yj "오셨네요. 시안은 여기 나란히 놓아뒀어요."
    yj "A는 조명이 만드는 분위기, B는 오늘 할 행동을 먼저 보여 줘요. 어느 쪽이 더 예쁜지만 고르려는 회의는 아니에요."
    dh "A는 조금 더 머물게 되고 B는 빨리 눌러 보고 싶네요."
    yj "그 차이를 느꼈다면 두 개를 만든 이유가 전달된 거네요."
    sy "첫 사용자가 시작 전에 무엇을 알아야 하는지도 함께 봐요."
    ri "행사에선 화면을 오래 안 볼 수 있어요. 그런데 제품이 뭔지도 모르면 바로 누르기는 어려울 거고요."
    "유진은 바로 대답하지 않고 두 시안 사이에 종이를 놓았다. 의견을 버리는 대신 각 의견이 필요한 자리를 찾고 있었다."
    $ ui_speaker = "yujin"
    menu:
        "각 시안의 목적을 듣고 첫 화면과 후속 화면을 구분한다. (오전 / 호감 +10 / 신뢰 +12)":
            dh "첫 화면은 B처럼 행동을 보여 주고, 다음 화면에 A의 여백과 빛을 남길 수 있나요?"
            yj "가능해요. 다만 A를 장식으로만 붙이지 말고, 조명을 켠 다음의 경험으로 이어 주세요."
            dh "그럼 누른 뒤 무엇이 바뀌는지 먼저 정해야겠네요."
            yj "네. 남길 이유와 바꿀 이유를 같이 적어 봐요."
            $ flags["yj01_choice"] = "purpose"
            $ complete_week_event("YJ01","yujin",{"affection":10,"trust":12},stage=1)
        "취향으로 A를 고른 뒤 첫 사용자의 목적을 다시 확인한다. (오전 / 호감 +5 / 신뢰 +6)":
            dh "저는 A가 더 마음에 들어요. 분위기가 오래 남거든요."
            yj "그 감상은 고마워요. 다만 처음 보는 사람도 다음 행동을 찾을 수 있을까요?"
            dh "제 취향과 사용 목적은 다른 질문이네요. B의 시작 위치와 비교해 볼까요?"
            yj "좋아요. A를 좋아했다는 말까지 취소하지는 않아도 돼요. 어디에 쓸지 찾으면 되니까요."
            $ flags["yj01_choice"] = "taste"
            $ complete_week_event("YJ01","yujin",{"affection":5,"trust":6},stage=1)
    "보류한 시안에도 이유가 적혔다. 선택받지 못한 것을 실패로만 남기지 않는 방식이었다."
    dh "설명 없이 시안을 바꾸면 이 메모들은 다 사라지겠네요."
    yj "그래서 함께 남기고 싶었어요. 나중에 제가 봐도 왜 바꿨는지 알 수 있게요."
    "유진이 폴더 가장자리를 정리했다. 회의가 끝나고 나니 그 손의 움직임이 조금 느려졌다."
    call week_yj_private
    call week_choose_lunch
    $ week_scene("office","모멘트웍스 / 오픈 오피스","17:30","lunch","내일 결정할 것")
    jh "내일 목표 합의에서는 오늘 만든 기준부터 보죠. 행사 방문과 서비스 재방문을 따로 적어 주세요."
    sy "역할표도 같은 순서로 정리해 둘게요. 담당자가 없는 칸은 숨기지 않고 남기겠습니다."
    ri "검증할 질문은 제가 가져갈게요. 아직 모르는 걸 아는 것처럼 쓰지는 않을게요."
    yj "화면은 첫 행동과 후속 경험으로 나눠 설명할 수 있어요."
    yj "퇴근하면서 잠깐 지도 보여 드릴까요? 파일 제목 말고 골목 이야기로요."
    dh "네. 카페에서 잠깐 보고 갈게요."
    $ week_scene("elevator","모멘트웍스 / 엘리베이터","18:40","evening","짧게 이어진 설명")
    $ ring_who = "yujin"
    $ phone_focus = "yujin"
    $ ring_pending = True
    "유진에게 전화가 왔다. 긴 회의로 이어갈 필요 없이 짧게 확인하거나 문자로 받을 수 있다."
    call screen phone(mode="call",initial_contact="yujin")
    $ ring_pending = False
    if _return == "accept":
        $ phone_calls.append("DAY 04 / 18:40 / 차유진 / 통화 완료")
        $ ui_phone_call_begin("yujin", "ui_d4_call_done")
        yj "지금 통화 괜찮아요? 비교 자료 제목을 정하다가 한 가지만 확인하고 싶어서요."
        dh "네. 어떤 부분인가요?"
        yj "'분위기와 행동'이라고 썼는데, 둘 중 하나를 포기한 것처럼 들리지는 않나요?"
        dh "'처음의 행동, 그다음의 경험'이면 순서가 보일 것 같아요."
        yj "그쪽이 오늘 정리한 내용에 가깝네요. 제목은 내일 반영할게요. 오늘 다시 파일 여실 필요는 없어요."
        label ui_d4_call_done:
            $ ui_phone_call_end()
        $ flags["d4_yj_call"] = "answered"
    else:
        $ phone_calls.append("DAY 04 / 18:40 / 차유진 / 부재중")
        $ phone_messages.append({"who":"yujin","out":True,"text":"지금은 통화가 어려워요. 문자로 남겨 주시면 확인할게요.","time":clock,"day":day})
        $ phone_messages.append({"who":"yujin","out":False,"text":"자료 제목만 확인하려던 거예요. 내일 만나서 정해도 괜찮아요. 편히 들어가세요.","time":clock,"day":day})
        $ flags["d4_yj_call"] = "deferred"
        "화면에 급하지 않다는 문장이 남았다. 지금 답하지 않아도 내일 이어갈 수 있는 이야기였다."
    $ complete_week_event("d4_evening",effects={"stress":-15})
    call intro_yujin_evening
    $ intro_mark_day()
    $ send_message("d4_yj_night")
    call week_close_day
    if _return == "continue":
        jump day05
    return

label day05:
    $ start_week_day(5,"우리의 첫 목표")
    $ week_scene("meeting","모멘트웍스 / 회의실","09:00","morning")
    $ send_message("d5_jh")
    $ phone_focus = "jihyun"
    "첫 금요일이다. 지현의 연락에는 오늘 결정해야 할 것이 두 줄로 정리되어 있었다."
    call screen phone(mode="story",initial_contact="jihyun",required_reply="d5_jh")
    $ clock = "10:00"
    jh "오셨군요. 다들 모였으니 시작할까요?"
    jh "오늘 무엇을 결정해야 하죠? 먼저 각자 성공이라고 부르는 결과부터 이야기해 주세요."
    ri "행사에서 많은 사람이 멈추고, 실제로 시작 버튼까지 누르는 것요. 둘은 따로 셀게요."
    sy "저는 다음 날에도 기록을 이어갈 수 있는 경험이요. 첫 화면만 성공하면 이후 문의가 늘어날 수 있어요."
    yj "제품이 왜 필요한지와 어떤 느낌을 주는지가 같이 남았으면 해요. 클릭 수만으로는 그 부분을 설명하기 어렵죠."
    jh "행사 반응과 서비스 재방문을 한 숫자로 적으면, 잘된 부분 뒤에 빠진 부분이 가려지겠네요."
    dh "방문, 첫 행동, 다음 날 돌아오는 이유까지 나눠 보면 어떨까요?"
    menu:
        "경험을 단계별로 적고 각 단계의 담당과 확인 방법을 정한다. (오전 / 프로젝트 +10)":
            $ flags["c01_method"] = "steps"
            dh "리아 씨는 방문과 첫 질문, 유진 씨는 화면의 순서, 서윤 씨는 다음 행동과 문의를 정리해 주세요. 저는 접점 사이의 빈칸을 찾겠습니다."
            sy "확인할 수 없는 항목은 담당자만 적지 말고 확인 시각도 남겨요."
            ri "첫 방문과 재방문을 같은 설문으로 묻지 않으면 좋겠네요."
            yj "디자인에서 지켜야 할 기준도 각 단계에 붙여 둘게요."
        "이번 주 확정한 것과 다음 주 검증할 것을 나눈다. (오전 / 프로젝트 +10)":
            $ flags["c01_method"] = "verify"
            dh "행사 유입은 지금 가진 자료로 가설을 세울 수 있어요. 재방문 이유는 아직 실제 사용자를 만나야 확인됩니다."
            ri "그럼 모르는 질문을 성공 목표 칸에 써 넣지 않아도 되겠네요."
            sy "다음 주에 확인할 대상으로 남기고 테스트 준비를 하죠."
            yj "가설이 바뀌면 시안도 바뀔 수 있다는 걸 기준에 적어 두겠습니다."
        "빠진 접점을 표시하고 단계별 검증 순서를 제안한다. (기획 50 이상 / 오전 / 프로젝트 +10)" if stats["planning"] >= 50:
            $ flags["c01_method"] = "gaps"
            dh "행사에서 시작한 기록이 집에서도 이어지는지 확인할 접점이 비어 있어요. 첫날 종료 화면과 다음 날 안내를 먼저 검증해 봅시다."
            sy "좋아요. 단순 재방문 횟수보다 돌아와서 할 일이 있는지 확인할 수 있겠네요."
            jh "그 검증부터 하죠. 다른 항목을 더 넣기 전에 빈 연결을 채웁시다."
    $ complete_week_event("C01",effects={"project":10})
    jh "역할표 수정본을 기준으로 갑시다. 다만 아직 확인하지 못한 항목은 확정이라고 외부에 말하지 않을게요."
    dh "저도 연결되는 문장과 담당자를 같이 남기겠습니다."
    jh "좋아요. 제가 전달할 내용과 팀에서 검증할 내용을 구분할 수 있겠어요."
    "한 주를 끝낸다고 모르는 것이 없어지는 것은 아니었다. 모르는 것을 누구와 확인할지 정한 것이 오늘의 결과였다."
    call week_choose_lunch
    $ week_scene("office","모멘트웍스 / 오픈 오피스","17:50","lunch","금요일의 역할표")
    $ send_message("d5_sy_roles")
    sy "역할표 올렸어요. 다음 주엔 제가 먼저 담당자 칸을 채우기 전에 물어볼게요."
    ri "제 자료에도 바꾼 이유까지 적어 뒀어요. 다음에 제가 발표할 때 그대로 설명할 수 있게요."
    yj "두 시안은 같이 보관했어요. 고르지 않은 쪽도 쓰일 곳을 찾을 수 있겠죠."
    jh "오늘의 결정은 여기까지입니다. 첫 주 수고했어요."
    "월요일에는 처음 듣는 이름들이었다. 금요일에는 각자의 질문을 떠올릴 수 있는 이름들이 되었다."
    $ week_scene("elevator","모멘트웍스 / 엘리베이터","18:30","evening","첫 주의 마지막 저녁")
    call intro_friday_group
    $ intro_mark_day()
    $ send_message("d5_jh_night")
    $ week_finished = True
    $ week_scene("home","도현의 집","21:30","evening","첫 주의 기록")
    "집에 돌아와 첫 주의 기록을 닫았다. 네 사람 모두와 가까워질 길은 열려 있고, 누구와 더 이야기하고 싶은지는 아직 정해 가는 중이다."
    "다음 주에는 누구를 조금 더 알아보고 싶은지 처음으로 고른다. 그 마음도 함께 보낸 시간에 따라 달라질 수 있다."
    $ queue_photo_rewards()
    $ renpy.retain_after_load()
    call screen day_result
    if _return == "continue":
        jump day06
    return



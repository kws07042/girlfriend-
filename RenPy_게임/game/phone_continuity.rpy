# Authored phone continuity; does not change story branches or meeting rewards.
init 35 python:
    # Keep the deadline/day policy. Only copy late choices for dialogue adjustment.
    _phone_reply_options_before_continuity = phone_reply_options
    phone_late_personality_responses = {
        "goodnight": (
            "저도요! 첫날 커피 들고 인사하길 잘했네요. 다음에는 도현 씨 얘기도 더 들어볼래요.",
            "천천히 주셔도 돼요! 잘 쉬셨으면 됐죠. 회사에서 봐요."),
        "d2_sy_night": (
            "좋아요. 남겨 주신 메모부터 볼게요. 제가 먼저 전부 확인하러 가지는 않을게요.",
            "네. 차도 식기 전에 마셨어요. 체크리스트 닫고 나니 조금 허전했는데, 쉬는 것도 익숙해져야겠죠."),
        "d3_ri_night": (
            "맞아요! 나중에 봐도 '왜 바꿨지?' 하고 멈추진 않겠더라고요. 안 된 것도 남겨 두길 잘했어요.",
            "네! 이번엔 컵 비우고 퇴근했어요. 답장은 시간 날 때 주셔도 돼요."),
        "d4_yj_night": (
            "지금 다시 봐도 다른 자리에서 쓸 수 있겠더라고요. 지우지 않고 남겨 두길 잘했어요.",
            "그 부분이 남았군요. 다음에 같이 볼 때, 도현 씨 눈에는 어떻게 보이는지도 듣고 싶어요."),
        "d5_jh_night": (
            "네. 메모해 두셨으면 충분해요. 확인은 업무 시간에 하죠. 지금은 쉬세요.",
            "저도 도현 씨 질문 덕분에 정리하기 편했어요. 다음에 뵙죠. 오늘은 편히 쉬세요."),
    }

    def phone_reply_options(key):
        options = _phone_reply_options_before_continuity(key)
        gap = day - phone_event_day(key)
        if gap <= 0 or key not in phone_late_personality_responses:
            return options
        adjusted = [dict(option) for option in options]
        for option, response in zip(adjusted,phone_late_personality_responses[key]):
            option["response"] = response
        if key == "d2_sy_night":
            adjusted[1]["text"] = "어제는 체크리스트 닫고 좀 쉬셨어요?" if gap == 1 else "그날은 체크리스트 닫고 좀 쉬셨어요?"
            if gap > 1:
                adjusted[0]["text"] = "그때 나눠 맡으니 진행 상황도 정리하기 편했어요."
                adjusted[0]["response"] = "네. 제 이름만 줄이는 게 아니라 누가 맡았는지 보이는 게 좋더라고요."
        return adjusted

    phone_hangup_followups = {
        "ria":"남은 얘기는 다음에 해요! 지금 답장 안 하셔도 돼요. 푹 쉬어요.",
        "seoyun":"남은 내용은 다음에 같이 확인해요. 오늘 다시 열어 보실 필요는 없어요. 편히 쉬세요.",
        "yujin":"전화로 못 한 이야기는 다음에 이어가요. 지금 답을 정하지 않아도 괜찮아요.",
        "jihyun":"남은 내용은 다음 업무 시간에 확인하죠. 지금 답하실 필요는 없어요.",
    }

    def phone_interrupted_call_followup(who, target):
        if who not in phone_hangup_followups:
            return False
        message_id = "hangup:%s:%s:%s" % (day,who,target or "call")
        if any(msg.get("id") == message_id for msg in phone_messages):
            return False
        text = phone_hangup_followups[who]
        if who == "seoyun" and target == "ui_d2_call_done":
            text = "아까 전화는 계정 알림 때문이었어요. 내일 같이 확인해요. 오늘 다시 접속하지 않으셔도 돼요."
        elif who == "yujin" and target == "ui_d4_call_done":
            text = "아까 전화는 비교 자료 제목 때문이었어요. 내일 같이 정해도 괜찮아요. 오늘은 편히 들어가세요."
        elif who == "ria" and target == "d1_home" and "cafe_photo" in phone_events:
            text = "사진은 카페에서 쉬는 김에 보낸 거예요! 오늘은 푹 쉬어요. 남은 얘기는 다음에 해도 되니까."
        phone_messages.append({"who":who,"out":False,"text":text,"time":clock,"day":day,"id":message_id})
        viewed = renpy.get_screen("phone")
        if not viewed or viewed.scope.get("contact") != who or viewed.scope.get("tab") != "messages":
            phone_unread[who] = phone_unread.get(who,0) + 1
            renpy.notify(names[who] + " · 새 메시지")
        renpy.retain_after_load()
        renpy.restart_interaction()
        return True

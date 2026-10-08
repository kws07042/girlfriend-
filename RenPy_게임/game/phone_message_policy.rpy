# Message deadlines and day-aware replies. Ordinary check-ins stay actionable.
default phone_event_days = {}

init 30 python:
    phone_reply_deadlines = {
        "lunch_invite": "12:30", "d2_sy": "09:30",
        "d2_ri_plan": "12:30", "d2_ri_free": "12:30",
        "d3_ri": "09:30", "d4_yj": "09:30", "d5_jh": "10:00",
    }
    phone_late_replies = {
        "goodnight": [
            {"text":"어제 이야기 좋았어요. 다음에도 이어서 이야기해요.", "response":"저도 좋았어요! 다음에 또 얘기해요."},
            {"text":"답장이 늦었네요. 첫날 챙겨 주셔서 고마웠어요.", "response":"괜찮아요. 시간 될 때 답해 주시면 돼요!"}],
        "d2_sy_night": [
            {"text":"맡은 부분 진행 상황도 정리해서 알려 드릴게요.", "response":"좋아요. 메모를 남겨 주시면 제가 볼게요."},
            {"text":"그날은 체크리스트 닫고 좀 쉬셨어요?", "response":"네. 차도 따뜻할 때 마셨어요. 덕분에요."}],
        "d3_ri_night": [
            {"text":"수정 이유까지 남겨 두니 다시 보기도 편하겠어요.", "response":"맞아요! 다음에 봐도 왜 바꿨는지 바로 알겠더라고요."},
            {"text":"답장이 늦었네요. 그날 커피는 다 마셨어요?", "response":"네! 컵만 들고 갈 뻔했지만 잘 챙겼어요. 답장은 천천히 주셔도 돼요."}],
        "d4_yj_night": [
            {"text":"다시 봐도 시안마다 장점이 다르게 보여요.", "response":"어디에 어울릴지도 기록해 뒀으니 다음에 참고할 수 있어요."},
            {"text":"답장이 늦었네요. 설명해 주신 여백이 기억에 남아요.", "response":"기억해 주셔서 고마워요. 다음에는 그 부분부터 같이 봐요."}],
        "d5_jh_night": [
            {"text":"말씀하신 검증 순서는 메모해 두었습니다.", "response":"좋아요. 다음 업무 시간에 확인하죠."},
            {"text":"첫 주 동안 방향 잡아 주셔서 고마웠어요.", "response":"질문을 분명하게 해 주셔서 저도 판단하기 편했어요. 다음에 봐요."}],
    }

    def phone_time_minutes(value):
        hour, minute = value.split(":")
        return int(hour) * 60 + int(minute)

    def phone_event_day(key):
        if key in phone_event_days:
            return phone_event_days[key]
        for msg in phone_messages:
            if msg.get("event") == key:
                return msg.get("day", 1)
        if key.startswith("d") and "_" in key and key[1:key.index("_")].isdigit():
            return int(key[1:key.index("_")])
        return 1

    def phone_reply_has_expired(key):
        if key not in phone_events or key in phone_replied or key not in phone_reply_deadlines:
            return False
        sent_day = phone_event_day(key)
        return day > sent_day or (day == sent_day and phone_time_minutes(clock) > phone_time_minutes(phone_reply_deadlines[key]))

    def phone_reply_available(key):
        return (key in phone_events and key not in phone_replied
                and bool(message_data.get(key, {}).get("reply")) and not phone_reply_has_expired(key))

    def phone_reply_keys(who):
        return [key for key in reversed(phone_events)
                if message_data[key].get("who", "ria") == who and phone_reply_available(key)]

    def phone_selected_reply(who, selected=None, required=None):
        keys = phone_reply_keys(who)
        if selected in keys:
            return selected
        if required in keys:
            return required
        return keys[0] if keys else None

    def phone_next_reply(who, current):
        keys = phone_reply_keys(who)
        if not keys:
            return None
        return keys[(keys.index(current) + 1) % len(keys)] if current in keys else keys[0]

    def phone_reply_options(key):
        if day > phone_event_day(key) and key in phone_late_replies:
            options = [dict(option) for option in phone_late_replies[key]]
            if key == "goodnight" and day > phone_event_day(key) + 1:
                options[0]["text"] = "첫날 이야기 좋았어요. 다음에도 이어서 이야기해요."
            return options
        return message_data[key]["reply"]

    def phone_sync_reply_policy():
        last_day, last_time = 1, "00:00"
        sent_replies = {}
        for msg in phone_messages:
            msg_id = msg.get("id", "")
            if "day" not in msg:
                msg["day"] = last_day
                if msg_id.endswith(":response"):
                    sent = sent_replies.get(msg_id[:-len(":response")])
                    if sent and msg["day"] > sent[0]:
                        # Legacy delayed responses copied the previous day's send time.
                        msg["time"] = last_time
            if msg["day"] != last_day:
                last_time = "00:00"
            if phone_time_minutes(msg["time"]) < phone_time_minutes(last_time):
                # Repair old outgoing replies stamped before the message they answered.
                msg["time"] = last_time
            last_day, last_time = msg["day"], msg["time"]
            if msg["out"] and msg_id:
                sent_replies[msg_id] = (msg["day"], msg["time"])
            if msg.get("event") and msg["event"] not in phone_event_days:
                phone_event_days[msg["event"]] = msg["day"]
        phone_expired[:] = [key for key in phone_events if phone_reply_has_expired(key)]

    def phone_restore_message_policy():
        phone_sync_reply_policy()
        # Old night saves can have messages ahead of the phone's displayed clock.
        received = [msg["time"] for msg in phone_messages if not msg["out"] and msg.get("day") == day]
        if received:
            store.clock = max([clock] + received, key=phone_time_minutes)
        phone_sync_reply_policy()
        renpy.retain_after_load()

    config.after_load_callbacks.append(phone_restore_message_policy)

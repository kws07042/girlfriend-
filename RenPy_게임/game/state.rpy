default day = 1
default slot = "morning"
default clock = "09:00"
default place = "모멘트웍스"
default chapter = "첫 출근"
default stats = {"planning":40, "communication":40, "sensitivity":40, "project":0, "stress":20, "team_trust":40}
default people = {k:{"affection":10,"trust":10,"episode_stage":0,"relationship":"none","core_resolved":False,"photo_cap":0,"private_photo_ok":False,"breach":False} for k in ("seoyun","ria","yujin","jihyun")}
default flags = {}
default phone_messages = []
default phone_replied = []
default reply_reward_days = []
default phone_calls = []
default photo_received = []
default photo_saved = []
default photo_hidden = []
default phone_events = []
default promises = []
default ring_pending = False
default persistent.reduce_motion = False

define names = {"seoyun":"한서윤", "ria":"강리아", "yujin":"차유진", "jihyun":"백지현"}
define photo_tiers = [
    {"tier":1,"a":20,"t":20,"stage":0,"dating":False,"title":"일상 셀카"},
    {"tier":2,"a":40,"t":35,"stage":2,"dating":False,"title":"사복 데이트 사진"},
    {"tier":3,"a":60,"t":55,"stage":3,"dating":True,"title":"옷을 입은 가슴골 셀카"},
    {"tier":4,"a":80,"t":75,"stage":4,"dating":True,"title":"연인에게 보내는 드레스 사진"}
]
init python:
    def apply_effects(effects):
        for key, value in effects.items():
            if key in ("affection", "trust"):
                people["ria"][key] = max(0, min(100, people["ria"][key] + value))
            elif key in stats:
                stats[key] = max(0, min(100, stats[key] + value))

    def send_message(key):
        if key in phone_events: return
        phone_events.append(key)
        item = message_data[key]
        store.phone_event_days[key] = day
        if phone_time_minutes(item["time"]) > phone_time_minutes(clock):
            store.clock = item["time"]
        phone_sync_reply_policy()
        who = item.get("who", "ria")
        for text in item["texts"]:
            phone_messages.append({"who":who,"out":False,"text":text,"time":item["time"],"event":key,"day":day})
        phone_unread[who] = phone_unread.get(who,0) + len(item["texts"])
        if item.get("photo"):
            if "ria_cafe" not in photo_received: photo_received.append("ria_cafe")
            phone_messages.append({"who":who,"out":False,"text":"카페 사진을 보냈어요.","time":item["time"],"photo":"ria_cafe","day":day})

    def reply_message(key, choice):
        if not phone_reply_available(key) or phone_pending: return
        phone_replied.append(key)
        who = message_data[key].get("who","ria")
        message_id = "reply:" + key
        phone_messages.append({"who":who,"out":True,"text":choice["text"],"time":clock,"delivery":"sending","id":message_id,"day":day})
        delays = {"ria":(1.2,3.8),"seoyun":(1.8,4.5),"yujin":(2.0,4.8),"jihyun":(1.4,3.6)}
        typing_at, arrive_at = delays[who]
        phone_pending.append({"id":message_id,"who":who,"text":choice["response"],"time":clock,"elapsed":0.0,"typing_at":typing_at,"arrive_at":arrive_at,"day":day,"event":key})
        reward_id = "%s:%s" % (day,who)
        if reward_id not in reply_reward_days:
            reply_reward_days.append(reward_id)
            apply_person_effects(who,{"affection":1})
        if choice.get("plan"): flags["lunch_plan"] = choice["plan"]
        flags.update(choice.get("set",{}))
        renpy.retain_after_load()
        renpy.restart_interaction()

    def photo_allowed(person, rule):
        if person.get("breach") or person.get("relationship") == "paused": return False
        if person.get("photo_cap",0) < rule["tier"]: return False
        if person["affection"] < rule["a"] or person["trust"] < rule["t"]: return False
        if person["episode_stage"] < rule["stage"]: return False
        if rule["dating"] and person["relationship"] not in ("dating","group"): return False
        if rule["tier"] >= 3 and not person.get("private_photo_ok",False): return False
        if rule["tier"] >= 3 and not person.get("core_resolved",False): return False
        return True

    def queue_photo_rewards():
        # Invocation belongs to story/day-end boundaries, never screen redraws.
        for who in names:
            last = next((x for x in reversed(phone_messages) if x.get("tier_photo") and x["who"]==who), None)
            if last and day - last.get("day",day) < 2: continue
            for rule in photo_tiers:
                token = "%s_tier%d" % (who,rule["tier"])
                asset = "images/phone/%s.png" % token
                if token in photo_received or not photo_allowed(people[who],rule): continue
                if not renpy.loadable(asset): break
                photo_received.append(token)
                phone_messages.append({"who":who,"out":False,"text":"오늘의 제 모습, 보여 드리고 싶었어요.","time":clock,"photo":token,"tier_photo":True,"day":day})
                break

    def photo_path(token):
        if token == "ria_cafe": return "images/cg/ria_cafe_cg_v001.png"
        return "images/phone/%s.png" % token

    def set_photo_permission(who, cap):
        people[who]["photo_cap"] = cap
        people[who]["private_photo_ok"] = cap >= 3
        renpy.retain_after_load()
        renpy.restart_interaction()

    def toggle_photo_saved(token):
        global photo_saved
        photo_saved = [item for item in photo_saved if item != token] if token in photo_saved else photo_saved + [token]
        renpy.retain_after_load()
        renpy.restart_interaction()

    def hide_photo(token):
        global photo_hidden, photo_saved
        if token not in photo_hidden: photo_hidden = photo_hidden + [token]
        photo_saved = [item for item in photo_saved if item != token]
        renpy.retain_after_load()
        renpy.restart_interaction()

init python:
    class OfficeFileLoad(FileLoad):
        def __call__(self):
            if not self.get_sensitive(): return
            page = str(self.page if self.page is not None else persistent._file_page)
            renpy.session["office_load_slot"] = str(self.name) if self.slot else page + "-" + str(self.name)
            return super(OfficeFileLoad,self).__call__()

    def restore_phone_ui_after_load():
        # Screen edits can occur after the current story statement checkpoint.
        # Restore these UI preferences from the selected native save, not another slot.
        global photo_saved, photo_hidden, phone_pending, phone_messages, phone_unread
        global phone_replied, reply_reward_days, flags, people, week_schedule, promises, phone_events, phone_expired, completed_events
        slot_name = renpy.session.pop("office_load_slot",None)
        if not slot_name: return
        saved = renpy.get_save_data(slot_name)
        if not saved: return
        phone_pending = list(saved.get("phone_pending", []))
        phone_messages = list(saved.get("phone_messages", phone_messages))
        phone_unread = dict(saved.get("phone_unread", {k:0 for k in names}))
        photo_saved = list(saved.get("photo_saved",photo_saved))
        photo_hidden = list(saved.get("photo_hidden",photo_hidden))
        phone_replied = list(saved.get("phone_replied",phone_replied))
        reply_reward_days = list(saved.get("reply_reward_days",reply_reward_days))
        phone_events = list(saved.get("phone_events",phone_events))
        phone_expired = list(saved.get("phone_expired",[]))
        completed_events = list(saved.get("completed_events",[]))
        flags = dict(saved.get("flags",flags))
        week_schedule = list(saved.get("week_schedule",[]))
        promises = list(saved.get("promises",promises))
        people = saved.get("people",people)

        saved_people = saved.get("people",{})
        for who in people:
            if who in saved_people:
                people[who]["photo_cap"] = saved_people[who].get("photo_cap",0)
                people[who]["private_photo_ok"] = saved_people[who].get("private_photo_ok",False)
        renpy.retain_after_load()
    config.after_load_callbacks.append(restore_phone_ui_after_load)

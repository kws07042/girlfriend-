# Fictional smartphone. Timed replies are native saveable game state.
default phone_pending = []
default phone_unread = {k: 0 for k in ("seoyun", "ria", "yujin", "jihyun")}

init python:
    phone_roles = {"seoyun":"서비스기획 과장", "ria":"캠페인 매니저", "yujin":"브랜드디자인 과장", "jihyun":"사업전략 팀장"}
    config.overlay_screens.append("phone_delivery_clock")

    class PhoneChatAdjustment(renpy.display.behavior.Adjustment):
        def __init__(self):
            self.follow_latest = True
            self.force_latest = True
            self.contact_key = None
            super(PhoneChatAdjustment,self).__init__(range=0.0,value=0.0,adjustable=True,
                changed=self.user_scrolled,ranged=self.content_resized)

        def user_scrolled(self,value):
            self.follow_latest = self.range - value <= 24

        def content_resized(self,adjustment):
            # Called after layout has measured the new bubble heights.
            # Use direct value assignment to avoid treating auto-follow as user scrolling.
            if self.follow_latest or self.force_latest:
                self.value = self.range
                self.force_latest = False
            else:
                self.value = min(self.value,self.range)

        def select_contact(self,who):
            if self.contact_key != who:
                self.contact_key = who
                self.follow_latest = True
                self.force_latest = True

        def latest(self):
            self.follow_latest = True
            self.force_latest = True
            self.change(self.range)
            renpy.restart_interaction()

    def phone_has_replies(who):
        return current_reply_key(who) is not None

    def phone_mark_read(who):
        phone_unread[who] = 0

    def phone_is_typing(who):
        return any(p["who"] == who and p["elapsed"] >= p["typing_at"] for p in phone_pending)

    def phone_message_status(msg):
        if not msg["out"]:
            return msg["time"]
        return {"sending":"전송 중", "sent":"전송됨", "read":"읽음"}.get(msg.get("delivery", "read"), "전송됨") + " / " + msg["time"]

    def phone_delivery_tick():
        if not phone_pending: return
        screen = renpy.get_screen("phone")
        viewed = screen.scope.get("contact") if screen else None
        tab = screen.scope.get("tab") if screen else None
        for pending in list(phone_pending):
            pending["elapsed"] += 0.15
            for msg in phone_messages:
                if msg.get("id") == pending["id"]:
                    msg["delivery"] = "read" if pending["elapsed"] >= 1.2 else ("sent" if pending["elapsed"] >= 0.6 else "sending")
            if pending["elapsed"] >= pending["arrive_at"]:
                phone_messages.append({"who":pending["who"],"out":False,"text":pending["text"],"time":clock,"day":day,"event":pending.get("event"),"id":pending["id"]+":response"})
                phone_pending.remove(pending)
                if viewed != pending["who"] or tab != "messages":
                    phone_unread[pending["who"]] += 1
                    renpy.notify(names[pending["who"]] + " · 새 메시지")
        if viewed and tab == "messages": phone_unread[viewed] = 0
        renpy.retain_after_load()
        renpy.restart_interaction()

screen phone_delivery_clock():
    if not main_menu and phone_pending and not renpy.get_screen("save") and not renpy.get_screen("load") and not renpy.get_screen("preferences") and not renpy.get_screen("history"):
        timer 0.15 repeat True action Function(phone_delivery_tick)

screen phone_typing(who):
    frame:
        background ui_panel("incoming") padding (18,14)
        hbox:
            spacing 12
            text names[who] + " 입력 중" size 19 color "#68757B" yalign 0.5
            for n in range(3):
                if persistent.reduce_motion:
                    add Transform("images/ui_v2/typing_dot.png",xysize=(7,7)) yalign 0.5
                else:
                    add Transform("images/ui_v2/typing_dot.png",xysize=(7,7)) yalign 0.5 at phone_typing_dot(delay=n*0.14)

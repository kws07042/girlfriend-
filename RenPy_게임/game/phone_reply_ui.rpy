# Contact cues distinguish an actionable reply from an unread message.
init python:
    def phone_contact_attention(who, required_reply=None):
        required = required_reply and phone_reply_available(required_reply)
        if required:
            target = message_data[required_reply].get("who", "ria")
            if who == target:
                return "reply"
        if current_reply_key(who):
            return "reply"
        if phone_unread.get(who, 0):
            return "unread"
        return None

transform phone_attention_pulse:
    alpha 0.45
    block:
        ease 0.65 alpha 1.0
        ease 0.65 alpha 0.45
        repeat

screen phone_contact_marker(who, required_reply=None):
    fixed:
        xsize 126 ysize 64
        $ attention = phone_contact_attention(who, required_reply)
        if attention:
            if not persistent.reduce_motion:
                add AlphaMask(Solid("#D74C4C"), Transform("images/ui_v2/circle.png", xysize=(6,6))) xpos 84 ypos 20 at phone_attention_pulse
            else:
                add AlphaMask(Solid("#D74C4C"), Transform("images/ui_v2/circle.png", xysize=(6,6))) xpos 84 ypos 20


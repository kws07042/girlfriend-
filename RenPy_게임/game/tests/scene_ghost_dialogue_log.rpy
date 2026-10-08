init 97 python:
    import os as _ghost_log_os
    if _ghost_log_os.environ.get("OFFICE_GHOST_DIALOGUE_LOG"):
        import json as _ghost_log_json
        def _ghost_qa_run(label,abnormal=False):
            if label == "start":
                _ghost_qa_dialogue.run += 1
        def _ghost_qa_dialogue(event,**kwargs):
            if event != "begin":
                return
            who = {"sy":"seoyun","ri":"ria","yj":"yujin","jh":"jihyun"}.get(getattr(store,"_last_say_who",None))
            if not who:
                return
            _ghost_qa_dialogue.entries.append({"run":_ghost_qa_dialogue.run,"day":day,"who":who,"text":getattr(store,"_last_say_what","")})
            with open(_ghost_log_os.environ["OFFICE_GHOST_DIALOGUE_LOG"],"w",encoding="utf-8") as _ghost_log_file:
                _ghost_log_json.dump(_ghost_qa_dialogue.entries,_ghost_log_file,ensure_ascii=False,indent=2)
        _ghost_qa_dialogue.entries = []
        _ghost_qa_dialogue.run = 0
        config.label_callbacks.append(_ghost_qa_run)
        config.all_character_callbacks.append(_ghost_qa_dialogue)

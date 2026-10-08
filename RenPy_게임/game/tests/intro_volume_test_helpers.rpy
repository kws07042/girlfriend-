# Records visible reading volume only during engine tests.
init 97 python:
    import os as _intro_qa_os
    import json as _intro_qa_json
    def intro_qa_record(event, **kwargs):
        if event != "begin" or renpy.game.args.command != "test":
            return
        path = _intro_qa_os.environ.get("OFFICE_INTRO_VOLUME_LOG")
        if not path:
            return
        rows = getattr(intro_qa_record,"rows",[])
        rows.append({"run":getattr(intro_qa_label,"run",0),"day":day,"who":getattr(store,"_last_say_who",None),"text":getattr(store,"_last_say_what","")})
        intro_qa_record.rows = rows
        with open(path,"w",encoding="utf-8") as stream:
            _intro_qa_json.dump(rows,stream,ensure_ascii=False)
    def intro_qa_label(label, abnormal):
        if label == "start":
            intro_qa_label.run = getattr(intro_qa_label,"run",0)+1
    if renpy.game.args.command == "test":
        config.all_character_callbacks.append(intro_qa_record)
        config.label_callbacks.append(intro_qa_label)

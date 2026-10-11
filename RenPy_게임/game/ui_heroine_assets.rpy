# One canonical image store: the repository's sibling heroine directory.
# config.searchpath is configured during init before any portrait/pose renderer.
init -100 python:
    import os as ui_heroine_os

    ui_heroine_root = ui_heroine_os.path.abspath(ui_heroine_os.path.join(config.basedir, ".."))
    if ui_heroine_root not in config.searchpath:
        config.searchpath.append(ui_heroine_root)

    ui_heroine_names = {"ria": "강리아", "seoyun": "한서윤", "yujin": "차유진", "jihyun": "백지현"}
    ui_heroine_pose_names = {
        "master": "MASTER", "listening": "듣는자세", "explaining": "설명",
        "work": "업무", "casual": "캐주얼", "signature": "대표",
        "greeting": "인사", "honest": "솔직한대화",
        "daily_a": "MASTER", "daily_b": "MASTER", "date_a": "MASTER", "date_b": "MASTER",
    }

    def ui_heroine_file(who, pose="master", state=None):
        prefix = "히로인/%s/업스케일/" % ui_heroine_names[who]
        name = ui_heroine_pose_names[pose]
        if state is not None:
            return prefix + "표정/%s_%s.png" % (name, state)
        if name == "MASTER":
            return prefix + "MASTER.png"
        return prefix + "포즈/%s.png" % name

    def ui_heroine_animation_file(who, name):
        return "히로인/%s/업스케일/애니메이션/%s" % (ui_heroine_names[who], name)

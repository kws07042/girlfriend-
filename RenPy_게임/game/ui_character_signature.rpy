# Signature gestures use their authored facial expression for short positive beats.
init 50 python:
    for _signature_who in ("ria", "seoyun", "yujin", "jihyun"):
        ui_pose_files[_signature_who]["signature"] = "images/characters/%s_poses/signature.png" % _signature_who

    ui_signature_beats = {
        "ria": (
            "네. 약속 지켰으니까, 이제는 진짜 점심 끝!",
            "어, 도현 씨! 여기예요. 사진이랑 같은 자리죠? 제가 약속 장소 설명은 잘해요.",
        ),
        "seoyun": (
            "도현 씨, 오셨어요? 여기 앉으시면 같이 보기 편해요.",
            "자료 위치는 메신저에 남겨 둘게요. 첫날에 전부 외우려고 하지 않아도 돼요.",
        ),
        "yujin": (
            "그 차이를 느꼈다면 두 개를 만든 이유가 전달된 거네요.",
            "그럼 다음엔 접시 이야기로요. 그쪽은 조금 더 삐뚤어졌어요.",
        ),
        "jihyun": (
            "좋아요. 제가 전달할 내용과 팀에서 검증할 내용을 구분할 수 있겠어요.",
            "오늘의 결정은 여기까지입니다. 첫 주 수고했어요.",
        ),
    }
    for _signature_who, _signature_lines in ui_signature_beats.items():
        for _signature_line in _signature_lines:
            ui_pose_beats[_signature_who][_signature_line] = "signature"

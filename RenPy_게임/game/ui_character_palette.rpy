# Whole-sprite palette calibration. Original faces, hands, silhouette and alpha stay authored.
init 31 python:
    import json as ui_palette_json
    with renpy.file("ui_pose_palette.json") as ui_palette_file:
        ui_pose_palette = ui_palette_json.load(ui_palette_file)
    renpy.register_shader("office.pose_palette", variables="""
        uniform vec3 u_pose_palette_anchor0;
        uniform vec3 u_pose_palette_delta0;
        uniform float u_pose_palette_radius0;
        uniform vec3 u_pose_palette_anchor1;
        uniform vec3 u_pose_palette_delta1;
        uniform float u_pose_palette_radius1;
        uniform vec3 u_pose_palette_anchor2;
        uniform vec3 u_pose_palette_delta2;
        uniform float u_pose_palette_radius2;
        uniform vec3 u_pose_palette_anchor3;
        uniform vec3 u_pose_palette_delta3;
        uniform float u_pose_palette_radius3;
        uniform vec3 u_pose_palette_anchor4;
        uniform vec3 u_pose_palette_delta4;
        uniform float u_pose_palette_radius4;
        uniform vec3 u_pose_palette_anchor5;
        uniform vec3 u_pose_palette_delta5;
        uniform float u_pose_palette_radius5;
        uniform vec3 u_pose_palette_anchor6;
        uniform vec3 u_pose_palette_delta6;
        uniform float u_pose_palette_radius6;
        uniform vec3 u_pose_palette_anchor7;
        uniform vec3 u_pose_palette_delta7;
        uniform float u_pose_palette_radius7;
        uniform vec3 u_pose_palette_anchor8;
        uniform vec3 u_pose_palette_delta8;
        uniform float u_pose_palette_radius8;
        uniform vec3 u_pose_palette_anchor9;
        uniform vec3 u_pose_palette_delta9;
        uniform float u_pose_palette_radius9;
        uniform vec3 u_pose_palette_anchor10;
        uniform vec3 u_pose_palette_delta10;
        uniform float u_pose_palette_radius10;
        uniform vec3 u_pose_palette_anchor11;
        uniform vec3 u_pose_palette_delta11;
        uniform float u_pose_palette_radius11;
    """,fragment_300="""
        float palette_alpha = gl_FragColor.a;
        vec3 palette_rgb = gl_FragColor.rgb / max(palette_alpha,0.00001);
        float palette_sum = 0.0;
        vec3 palette_delta = vec3(0.0);
        vec3 palette_distance0 = palette_rgb - u_pose_palette_anchor0;
        float palette_weight0 = exp(-0.5 * dot(palette_distance0, palette_distance0) / (u_pose_palette_radius0 * u_pose_palette_radius0));
        palette_sum += palette_weight0;
        palette_delta += palette_weight0 * u_pose_palette_delta0;
        vec3 palette_distance1 = palette_rgb - u_pose_palette_anchor1;
        float palette_weight1 = exp(-0.5 * dot(palette_distance1, palette_distance1) / (u_pose_palette_radius1 * u_pose_palette_radius1));
        palette_sum += palette_weight1;
        palette_delta += palette_weight1 * u_pose_palette_delta1;
        vec3 palette_distance2 = palette_rgb - u_pose_palette_anchor2;
        float palette_weight2 = exp(-0.5 * dot(palette_distance2, palette_distance2) / (u_pose_palette_radius2 * u_pose_palette_radius2));
        palette_sum += palette_weight2;
        palette_delta += palette_weight2 * u_pose_palette_delta2;
        vec3 palette_distance3 = palette_rgb - u_pose_palette_anchor3;
        float palette_weight3 = exp(-0.5 * dot(palette_distance3, palette_distance3) / (u_pose_palette_radius3 * u_pose_palette_radius3));
        palette_sum += palette_weight3;
        palette_delta += palette_weight3 * u_pose_palette_delta3;
        vec3 palette_distance4 = palette_rgb - u_pose_palette_anchor4;
        float palette_weight4 = exp(-0.5 * dot(palette_distance4, palette_distance4) / (u_pose_palette_radius4 * u_pose_palette_radius4));
        palette_sum += palette_weight4;
        palette_delta += palette_weight4 * u_pose_palette_delta4;
        vec3 palette_distance5 = palette_rgb - u_pose_palette_anchor5;
        float palette_weight5 = exp(-0.5 * dot(palette_distance5, palette_distance5) / (u_pose_palette_radius5 * u_pose_palette_radius5));
        palette_sum += palette_weight5;
        palette_delta += palette_weight5 * u_pose_palette_delta5;
        vec3 palette_distance6 = palette_rgb - u_pose_palette_anchor6;
        float palette_weight6 = exp(-0.5 * dot(palette_distance6, palette_distance6) / (u_pose_palette_radius6 * u_pose_palette_radius6));
        palette_sum += palette_weight6;
        palette_delta += palette_weight6 * u_pose_palette_delta6;
        vec3 palette_distance7 = palette_rgb - u_pose_palette_anchor7;
        float palette_weight7 = exp(-0.5 * dot(palette_distance7, palette_distance7) / (u_pose_palette_radius7 * u_pose_palette_radius7));
        palette_sum += palette_weight7;
        palette_delta += palette_weight7 * u_pose_palette_delta7;
        vec3 palette_distance8 = palette_rgb - u_pose_palette_anchor8;
        float palette_weight8 = exp(-0.5 * dot(palette_distance8, palette_distance8) / (u_pose_palette_radius8 * u_pose_palette_radius8));
        palette_sum += palette_weight8;
        palette_delta += palette_weight8 * u_pose_palette_delta8;
        vec3 palette_distance9 = palette_rgb - u_pose_palette_anchor9;
        float palette_weight9 = exp(-0.5 * dot(palette_distance9, palette_distance9) / (u_pose_palette_radius9 * u_pose_palette_radius9));
        palette_sum += palette_weight9;
        palette_delta += palette_weight9 * u_pose_palette_delta9;
        vec3 palette_distance10 = palette_rgb - u_pose_palette_anchor10;
        float palette_weight10 = exp(-0.5 * dot(palette_distance10, palette_distance10) / (u_pose_palette_radius10 * u_pose_palette_radius10));
        palette_sum += palette_weight10;
        palette_delta += palette_weight10 * u_pose_palette_delta10;
        vec3 palette_distance11 = palette_rgb - u_pose_palette_anchor11;
        float palette_weight11 = exp(-0.5 * dot(palette_distance11, palette_distance11) / (u_pose_palette_radius11 * u_pose_palette_radius11));
        palette_sum += palette_weight11;
        palette_delta += palette_weight11 * u_pose_palette_delta11;
        float palette_value = max(palette_rgb.r,max(palette_rgb.g,palette_rgb.b));
        float palette_gate = smoothstep(0.12,0.25,palette_value) * min(palette_sum,1.0);
        vec3 palette_corrected = clamp(palette_rgb + palette_delta / max(palette_sum,0.00000001) * palette_gate,0.0,1.0);
        gl_FragColor = vec4(palette_corrected * palette_alpha,palette_alpha);
    """)

    with renpy.file("ui_pose_head_tones.json") as ui_head_tones_file:
        ui_pose_head_tones = ui_palette_json.load(ui_head_tones_file)
    renpy.register_shader("office.pose_head_tones", variables="""
        uniform vec3 u_head_anchor0;
        uniform vec3 u_head_delta0;
        uniform float u_head_radius0;
        uniform vec3 u_head_anchor1;
        uniform vec3 u_head_delta1;
        uniform float u_head_radius1;
        uniform vec3 u_head_anchor2;
        uniform vec3 u_head_delta2;
        uniform float u_head_radius2;
        uniform vec3 u_head_anchor3;
        uniform vec3 u_head_delta3;
        uniform float u_head_radius3;
        uniform vec3 u_head_anchor4;
        uniform vec3 u_head_delta4;
        uniform float u_head_radius4;
        uniform vec3 u_head_anchor5;
        uniform vec3 u_head_delta5;
        uniform float u_head_radius5;
    """, fragment_400="""
        float head_alpha = gl_FragColor.a;
        vec3 head_rgb = gl_FragColor.rgb / max(head_alpha,0.00001);
        float head_sum = 0.0;
        vec3 head_delta = vec3(0.0);
        vec3 head_distance0 = head_rgb - u_head_anchor0;
        float head_weight0 = exp(-0.5 * dot(head_distance0,head_distance0) / (u_head_radius0*u_head_radius0));
        head_sum += head_weight0;
        head_delta += head_weight0 * u_head_delta0;
        vec3 head_distance1 = head_rgb - u_head_anchor1;
        float head_weight1 = exp(-0.5 * dot(head_distance1,head_distance1) / (u_head_radius1*u_head_radius1));
        head_sum += head_weight1;
        head_delta += head_weight1 * u_head_delta1;
        vec3 head_distance2 = head_rgb - u_head_anchor2;
        float head_weight2 = exp(-0.5 * dot(head_distance2,head_distance2) / (u_head_radius2*u_head_radius2));
        head_sum += head_weight2;
        head_delta += head_weight2 * u_head_delta2;
        vec3 head_distance3 = head_rgb - u_head_anchor3;
        float head_weight3 = exp(-0.5 * dot(head_distance3,head_distance3) / (u_head_radius3*u_head_radius3));
        head_sum += head_weight3;
        head_delta += head_weight3 * u_head_delta3;
        vec3 head_distance4 = head_rgb - u_head_anchor4;
        float head_weight4 = exp(-0.5 * dot(head_distance4,head_distance4) / (u_head_radius4*u_head_radius4));
        head_sum += head_weight4;
        head_delta += head_weight4 * u_head_delta4;
        vec3 head_distance5 = head_rgb - u_head_anchor5;
        float head_weight5 = exp(-0.5 * dot(head_distance5,head_distance5) / (u_head_radius5*u_head_radius5));
        head_sum += head_weight5;
        head_delta += head_weight5 * u_head_delta5;
        float head_gate = smoothstep(0.12,0.25,max(head_rgb.r,max(head_rgb.g,head_rgb.b))) * min(head_sum,1.0);
        vec3 head_corrected = clamp(head_rgb + head_delta / max(head_sum,0.00000001) * head_gate,0.0,1.0);
        gl_FragColor = vec4(head_corrected * head_alpha,head_alpha);
    """)

    def ui_character_palette_sprite(who,pose=None):
        pose = pose or ui_pose_current(who)
        original = Image(ui_character_pose_file(who,pose))
        if not ui_pose_palette.get("enabled",True):
            return original
        calibration = ui_pose_palette["characters"].get(who,{}).get(pose)
        head = ui_pose_head_tones["characters"].get(who,{}).get(pose) if ui_pose_head_tones.get("enabled",True) else None
        if calibration is None and head is None:
            return original
        cache = getattr(ui_character_palette_sprite,"cache",None)
        if cache is None:
            ui_character_palette_sprite.cache = cache = {}
        key = (who,pose,bool(head))
        if key not in cache:
            uniforms = {}
            shaders = []
            if calibration:
                shaders.append("office.pose_palette")
                for index in range(ui_pose_palette["cluster_count"]):
                    uniforms["u_pose_palette_anchor%d" % index] = tuple(calibration["anchors"][index])
                    uniforms["u_pose_palette_delta%d" % index] = tuple(calibration["deltas"][index])
                    uniforms["u_pose_palette_radius%d" % index] = float(calibration["radii"][index])
            if head:
                shaders.append("office.pose_head_tones")
                for index in range(ui_pose_head_tones["cluster_count"]):
                    uniforms["u_head_anchor%d" % index] = tuple(head["anchors"][index])
                    uniforms["u_head_delta%d" % index] = tuple(head["deltas"][index])
                    uniforms["u_head_radius%d" % index] = float(head["radii"][index])
            cache[key] = Transform(original,shader=shaders,**uniforms)
        return cache[key]

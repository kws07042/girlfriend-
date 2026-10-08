init 96 python:
    import os as _ghost_window_os
    if _ghost_window_os.environ.get("OFFICE_GHOST_HIDDEN_GL") == "1":
        _ghost_pg = renpy.display.core.pygame
        _ghost_original_set_mode = _ghost_pg.display.set_mode
        def _ghost_hidden_set_mode(*args,**kwargs):
            args = list(args)
            if len(args)>1:
                args[1] |= _ghost_pg.WINDOW_HIDDEN
            else:
                kwargs["flags"] = kwargs.get("flags",0) | _ghost_pg.WINDOW_HIDDEN
            if len(args)>3:
                args[3] = (-32000,-32000)
            else:
                kwargs["pos"] = (-32000,-32000)
            return _ghost_original_set_mode(*args,**kwargs)
        _ghost_pg.display.set_mode = _ghost_hidden_set_mode
        preferences.fullscreen = False
        preferences.restore_window_position = False

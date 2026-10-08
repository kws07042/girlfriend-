init 96 python:
    import os as _ghost_debug_os
    if _ghost_debug_os.environ.get("OFFICE_GHOST_INTROSPECT") == "1":
        _ghost_pg = renpy.display.core.pygame
        print("MODE_DOC",_ghost_pg.display.set_mode.__doc__,flush=True)
        print("HIDDEN_FLAGS",[(name,getattr(_ghost_pg,name)) for name in dir(_ghost_pg) if "HIDDEN" in name or "OPENGL" in name],flush=True)

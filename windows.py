def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDPIAwareness(1)
    except:
        pass
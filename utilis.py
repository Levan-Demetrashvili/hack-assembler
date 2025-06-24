def safe_int(s, base=10, default=None):
    try:
        return int(s, base)
    except (ValueError, TypeError):
        return default
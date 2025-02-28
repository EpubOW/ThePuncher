def print_bytes_at_nice_view(msg: bytes):
    if len(msg) > 0:
        return ' '.join(f'{b:02X}' for b in msg)
    else: return ''
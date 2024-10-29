def fix_str_encoding(str_with_broken_encoding: str) -> str:
    return str_with_broken_encoding.encode('latin1', errors="ignore").decode('utf8')

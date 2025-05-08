def stringify_value(value):
    """Преобразует значение в строку."""
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return f"{format_diff(build_diff(value, {}))}"
    if isinstance(value, list):
        return f"[{', '.join(map(stringify_value, value))}]"
    return str(value)


def build_diff(data1, data2):
    """Строит дерево различий."""
    diff = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    for key in keys:
        if key not in data2:
            diff.append(('removed', key, data1[key]))
        elif key not in data1:
            diff.append(('added', key, data2[key]))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append(('removed', key, data1[key]))
            diff.append(('added', key, data2[key]))
        elif data1[key] != data2[key]:
            diff.append(('removed', key, data1[key]))
            diff.append(('added', key, data2[key]))
        else:
            diff.append(('unchanged', key, data1[key]))
    
    return diff


def format_diff(diff):
    """Форматирует различия в строку."""
    lines = ['{']
    for status, key, value in diff:
        prefix = {
            'added': '  + ',
            'removed': '  - ',
            'unchanged': '    '
        }[status]
        lines.append(f"{prefix}{key}: {stringify_value(value)}")
    lines.append('}')
    return '\n'.join(lines)

def format_plain(diff, parent_key=''):
    lines = []
    for node in sorted(diff, key=lambda x: x['key']):
        key = node['key']
        status = node['status']
        full_key = f"{parent_key}.{key}" if parent_key else key

        if status == 'nested':
            lines.extend(format_plain(node['children'], full_key).splitlines())
        elif status == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{full_key}' was added with value: {value}")
        elif status == 'removed':
            lines.append(f"Property '{full_key}' was removed")
        elif status == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{full_key}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)

def format_value(value, depth):
    if isinstance(value, dict):
        indent_size = 4
        indent = ' ' * (depth * indent_size)
        closing_indent = ' ' * ((depth - 1) * indent_size)
        lines = []

        for key, val in value.items():
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{indent}{key}: {formatted_val}")

        return '{\n' + '\n'.join(lines) + f'\n{closing_indent}}}'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)


def format_stylish(diff_tree, depth=0):
    lines = []
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    sign_indent = ' ' * (depth * indent_size - 2) if depth > 0 else ''

    for node in diff_tree:
        key = node['key']
        status = node['status']

        if status == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{sign_indent}+ {key}: {value}  # Добавлена")
        elif status == 'removed':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{sign_indent}- {key}: {value}  # Удалена")
        elif status == 'changed':
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            lines.append(
                f"{sign_indent}- {key}: {old_value}  "
                "# Старое значение"
                )
            lines.append(
                f"{sign_indent}+ {key}: {new_value}  "
                "# Новое значение"
                )
        elif status == 'unchanged':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
        elif status == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}    {key}: {{\n{children}\n{indent}    }}")

    return '\n'.join(lines)









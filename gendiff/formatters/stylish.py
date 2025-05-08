def format_value(value, depth):
    """Форматирует значения с учётом их типа и глубины вложенности."""
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    closing_indent = ' ' * ((depth - 1) * indent_size) if depth > 0 else ''
    
    if isinstance(value, dict):
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
    """Форматирует дерево различий в стиле stylish с учётом вложенности."""
    lines = []
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    
    for node in diff_tree:
        key = node['key']
        status = node['status']

        if status == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}+ {key}: {value}")
        elif status == 'removed':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}- {key}: {value}")
        elif status == 'changed':
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            lines.append(f"{indent}- {key}: {old_value}")
            lines.append(f"{indent}+ {key}: {new_value}")
        elif status == 'unchanged':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
        elif status == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}    {key}: {{\n{children}\n{indent}    }}")

    return '\n'.join(lines)

def format_value(value, depth):
    print(f"Formatting value: {value}")
    if isinstance(value, bool):
        return 'false' if value is False else 'true'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        lines = [
            f'{indent}    {k}: {format_value(v, depth + 1)}'
            for k, v in value.items()
        ]
        return "{\n" + "\n".join(lines) + f"\n{indent}  }}"
    if isinstance(value, list):
        indent = ' ' * (depth * 4)
        lines = [
            f'{indent}    {item}' for item in value
        ]
        return "[\n" + "\n".join(lines) + f"\n{indent}  ]"
    return str(value)


def format_stylish(diff_tree, depth=0):
    result = []
    indent = '  ' * depth
    for node in diff_tree:
        print(f"Processing node: {node}")
        key = node['key']
        status = node['status']

        if status == 'added':
            result.append(f"{indent}+ {key}: {node['value']}")
        elif status == 'removed':
            result.append(f"{indent}- {key}: {node['value']}")
        elif status == 'changed':
            result.append(f"{indent}- {key}: {node['old_value']}")
            result.append(f"{indent}+ {key}: {node['new_value']}")
        elif status == 'unchanged':
            result.append(f"{indent}  {key}: {node['value']}")
        elif status == 'nested':
            result.append(f"{indent}  {key}: {{")
            result.append(format_stylish(node['children'], depth + 1))
            result.append(f"{indent}  }}")
        elif isinstance(node['value'], list):
            result.append(f"{indent}  {key}: [")
            for item in node['value']:
                result.append(f"{indent}    {item}")
            result.append(f"{indent}  ]")
    return '\n'.join(result)








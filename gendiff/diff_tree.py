def build_diff(data1, data2):
    """Строит дерево различий между двумя словарями."""
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        node = {'key': key}

        if key not in data1:
            node.update({
                'status': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            node.update({
                'status': 'removed',
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            node.update({
                'status': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        elif data1[key] != data2[key]:
            node.update({
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
        else:
            node.update({
                'status': 'unchanged',
                'value': data1[key]
            })

        diff.append(node)

    return diff

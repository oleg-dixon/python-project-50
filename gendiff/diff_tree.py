def build_diff_tree(data1, data2):
    print(f"Data1: {data1}")
    print(f"Data2: {data2}")
    keys = sorted(set(data1) | set(data2))
    diff = []

    for key in keys:
        print(f"Comparing key: {key}")
        print(f"Value in file1: {data1.get(key)}")
        print(f"Value in file2: {data2.get(key)}")

        if key not in data1:
            diff.append({
                'key': key,
                'status': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            diff.append({
                'key': key,
                'status': 'removed',
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff_tree(data1[key], data2[key])
            diff.append({
                'key': key,
                'status': 'nested',
                'children': children
            })
        elif isinstance(data1[key], list) and isinstance(data2[key], list):
            if data1[key] != data2[key]:
                diff.append({
                    'key': key,
                    'status': 'changed',
                    'old_value': data1[key],
                    'new_value': data2[key]
                })
        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
        else:
            diff.append({
                'key': key,
                'status': 'unchanged',
                'value': data1[key]
            })
    return diff

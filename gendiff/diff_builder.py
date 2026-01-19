def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key not in data2:
            diff.append({"key": key, "type": "removed", "value": val1})
        elif key not in data1:
            diff.append({"key": key, "type": "added", "value": val2})
        elif val1 == val2:
            diff.append({"key": key, "type": "unchanged", "value": val1})
        elif isinstance(val1, dict) and isinstance(val2, dict):
            children = build_diff(val1, val2)
            diff.append({"key": key, "type": "nested", "children": children})
        else:
            diff.append({
                "key": key,
                "type": "changed",
                "value": {"old": val1, "new": val2}
            })

    return diff

def iou(bbox1: list, bbox2: list) -> float:
    y1, h1, x1, w1 = bbox1
    y2, h2, x2, w2 = bbox2

    s1 = h1 * w1 * 1.0
    h = y1 + h1 - y2 if y1 < y2 else y2 + h2 - y1
    w = x1 + w1 - x2 if x1 < x2 else x2 + w2 - x1

    if h < 0 or w < 0:
        return 0

    return h * w / s1

bbox1 = [0, 10, 0, 10]
bbox2 = [0, 10, 1, 10]
bbox3 = [20, 30, 20, 30]
bbox4 = [5, 15, 5, 15]

assert iou(bbox1, bbox1) == 1.0
assert iou(bbox1, bbox2) == 0.9
assert iou(bbox1, bbox3) == 0.0
assert round(iou(bbox1, bbox4), 2) == 0.14

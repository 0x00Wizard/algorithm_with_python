def merge(left_half, right_half):
    if not left_half or not right_half:
        return left_half or right_half

    result = []
    i, j = 0, 0

    while True:
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1


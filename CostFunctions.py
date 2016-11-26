
def Linear(criterion_data, reversed=False, min_v=None, max_v=None):
    result = []
    d_max = max(criterion_data)
    d_min = min(criterion_data)

    k = 100/(d_max-d_min)

    for value in criterion_data:
        if min_v is not None and value < min_v:
            result.append(0)
        elif max_v is not None and value > max_v:
            result.append(100)
        else:
            if reversed:
                result.append(100 - k * (value - d_min))
            else:
                result.append(k * (value - d_min))

    return result

def Discrete(criterion_data, dic):
    result = []
    for value in criterion_data:
        result.append(dic[value])
    return result
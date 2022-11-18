## Сложность данного алгоритма O(n)
def maxScoreSightseeingPair(values):
    max_value = 0
    cur_value = 0
    for i in range(1, len(values)): ##Пробегаемся циклом по значениям, которые нам дали
        cur_value = max(cur_value, values[i-1]+i-1)
        max_value = max(max_value, cur_value+values[i]-i)
    return max_value
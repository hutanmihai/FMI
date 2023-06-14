if __name__ == '__main__':
    unordered_list = [2, 3, 4, 5, 1, 6, 8]
    max_weight = 8
    weights = {0}
    total = 0
    for w in unordered_list:
        temp = weights.copy()
        while temp:
            val = temp.pop()
            if val + w <= max_weight:
                weights.add(val + w)
                total = max(total, val + w)
    print(total)

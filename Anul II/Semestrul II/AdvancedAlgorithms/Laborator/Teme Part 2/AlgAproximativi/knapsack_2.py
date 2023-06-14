if __name__ == '__main__':
    unordered_list = [2, 3, 4, 5, 1]
    max_weight = 10  # var 1
    total = 0  # var 2
    for val in unordered_list:  # var 3
        total += val
        if total > max_weight:
            print(max(total - val, val))
            break

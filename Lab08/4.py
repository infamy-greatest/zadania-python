def rec_sum(num):
    if num == 1:
        return 1
    else:
        return rec_sum(num - 1) + num


print(rec_sum(5))

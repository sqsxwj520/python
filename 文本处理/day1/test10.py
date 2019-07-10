def get_human_str(size: int) -> str:
    units = " KMGTP"
    # units = ['', 'K', 'M', 'G', 'T', 'P']
    index = 0
    length = len(units)
    while size >= 1000 and index < length - 1:  # and后是考虑边界问题
        size //= 1000
        index += 1

    return '{}{}'.format(size, units[index])


print(get_human_str(1300))  # 1k
print(get_human_str(1300000))  # 1M
print(get_human_str(130))  # 130

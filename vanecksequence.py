import collections
num = 0
count = 0
visited_dict = collections.defaultdict()

print("0",end=" ")
while num <= 100:
    count += 1
    #visited_dict[num] = count if visited_dict[num] is None else count - visited_dict[num]

    if num in visited_dict.keys():
        val = count - visited_dict[num]
        visited_dict[num] = count
        num = val
    else:
        visited_dict[num] = count
        num = 0

    print(num, end=" ")

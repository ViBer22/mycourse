def balance_lists(list1, list2):
    total_elements = len(list1) + len(list2)
    target_size = total_elements // 2

    while len(list1) > target_size:
        list2.append(list1.pop())

    while len(list2) > target_size:
        list1.append(list2.pop())

    return list1, list2

# Testfall
list1 = [1, 2, 3]
list2 = [4, 5, 6, 7, 8]

result_list1, result_list2 = balance_lists(list1, list2)

print(result_list1)
print(result_list2)

def balance_lists(list1, list2):
    total_elements = len(list1) + len(list2)
    target_size = total_elements // 2

    def move_elements(source, target, target_size):
        while len(source) > target_size:
            target.append(source.pop())

    move_elements(list1, list2, target_size)
    move_elements(list2, list1, target_size)

    return list1, list2


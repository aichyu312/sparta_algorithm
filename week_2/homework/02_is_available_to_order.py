shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# def is_available_to_order(menus, orders):
#     menus.sort()  # menus 정렬!
#     for order in orders:
#         if not is_existing_target_number_binary(order, menus):
#             return False
#     return True
#
#
# def is_existing_target_number_binary(target, array):
#     current_min = 0
#     current_max = len(array) - 1
#     current_guess = (current_min + current_max) // 2
#
#     while current_min <= current_max:
#         if array[current_guess] == target:
#             return True
#         elif array[current_guess] < target:
#             current_min = current_guess + 1
#         else:
#             current_max = current_guess - 1
#         current_guess = (current_min + current_max) // 2
#
#     return False

# O((M+N)*logn) 만큼의 시간 복잡도가 소요된다 아래의 코드는
# O(M+N) 만큼의 시간 복잡도가 소요된다. *이분탐색이 무조건 효율적인 코드는 아니다.

def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
def find_sum(price_list):
    if not price_list:
        return 0
    coupons_num = len(list(filter(lambda x: x > 100, price_list)))
    max_price = price_list[len(price_list) - 1]
    total = sum(price_list)
    if max_price > 100:
        coupons_num -= 1
    print(coupons_num)
    for i in range(len(price_list) - 2, -1, -1):
        price = price_list[i]
        print(price)
        if price - max_price > 100 and coupons_num > 1:
            coupons_num -= 2
            total -= price
        elif price > 100 and coupons_num > 0:
            coupons_num -= 1
            total -= max_price
            max_price = 0
        elif price > max_price:
            max_price = price
    return total


print(find_sum([0]))

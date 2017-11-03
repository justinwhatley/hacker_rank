import sys


def get_icecream(money_available, sorted_prices):
    # binary search for ice cream
    temp_available = money_available
    ice_cream_prices = []
    success = False
    i_start = 0
    while (not success):
        i = i_start
        while (i < len(sorted_prices)):
            lower_bound = i
            upper_bound = len(sorted_prices) - 1

            def helper(i, lower_bound, upper_bound, sorted_prices, money_available):

                ice_cream_1 = sorted_prices[i][0]
                target = money_available - ice_cream_1

                lower_bound = 0
                middle = lower_bound + (upper_bound - lower_bound) // 2
                if sorted_prices[middle][0] < target:
                    return False

                while lower_bound <= upper_bound:
                    middle = lower_bound + (upper_bound - lower_bound) // 2
                    val = sorted_prices[middle][0]

                    if target > val:
                        if lower_bound == middle:
                            break
                        lower_bound = middle + 1
                    elif target < val:
                        upper_bound = middle - 1
                    else:
                        return sorted_prices[i][1], sorted_prices[middle][1]
                return False

                """
                j = lower_bound + ((upper_bound-lower_bound)//2)
                print('j' + str(j))
                ice_cream_2 = sorted_prices[j][0]

                diff = money_available - (ice_cream_1+ice_cream_2)
                print('diff' + str(diff))

                if diff > 0:
                    helper(i, j, upper_bound, sorted_prices, money_available)
                elif diff < 0:
                    helper(i, lower_bound, j, sorted_prices, money_available)
                else:
                    return sorted_prices[i][1], sorted_prices[j][1]
                """

            success = helper(i, lower_bound, upper_bound, sorted_prices, money_available)
            if success:
                break
            i = i + 1

    return success


trip_count = int(input())
i = 0
data_list = []
while (i < trip_count):
    money_available = int((sys.stdin.readline().strip().split(' '))[0])
    number_of_options = int((sys.stdin.readline().strip().split(' '))[0])
    counter = 1
    indexes = []
    while counter <= number_of_options:
        indexes.append(counter)
        counter = counter + 1
    prices = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    sorted_prices = sorted(zip(prices, indexes))

    result = sorted(get_icecream(money_available, sorted_prices))
    print(' '.join([str(x) for x in result]))
    i = i + 1




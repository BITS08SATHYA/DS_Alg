def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1

    i = 0
    while i <= furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1

    return furthest_reached >= last_idx


# A1 = [3, 3, 1, 0, 2, 0, 1]
# print(array_advance(A1))

# finite preicsion problem
A = [1, 4, 9]
A1 = [9, 9, 9]
s = ''.join(map(str, A))


# print(int(s) + 1)

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


# print(plus_one(A1))

A = [-2, 1, 2, 4, 7, 11]


def sum_two_numbers(A, target):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                return A[i], A[j]
    return False


# print(sum_two_numbers(A, 20))
Ab = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def buy_and_sell_once(A):
    max_profit = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit


def buy_and_sell_once_1(A):
    max_profit = 0.0
    min_price = A[0]
    for price in A:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit


print(buy_and_sell_once_1(Ab))

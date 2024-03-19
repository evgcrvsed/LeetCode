# Составить программу для нахождения чисел из интервала [M, N] имеющих наибольшее количество делителей

def find_numbers_with_max_divisors(M, N):
    max_divisors = 0
    numbers_with_max_divisors = []

    for num in range(M, N + 1):
        divisors_count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisors_count += 1

        if divisors_count > max_divisors:
            max_divisors = divisors_count
            numbers_with_max_divisors = [num]
        elif divisors_count == max_divisors:
            numbers_with_max_divisors.append(num)

    return numbers_with_max_divisors


M = 0
N = 30

print("Числа с наибольшим количеством делителей:", find_numbers_with_max_divisors(M, N))

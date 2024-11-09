def is_prime(func):
    def wrapper(*args):
        i = func(*args)
        if i > 1 and isinstance(i, int):
            is_prime_ = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime_ = False
                    break
            if is_prime_:
                print('Простое')
            else:
                print('Составное')
        else:
            print('Число не является ни простым, ни составным')
        return i

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

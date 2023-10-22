start_num = 2
end_num = 10
twin_primes_list = []

for num in range(start_num, end_num):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        if num + 2 <= end_num:
            is_twin_prime = True
            for i in range(2, int((num + 2)**0.5) + 1):
                if (num + 2) % i == 0:
                    is_twin_prime = False
                    break
            if is_twin_prime:
                twin_primes_list.append((num, num + 2))

print("Twin Primes between", start_num, "and", end_num, "are:")
for twin in twin_primes_list:
    print(twin)
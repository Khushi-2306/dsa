import time
n1 = int(input("Enter first value of n: "))
n2 = int(input("Enter second value of n: "))
n3 = int(input("Enter third value of n: "))
for n in [n1, n2, n3]:
    start = time.time()
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1  
    end = time.time()
    print(f"Time taken for n = {n} (O(n^2)) is {end - start:.6f} seconds")

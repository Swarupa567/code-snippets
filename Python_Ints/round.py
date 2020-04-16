import random

def truncate(num):
    return int(num * 1000) / 1000

arr = [random.uniform(0.01, 0.05) for _ in range(1000000)]
sum_num = 0
sum_truncate = 0
for i in arr:
    sum_num = sum_num + i
    sum_truncate = truncate(sum_truncate + i)

print("Testing by using truncating upto 3 decimal places")
print("The original sum is = ", sum_num)
print("The total using truncate = ", sum_truncate)
print("The difference from original - truncate = ", sum_num - sum_truncate)

print("\n\n")
print("Testing by using round() upto 3 decimal places")
sum_num1 = 0
sum_truncate1 = 0
for i in arr:
    sum_num1 = sum_num1 + i
    sum_truncate1 = round(sum_truncate1 + i, 3)


print("The original sum is =", sum_num1)
print("The total using round = ", sum_truncate1)
print("The difference from original - round =", sum_num1 - sum_truncate1)

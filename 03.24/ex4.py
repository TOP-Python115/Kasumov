list = input("Введите список целых чисел: ").split()
nat_num = [int(n) for n in list]
count = 0

for i in range(1, len(nat_num)):
    if nat_num[i] > nat_num[i - 1]:
        count += 1
        
print(count)
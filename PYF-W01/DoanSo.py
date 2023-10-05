import random
so = int(input("nhap vao so du doan: "))

so_may = random.randint(0,9)
print(f"so may la: {so_may}")
if so == so_may:
    print("Ban du doan dung")
    print(f"So may du doan: {so_may}")
else:
    print("Ban du doan sai")
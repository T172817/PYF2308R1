chieuCao = float(input("Nhap vao chieu cao (m): "))
canNang = float(input("Nhap vao can nang (kg): "))
chiSoBMI = canNang / (chieuCao**2)
if chiSoBMI < 16:
    print("Gay cap do III")
elif 16 <= chiSoBMI < 17:
    print("Gay cap do II")
elif 17<= chiSoBMI < 18.5:
    print("Gay cap do I")
elif 18.5 <= chiSoBMI < 25:
    print("Bình thường")
elif 25 <= chiSoBMI < 30:
    print("Thừa cân")
elif 30 <= chiSoBMI < 35:
    print("Béo phì cấp độ I")
elif 35 <= chiSoBMI < 40:
    print("Béo phì cấp độ II")
elif chiSoBMI > 40:
    print("Béo phì cấp độ III")
else:
    print("out")
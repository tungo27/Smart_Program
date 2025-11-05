def salary(sogiolam, luonggio ):
    if sogiolam <= 40:
        tong = sogiolam * luonggio
    elif  sogiolam > 40 :
        giotangca  = sogiolam - 40
        sogiolam -= giotangca
        tong = (sogiolam * luonggio) + (giotangca * luonggio * 1.5)
    return tong
sogiolam= float(input("Nhập vào số giờ làm: "))
luonggio= float(input("Nhập vào số lương: "))
print(f'Tổng số tiền bạn nhận được là: {salary(sogiolam, luonggio):.2f}')
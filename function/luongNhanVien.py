def salaryList(dsluong):
    for i in range(len(dsluong)):
        for j in range(i+1, len(dsluong)):
            if dsluong[i] > dsluong[j]:
                tmp = dsluong[i]
                dsluong[i] = dsluong[j]
                dsluong[j] = tmp
    return dsluong 
so_nhan_vien = int(input("Nhập số nhân viên: "))
ds_luong =[]
for i in range(1,so_nhan_vien+1):
    luong = float(input(f"Nhập lương nhân viên thứ {i}: "))
    ds_luong.append(luong)
print(f"Danh sách lương sau khi đã sắp xếp là: {salaryList(ds_luong)}")

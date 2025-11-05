def num_subject_of_score():
    ds_diem =[]
    ds_he_so = []
    so_mon = int(input("Tong so mon hoc can tinh DTB: "))
    for i in range(1,so_mon+1):
        diem = float(input(f"Diem mon hoc {i}: "))        
        while diem < 0 or diem > 10:           
            diem = float(input(f"""Bạn đã nhập sai quy tắc điểm. Nếu bạn muốn thoát chương trình, hãy nhập "-1"
Nếu bạn muốn tiếp tục hãy nhập vào số từ 0 đến 10: """))
            if diem == -1:
                break
        if diem == -1:
                break
        if 0<= diem <= 10:
            ds_diem.append(diem)
            
        he_so = (input(f'He so mon hoc {i}: '))
        while he_so not in ("1", "1.5", "2", "2.5","3"):           
            he_so = (input(f"""Bạn đã nhập sai quy tắc hệ số. Nếu bạn muốn thoát chương trình, hãy nhập "E"
Nếu bạn muốn tiếp tục hãy nhập theo đúng quy tắc điểm là một trong các số sau đây : 1, 1.5, 2, 2.5, 3: """))
            if he_so == "E":
                break
        if he_so == "E":
                break
        if he_so in ("1", "1.5", "2", "2.5","3"):
            ds_he_so.append(he_so)
    if len(ds_diem) == 0 or len(ds_he_so) == 0 or len(ds_he_so) == len(ds_diem) and len(ds_he_so) != so_mon:
        return False, False 
    elif len(ds_diem) != len(ds_he_so):
        return False, False 
    else:
        return ds_diem, ds_he_so
            
            
def tinh_dtb():
    ds_diem, ds_he_so = num_subject_of_score()
    if ds_diem or ds_he_so != False: 
        tong_he_so = 0
        dtb_mon =0
        dtb = 0
        for i in range (len(ds_diem)) :
            dtb_mon += float(ds_he_so[i])*float(ds_diem[i]) 
        for i in ds_he_so:
            tong_he_so += float(i)
        dtb = dtb_mon / tong_he_so
        return f'Tong so he so: {tong_he_so}\nDTB của mon hoc là: {dtb:.2f}'   
    else:
        return "Cảm ơn bạn đã sử dụng chương trình tính điểm."

dtb = tinh_dtb() 
print (dtb)


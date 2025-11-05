def dayOfMonth(thang):
    if thang in (1,3,5,7,8,10,12):
        return 31
    elif thang in (4,6,9,11):
        return 30
    elif thang == 2 :
        nam = int(input("Nhập năm: "))
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        else:
            return 28
    else:
        return False 
thang = int(input("Nhập vào tháng: "))
ngày = dayOfMonth(thang)
if ngày :
            print(f'Có {ngày} ngày trong tháng này')
else:
            print(f'Không có tháng {thang} trong năm')

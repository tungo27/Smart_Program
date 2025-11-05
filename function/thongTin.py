
def nameOfStaff(ten_day_du):    
    while ten_day_du [0] == " ":
        ten_day_du  = ten_day_du [1:]
    while ten_day_du [-1] == " ":
        ten_day_du  = ten_day_du [:-1]
    tên   =''
    hovalot =''
    for i in ten_day_du :
        if i != " ":
            tên  += i
        else :
            hovalot+= tên +" "
            tên  = ""
    return (f"""Họ và tên lót của nhân viên là: {hovalot.title()}
Tên của nhân viên là: {tên.title()}
Tên đầy đủ của nhân viên là: {ten_day_du .title()}""")

ten_day_du = input("Nhập tên đầy đủ của nhân viên: ")
print(nameOfStaff(ten_day_du))
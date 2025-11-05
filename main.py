import function
from function import menu 

type = int(input("Nhập số chuong trình muốn chạy: "))
while 1<= type <= 6:
    if type == 1:
        from function import xemLich
           
    elif type == 2 :
        from function import luongNhanVien   
        
    elif type == 3:
        from function import tinhLuong 
        
    elif type ==  4 :
      from function import thongTin 
        
    elif type == 5 :
       from function import tinhDiem 
    elif type == 6 :
        break
    type = int(input("""
Bạn có muốn tiếp tục chương trình hay không?
Nếu muốn, bạn hãy nhấn 1 trong các phím từ 1 đến 5.
Nếu không, hãy nhấn phím 6 để thoát chương trình!
Mời bạn nhập: """))
print("Cảm ơn bạn đã sử dụng chương trình của tôi.")

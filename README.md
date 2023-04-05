FSBMSE: Python For Engineer Assignments
CLASS : FSB-MSE12-2022
MSHV : 22MSE23088
HV NAME : LÊ CHÍ NGOAN
Releases : https://github.com/ngoan22mse23088/python4engineers-assignments

Assignments 2:

Đọc dữ liệu cost_revenue_dirty.csv vào server, sau đó thực hiện truy vấn dữ liệu từ mysql-python.
Chuyển dữ liệu thành DataFrame Pandas và thực hiện xử lý dữ liệu.
Cuối cùng trực quan thể hiện doanh thu toàn cầu của 5 bộ phim đầu tiên của bảng.
Môi trường Colab : https://github.com/ngoan22mse23088/python4engineers-assignments/blob/master/Assignments_2.ipynb
Môi trường local : https://github.com/ngoan22mse23088/python4engineers-assignments/tree/master/Assignments%202

Assignments 3:

Dựa trên templates và dữ liệu được cung cấp. 
Viết CRUD database function thông qua api với Flask. Hiển thị kết quả trên cửa sổ thực thi và templates.
Templates : https://drive.google.com/file/d/1LUZuEqw2NiRaiQ2sVrDkFt5r4H-3UXgR/view
Môi trường Colab : https://github.com/ngoan22mse23088/python4engineers-assignments/blob/master/Assignments_3.ipynb
Môi trường local : https://github.com/ngoan22mse23088/python4engineers-assignments/tree/master/Assignments%203

Final Assignments:

Cho link web sau: https://gearvn.com/collections/laptop-gaming-ban-chay
Yêu cầu:
Thực hiện Web scraping lấy hết các dữ liệu trong mục “LAPTOP GAMING BÁN CHẠY” với mỗi mục dữ liệu 
gồm các trường (fields) sau:
Name: ví dụ Laptop Gaming Acer Nitro 5 Eagle AN515 57 53F9
OldPrice: ví dụ 25,990,000₫
NewPrice: ví dụ 20,990,000₫
PercentDiscount: ví dụ -19%
BestSeller: ví dụ 1 (nếu có Best Seller) hoặc 0 (nếu không có Best Seller)
Thực hiện xử lý dữ liệu thành các định dạng sau:
Name (Str): Nitro 5 Eagle
Brand (Str): Acer
OldPrice (int): 2599000
NewPrice (int): 20990000
PercentDiscount (int): 19
BestSeller (bool): 1
Thực hiện trực quan sau:
Trực quan trung bình và trung vị giá bán cũ và mới với các Brand. Cho nhận xét
Trực quan đếm số sản phẩm của các Brand. Cho nhận xét
Trực quan mức giảm giá cao nhất và thấp nhất của sản phẩm mỗi Brand. Cho nhận xét
Trực quan mức giá mới của các sản phẩm là BestSeller. Cho nhận xét
Tạo Database tên LAPTOP Table với các fields đã nêu trên đặt tên LAPTOPBESTSELLER. Viết CRUD database function với Flask cho phép ghi, đọc, chỉnh sửa và xoá các dữ liệu đã được xử lý vào database.

Môi trường Colab : https://github.com/ngoan22mse23088/python4engineers-assignments/blob/master/Assignments_Final.ipynb
Môi trường local : https://github.com/ngoan22mse23088/python4engineers-assignments/tree/master/Assignments%20Final

Contributions
import pandas as pd 
import matplotlib.pyplot as plt
def Doc_du_lieu() :
    df = pd.read_excel("d:/Drug (1).xlsx",engine='openpyxl')
    # In kết quả đọc dữ liệu
    print(df)
def Cap_nhat_du_lieu() :
    # Khai báo thư viện
    import pandas as pd
    df = pd.read_excel("d:/Drug (1).xlsx",engine='openpyxl')
    df['ReviewCount'] = df['Reviews'].str.extract(r'(\d+)').astype(float) # Tách số lượng review từ trường 'Reviews'
    grouped_data = df.groupby('[Condition','Drug]').agg({
    'Indication': 'first',  # giá trị đầu tiên của 'Indication'
    'Type': 'first',  # giá trị đầu tiên của 'Type'
    'ReviewCount': 'sum',  # Tổng số lượng reviews
    'Effective': 'mean',  # Trung bình hiệu quả
    'EaseOfUse': 'mean',  # Trung bình độ dễ sử dụng
    'Satisfaction': 'mean',  # Trung bình mức độ hài lòng
    'Information': list  # Tất cả thông tin khác về thuốc 
}).reset_index() # Gộp các dòng cùng bệnh và trùng loại thuốc
    print("df['ReviewCount']")
    print("grouped_data")
def Tao_du_lieu_moi() :
    # Khai báo thu viện
    import pandas as pd 
    df = pd.read_excel("d:/Drug (4).xlsx",engine="openpyxl")
    # In kết quả tạo dữ liệu mới
    print(df)
def Xoa_du_lieu() :
    # In kết quả xóa dữ liệu
    print(Xoa_du_lieu)
def Tinh_trung_binh() :
    # Khai báo thư viện
    import pandas as pd
    df = pd.read_excel("d:/Drug (4).xlsx",engine="openpyxl")
    # Lựa chọn hết dòng : và lấy 3 cột từ 6:9
    df.iloc[:,6:9]
    # Tính trung bình của ba trường 'Effective', 'EaseOfUse', và 'Satisfaction'
    df['Average_Effectiveness'] = df.groupby[['Effective', 'EaseOfUse', 'Satisfaction']].mean(axis=1)
    print(df['Average_Effectiveness'])
def Bieu_do() :
    # Khai báo thu viện
    import pandas as pd 
    import matplotlib.pyplot as plt
    df = pd.read_excel("d:/Drug (4).xlsx",engine="openpyxl") #đọc file excel, sheet name cho biết là sheet đầu tiên của file 
    a = df['Reviews'].tolist() # a là danh sách giá trị từ cột reviews
    b = df['Effective'].tolist() # b là danh sách giá trị từ cột effective 
    fig = plt.figure() # tạo không gian biểu đồ để thêm các trục 
    ax = fig.add_axes([0,0,1,1]) # thêm trục vào figure (0,0) góc dưới trục là góc toạ độ của figure (1,1) trục kéo dài đến điểm (1,1) chiếm toàn bộ diện tích figure 
    ax.axis('equal') # đảm bảo tỉ lệ 2 trục bằng nhau 
    explode = (0,0.2,0.4,0.6,0.8,1) # tưng pie được văng ra tính từ gốc trung tâm 
    ax.pie(a,explode=explode,labels=b,autopct='%1.2f%%') # a:giá trị của từng pie , explode: chỉ ra khoảng cách của từng slice , gán nhãn từ cột effective cho mỗi pie , autopct : hiển thị phần trăm trong tuừng pie với 2 chữ số thập phân 
    # Hiển thị biểu đồ
    plt.show()
def Khong_hop_le() :
    print("Lựa chọn không hợp lệ!")
luachon_dict = { 
    1: Doc_du_lieu ,
    2: Cap_nhat_du_lieu ,
    3: Tao_du_lieu_moi ,
    4: Xoa_du_lieu ,
    5: Tinh_trung_binh ,
    6: Bieu_do ,
    7: Khong_hop_le
}
def menu() :
    while True :
        # In ra menu
        print("menu")
        print("1.Doc_du_lieu")
        print("2.Cap_nhat_du_lieu")
        print("3.Tao_du_lieu_moi")
        print("4.Xoa_du_lieu")
        print("5.Tinh_trung_binh")
        print("6.Bieu_do")
        print("7.Thoat_chuong_trinh")
        chon = input("Mời chọn tính năng:")
        if chon.isdigit() :
            chon = int(chon)
            if chon == 0 :
                break
            else :
                luachon_dict.get(chon, Khong_hop_le)()
        else :
            print("Hãy nhập lại,dữ liệu là Số nhé !")
# Chạy menu
menu()
       

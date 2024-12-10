import pandas as pd 
import matplotlib.pyplot as plt
def Doc_du_lieu() :
    df = pd.read_excel("d:/Drug (1).xlsx",engine='openpyxl')
    # In kết quả đọc dữ liệu
    print(df)
def Cap_nhat_du_lieu() :
    # Khai báo thư viện
    import pandas as pd
    df = pd.read_excel("d:/Drug (1).xlsx",engine="openpyxl")
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
def Tao_data() :
    # Khai báo thư viện
    import pandas as pd
    # mở + đọc file 
    file_path = 'Drug_cleanedcc.xlsx'  #bạn đặt tên file ntn thì sửa lại như vậy để code tìm 
    data = pd.read_excel("d:/Drug (1).xlsx",engine='openpyxl')
    # lọc / tìm kiếm thông tin chứa :"Acute Bacterial Sinusitis"
    condition_to_cut = "Acute Bacterial Sinusitis" # điều kiện
    filtered_rows = data[data['Condition'].str.contains(condition_to_cut, na=False)] # phần tìm kiếm thông tin
    # dữ liệu từ file cũ (tức là các dữ liệu ko liên quan sẽ được giữ nguyên)
    remaining_data = data[data['Condition'].str.contains(condition_to_cut, na=False)]
    # lưu dữ liệu các hàng chứa Acute Bacterial Sinusitis sang file mới
    filtered_file_path = 'Acute_Bacterial_Sinusifalkfhskhfakfhjsflshkfdjdhlkajhfdlsdkjhfkjahlkf.xlsx'          #bạn muốn đổi tên ntn cũng được :))
    filtered_rows.to_excel(filtered_file_path, index=False)             #các thông tin ko liên quan sẽ ko được đổi tên như trên
    # lưu lại các thông tin ko liên quan sang file mới 
    updated_file_path = 'hkfshaflksjhfkjahlsfhskfa.xlsx'         # đặt tên ntn cũng được
    remaining_data.to_excel(updated_file_path, index=False)
    print(f"Filtered rows saved to: {filtered_file_path}")       #trong phần mô tả của code, nó sẽ nói lại các thông tin được lưu ở file nào (có hay ko cũng được)
    print(f"Updated data saved to: {updated_file_path}")
def Xoa_du_lieu() :
    import pandas as pd
    from openpyxl import load_workbook
    # Read the Excel file
    workbook =  load_workbook(filename="d:/Drug (1).xlsx",engine="openpyxl")
    # Chọn sheet làm việc mặc định
    sheet = workbook.active  
    # Read data from sheet to DataFrame
    data = pd.DataFrame(sheet.values)
    df = pd.read_excel("d:/Drug (1).xlsx",engine="openpyxl")  #chỗ "drug (1)" là tên file mình đã tải về, bạn đặt tên file ntn thì ghi lại ở đây như vậy. ".xlsx" là định dạng loại tệp, ở đây là tệp excel.
    # Filter duplicated datas of 4 collums of reviews, efective, ease of use, Satisfaction 
    df = df.drop_duplicates(subset=['Reviews', 'Effective', 'EaseOfUse', 'Satisfaction'])
    # Display DataFrame after deleting duplicated rows - hiển thị số dòng trong file (optional)
    print(df)
    # Save the excel file - phần đặt tên file , đặt gì cũng được
    df.to_excel("drug sus.xlsx", index=False)
def Bieu_do_tron() :
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
def Bieu_do_cot() :
    # Khai báo thư viện
    import pandas as pd
    import matplotlib.pyplot as plt
    # Đọc file Excel
    data=pd.read_excel("d:/Drug (1).xlsx",engine="openpyxl")
    # Lấy cột dữ liệu Condition và chuyển thành kiểu danh sách với điều kiện chỉ lấy 1 dữ liệu duy nhất nếu bị trùng 
    conditions=data['Condition'].unique().tolist()
    # Tạo danh sách dùng để chứa số lượng thuốc của mỗi loại bệnh
    lst_drug=[]
    # Duyệt qua từng dữ liệu của danh sách Conditions ( Đi qua từng loại bệnh trong danh sách)
    for condition in conditions:
        # Lọc dữ liệu lấy những hàng với điều kiện giống nhau về tên bệnh
        data_new=data.loc[data['Condition']==condition] 
        # Lấy cột dữ liệu Drug trong data vừa lọc ở trên và chuyển thành kiểu danh sách với điều kiện chỉ lấy 1 dữ liệu duy nhất nếu bị trùng 
        drugs=data_new['Drug'].unique().tolist() 
        # Đếm số lượng thuốc dùng để chữa bệnh
        count_drug=len(drugs) 
        # Thêm tổng số thuốc dùng để chữa trị bệnh vào danh sách
        lst_drug.append(count_drug)
    # In ra danh sách cột Conditions và danh sách số lượng thuốc
    print(conditions)
    print(lst_drug)
    # Vẽ biểu đồ cột với trục ngang là tên các bệnh và trục dọc là số lượng thuốc điều trị bệnh đó
    plt.bar(conditions,lst_drug,color='green') 
    plt.xticks(rotation=30,ha="right") # Xoay tên của các cột 45 độ theo chiều kim đồng hồ và căn chỉnh các nhãn về phía bên phải 
    plt.yticks(range(0,100,5)) # Hiển thị giá trị cột y từ 0 đến 95 và mỗi đơn vị liên tiếp cách nhau 5 
    plt.xlabel('Triệu chứng bệnh') # Đặt tên trục x
    plt.ylabel('Số lượng thuốc') # đặt tên trục y
    plt.title('Tổng số lượng thuốc điều trị của mỗi bệnh') # Đặt tên biểu đồ
    plt.subplots_adjust(bottom=0.26) # Dịch chuyển khung biểu đồ lên trên
    plt.show() # Hiển thị biểu đồ
def Khong_hop_le() :
    print("Lựa chọn không hợp lệ!")
luachon_dict = { 
    1: Doc_du_lieu ,
    2: Cap_nhat_du_lieu ,
    3: Tao_du_lieu_moi ,
    4: Tao_data ,
    5: Xoa_du_lieu ,
    6: Bieu_do_tron ,
    7: Bieu_do_cot ,
    8: Khong_hop_le
}
def menu() :
    while True :
        # In ra menu
        print("menu")
        print("1.Doc_du_lieu")
        print("2.Cap_nhat_du_lieu")
        print("3.Tao_du_lieu_moi")
        print("4.Tao_data")
        print("5.Xoa_du_lieu")
        print("6.Bieu_do_tron")
        print("7.Bieu_do_cot")
        print("8.Thoat_chuong_trinh")
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
       

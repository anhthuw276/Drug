def Doc_du_lieu():
    chon1=input('Bạn chọn dữ liệu gốc hay đã chỉnh sửa(g/c):')
    if chon1=='g':
        df = pd.read_excel("Drug.xlsx",engine='openpyxl')
    # In kết quả đọc dữ liệu
        print(df)
    else:
        file_path = "Drug_1.xlsx"
        try: # sử dụng try - except để bắt lỗi
            df = pd.read_excel(file_path, engine='openpyxl') # Thử đọc tệp dữ liệu
            print("Đã đọc tệp thành công!")
            print(df.head())
        except FileNotFoundError: # nếu tệp không tồn tại thì in câu tệp chưa tồn tại 
            print(f"Tệp {file_path} chưa tồn tại.")

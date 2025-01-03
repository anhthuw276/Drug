
import pandas as pd

# Đọc file Excel
file = 'dataset.xlsx'
data = pd.read_excel(file)
print("Dữ liệu hiện tại:\n", data)

# Yêu cầu người dùng nhập dữ liệu mới cho từng cột
new_data = {}
for column in data.columns:
    new_data[column] = input(f"Nhập dữ liệu cho cột '{column}': ")

# Chuyển đổi dữ liệu mới thành DataFrame
new_data_df = pd.DataFrame([new_data])

# Thêm dữ liệu mới vào DataFrame ban đầu
df = pd.concat([data, new_data_df], ignore_index=True)
print("Dữ liệu sau khi thêm mới:\n", df)

# Lưu DataFrame đã chỉnh sửa vào tệp Excel
df.to_excel(file, index=False)
print(f"Dữ liệu đã được lưu vào file: {file}")

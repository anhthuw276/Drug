import pandas as pd

# mở + đọc file 
file_path = 'Drug_cleanedcc.xlsx'  #bạn đặt tên file ntn thì sửa lại như vậy để code tìm 
data = pd.read_excel(file_path)

# lọc / tìm kiếm thông tin chứa :"Acute Bacterial Sinusitis"
condition_to_cut = "Acute Bacterial Sinusitis" # điều kiện
filtered_rows = data[data['Condition'].str.contains(condition_to_cut, na=False)] # phần tìm kiếm thông tin

# dữ liệu từ file cũ (tức là các dữ liệu ko liên quan sẽ được giữ nguyên)
remaining_data = data[~data['Condition'].str.contains(condition_to_cut, na=False)]

# lưu dữ liệu các hàng chứa Acute Bacterial Sinusitis sang file mới
filtered_file_path = 'Acute_Bacterial_Sinusifalkfhskhfakfhjsflshkfdjdhlkajhfdlsdkjhfkjahlkf.xlsx'          #bạn muốn đổi tên ntn cũng được :))
filtered_rows.to_excel(filtered_file_path, index=False)             #các thông tin ko liên quan sẽ ko được đổi tên như trên

# lưu lại các thông tin ko liên quan sang file mới 
updated_file_path = 'hkfshaflksjhfkjahlsfhskfa.xlsx'         # đặt tên ntn cũng được
remaining_data.to_excel(updated_file_path, index=False)

print(f"Filtered rows saved to: {filtered_file_path}")       #trong phần mô tả của code, nó sẽ nói lại các thông tin được lưu ở file nào (có hay ko cũng được)
print(f"Updated data saved to: {updated_file_path}")

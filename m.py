import matplotlib.pyplot as plt
import pandas as pd #khai báo thư viện 
df=pd.read_excel('d:\\Drug (4).xlsx',sheet_name=0) #đọc file excel, sheet name cho biết là sheet đầu tiên của file 
a=df['Reviews'].tolist() # a là danh sách giá trị từ cột reviews
b=df['Effective'].tolist() # b là danh sách giá trị từ cột effective 
fig=plt.figure() # tạo không gian biểu đồ để thêm các trục 
ax=fig.add_axes([0,0,1,1]) # thêm trục vào figure (0,0) góc dưới trục là góc toạ độ của figure (1,1) trục kéo dài đến điểm (1,1) chiếm toàn bộ diện tích figure 
ax.axis('equal') # đảm bảo tỉ lệ 2 trục bằng nhau 
explode=(0,0.2,0.4,0.6,0.8,1) # tưng pie được văng ra tính từ gốc trung tâm 
ax.pie(a,explode=explode,labels=b,autopct='%1.2f%%') # a:giá trị của từng pie , explode: chỉ ra khoảng cách của từng slice , gán nhãn từ cột effective cho mỗi pie , autopct : hiển thị phần trăm trong tuừng pie với 2 chữ số thập phân 
plt.show()
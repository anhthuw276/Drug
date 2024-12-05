import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('d:\\Drug (4).xlsx',sheet_name=0)
a=df['Reviews'].tolist()
b=df['Effective'].tolist()
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.axis('equal')
explode=(0,0.2,0.4,0.6,0.8,1)
ax.pie(a,explode=explode,labels=b,autopct='%1.2f%%')
plt.show()
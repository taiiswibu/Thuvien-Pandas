import pandas as pd
f1 = pd.read_excel(r'C:\codebaitappython\python-pandas\testpandas.xlsx')
#------------------------------------------------------------
#print(f1)# đọc cả tiệp
#print(f1.shape)# điếm số hàng số cột
# -----------------------------------------------------------
#c2 = pd.DataFrame(f1,columns=['STT','Họ Tên ',' sử '])
#print(c2)
#-------------------------------------------------------
#thêm mới một cột rỗng
#f1['DTB'] =''
#f1['tong ket']= ' '
f1['DTB']=(f1['Toán']+f1['Lý']+f1['Hóa']+f1['Văn']+f1['Sử']+f1['Địa'])/6 
#----------------------------------------------------------------------------
print(f1)

# lưu ra file mới
#f1.to_excel(r'C:\codebaitappython\python-pandas\testpandas_edit.xlsx')
#---------------------------------------------------------------------
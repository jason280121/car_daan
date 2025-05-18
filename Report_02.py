import pandas as pd
import time

# # nrows = 202505035

file_name = input("請輸入CSV檔名:")

# datas = pd.read_csv("0516.csv", usecols=['編號', '車號', '進廠日期', '進廠時間', '出廠日期', '出廠時間',
#                                          '客戶', '品名', '料號', '重量', '總重'], encoding="utf-8")

datas = pd.read_csv(file_name, usecols=['編號', '車號', '進廠日期', '進廠時間', '出廠日期', '出廠時間',
                                        '客戶', '品名', '料號', '重量', '總重'], encoding="utf-8")


# datas = pd.read_csv("0516.csv")


# 刪除第8個欄位開始到最後，切片
# data = datas.astype('int16').st

# 新增欄位columns
# datas["淨重"] = ""  # 新增 "new_column" 欄位

# 新增欄位columns
# date = 20250516

date = int(input("請輸入計算的日期:"))


company = list(datas['客戶'])

datas.insert(len(datas.columns), "淨重", "")  # 在最後面新增 "new_column" 欄位

result = datas[datas["進廠日期"] == date]

result['淨重'] = list(result["總重"]-result["重量"])

eight1 = list(result["客戶"].str.contains("八德區垃圾車"))
eight2 = list(result["客戶"].str.contains("八德區清潔隊"))

# 八德區中隊 + 八德區清潔隊
other1 = result[eight1]["淨重"].sum()
other2 = result[eight2]["淨重"].sum()

sum_all = other1 + other2
print(f'八德區垃圾車+八德區清潔隊總計:{round(sum_all/1000, 3)}噸')


print('---------------------------------------------------------------------')
result['品名'] = result['品名'].fillna(value='沒有組別')

market = list(result["品名"].str.contains("市場車"))
community = list(result["品名"].str.contains("社區定點"))
black = list(result["品名"].str.contains("黑包組"))


# 夜班
other1 = other1 - 2210
print(f'(夜班)八德區垃圾車:{round(other1/1000, 3)}噸')

# 市場車
m3 = result[market]["淨重"].sum()
print(f'(市場車)過磅重量:{round(m3/1000, 3)}噸')

# 社區定點
co = result[community]["淨重"].sum()
print(f'(社區定點)過磅重量:{round(co/1000, 3)}噸')

# 黑包組
bl = result[black]["淨重"].sum()
print(f'(黑包組)過磅重量:{round(bl/1000, 3)}噸')


# 日班
other2 = other2+2210
# 日班過磅all重量
print('----------------------------日班(市場組+社區定點+黑包組)-----------------------------------------')
print(f'(日班)過磅重量:{round(other2/1000, 3)}噸')




print('----------------------------驗算-----------------------------------------')

# 驗算
# 夜班+市場組+社區定點+黑包組
total_1 = other1 + m3 + co + bl
print(f'夜班+市場組+社區定點+黑包組:{round(total_1/1000, 3)}噸')

total_2 = m3 + co + bl
print(f'市場組+社區定點+黑包組:{round(total_2/1000, 3)}噸')

total_3 = (other2 - (m3 + co + bl))/2
print(f'大型傢俱:{round(total_3/1000, 3)}噸')

print('----------------------------實際日班進廠重量-----------------------------------')
total_4 = other2 - total_2
print(f'實際日班進廠重量:{round(total_4/1000, 3)}噸')

print('----------------------------日班+夜班核算總量-----------------------------------')
total_5 = total_4 + total_1
print(f'日班+夜班:{round(total_5/1000, 3)}噸')

# 查詢表格內None 數量
# print(result.isnull().sum())

# 查詢表格內None
# print(result.info)

# result.to_excel('data_x.xlsx')
# result.to_excel('data8.xlsx')

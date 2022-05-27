'''
Created on 2022. 5. 26.
'''
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

pd.set_option('display.max_columns', None)
GangNam = pd.read_csv('../datas/TotalData_Gangnam.csv')
print(GangNam.head(5))
# 표준화
scaler1 = StandardScaler()
GN1 = scaler1.fit_transform(GangNam)
print('StandardScaler : ', GN1[:10])
# 정규화
scaler2 = MinMaxScaler(feature_range=(0,1))
GN2 = scaler2.fit_transform(GN1)
np.set_printoptions(precision=6, suppress=True)
print('MinMaxScaler : ', GN2[:10])


# data = []
#
# for i in list(range(2011, 2022, 1)):
#     for j in list(range(1, 13, 1)):
#



df = pd.DataFrame(GN2, index = [201101, 201102, 201103, 201104, 201105, 201106, 201107, 201108, 201109, 201110, 201111, 201112, 201201, 201202, 201203, 201204, 201205, 201206, 201207, 201208, 201209, 201210, 201211, 201212, 201301, 201302, 201303, 201304, 201305, 201306, 201307, 201308, 201309, 201310, 201311, 201312, 201401, 201402, 201403, 201404, 201405, 201406, 201407, 201408, 201409, 201410, 201411, 201412, 201501, 201502, 201503, 201504, 201505, 201506, 201507, 201508, 201509, 201510, 201511, 201512, 201601, 201602, 201603, 201604, 201605, 201606, 201607, 201608, 201609, 201610, 201611, 201612, 201701, 201702, 201703, 201704, 201705, 201706, 201707, 201708, 201709, 201710, 201711, 201712, 201801, 201802, 201803, 201804, 201805, 201806, 201807, 201808, 201809, 201810, 201811, 201812, 201901, 201902, 201903, 201904, 201905, 201906, 201907, 201908, 201909, 201910, 201911, 201912, 202001, 202002, 202003, 202004, 202005, 202006, 202007, 202008, 202009, 202010, 202011, 202012, 202101, 202102, 202103, 202104, 202105, 202106, 202107, 202108, 202109, 202110, 202111, 202112], 
                  columns=['ymd','interest rating', 'm2(%)','m2(abs)','cpi(%)','cpi(abs)','expected_inflation','supply','tax_jongso','tax_chuideuk','price','trading','marry','popul'])
print(df)
print(df.corr())
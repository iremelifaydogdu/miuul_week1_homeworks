
##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

df.head()

num_cols= ["NUM_" + col.upper() for col in df.columns if df[col].dtype != "O" ]

print(num_cols)

#????? Kategorik ama aslında nümerik olanları bulmaya çalıştım ama bulamadım???????
#cat_but_num_cols=[col for col in df.columns [df[col].nunique()>5 and df[col].dtypes in ["bool", "object", "category"]]]
#print(cat_but_num_cols)

#başka çözüm
liste = [("NUM_"+i).upper() if str(df[i].dtypes) in ["float64"] else i.upper() for i in df.columns]
print(liste)
#başka çözüm
["NUM_" + i.upper() if  df[i].dtype != "O" else i.upper() for i in df.columns ]
#başka çözüm
num_cols = [col for col in df.columns if df[col].dtype != "O"]
#başka çözüm
numdf = ['NUM' + col.upper() if df[col].dtype == "f8" else col.upper() for col in df.columns]

# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("car_crashes")
df.columns
df.info()
[col + "_FLAG" for col in df.columns if "NO" not in col]


#başka çözüm
[(i+"_FLAG").upper() if "no" not in i else i.upper() for i in df.columns]

#başka çözüm
[i.upper()+"_FLAG" if "no" not in i else i.upper() for i in df.columns]

#başka çözüm
new_columns = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
print(new_columns)
#başka çözüm
[col.upper() + '_FLAG' if "no" not in col else col.upper() for col in df2.columns]


# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("car_crashes")

df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]

new_col=[]
new_col = [col for col in df.columns if col not in og_list]
new_df = df[new_col]
print(new_df)

#başka çözüm

og_list = ["abbrev", "no_previous"]
new_cols =[]

[new_cols.append(i) for i in df.columns if i not in og_list]
new_df=df[['total', 'speeding', 'alcohol', 'not_distracted', 'ins_premium', 'ins_losses']]


#başka çözüm
new_cols = []

[new_cols.append(eleman) for eleman in df3.columns if eleman not in og_list]

new_df = df[new_cols]




# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#








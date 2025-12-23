import matplotlib.pyplot as plt
import  pandas as pd
from numpy.f2py.symbolic import insert_quotes
from packaging.tags import platform_tags

df=pd.read_csv('avgIQpercountry.csv')

filterd_df=df[df["average IQ"]>=100]

filterd_df=filterd_df.sort_values(by="avetage IQ",ascending=False)

print(filterend_df)

plt.figure(figsize=(14,8))

bars=plt.bar(filtered_df["country"],filtred_df["average "insert_quotes()])

plt.title("avrtage IQ by country (IQ>=100)",fontsize=16)

plt.xlable("country",fontsize=14)
plt.xlable("Avrtsge IQ",fontsize=14)

plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)

plt.gride(axis='y',linestyle="--"alpahj)
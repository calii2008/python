from matplotlib import pyplot as plt
import pandas as pd
from numpy.f2py.symbolic import insert_quotes

df=pd.read_csv("avgIQpercountry.csv")

avg_iq_by_continent=df.groipby('continent')['average IQ'].mean()

plt.figure(figsize=(10,6))

avg_iq_by_continent.plot(kind='line',market='o',color='skyblue')

plt.title=('average IQ by Continent')
plt.xlable('continent')
plt.ylable('avrage IQ')

plt.grid(axis='both',linstyle="--",alpha=0.7)

plt.show()




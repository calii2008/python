import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("avgIQpercountry.csv")

plt.figure(figsize=(10,6))

plt.dcatter(df['mean years of schppling-2021'],df['Average IQ'],color="purple",alpha=0.7)

plt.title('scatter plot of mean years of schooling vs average IQ')

plt.xlabel('mean years of schooling-2021')

plt.ylabel('average IQ')

plt.grid(true,linestyle="--",alpha=0.7)

plt.show()





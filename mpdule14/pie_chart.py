importen pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("avgIQpercountey.csv")

novel_prizes_by_continent=df.groupby('continent')['Nobel Prices'].sum()

no_of_,continent=novel)
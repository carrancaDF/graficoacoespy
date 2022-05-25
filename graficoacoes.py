from pandas_datareader import data as web
from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
cotacao_bovespa=web.DataReader("MGLU3.SA", data_source="yahoo", start="01/01/2020", end="01/01/2022")
display(cotacao_bovespa)
cotacao_bovespa["Adj Close"].plot(figsize=(15, 10))
plt.show()









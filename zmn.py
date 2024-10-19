import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import tkinter as tk
import datetime



syf=tk.Tk()
syf.title("mrb")
syf.geometry("500x500")
"""  """

hısseler=['AAPL', 'MSFT', 'GOOGL','TSLA','AMZN', 'NFLX', 'NVDA', 'PYPL', 'BABA' ]


def grafık(hname):
    
    
     s=datetime.datetime.now()
     e=datetime.datetime(s.year , 1,1)       
     ındır=yf.download(hname, start=e , end=s)    
     

     plt.plot(ındır['Close'], label=f"{hname}close price" ,color="blue")
     plt.grid(True)
     plt.show()   
     
for hhıse in hısseler:
     ındr=yf.download(hhıse ,period="1d" )
     sfh=ındr['Close'].iloc[-1]
    
     tus=tk.Button(syf ,text=f"hisse:{hhıse}: {sfh} " , command=lambda h=hhıse: grafık(h))
     tus.pack()

syf.mainloop()

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

hısseler=['AAPL', 'MSFT', 'GOOGL','TSLA','AMZN', 'NFLX', 'NVDA', 'PYPL', 'BABA','A1CAP.IS', 'ACSEL.IS', 'ADEL.IS', 'ADESE.IS', 'ADGYO.IS', 'AEFES.IS', ]



def grafık(hname):
     s=datetime.datetime.now()
     e=datetime.datetime(s.year , 1,1)       
     ındır=yf.download(hname, start=e , end=s)

     ındır['Daily Return']= ındır['Adj Close'].pct_change()

     """ risksiz getiri oranı """
     rıskfr= 0.02 /252

     """ ortalama günlük getiri """
     mean_retur=ındır['Daily Return'].mean()

     """ günlük getirinin standart sapması """
     std_return=ındır['Daily Return'].std()

     """ günlük sharp oranı """
     daıly_return=(mean_retur - rıskfr) / std_return

     """ yıllık sharp oranı """
     years_return=daıly_return * np.sqrt(252)

     




     ylbs=ındır['Close'].iloc[0]  # ilk kapanış fiyatını alır.
     gncl=ındır['Close'].iloc[-1] # Son kapanış fiyatını alır.
     yzd=((gncl - ylbs) / ylbs) * 100  
     gor=tk.Label(syf, text=f"yüzdelik değişim:{yzd:.2f}%  , sharp oranı:{years_return} " , font=('Helvetica',12))
     gor.pack()
     
     plt.plot(ındır['Close'], label=f"{hname}close price" ,color="blue")
     plt.grid(True)
     plt.legend()
     plt.show()   

for hhıse in hısseler :
     ındr=yf.download(hhıse ,period="1d" )
     sfh=ındr['Close'].iloc[-1] 
     tus=tk.Button(syf ,text=f"hisse:{hhıse}: {sfh:.2f} " , command=lambda h=hhıse: grafık(h))
     tus.pack()

     



syf.mainloop()


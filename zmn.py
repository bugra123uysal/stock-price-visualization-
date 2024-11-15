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

hısseler=['AAPL', 'MSFT', 'GOOGL','TSLA','AMZN', 'NFLX', 'NVDA', 'PYPL', 'BABA' ]

sto =[ 'A1CAP.IS', 'ACSEL.IS', 'ADEL.IS', 'ADESE.IS', 'ADGYO.IS', 'AEFES.IS', ]

def grafık(hname):
     s=datetime.datetime.now()
     e=datetime.datetime(s.year , 1,1)       
     ındır=yf.download(hname, start=e , end=s) 


     ylbs=ındır['Close'].iloc[0]
     gncl=ındır['Close'].iloc[-1] 
     yzd=((gncl - ylbs) / ylbs) * 100  
     gor=tk.Label(syf, text=f"yüzdelik değişim:{yzd:.2f}%" , font=('Helvetica',12))
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

   
def grafıctwopage(twopack):
     try:

        n=datetime.datetime.now()
        y=datetime.datetime(n.year , 1,1)
   
        alst=yf.download(twopack , start=y , end=n)
        ba=alst['Close'].iloc[0]
        yson=alst['Close'].iloc[-1]
   
        """ yüzde """
       
   
        yyıl=((yson - ba )/ ba)* 100
   
        yzdgorr=tk.Label(second, text=f"hisse yüzdeleri {yyıl:.2f}%", font=('Helvetica',12))
        yzdgorr.pack()

        plt.plot(alst['Close'], color='blue'   )
        plt.grid(True)
        plt.show()  
     except Exception as e:
          print(f"hata: {e}")

""" ikinci sayfa  """
def open_second():
     global second

     second=tk.Toplevel(syf)
     second.title("yıllık yüzde değişimleri")
     second.geometry("500x500")

     for yy in sto:
        üü = yf.download(yy, period="1d")
        oa = üü['Close'].iloc[-1]
        ıstbrs = tk.Button(second, text=f"Hisse: {yy} - Fiyat: {oa:.2f}", command=lambda ıst=yy: grafıctwopage(ıst))
        ıstbrs.pack()

     
     """ ıkıncı sayfaya tr borsası hisselerini koymak  """

     """ ikinci sayfadan birinciye geçmek """
     ıkıbır=tk.Button(second, text="abd hısse senetlerı", command=second.destroy)
     ıkıbır.pack()
    
""" birden ıkıncı sayfaya geçmek için button """
yuzdelersayfası=tk.Button(syf,text="Türkiye barsası", command=open_second)
yuzdelersayfası.pack(pady=20)
syf.mainloop()

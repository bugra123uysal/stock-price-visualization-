import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import tkinter as tk
import datetime
import time

syf=tk.Tk()
syf.title("mrb")
syf.geometry("500x500")
syf.mainloop()
hısseler=['AAPL', 'MSFT', 'GOOGL', 'AMZN',  'TSLA', 'NFLX', 'NVDA', 'PYPL', 'BABA']
""" şimdi """


for i in hısseler:
    print(i)
    s=datetime.datetime.now()
    e=datetime.datetime(s.year , 1,1)

    ındır=yf.download(i, start=e , end=s)


    plt.plot(ındır['Close'], label=f"{i}close price" ,color="blue")
    plt.grid(True)
    plt.show()




    

 


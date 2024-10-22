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
     ylbs=ındr['Close'].iloc[0]
     gncl=ındr['Close'].iloc[-1]   
     
     plt.plot(ındır['Close'], label=f"{hname}close price" ,color="blue")
     plt.grid(True)
     plt.show()   
     
for hhıse in hısseler:
     ındr=yf.download(hhıse ,period="1d" )
     sfh=ındr['Close'].iloc[-1]
    
     tus=tk.Button(syf ,text=f"hisse:{hhıse}: {sfh} " , command=lambda h=hhıse: grafık(h))
     tus.pack()
 
""" ikinci sayfa  """
def open_second():

     second=tk.Toplevel(syf)
     second.title("yıllık yüzde değişimleri")
     second.geometry("500x500")
     

     yy=tk.Label(second,text="ıkıncı desın")
     yy.pack()



     sto =[
           'A1CAP.IS', 'ACSEL.IS', 'ADEL.IS', 'ADESE.IS', 'ADGYO.IS', 'AEFES.IS', 
    'AFYON.IS', 'AGESA.IS', 'AGHOL.IS', 'AGROT.IS', 'AGYO.IS', 'AHGAZ.IS', 
    'AHSGY.IS', 'AKBNK.IS', 'AKCNS.IS', 'AKENR.IS', 'AKFGY.IS', 'AKFYE.IS', 
    'AKGRT.IS', 'AKMGY.IS', 'AKSA.IS', 'AKSEN.IS', 'AKSGY.IS', 'AKSUE.IS', 
    'AKYHO.IS', 'ALARK.IS', 'ALBRK.IS', 'ALCAR.IS', 'ALCTL.IS', 'ALFAS.IS', 
    'ALGYO.IS', 'ALKA.IS', 'ALKIM.IS', 'ALKLC.IS', 'ALMAD.IS', 'ALTIN.IS', 
    'ALTNY.IS', 'ALVES.IS', 'ANELE.IS', 'ANGEN.IS', 'ANHYT.IS', 'ANSGR.IS', 
    'ARASE.IS', 'ARCLK.IS', 'ARDYZ.IS', 'ARENA.IS', 'ARSAN.IS', 'ARTMS.IS', 
    'ARZUM.IS', 'ASELS.IS', 'ASGYO.IS', 'ASTOR.IS', 'ASUZU.IS', 'ATAGY.IS', 
    'ATAKP.IS', 'ATATP.IS', 'ATEKS.IS', 'ATLAS.IS', 'ATSYH.IS', 'AVGYO.IS', 
    'AVHOL.IS', 'AVOD.IS', 'AVPGY.IS', 'AVTUR.IS', 'AYCES.IS', 'AYDEM.IS', 
    'AYEN.IS', 'AYES.IS', 'AYGAZ.IS', 'AZTEK.IS', 'BAGFS.IS', 'BAHKM.IS', 
    'BAKAB.IS', 'BALAT.IS', 'BANVT.IS', 'BARMA.IS', 'BASCM.IS', 'BASGZ.IS', 
    'BAYRK.IS', 'BEGYO.IS', 'BERA.IS', 'BEYAZ.IS', 'BFREN.IS', 'BIENY.IS', 
    'BIGCH.IS', 'BIMAS.IS', 'BINBN.IS', 'BINHO.IS', 'BIOEN.IS', 'BIZIM.IS', 
    'BJKAS.IS', 'BLCYT.IS', 'BMSCH.IS', 'BMSTL.IS', 'BNTAS.IS', 'BOBET.IS', 
    'BORLS.IS', 'BORSK.IS', 'BOSSA.IS', 'BRISA.IS', 'BRKO.IS', 'BRKSN.IS', 
    'BRKVY.IS', 'BRLSM.IS', 'BRMEN.IS', 'BRSAN.IS', 'BRYAT.IS', 'BSOKE.IS', 
    'BTCIM.IS', 'BUCIM.IS', 'BURCE.IS', 'BURVA.IS', 'BVSAN.IS', 'BYDNR.IS', 
    'CANTE.IS', 'CASA.IS', 'CATES.IS', 'CCOLA.IS', 'CELHA.IS', 'CEMAS.IS', 
    'CEMTS.IS', 'CEMZY.IS', 'CEOEM.IS', 'CIMSA.IS', 'CLEBI.IS', 'CMBTN.IS', 
    'CMENT.IS', 'CONSE.IS', 'COSMO.IS', 'CRDFA.IS', 'CRFSA.IS', 'CUSAN.IS', 
    'CVKMD.IS', 'CWENE.IS', 'DAGHL.IS', 'DAGI.IS', 'DAPGM.IS', 'DARDL.IS', 
    'DCTTR.IS', 'DENGE.IS', 'DERHL.IS', 'DERIM.IS', 'DESA.IS', 'DESPC.IS', 
    'DEVA.IS', 'DGATE.IS', 'DGGYO.IS', 'DGNMO.IS', 'DIRIT.IS', 'DITAS.IS', 
    'DMRGD.IS', 'DMSAS.IS', 'DNISI.IS', 'DOAS.IS', 'DOBUR.IS', 'DOCO.IS', 
    'DOFER.IS', 'DOGUB.IS', 'DOHOL.IS', 'DOKTA.IS', 'DURDO.IS', 'DURKN.IS', 
    'DYOBY.IS', 'DZGYO.IS', 'EBEBK.IS', 'ECILC.IS', 'ECZYT.IS', 'EDATA.IS', 
    'EDIP.IS', 'EFORC.IS', 'EGEEN.IS', 'EGEPO.IS', 'EGGUB.IS', 'EGPRO.IS', 
    'EGSER.IS', 'EKGYO.IS', 'EKIZ.IS', 'EKOS.IS', 'EKSUN.IS', 'ELITE.IS', 
    'EMKEL.IS', 'EMNIS.IS', 'ENERY.IS', 'ENJSA.IS', 'ENKAI.IS', 'ENSRI.IS', 
    'ENTRA.IS', 'EPLAS.IS', 'ERBOS.IS', 'ERCB.IS', 'EREGL.IS', 'ERSU.IS', 
    'ESCAR.IS', 'ESCOM.IS', 'ESEN.IS', 'ETILR.IS', 'ETYAT.IS', 'EUHOL.IS', 
    'EUKYO.IS', 'EUPWR.IS', 'EUREN.IS', 'EUYO.IS', 'EYGYO.IS', 'FADE.IS', 
    'FENER.IS', 'FLAP.IS', 'FMIZP.IS', 'FONET.IS', 'FORMT.IS', 'FORTE.IS', 
    'FRIGO.IS', 'FROTO.IS', 'FZLGY.IS', 'GARAN.IS', 'GARFA.IS', 'GEDIK.IS', 
    'GEDZA.IS', 'GENIL.IS', 'GENTS.IS', 'GEREL.IS', 'GESAN.IS', 'GIPTA.IS', 
    'GLBMD.IS', 'GLCVY.IS', 'GLRYH.IS', 'GLYHO.IS', 'GMTAS.IS', 'GOKNR.IS', 
    'GOLTS.IS', 'GOODY.IS', 'GOZDE.IS', 'GRNYO.IS', 'GRSEL.IS', 'GRTHO.IS', 
    'GSDDE.IS', 'GSDHO.IS', 'GSRAY.IS', 'GUBRF.IS', 'GUNDG.IS', 'GWIND.IS', 
    'GZNMI.IS', 'HALKB.IS', 'HATEK.IS', 'HATSN.IS', 'HDFGS.IS', 'HEDEF.IS', 
    'HEKTS.IS', 'HKTM.IS', 'HLGYO.IS', 'HOROZ.IS', 'HRKET.IS', 'HTTBT.IS', 
    'HUBVC.IS', 'HUNER.IS', 'HURGZ.IS', 'ICBCT.IS', 'ICUGS.IS', 'IDGYO.IS', 
    'IEYHO.IS', 'IHAAS.IS', 'IHEVA.IS', 'IHGZT.IS', 'IHLAS.IS', 'IHLGM.IS', 
    'IHYAY.IS', 'IMASM.IS', 'INDES.IS', 'INFO.IS', 'INGRM.IS', 'INTEK.IS', 
    'INTEM.IS', 'INVEO.IS', 'INVES.IS', 'IPEKE.IS', 'ISATR.IS', 'ISBIR.IS', 
    'ISBTR.IS', 'ISCTR.IS', 'ISDMR.IS', 'ISFIN.IS', 'ISGSY.IS', 'ISGYO.IS', 
    'ISKPL.IS', 'ISKUR.IS', 'ISMEN.IS', 'ISSEN.IS', 'ISYAT.IS', 'IZENR.IS', 
    'IZFAS.IS', 'IZINV.IS'
         
         ]



     for yy in sto:
          üü=yf.download(yy,period="1d")
          oa=üü['Close'].iloc[-1]
          ıstbrs=tk.Button(second, text=f"hisse:{yy}: {oa}", command=lambda ıst=yy: grafıctwopage(ıst)) 
          ıstbrs.pack()
     """ ıkıncı sayfaya tr borsası hisselerini koymak  """

     """ ikinci sayfadan birinciye geçmek """
     ıkıbır=tk.Button(second, text="abd hısse senetlerı", command=second.destroy)
     ıkıbır.pack()
   
def grafıctwopage(twopack):

     n=datetime.datetime.now()
     y=datetime.datetime(n.year , 1,1)

     alst=yf.download(twopack , start=y , end=n)
     ba=alst['Close'].iloc[0]
     gncl=alst['Close'].iloc[-1]

     plt.plot(alst['Close'], color='blue'   )
     plt.grid(True)
     plt.show()    
    
""" birden ıkıncı sayfaya geçmek için button """
yuzdelersayfası=tk.Button(syf,text="Türkiye barsası", command=open_second)
yuzdelersayfası.pack(pady=20)
syf.mainloop()

import os
import zipfile
import pandas as pd
import sqlite3


"""
veri isimli bir klasör oluşturun
zip dosyasını veri klasörüne çıkartın
zip dosyası içindeki csv dosyalarının tüm içeriğinin tek bir csv dosyasında birleştirin
volume olmasın
bu kayıtların tamamını sqlite veritabanına bir tablo oluştururarak yükleyin
kullanıcının belirlediği paritenin 
kullanıcının belirlediği aralığın 
kullanıcının belirlediği değerin
grafiğini çizdirin(veriler salite tan çekilecek)
"""

if not os.path.exists("veri"):
     os.mkdir('veri')
     arsiv = "C:\Users\kaanb\OneDrive\Masaüstü\Python-Programlama\Python-Programlama\pariteler_cikti_1hour_2022_2022.zip"
     arsiv.extractall("veri/") 

tüm_dosyalar = os.listdir("veri")
pandas_csv_listesi =[]
for csv_dosya in tüm_dosyalar:
    veri = pd.read_csv("veri/"+ csv_dosya)
    del veri["volume"]
    pandas_csv_listesi.append(veri)

birlesmis_csv_ler = pd.concat(pandas_csv_listesi)
birlesmis_csv_ler.to_csv('hepsi.csv', index=False)

bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor("CREATE TABLE IF NOT EXIST parite("
                     +id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     +otime TEXT, open FLOAT, "
                     +"high FLOAT, low FLOAT, close FLOAT);")

  








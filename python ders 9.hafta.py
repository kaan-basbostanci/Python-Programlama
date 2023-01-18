import sqlite3
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/merhaba")
def merhaba():
    return "<p>Merhaba!</p>"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=22222)








    app = Flask(__name__)

@app.route("/getir")
def getir():
    bag = sqlite3.connect("kripto.vt")
    cursor = bag.cursor()
    sorgu = "SELECT * FROM parite WHERE " \
            "(otime BETWEEN '2022-02-03' " \
            "AND '2022-02-04') "\
            "AND parite='AVAXUSDT'"
    cursor.execute(sorgu)
    sonuc = cursor.fetchall()
    bag.close()
    return sonuc

@app.route("/saglam_getir/<parite>/<tarih1>/<tarih2>")
def saglam_getir(parite, tarih1, tarih2):
    bag = sqlite3.connect("kripto.vt")
    cursor = bag.cursor()
    sorgu = "SELECT * FROM parite WHERE " \
            "(otime BETWEEN '"+tarih1+"' " \
            "AND '"+tarih2+"') "\
            "AND parite='"+parite+"'"
    cursor.execute(sorgu)
    sonuc = cursor.fetchall()
    bag.close()
    return json.dumps(sonuc)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=22222)





from flask import Flask, render_template
import getData

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', imagecloud=getData.listImagescloud, nbval=len(getData.listcloud), cloud=getData.listcloud, pres=getData.listprecipitation , temperatures=getData.listetemperature, winds=getData.listewind, Lyouma=getData.Lyouma)






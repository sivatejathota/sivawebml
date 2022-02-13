
from flask import Flask,render_template,request
import joblib
import numpy as np
import pyttsx3
from PIL import Image
import cv2


app=Flask(__name__,template_folder="temp",static_url_path="/static")

@app.route("/")
def index():
    return render_template("index.html",**locals())


@app.route('/predict',methods=['POST','GET'])

def predict():

    spl=float(request.form['spl'])
    spw=float(request.form['spw'])
    ptl=float(request.form['ptl'])
    ptw=float(request.form['ptw'])
    model=joblib.load("machine")
    result=model.predict([[spl,spw,ptl,ptw]])[0]
    text_speech=pyttsx3.init()
    
    if(result==0):
        data1="setosa"
    elif(result==1):
        data1="versicolor"
    else:
        data1="virginica"
    text_speech=pyttsx3.init()
    text_speech.setProperty("rate",120)
    text_speech.setProperty("volume",5)
    voices=text_speech.getProperty("voices")
    text_speech.setProperty('voice','com.apple.speech.synthesis.voice.samantha')
    text_speech.say(data1)
    text_speech.runAndWait()
    
        
        
    return render_template('index.html',**locals())



if __name__=="__main__":
    app.run(debug=True)


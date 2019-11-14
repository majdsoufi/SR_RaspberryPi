#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,url_for,request
import speech_recognition as sr


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/speechtotext',methods=['POST'])

def index():
    if request.method == "POST":
        recognizer = sr.Recognizer()
        mic  = sr.Microphone()
        with mic as source:
            audio_data = recognizer.record(source)
        my_text = recognizer.recognize_google(audio_data)
    return render_template('result.html',text = my_text)


if __name__ == '__main__':
	app.run(debug=True)


# In[ ]:





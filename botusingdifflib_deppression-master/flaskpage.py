from flask import Flask
from flask import render_template,request
#from pymongo import MongoClient
from bot import get_close_matches_indexes

app=Flask(__name__)



message=[]
@app.route('/')
def index():
    message.clear()
    
    return render_template('chatbox.html')
@app.route('/mainpage',methods=['POST'])
def mainpage():
    if request.method=='POST':
        search=request.form
        sdata=search['msg']
        reply=get_close_matches_indexes(sdata)
        d1={"user":sdata,"reply":reply}
        message.append(d1)
        
        
        
    return render_template('chatbox.html',messages=message)

if __name__=='__main__':
    app.run(debug=True)
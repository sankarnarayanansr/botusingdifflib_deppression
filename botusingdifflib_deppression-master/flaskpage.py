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
        if sdata=="hii" or sdata=="hello":
            d1={"user":sdata,"reply":"heyy hello"}
        else:
            try:
                reply=get_close_matches_indexes(sdata)
            except:
                reply="Dont worry! Life will become easier soon"
                
            d1={"user":sdata,"reply":reply}
        message.append(d1)
    mapvalue={"user":"msg left-msg","reply":"msg right-msg"}
        
        
    return render_template('chatbox.html',messages=message,x=mapvalue)

if __name__=='__main__':
    app.run(debug=True)

from flask import Flask,render_template,request
from genaiweb import chatbot
app=Flask(__name__)

@app.route('/')
def call():
    return render_template('home.html')

@app.route('/call')
def callgemini():
    key=request.args.get('k')
    question=request.args.get('q')
    response=chatbot(key,question)
    return "<body bgcolor='yellow' text='red'><h3>the response is {}</h3></body>".format(response)

    


if __name__=='__main__':
    app.run(debug=True)

    



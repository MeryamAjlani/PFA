
from flask import Flask, render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pickle


app =Flask(__name__)
app.secret_key="Secret_test"

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:''@localhost/crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/aspect',methods=['GET'])
def get():
    print(request.form)
    txt=request.form.get('txt')
    with open('best_model_state.bin', 'rb') as f_in:
       model = pickle.load(f_in)
       prediction= model.predict([txt])
       print(prediction)

if __name__=="__main__":
    app.run(debug=True)


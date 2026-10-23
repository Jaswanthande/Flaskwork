from flask import Flask,render_template,url_for,redirect,request
import uuid
app = Flask(__name__)
id='';name='';attendence=0;path='';uid=''
@app.route('/')
def home():
    # return "flask is running"
    return render_template('index.html')
@app.route('/getData/',methods=['GET'])
def getData():
    name = request.args.get('name')
    email = request.args.get('email')
    return f"Name : {name} Email : {email}"
@app.route('/getDatafromPOST/',methods=['POST'])
def getDatafrompost():
    data=request.get_json()
    name = data['name']
    email = data['email']
    return f"Name : {name} Email : {email}"
@app.route('/postData/',methods=['POST'])
def postData():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if(name is None or len(name)<5):
        return render_template('index.html',error="Name should be more than 5 characters")
    if(email is None):
        return render_template('index.html',error="invalid email")
    if(password is None or len(password)<4):
        return render_template('index.html',error="Password should be more than 4 characters")
    return render_template('index.html',success="Data submitted successfully ")

@app.route('/updateData/<email>',methods=['PUT'])
def updateData(email):
    data=request.get_json()
    name = data['name']
    password = data['password']
    return f"Name : {name} Email : {email} Password : {password}"
@app.route('/deleteData/<email>',methods=['DELETE'])
def deleteData(email):
    return f"Email : {email} deleted successfully"
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        name = request.args.get('name')
        email = request.args.get('email')
    if request.method == 'POST':
        data=request.get_json()
        name = data['name']
        email = data['email']
    return f"Name : {name} Email : {email} registered successfully"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
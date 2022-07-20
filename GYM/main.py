from flask import Flask,request,redirect,render_template,session
from dbms import addData,fetchData, specificdata, updatedata,deletedata,addData2,addData3,addData4,addData5
import pymysql as p

app=Flask(__name__)

app.secret_key="abc"

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='gym')


#First Routing
@app.route("/")
def home_func():
    return render_template("home.html")

#index
@app.route("/indexlink")
def index_func():
      return render_template("index.html")

@app.route("/contactlink")
def contact_func():
      return render_template("contact.html")

@app.route("/aboutlink")
def about_func():
      return render_template("about.html")


#memebers
@app.route("/memberslink")
def mem_func():
      return render_template("members.html")

@app.route("/addlink")
def aur_func():
      return render_template("add.html")


@app.route("/save3link",methods=["POST"])
def add_func():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    dob=request.form['dob']
    email=request.form['email']
    membership_type=request.form['membership_type']
    active=request.form['active']
    t=(first_name,last_name,dob,email,membership_type,active)
    addData2(t)
    return render_template("members.html")



#Second Routing
@app.route("/reglink")
def register_func():
      return render_template("resgister.html")



#third Routing
@app.route("/savelink",methods=["POST"])
def save_func():
    name=request.form["name"]
    email=request.form["email"]
    age=request.form["age"]
    city=request.form["city"]
    number=request.form["number"]
    password=request.form["password"]
    t=(name,email,age,city,number,password)
    addData(t)

    return redirect("reglink")
    

@app.route("/savelink16",methods=["POST"])
def con_func():
    fname=request.form['fname']
    lname=request.form['lname']
    subject=request.form['subject']
    t=(fname,lname,subject)
    addData5(t)
    return render_template("home.html")    

#Fourth Routing
@app.route("/loginlink")
def login_func():
    return render_template("login.html")


@app.route("/savelink2",methods=["POST"])
def login_save():
    if request.method=='POST' and 'name' in request.form and 'password' in request.form:
        username=request.form['name']
        password=request.form['password']
        con=getConnection()
        cur=con.cursor()
        cur.execute("select * from register_details where name=% s AND password=% s",(username,password))
        result=cur.fetchone()
        
    return redirect("indexlink")
    


@app.route("/classeslink")
def menu_func():
      return render_template("classes.html")

@app.route("/addfitlink")
def sab_func():
      return render_template("addfit.html")

#third Routing
@app.route("/savelink7",methods=["POST"])
def save3_func():
    name=request.form['name']
    capacity=request.form['capacity']
    start_time=request.form['start_time']
    duration=request.form['duration']
    day =request.form['day']
    active =request.form['active']
    t=(name,capacity,start_time,duration,day,active)
    addData3(t)
    return render_template("classes.html")

#plan
@app.route("/planlink")
def plan_func():
      return render_template("plans.html")

@app.route("/informationlink")
def information_func():
    return render_template("information.html")

@app.route("/savelink11",methods=["POST"])
def information_save():
    if request.method=='POST':
        
        Age=request.form['Age']
        choosefor=request.form['choosefor']
        coverage=request.form['coverage']
        premium_oneyear=(int(choosefor)*int(coverage))/20
        return render_template("premium.html",premium=premium_oneyear)

  



#fifth Routing
@app.route('/logoutlink')
def logout_func():
    session.pop('name',None)
    session.pop('password',None)
    return render_template("login.html")
   # return "<h1> LOGOUT SUCCESSFUL </h1>"

#sixth Routing
@app.route('/showlink')
def show_func():
    datalist=fetchData()
    return render_template("show.html",data=datalist)

@app.route("/editlink/<int:id>")
def displayforupdate(id):
    datalist=specificdata(id)
    return render_template("edit.html",data=datalist)

@app.route("/updatelink/<int:id>",methods=["POST"])
def updatefun(id):
    name=request.form["name"]
    password=request.form["password"]
    city=request.form["city"]
    t=(name,password,city,id)
    updatedata(t)
    return redirect("/showlink")

@app.route("/deletelink/<int:id>")
def deletefun(id):
    deletedata(id)
    return redirect("/showlink") 
 
if __name__=='__main__':
     app.run(debug=True)
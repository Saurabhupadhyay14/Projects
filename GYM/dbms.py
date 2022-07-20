import pymysql as p

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='gym')

def addData(t):
    con=getConnection()
    cur=con.cursor()
    query2="insert into gym1 (name,email,age,city,number,password)values(%s,%s,%s,%s,%s,%s)"
    cur.execute(query2,t)
    con.commit()
    con.close()

def addData5(t):
    con=getConnection()
    cur=con.cursor()
    query6="insert into contact (fname,lname,subject)values(%s,%s,%s)"
    cur.execute(query6,t)
    con.commit()
    con.close()

def addData2(t):
    con=getConnection()
    cur=con.cursor()
    query1="insert into Members (first_name ,last_name ,dob,email,membership_type,active ) values(%s,%s,%s,%s,%s,%s)"
    cur.execute(query1,t)
    con.commit()
    con.close()

def addData3(t):
    con=getConnection()
    cur=con.cursor()
    query3="insert into fitness_classes (name,capacity,start_time,duration,day,active) values(%s,%s,%s,%s,%s,%s)"
    cur.execute(query3,t)
    con.commit()
    con.close()

def addData4(t):
    con=getConnection()
    cur=con.cursor()
    query4="insert into trainer2 (trainer_name,batch,start_time1,duration1,day1) values(%s,%s,%s,%s,%s)"
    cur.execute(query4,t)
    con.commit()
    con.close()

def fetchData():
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from register_details")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def fetchData():
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from bookings")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def specificdata(id):
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from register_details where id=%s",(id,))
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]

def updatedata(t):
    con=getConnection()                  
    cur=con.cursor()
    query="update register_details set name=%s,password=%s,city=%s where id=%s"
    cur.execute(query,t)
    con.commit()
    con.close()


def deletedata(id):
    con=getConnection()                  
    cur=con.cursor()
    query="delete from register_details where id=%s"
    cur.execute(query,(id,))
    con.commit()
    con.close()
    
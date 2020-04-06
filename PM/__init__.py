from . import DB_Action
import random

##x = DB_Action.get_user_by_ID("20")
#newUser = {"_id":"23","userName":"king","password":"2323","firstName":"lebron","lastName":"james","role":1}
#DB_Action.insert_user("24","user","user","user","user",1)
#DB_Action.update_user_by_ID(20)
#user = DB_Action.get_user_by_userName("king")
#if(user != None):
#    x = user['_id']
#    y = user['userName']
#    z= user['password']
#c=""
firstnames = ["yossi","shimi","avi","aviel","motti","gall","static","ben-el","eden","lea","ruti","simcha","avihu","ivri"]
lastnames = ["cohen","levy","friedman","tavori","shilo","bandel","maymon"]
for i in range(50):
        DB_Action.insert_user("10"+str(i),"admin"+str(i), "1234", random.choice(firstnames),random.choice(lastnames),1)
        DB_Action.insert_user("40"+str(i),"user"+str(i),"1234",random.choice(firstnames),random.choice(lastnames),3)
        DB_Action.insert_user("30"+str(i),"trainer"+str(i),"1234",random.choice(firstnames), random.choice(lastnames),2)












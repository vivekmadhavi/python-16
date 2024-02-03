#wapp to create emp record


from pymongo import *
con=None
try:
	con = MongoClient("localhost",27017)
	db = con["kc_24dec23"]
	coll = db["emp"]

	eid= int(input("enter id "))
	ename = input("enter name")
	salary = int(input("enter salary"))

	info = {"_id":eid , "name" : ename, "salary":salary}
	coll.insert_one(info)
	print("record created")
except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()
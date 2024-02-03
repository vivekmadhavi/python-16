#wapp to  emp record


from pymongo import *
con=None
try:
	con = MongoClient("localhost",27017)
	db = con["kc_24dec23"]
	coll = db["emp"]
	
	data = coll.find()
	for d in data:
		info=""
		if d.get("_id"):
			info = "id = " + str(d.get("_id")) + "  " 
		if d.get("name"):
			info =info + "name = " + str(d.get("name")) + "  " 
		if d.get("salary"):
			info = info +"salary = " + str(d.get("salary")) + "  " 
		print(info)
except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()
#wapp to  delete record


from pymongo import *
con=None
try:
	con = MongoClient("localhost",27017)
	db = con["kc_24dec23"]
	coll = db["emp"]
	
	id =  int(input("enter id "))
	c = coll.count_documents({"_id":id})
	if c == 1:
		coll.delete_one({"_id":id})
		print("record deleted")
			
			
	else:
		print(id,"does not exists")
		
except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()
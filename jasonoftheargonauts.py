di={}

import json

def additem(unid,data):
    with open("file.json",'w') as file:
        di[unid] = data
        json.dump(di,f)
        return ("success")

def retrivedata(unid):
    with open("file.json","w") as file:
        if unid in di:
            di = json.load(f)
            return di
    raise json.decoder.JSONDecodeError("invalid inpur")

def updatedata(inid,new_data):
   with open("file.json","w+") as f:
       if unid in di:
           di[unid] = new_data
           json.dump(di,f)
           return ("updated sucessfully")
   raise json.decoder.JSONDecodeError("invalid operation")

def deletedata(unid):
    with open("file.json","w+"):
        if unid in di:
            del di[unid]
            return("deleted successfully")
    raise json.decoder.JSONDecodeError('invalid imput')

while True:
    print("Welcome \nto add data pres 1\nto retrive data pres 2\n"
          "to update data pres 3\nto delete data pres 4\nto quit pres 5\n"
          )

    if choice == '1':
        unid = max(di.values(), default=0)+1
        print(F"your key is:{unid}")
        data = input("enter data you want to add: ")
        print(additem(unid,data))
    if choice == '2':
        unid = int(input("enter the data id you want to retrive: "))
        print(retrivedata(unid))
    if choice == '3':
        unid = int(input("enter the data id you want to change: "))
        new_data = input("enter the data you wnat to update")
        print(updatedata(unid,data))
    if choice == '4':
        unid = int(input("enter the id of the data you want to delete: "))
        print(deletedata(unid))
    if choice == '5':
        print("exiting the program")
        break
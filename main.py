# main.py
from fastapi import FastAPI, Body
import schemas


app = FastAPI()

fakeDatabase = {
    1:{'task':'clean car'},
    2:{'task':'write blog'},
    3:{'task':'start stream'}
}

# get items from database
@app.get("/{id}")
def getItems(id:int):
    return fakeDatabase[id]

# Add items to database
@app.post("/")
def addItem(body = Body()):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":body["task"]}
    return fakeDatabase

# Update items in database
@app.put("/{id}")
def updateItem(id:int, item:schemas.Item):
    fakeDatabase[id]["task"] = item.task
    return fakeDatabase

# Delete items from database
@app.delete("/{id}")
def deleteItem(id:int):
    del fakeDatabase[id]
    return fakeDatabase

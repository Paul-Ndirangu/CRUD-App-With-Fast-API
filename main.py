# main.py
from fastapi import FastAPI

app = FastAPI()

fakeDatabase = {
    1:{'task':'clean car'},
    2:{'task':'write blog'},
    3:{'task':'start stream'}
}

@app.get("/{id}")
def getItems(id:int):
    return fakeDatabase[id]

@app.post("/")
def addItem(task:str):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":task}
    return fakeDatabase


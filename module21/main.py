 from fastapi import fastAPI

app = fastAPI()

@app.get("/")
def root():
    return{"message":"qkemi"}



@app.get("/item")
def read_items():
    return{"items":["item1","item2","item3"]}

@app.post("/item/")
def careat_item(name:str,price:float):
    return {"item_name":name "item_price":price}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return {"item_id": item_id "item_name":name, "item_price": price}

@app.put("/items/{item_id}")
def update_item(item_id:int,name:str,price:float):
    return {"item_id": item_id "item_name":name, "item_price": price}

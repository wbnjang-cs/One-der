from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []


@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id:  int) -> str:
     if item_id < len(items):
        item = items[item_id]
        return item
     else:
         raise HTTPException(status_code=404, detail = f"Item {item_id} not found")
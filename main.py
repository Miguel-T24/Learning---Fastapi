# To View the auto doc with swagger
# route + /docs
# Example http://127.0.0.1:8000/docs

# or with redoc
# route + /ReDoc
# Example: http://127.0.0.1:8000/redoc


from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello'}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id" : item_id}

# parameters with types
@app.get("/types/{item_id}")
async def read_item(item_id : int):
    return{"item_id" : item_id}


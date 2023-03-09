from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello'}




# To View the auto doc with swagger
# route + /docs
# Example http://127.0.0.1:8000/docs

# or with redoc
# route + /ReDoc
# Example: http://127.0.0.1:8000/redoc
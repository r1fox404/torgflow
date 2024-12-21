from fastapi import FastAPI


app = FastAPI(title="ТоргФлоу")


@app.get("/")
async def main_page():
    return {"msg": "Hello!"}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#  uvicorn users:app --reload


@app.get("/usersjson")
async def usersjson():
    return [
        {"name": "Brais", "surname": "moure", "url": "https://moure.com/python"},
        {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com/python"},
        {"name": "Haskon", "surname": "Danilberg",
            "url": "https://heakon.com/python"}
    ]
# VOY MINUTO 1h:56
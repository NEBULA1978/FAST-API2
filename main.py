from fastapi import FastAPI
# from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return "!Hola FastAPI"



# Inicio Servidor:
#  uvicorn main:app --reload

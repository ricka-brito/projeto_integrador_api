from fastapi import FastAPI
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class bd:
    def __init__(self):
        self.cnx = mysql.connector.connect(user="rick@primavera-senai", password="Bingo2013_",
                                      host="primavera-senai.mariadb.database.azure.com", port=3306,
                                      database="banco_primavera")
        self.cursor = self.cnx.cursor()

    def read(self):
        self.cursor.execute("SELECT * FROM produtos")
        dados = self.cursor.fetchall()
        formatado = []
        for i in dados:
            formatado.append({"nome": i[1], "src": i[2], "preco": i[3], "detalhes": i[4], "descricao": i[5]})

        return formatado


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/produtos")
def teste():
    a = bd()
    return a.read()

if __name__ ==  '__main__':
   import uvicorn
   uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
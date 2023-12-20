from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()
class  WikiInput(BaseModel):
    name: str
    quantity: int


@app.get("/route") #роут который выдает две статьи
def wiki(name: str):
    return wikipedia.search(name, results=2)


@app.post("/wiki/{name}") #роут который ищет имя и задаваемое кол-во статей
def wiki_search(name, quantity: WikiInput):
    return wikipedia.search(name, results=quantity)

@app.get("/wikipedia/{name}") #роут ко орый исправляет граматические ошибки
def wiki_suggest(name: str):
    return wikipedia.suggest(name)

@app.get("/name") #роут который выдает краткое содержание cтатьи
def wiki_summary(name:str):
    return wikipedia.summary(name)
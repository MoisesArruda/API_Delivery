from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definir um decorador de rota, que será responsável por tratar as requisições que vão para a rota “ / ” usando o operador get
@app.get("/")
def hello_root():
    """
    Exemplo de aplicação"""
    return {"message": "Hello World"}

# Rodar o comando no terminal para iniciar o servidor FastAPI
# uvicorn Fast_API:app --reload

# Podemos acessar a página docs
# http://127.0.0.1:8000/docs

# Podemos acessar a página redoc
# http://127.0.0.1:8000/redoc


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "Colher de cha"):
    """
    Exemplo de aplicação"""
    return {"item_id": item_id, "q": q}


# Simulando um banco de dados em memória
fake_db = {}

# Rota POST para receber dados.
class Item(BaseModel):
    name: str
    price: float
    tax: float = None
    description: str = None

@app.post("/items/")
def create_item(item: Item):
    """
    Exemplo de aplicação"""
    return {"item": item}

# Rota PUT para atualizar dados já existentes.
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    Exemplo de aplicação
    """
    return {"item_id": item_id, "item": item}

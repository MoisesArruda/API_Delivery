from fastapi import FastAPI, HTTPException, Path, Query, Body
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime
import uvicorn

app = FastAPI(title="Testes FastAPI", description="API com exemplos práticos")

class Usuario(BaseModel):
    id: int
    nome: str
    email: EmailStr
    idade: Optional[int] = None
    data_criacao: datetime = Field(default_factory=datetime.now)

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    descricao: Optional[str] = None
    estoque: int = Field(ge=0) # ge = greater or equal (maior ou igual)

class Pedido(BaseModel):
    id: int
    usuario_id: int
    produtos: List[Produto]
    total: float
    status: str = "pendente"

# Banco de dados simulado
db_usuarios = {}
db_produtos = {}
db_pedidos = {}

# Rotas GET
@app.get("/")
def root():
    """
    Rota raiz da nossa página
    """
    return {"message": "Bem-vindo à nossa primeira API de exemplo utilizando o FastAPI"}


@app.get("/usuarios/", response_model=List[Usuario]) # A API sempre vai buscar o padrão Usuario para retornar os dados
def listar_usuarios():
    """
    Lista todos os usuários cadastrados na plataforma
    """
    if not db_usuarios:
        raise HTTPException(status_code=404, detail="Nenhum usuário cadastrado")
    return list(db_usuarios.values())

@app.get("/produtos/", response_model=List[Produto])
def listar_produtos():
    """
    Lista todos os produtos cadastrados na plataforma
    """
    if not db_produtos:
        raise HTTPException(status_code=404, detail="Nenhum produto cadastrado")
    return list(db_produtos.values())

@app.get("/usuarios/{usuario_id}", response_model= Usuario)
def obter_usuario(usuario_id: int = Path(..., gt=0)):
    """
    Obtém um usuário específico pelo ID
    """
    if usuario_id not in db_usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuarios[usuario_id]

@app.get("/produtos/{produto_id}", response_model= Produto)
def obter_produto(produto_id: int = Path(..., gt=0)):
    """
    Obtém um produto específico pelo ID
    """
    if produto_id not in db_produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_produtos[produto_id]

# Rotas POST
@app.post("/usuarios/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    """
    Cria um novo usuário
    """
    if usuario.id in db_usuarios:
        raise HTTPException(status_code=400, detail="ID de usuário já existe")
    db_usuarios[usuario.id] = usuario
    return usuario

@app.post("/produtos/", response_model=Produto)
def criar_produto(produto: Produto):
    """
    Cria um novo produto
    """
    if produto.id in db_produtos:
        raise HTTPException(status_code=400, detail="ID de produto já existe")
    db_produtos[produto.id] = produto
    return produto

# Rota PUT (Atualizar)
@app.put("/usuarios/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, usuario: Usuario):
    """
    Atualiza um usuário existente
    """
    if usuario_id not in db_usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db_usuarios[usuario_id] = usuario
    return usuario

@app.put("/produtos/{produto_id}", response_model=Produto)
def atualizar_produto(produto_id: int, produto: Produto):
    """
    Atualiza um produto existente
    """
    if produto_id not in db_produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db_produtos[produto_id] = produto
    return produto

# Rota DELETE (Remover)
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    """
    Remove um usuário
    """
    if usuario_id not in db_usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    del db_usuarios[usuario_id]
    return {"mensagem": "Usuário removido com sucesso"}

if __name__ == "__main__":
    uvicorn.run("Aprendizados_FastAPI:app", host="127.0.0.1", port=8000, reload=True) 

    # Usuario:
    # {
    # "id": 1,
    # "nome": "João",
    # "email": "joao@email.com",
    # "idade": 25
    # }

    # Produto:
#    {
#     "id": 1,
#     "nome": "Produto 1",
#     "preco": 10.0,
#     "estoque": 5
#     } 

    # Pedido:
    # {
    # "usuario_id": 1,
    # "produtos": [{"nome": "Produto 1", "preco": 10.0}]
    # "total": 10.0
    # } 


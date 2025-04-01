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
    return {"message": "Bem-vindo à API de Exemplos"}


@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    """
    Lista todos os usuários cadastrados na plataforma
    """
    return list(db_usuarios.values())

@app.get("/usuarios/{usuario_id}", response_model= Usuario)
def obter_usuario(usuario_id: int = Path(..., gt=0)):
    """
    Obtém um usuário específico pelo ID
    """
    if usuario_id not in db_usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuarios[usuario_id]

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

# Introdução
Os dois frameworks possuem algumas diferenças importantes em seu funcionamento. 
- FastAPI: Enquanto o **FastAPI** é uma versão mais rápida, permite typehints, possuí uma validação nativa com o Pydantic e ainda conta com uma barreira de entrada um pouco menor. 

- Flask: Já o **Flask**, tem a vantagem de ter um servidor próprio para rodar e conseguir realizar seus testes.

## FastAPI
Quando vamos criar nosso endpoints, já passamos ele com o método que queremos utilizar.

1. Acessando dados
```python
app.get("/usuarios/")
def hello_world():
    """
    Acessando o caminho raiz
    """
    return {"message":"Hello World"}
```
2. Inserindo dados
```python
app.post("/usuarios/")
def criar_usuarios(usuario: Usuario):
    if usuario_existe(usuario.id):
        raise HTTPException(status_code=400,detail= "Usuário já existe")
    return {"message":"Usuario criado"}
```

## Flask
Com o Flask, temos o decorator padrão @app.route onde temos que passar o **método** que queremos utilizar como o **Endpoint** a ser utilizado

```python
@app.route("/usuario/",methods=['POST'])
def criar_usuarios(usuario: Usuario):
    if usuario_existe(usuario.id):
        raise HTTPException(status_code=400,detail= "Usuário já existe")
    return {"message":"Usuario criado"}
```


## Métodos utilizado em APIs

1. **Get** - Busca, localizar os dados
2. **Post** - Adicionar os dados
3. **Put** - Alterar os dados existentes
4. **Delete** - Excluir a informação

## Endpoints

1. **("/")** - Raiz do projeto
2. **("/Usuario/")** - Caminho com informações da nossa aplicação
3. **("/Usuario/1")** - Localizando uma informação especifica, por exemplo, um ID



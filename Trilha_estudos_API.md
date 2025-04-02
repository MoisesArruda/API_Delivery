1️⃣ Autenticação e Autorização 🔐
JWT (JSON Web Token): Como gerenciar autenticação com tokens

OAuth 2.0 e OpenID Connect: Padrões para autenticação segura

API Key e Basic Auth: Métodos alternativos de autenticação

2️⃣ Banco de Dados e ORM 🗄️
SQLAlchemy: ORM para Python (FastAPI e Flask podem usar)

Tortoise ORM: Alternativa assíncrona para FastAPI

MongoDB com FastAPI: APIs NoSQL com Motor (driver do MongoDB)

3️⃣ Testes de API ✅
Pytest + HTTPX: Testes automatizados para garantir o funcionamento da API

Postman: Ferramenta para testar manualmente seus endpoints

Mocking de APIs: Como simular respostas para testar dependências

4️⃣ Documentação de API 📜
Swagger/OpenAPI: Já embutido no FastAPI

Flasgger para Flask: Como gerar documentação automática no Flask

5️⃣ Deploy e Monitoramento 🚀
Docker e Docker Compose: Criando APIs em containers

Uvicorn + Gunicorn: Servidores para FastAPI em produção

Prometheus + Grafana: Monitoramento de APIs

6️⃣ WebSockets e Tempo Real ⏳
FastAPI + WebSockets: Criando comunicação em tempo real

Socket.IO com Flask: Alternativa para apps Flask

## Diferenças entre interação com Db

🔹 Usando psycopg2 (Interação Manual com SQL)

Com psycopg2, você escreve as consultas SQL manualmente e interage diretamente com o banco de dados. Isso dá mais controle, mas exige que você trate manualmente os dados e erros.

🔹 Usando ORM (Exemplo com SQLAlchemy)

O ORM abstrai o SQL e permite que você interaja com o banco através de classes e objetos Python.

Exemplo de busca de usuários com SQLAlchemy:
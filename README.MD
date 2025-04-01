# API Delivery

API para gerenciamento de entregas e pedidos.

## Descrição

Este projeto é uma API REST desenvolvida em Python utilizando Flask para gerenciamento de entregas e pedidos. A API permite o cadastro de clientes, pedidos, entregadores e o acompanhamento do status das entregas.

## Requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/API_Delivery.git
cd API_Delivery
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Executar

Para iniciar o servidor de desenvolvimento:

```bash
python main.py
```

O servidor estará disponível em `http://localhost:5000`

## Estrutura do Projeto

```
API_Delivery/
├── main.py              # Arquivo principal da aplicação
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## Contribuição

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

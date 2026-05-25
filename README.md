# Password Generator API

## 📌 Sobre o projeto

API REST desenvolvida em Python para geração de senhas fortes e seguras.

O projeto foi criado com foco em aprendizado de desenvolvimento back-end moderno, utilizando boas práticas de arquitetura, validação declarativa, modularização e testes automatizados.

A aplicação permite gerar senhas personalizadas com tamanho configurável, garantindo:

- Letras maiúsculas
- Letras minúsculas
- Números
- Caracteres especiais

---

## 🚀 Tecnologias utilizadas

- Python 3.13
- FastAPI
- Pydantic
- Pytest
- Uvicorn

---

## 📂 Estrutura do projeto

```text
password_generator/
│
├── routes/
│   └── password_creation_path.py
│
├── tests/
│   ├── test_api.py
│   └── test_generator.py
│
├── api.py
├── generator.py
├── schemas.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Raelsons10/password-generator-python.git
```

### 2. Acesse a pasta do projeto

```bash
cd password-generator-python
```

### 3. Crie um ambiente virtual

#### Windows

```bash
python -m venv .venv
```

#### Linux/Mac

```bash
python3 -m venv .venv
```

---

## ▶️ Ativando o ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 📦 Instalando dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando a API

```bash
uvicorn api:app --reload
```

Após iniciar o servidor:

### API

```text
http://127.0.0.1:8000
```

### Swagger/OpenAPI

```text
http://127.0.0.1:8000/docs
```

---

## 📖 Endpoint principal

### Gerar senha

```http
POST /create_password/generate_password
```

### Request Body

```json
{
  "length": 12
}
```

### Response

```json
{
  "password": "@Ab12#xYz9!",
  "length": 12
}
```

---

## 🧪 Executando os testes

```bash
pytest -v
```

---

## ✅ Funcionalidades

- Geração de senhas seguras
- Validação automática com Pydantic
- API REST com FastAPI
- Arquitetura modular
- Testes automatizados
- Response Models
- Documentação automática Swagger/OpenAPI

---

## 🎯 Objetivos do projeto

Este projeto foi desenvolvido com foco em:

- Evolução prática em desenvolvimento back-end
- Aprendizado de FastAPI
- Modelagem de APIs REST
- Estruturação de projetos Python
- Testes automatizados
- Boas práticas de arquitetura

---

## 📌 Status do projeto

✅ Versão 1.0 finalizada

---

## 👨‍💻 Autor

Desenvolvido por Raelson.

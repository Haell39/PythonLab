# 💰 Controle de Gastos

Gerencie suas **despesas e receitas** de forma simples e rápida!  
Este sistema permite **cadastrar pessoas**, criar **transações financeiras** e acompanhar seus gastos em uma interface.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando a **stack FARM**:

- ⚡ **FastAPI** - Backend rápido e eficiente.
- 🎨 **React.js** - Interface interativa e dinâmica.
- 🍃 **MongoDB** - Banco de dados NoSQL.

---

## 🚀 Funcionalidades

✅ **Cadastro e exclusão de Pessoas.**  
✅ **Registro e exclusão de Transações** (receitas e despesas).  
✅ **Listagem das Transações** (receitas e despesas).

---

## 🏗️ Como Rodar o Projeto

### 🔧 **1. Backend (FastAPI)**

1. Instale as dependências:
   ```sh
   pip install fastapi uvicorn pymongo python-dotenv
   ```
2. Crie e inicie a venv:
   ```sh
   python -m venv nome_do_ambiente #caso ainda nao tenha criado
   source nome_do_ambiente/Scripts/activate #Windos
   ```
3. Incie os servidores do backend:
   ```sh
   cd backend
   uvicorn main:app --reload
   ```

### 💻 **2. Frontend (React.js)**

1. Instale as dependências:
   ```sh
   npm install
   ```
2. Crie e inicie a venv:
   ```sh
   python -m venv nome_do_ambiente #caso ainda nao tenha criado
   source nome_do_ambiente/Scripts/activate #Windos
   ```
3. Incie o servidor do frontend:
   ```sh
   cd frontend
   npm run dev
   ```

### 🌐 **Para de fato rodar no navegador**

1. Acesse http://localhost:5173

OBS: Swagger para testar o backend está em http://localhost:8000/docs

---

📜 Licença

📝 Este projeto é licenciado sob a **MIT License**.

```

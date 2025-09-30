# Mini API Usuários

API REST desenvolvida com **FastAPI** para gerenciamento de usuários, utilizando **SQLite** (arquivo local), **SQLAlchemy** como ORM e **Pydantic** para validação. Inclui documentação automática via **Swagger UI** e testes com **Pytest**.

> **Compatibilidade com o enunciado:** o campo exigido como `data_criacao` no teste está implementado e exposto como **`created_at`** nesta API. É o mesmo **timestamp de criação**, apenas com nome em inglês.

---

## 🚀 Tecnologias

* **FastAPI** – Framework web moderno e rápido
* **Uvicorn** – Servidor ASGI de alto desempenho
* **SQLAlchemy** – ORM para banco de dados
* **Pydantic** – Validação de dados
* **Pytest** – Testes automatizados

---

## 🧩 Requisitos

* **Python 3.10+** (recomendado 3.11)
* **pip** atualizado
* (Opcional) **Docker** e **Docker Compose**

---

## ⚙️ Instalação

1. **Clone o repositório**

```sh
git clone <url-do-repositorio>
cd Mini_api
```

2. **(Opcional) Crie e ative um ambiente virtual**

```sh
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. **Instale as dependências**

Você pode seguir exatamente os comandos usados no teste:

```sh
pip install fastapi uvicorn sqlalchemy pydantic pytest
pip install pydantic[email]
```

> Alternativa (se existir `requirements.txt`):
>
> ```sh
> pip install -r requirements.txt
> ```

---

## ▶️ Executando a API (modo local)

Inicie o servidor:

```sh
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Após rodar, abra os links:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Health Check:** [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)
* **Rota raiz:** [http://localhost:8000](http://localhost:8000)
* **Usuários (lista):** [http://localhost:8000/api/v1/usuarios/](http://localhost:8000/api/v1/usuarios/)

---

## 🌐 Endpoints principais

* `POST /api/v1/usuarios` – Criar usuário
* `GET /api/v1/usuarios` – Listar usuários
* `GET /api/v1/usuarios/{id}` – Buscar usuário por ID
* `PUT /api/v1/usuarios/{id}` – Atualizar usuário
* `DELETE /api/v1/usuarios/{id}` – Remover usuário
* `GET /api/v1/health` – Verificar status da API

---

## ✅ Exemplo de requisição

**Criar usuário (POST /api/v1/usuarios):**

```json
{
  "nome": "Maria Silva",
  "email": "maria@example.com"
}
```

**Resposta esperada:**

```json
{
  "id": 1,
  "nome": "Maria Silva",
  "email": "maria@example.com",
  "created_at": "2025-09-30T22:44:48.951Z",
  "updated_at": "2025-09-30T22:44:48.951Z"
}
```

> **Nota:** `created_at` **≡** `data_criacao` citado no enunciado.

### Exemplos rápidos (cURL)

Criar:

```sh
curl -s -X POST http://localhost:8000/api/v1/usuarios/ \
  -H "Content-Type: application/json" \
  -d '{"nome":"Maria Silva","email":"maria@example.com"}'
```

Listar:

```sh
curl -s http://localhost:8000/api/v1/usuarios/
```

Buscar por ID:

```sh
curl -s http://localhost:8000/api/v1/usuarios/1
```

Atualizar:

```sh
curl -s -X PUT http://localhost:8000/api/v1/usuarios/1 \
  -H "Content-Type: application/json" \
  -d '{"nome":"Maria S. Silva"}'
```

Remover:

```sh
curl -s -X DELETE http://localhost:8000/api/v1/usuarios/1
```

---

## 🧪 Testes

Execute:

```sh
pytest
```

> Os testes verificam rotas essenciais (ex.: criação, listagem e health).
> Em SQLite local, o arquivo `usuarios.db` pode ser recriado automaticamente.

---

## 📂 Estrutura do Projeto

```
Mini_api/
├── app/
│   ├── core/         # config, database
│   ├── models/       # modelos ORM (SQLAlchemy)
│   ├── routes/       # rotas FastAPI (usuarios, health)
│   ├── schemas/      # Pydantic (entrada/saída)
│   └── services/     # regras de negócio/CRUD
├── tests/
├── usuarios.db       # SQLite (criado automaticamente)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

---

## 🐳 Docker (opcional)

Subir com Docker Compose:

```sh
docker-compose up --build
```

A API ficará disponível em **[http://localhost:8000](http://localhost:8000)**.

---

## ❗ Dicas e Troubleshooting

* **Porta em uso (8000):** troque a porta, por exemplo `--port 8001`.
* **Dependências faltando:** rode novamente os dois comandos `pip install` listados acima.
* **Permissão no Windows:** abra o terminal como **Administrador**.
* **Banco limpo:** apague `usuarios.db` para recomeçar do zero (em dev).

---

## ✅ Compatibilidade com o teste

* **POST /usuarios** – OK
* **GET /usuarios** – OK
* **GET /usuarios/{id}** – OK
* **Campos exigidos por usuário:**

  * `id` (auto) – OK
  * `nome` – OK
  * `email` – OK
  * `data_criacao` – **OK (exposto como `created_at`)**

---

## ✉️ Contato

Dúvidas ou sugestões?
Abra uma issue ou envie um e-mail para **[luiza.macena2013@gmail.com](mailto:luiza.macena2013@gmail.com)**.

Feito por **Luiza Macena** ✨


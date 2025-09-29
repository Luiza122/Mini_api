# Mini API de Cadastro de Usuários — Pro

Projeto organizado. Inclui:
- Estrutura por camadas (routes / schemas / services / models / core)
- Validação com Marshmallow
- Documentação **OpenAPI + Swagger UI** disponível em `/docs/`
- Blueprints (flask-smorest)
- SQLite (arquivo criado automaticamente)
- Testes básicos com `pytest`
- Dockerfile e docker-compose opcionais
- Makefile com atalhos comuns

## Endpoints
- `POST /usuarios` — cria um usuário
- `GET /usuarios` — lista todos
- `GET /usuarios/{id}` — busca por ID
- `GET /health` — healthcheck
- **Docs**: `GET /docs/` (Swagger UI) e `/docs/openapi.json`

## Rodando localmente
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run
```

## Via Docker
```bash
docker build -t miniapi-usuarios .
docker run -p 5000:5000 miniapi-usuarios
```

## Estrutura
```
app/
  core/
    config.py
    extensions.py
  models/
    user.py
  routes/
    users.py
  schemas/
    user.py
  services/
    user_service.py
__init__.py
app.py
requirements.txt
README.md
tests/
```

## Testes
```bash
pip install pytest
pytest -q
```

## Exemplos (curl)
```bash
curl -X POST http://localhost:5000/usuarios -H "Content-Type: application/json"   -d '{ "nome":"Luiza Dantas", "email":"luiza@example.com" }'

curl http://localhost:5000/usuarios
curl http://localhost:5000/usuarios/1
```

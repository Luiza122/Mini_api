.PHONY: run test docker-build docker-run clean

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest -v

docker-build:
	docker build -t miniapi-usuarios .

docker-run:
	docker run -p 8000:8000 miniapi-usuarios

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f usuarios.db

install:
	pip install -r requirements.txt
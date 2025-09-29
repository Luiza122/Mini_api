
.PHONY: run test install docker

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run:
	flask --app app run

test:
	pytest -q

docker:
	docker build -t miniapi-usuarios .

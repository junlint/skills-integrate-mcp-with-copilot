PYTHON?=python3

.PHONY: help build up down test

help:
	@echo "Targets: build, up, down, test"

build:
	docker build -t skills-integrate-mcp:local .

up:
	docker-compose up --build

down:
	docker-compose down

test:
	${PYTHON} -m pytest -q

.PHONY: all install build start test seed lint clean

all: install build test

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install
	cd vendor-dashboard && npm install
	cd admin-dashboard && npm install

build:
	cd frontend && npm run build
	cd vendor-dashboard && npm run build
	cd admin-dashboard && npm run build

start:
	uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload

seed:
	python backend/scripts/seed_data.py

test:
	pytest backend/tests/ -v

lint:
	flake8 backend/app/ || true

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf dist build .next

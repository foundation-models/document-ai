
setup:
	pipx install uv pre-commit
	uv sync --python 3.10 --all-extras # install RAGFlow dependent python modules
	uv run download_deps.py
	pre-commit install
	docker build --platform linux/amd64 -f Dockerfile -t infiniflow/ragflow:nightly .
	cd web
	npm install
	echo remember to add to /etc/hosts: 127.0.0.1       es01 infinity mysql minio redis sandbox-executor-manager

run-servers:
	docker compose -f docker/docker-compose-base.yml up -d
	
run-api:
	echo "Running API server..."
	. .venv/bin/activate
	export PYTHONPATH=/home/agent/workspace/document-ai
	python3 -m api.ragflow_server 

run-ui:
	cd web && npm run dev


.PHONY: setup run-api run-ui run-servers
build:
	./build.sh

render-start:
	/opt/render/.local/bin/python3 -m gunicorn --chdir hexlet-code task_manager.wsgi

install:
	uv sync

collectstatic:
	python3 manage.py collectstatic --noinput

migrate:
	python3 manage.py migrate
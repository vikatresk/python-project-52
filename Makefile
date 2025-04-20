build:
	./build.sh

render-start:
	/opt/render/.local/bin/python3 -m gunicorn --chdir hexlet-code task_manager.wsgi

.PHONY: install format lint test

install:
	pip install -r requirements.txt

format:
	black .

lint:
	ruff .

test:
	pytest --nbval notebook.ipynb
	pytest test_script.py
	pytest test_lib.py

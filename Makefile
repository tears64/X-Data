install:
	python3 -m pip install -r requirements.txt
	python3 -m pip install -e .

test:
	python3 -m pytest

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py devopslib

test:
	python -m pytest -vv --cov=devopslib test_*.py 

format:
	black *.py devopslib/*.py

deploy:
	echo "deploy does here"

all: install lint test format deploy


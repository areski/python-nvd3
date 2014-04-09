.PHONY: docs release clean build

clean:
	rm -rf nvd3_env htmlcov

build:
	virtualenv nvd3_env && source nvd3_env/bin/activate && \
		pip install -r requirements.txt

test: clean build
		source nvd3_env/bin/activate && \
		coverage run --source=nvd3_env setup.py test && \
		coverage html && \
		coverage report

docs:
	sphinx-build -aE docs docs/html > /dev/null

.PHONY: docs release clean build install test

clean:
	rm -rf nvd3_env htmlcov

build:
	virtualenv nvd3_env && source nvd3_env/bin/activate && \
		pip install -r requirements.txt

test: install 
	python setup.py test

# assume that the developer already works with virtualenv
# or virtualenv-wrapper
install:
	python setup.py install

coverage: install
	coverage run --source=nvd3 setup.py test
	coverage report
	coverage html

docs:
	sphinx-build -aE docs docs/html > /dev/null

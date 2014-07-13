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
	rm -f docs/manutils.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ nvd3
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	#open docs/_build/html/index.html

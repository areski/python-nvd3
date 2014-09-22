.PHONY: docs release clean build install test

test: buildenv install
	. nvd3_env/bin/activate; python setup.py test

buildenv:
	virtualenv nvd3_env
	. nvd3_env/bin/activate; pip install -Ur requirements.txt

# assume that the developer already works with virtualenv
# or virtualenv-wrapper
install:
	. nvd3_env/bin/activate; python setup.py install

coverage: install
	coverage run --source=nvd3 setup.py test
	coverage report
	coverage html

docs: buildenv
	$(MAKE) -C docs;

clean:
	rm -rf nvd3_env htmlcov

cleanall: clean
	$(MAKE) -C docs clean

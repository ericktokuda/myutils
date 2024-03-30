all:

package:
	rm dist/ erikunicamp_* build/ -rf
	python3 setup.py sdist bdist_wheel
	python -m twine upload --repository pypi dist/* --verbose
test:
	py.test
clean:
	rm dist/ erikunicamp_* build/ -rf

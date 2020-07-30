all:

package:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
test:
	py.test
clean:
	rm dist/ erikunicamp_* build/ -rf

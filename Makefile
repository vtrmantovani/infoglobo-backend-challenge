clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f coverage.xml

test: clean
	nosetests -s --rednose

coverage: clean
	nosetests --with-coverage --cover-package=lbo

build-eb: clean
	if [ -a infoglobo-backend-challenge.zip ] ; then rm infoglobo-backend-challenge.zip ; fi;
	zip infoglobo-backend-challenge.zip -r * .[^.]*
	zip -d infoglobo-backend-challenge __MACOSX/\*
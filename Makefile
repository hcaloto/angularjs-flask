# -*- coding:utf-8 -*-
# AngularJS and Flask
#
# Makefile for developing purposes: uses ´nosetests´ and ´pychecker´
#

all: 
	@echo ' _____         _        '
	@echo '|_   _|__  ___| |_ ___  '
	@echo '  | |/ _ \/ __| __/ __| '
	@echo '  | |  __/\__ \ |_\__ \ '
	@echo '  |_|\___||___/\__|___/ '
	@echo '                        '
	@echo 'make test            - Run unit tests (using nosetests)'
	@echo 'make test-auth       - Run auth tests (authentication module)'
	@echo 'make test-users      - Run users tests (users module)'
	@echo 'make test-all        - Run all tests (using nosetests)'
	@echo 'make coverage        - Check code coverage (using nostests)'
	@echo 'make check           - Check Python code (using pychecker)'
	@echo 'make pylint          - Check and evaluate Python code (using pylint)'
	@echo 'make pep8            - Run PEP8 compliance tests (using pep8)'
test:
	nosetests -s -v --all-modules -a '!nodefault'
test-auth:
	nosetests -s -v --all-modules -a 'auth'
test-users:
	nosetests -s -v --all-modules -a 'users'
test-all:
	nosetests -s -v --all-modules --no-skip
check:
	pyflakes `find app -name '*.py'`
	pyflakes `find test -name '*.py'`
coverage:
	nosetests -s -v --all-modules -a '!nodefault' --with-coverage --cover-package=app --cover-html --cover-erase --no-skip
	@echo ' TO SEE DETAILED RESULTS: cd cover && python -m SimpleHTTPServer 8000'
pylint:
	pylint `find app -name '*.py'`
pep8:
	-pep8 -r --ignore=E501,E221,W291,W391,E302,E251,E203,W293,E231,E303,E201,E225,E261,E241 app

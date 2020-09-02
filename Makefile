NAME := racache
VERSION := 0.0.1

init:
	pip3 install -r requirements.txt

test:
	nosetests

lint:
	@echo '---PEP8---'
	@pep8 -v $(NAME)
	@echo '---pylint---'
	@pylint $(NAME)

.PHONY: create-remote-repo
create-remote-repo:
	hub -p create $(NAME)
	git push --set-upstream origin master

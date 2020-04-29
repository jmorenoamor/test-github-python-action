build:
	@docker build -t jmorenoamor/test-github-python-action:latest .

test:
	@docker run --rm jmorenoamor/test-github-python-action

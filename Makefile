black = black -S -l 120 --target-version py39

.PHONY: install
install:
	pip install --progress-bar off -r requirements.txt

.PHONY: black
black:
	$(black) tests/

.PHONY: lint
lint:
	flake8 tests/
	$(black) --check tests/

.PHONY: test
test:
	tox
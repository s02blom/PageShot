install:
	pip install playwright selenium pillow
	playwright install --with-deps chromium


playwright:
	python playwright/main.py $(URL)

page_stitch:
	python page_stitch/main.py $(URL)

selenium:
	python selenium/main.py $(URL)

example:
	python playwright/main.py http://www.python.org
	python page_stitch/main.py http://www.python.org
	python selenium/main.py http://www.python.org
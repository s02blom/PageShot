install:  ## Install all needed dependecies for project
	pip install playwright selenium pillow
	playwright install --with-deps chromium

playwright:  ## Run playwright implementation with make playwright URL=<WEBSITE>
	python playwright/main.py $(URL)

page_stitch: ## Run page stitch selenium implementation with make 
	python page_stitch/main.py $(URL)

selenium: ## Run base selenium implementation with make selenium URL=<WEBSITE>
	python selenium/main.py $(URL)

example: ## Run on an example page
	python playwright/main.py http://www.python.org
	python page_stitch/main.py http://www.python.org
	python selenium/main.py http://www.python.org	python selenium/main.py http://www.python.org# Thanks to Andreas Bauer
help: ## Show this help
	@grep -E '^[.a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
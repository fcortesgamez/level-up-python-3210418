# Makefile

# Set the PYTHONPATH to include the src directory
export PYTHONPATH := ./src

# Target to run all unit tests
test:
	@echo "Running unit tests..."
	python -m unittest discover -s tests -v

# Phony targets
.PHONY: test
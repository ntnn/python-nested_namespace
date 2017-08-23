PYLIB ?= $(patsubst python-%, %, $(notdir $(PWD)))
PYFILES := $(shell find $(PYLIB) -name '*.py' -not -name '*_test.py')

PYTHON ?= python3
VIRTUALENV ?= virtualenv --python=$(PYTHON)
VENVD ?= venv

ifeq "x$(VIRTUAL_ENV)" "x"
	V := . $(VENVD)/bin/activate
else
	V := true
endif

.PHONY: venv
venv:
	$(VIRTUALENV) $(VENVD)
	$(V) && pip install --editable '.[test]'
	@echo ">>> Execute '$(V)' to activate virtualenv"

.PHONY: venv-clean
venv-clean:
	rm -rf $(VENV_DIR)

.PHONY: test
test: $(PYLIB) | $(PYFILES)
	$(V) && pep8 $^
	$(V) && pylint --msg-template='{path}:{line}:{column}: [{msg_id}({symbol})], {obj}] {msg}' $^
	$(V) && pytest $(patsubst %, --cov=%, $^) $^

.PHONY: shell
shell:
	$(V) && ipython

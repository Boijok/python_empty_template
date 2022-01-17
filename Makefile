install_dev_environment_in_local:
	@brew update
	pyenv --version || @brew install pyenv
	pyenv install -s 3.8.10
	pyenv local 3.8.10
	poetry --version || @brew install poetry
	PYENV_PREFIX="pyenv prefix"
	poetry env use $(PYENV_PREFIX)"/bin/python"
	poetry install
	poetry run pre-commit install
	echo "Your local environment is ready \!"

test:
	poetry run python -m pytest tests

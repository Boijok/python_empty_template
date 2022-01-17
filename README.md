# Use of the Python empty template

### Introduction
The purpose of this repository is to provide a clean codebase for any python project.

It's build to help anyone who wants to to start quickly

Here is the list of the tools used by this project:
- Pycharm (IDE Recommended to develop in python but optional)
- pyenv (to install a specific version of python)
- poetry (to manage python project dependencies)
- pre-commit (to ensure some rules are respected before commit)
- pre-commit hooks: check-yaml, check-toml, end-of-file-fixer
- flake8 (linter)
- black (code style)
- mypy (static type checker)
- pydantic (data validation and settings management using python type annotations)


## Setting up your tools
### Setting up Pycharm

#### Setup your local env
copy everything in your new project
rename the 
Run the command `make install_dev_environment_in_local` in the pycharm terminal
Then
1. Open the pycharm preferences
2. Go to the Project section
3. Go to Project interpreter
4. Add the poetry env you just created
    - Retrieve the Path by running `poetry env info` and add `/bin/python` to it

# pytemplate

{{Description}}

## Using the Application

{{Documentation}}

## Setting up the Application

### Installation

Prerequisite: this application was built using Python {{VERSION}}, so it is encouraged to ensure this is the python version being used when creating the virtual environment in step 2. See [this article](https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/) for how to use different python versions with `venv`.

1. First, clone the repo

   ```bash
   git clone https://github.com/{{path/to/project}}.git
   cd {{project}}/
   ```

2. Setup the virtual environment

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Create your configuration file `config.py` and adjust any desired parameters within it.

   ```bash
   cp {{project}}/config.default {{project}}/config.py
   ```

4. Test to make sure everything is working.

   ```bash
   # Make sure your virtual environment is activated
   python main.py
   ```

### Running Tests

To run the tests from the root directory, use

```bash
pytest tests/
```

or

```bash
docker compose run tests
```

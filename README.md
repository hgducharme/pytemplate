# pytemplate

To make this boilerplate yours, complete the following checklist:

1. Create a virtual environment

   ```sh
   python3 -m venv env/
   source env/bin/activate
   ```

2. Install the requirements in requirements.txt

   ```sh
   pip install requirements.txt
   ```

3. Change this README file wherever you see text inside of double curly brackets "{{text}}", and change the top level header
4. Rename the `pytemplate/` directory to the name of your project
5. Create a completely empty repository on Github and push this repo

   ```sh
   git add .
   git commit -m "initial commit"
   git branch -M main
   git remote add origin git@github.com:{{username}}/{{project name}}.git
   git push -u origin main
   ```

6. Edit the pyproject.toml wherever you find "PROJECTNAME" or "VERSIONNUMBER"

6. Finally, delete this checklist and replace it with a brief description of your project. For example:

**pytemplate allows you to hit the ground running with your python project. Remove all the frustration of creating python boilerplate so you can instantly get to coding!**

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

### Running test coverage report

Generate a coverage report,

   ```bash
   coverage run -m pytest arg1 arg2 arg3
   ```

then print out the report

   ```bash
   coverage report -m
   ```

or export the report to an HTML file

   ```bash
   coverage html
   ```

 which can be opened in your browser.

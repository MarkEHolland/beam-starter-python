instructions

Create a virtual environment & run pipeline:
1) activate py3.8.10 in vscode n.b. check the version with: python -V
2) create environment: python -m venv .myenv
3) go to the folder where environment is: cd .myenv
4) activate environment: Scripts\activate
[Don't do this step 5 deactivate: deactivate]
5) cd ..
6) upgrade setuptools & wheel: python -m pip install --upgrade pip setuptools wheel
7) install requirements.txt packages: pip install -e .
8) test pipeline: python main.py --input-text="Greetings"

[9) run pipeline with pyenv as environment: C:/Users/marke/.pyenv/pyenv-win/versions/3.8.10/python.exe c:/Users/marke/projects/beam-starter-python/main.py]



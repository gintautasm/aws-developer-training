# aws-developer-training

### enable venv in python

```
cd some-dir
python -m venv venv
$ source venv/bin/activate
python -m pip install aws-cdk-lib
pip freeze > requirements.txt
pip install -r requirements.txt
deactivate # disable venv
```

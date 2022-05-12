# Fun with .env

Simple example of the usage of .env in Python

## Config Python:

```
python3 -m venv env
source env/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Create a local file with your secrets

Save your secrets in a file called `.env` like this:

```
MY_SECRET="this is my secret"
MY_OTHER_SECRET=3210
```

### Run the example

```
python3 main.py
```

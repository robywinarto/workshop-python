pip freeze > ~/Works/github/rw/workshop-python/requirements.txt
export ENV=dev
# python -m dnbapi.main --host 0.0.0.0 --port 5000
uvicorn userapi.main:app --reload --host 0.0.0.0 --port 5000 --log-level debug
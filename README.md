# gridAssignment

packages that need to be installed are:
pip install -r requirements.txt

if all these packages are installed then just type:
uvicorn router:app --reload

You well see message like this:
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [8160] using StatReload
INFO:     Started server process [15424]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

click on http://127.0.0.1:8000 and change the route to:
http://127.0.0.1:8000/docs

You will be able to see FastApi screen having create user and get user tabs.

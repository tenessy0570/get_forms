# How to start this project:<br>
Open two bash terminals. <br>
First is used to launch uvicorn, second is to launch test requests
1. `git clone https://github.com/tenessy0570/get_forms.git`
2. `cd get_forms/`
3. create virtualenv
4. activate virtualenv
5. `pip install -r requirements.txt`
6. `uvicorn server:app --reload`

#### Switch to another bash terminal

1. `cd get_forms/`
2. activate virtualenv
3. `python send_test_requests.py`

Look at console output
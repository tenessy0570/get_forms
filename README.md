# How to start this project:<br>
Open two bash terminals. <br>
First is used to launch uvicorn, second is to launch test requests
1. `git clone https://github.com/tenessy0570/get_forms.git`
2. create virtualenv
3. activate virtualenv
4. `pip install -r requirements.txt`
5. `python uvicorn server:app --reload`

#### Switch to another bash terminal

1. activate virtualenv
2. `python send_test_requests.py`

Look at console output
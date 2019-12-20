# ABBCTF_BusinessLogic
Business Logic task for ABB CTF 2019. The task is to solve 10000 systems of linear equations

Run locally:

pip3 install -r requirements.txt\
python3 server.py

Run in docker:

docker build -t business_logic .\
docker run --restart always -p 9020:9020 -d business_logic

# how to run

1. start redis server

2. start celery worker

celery -A tasks.app worker --loglevel=info

3. start the app

In another terminal
python run.py


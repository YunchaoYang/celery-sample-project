# run.py
from tasks import long_task
from celery.result import AsyncResult
import time

# Submit a job
result = long_task.apply_async((10,))  # 10 represents the number of iterations (simulated task duration)

print(f'Task submitted. Task ID: {result.id}')

# Check the status of the task
while not result.ready():
    print(f'Current status: {result.state} - {result.info}')
    time.sleep(1)

print(f'Task result: {result.result}')

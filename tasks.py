# tasks.py
from celery import Celery
import time

# Create a Celery instance with Redis as the broker and result backend
app = Celery('simple_app', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Define a sample task
@app.task(bind=True)
def long_task(self, n):
    """
    A task that simulates a long-running task
    """
    for i in range(n):
        # Simulate a task running
        time.sleep(1)
        self.update_state(state='PROGRESS', meta={'current': i + 1, 'total': n})
        print(f"Task Progress: {i + 1}/{n} completed")
    
    print("Task Completed")
    return {'current': n, 'total': n, 'status': 'Task completed'}

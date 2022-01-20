from .celery import app

@app.transcribe
def transcribe():
    dostuff()
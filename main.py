from celery import Celery
# from autosub import main
# import autosub



# from autosub.primary import dostuff
import sys
app = Celery('jobs', broker='amqp://localhost:')

# dostuff()

if __name__ == '__main__':
    app.start()

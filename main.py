from flask import Flask
import logging
from logging.handlers import TimedRotatingFileHandler
import os

app = Flask(__name__)
# log_file,when="s",interval=2,backupCount=5
# set up logging

log_file = os.path.join(os.getcwd()+"/logs", 'app.log')
handler = TimedRotatingFileHandler(log_file,when="s",interval=2,backupCount=5 )

# daily rotation stores files for 30 days
# handler = TimedRotatingFileHandler(log_file, when='midnight', backupCount=30)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    app.logger.info('Hello, world!')
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
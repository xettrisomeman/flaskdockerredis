import time

import redis 
from flask import Flask 


app = Flask(__name__)
redisClient = redis.Redis(host='redis')

def get_hit_count():

    retries= 5
    while True:
        try:
            return redisClient.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc 
            retries -=1
            time.sleep(0.5)


@app.route('/')
def hello():
    count= get_hit_count()
    return f"Hello world ! I have been seen {count} times."



if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)


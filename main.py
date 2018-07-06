import json

import flask
import redis
import requests
from flask import Flask

from tracer import init_tracer

GET_DATA_FROM_REPO_URL = "http://localhost:8001/proxy-github/{}"
REDIS_KEY_CLEAN_DATA = "clean-data-from-git"
REDIS_KEY_CLEAN_DATA_RETURN = "clean-data-from-git-{}"

app = Flask(__name__)
tracer = init_tracer("gateway")
redis_client = redis.Redis()


def redis_push_data(data, repo_name):
    msg = {"queue_to_return_msg": REDIS_KEY_CLEAN_DATA_RETURN.format(repo_name), "data": data}
    redis_client.rpush(REDIS_KEY_CLEAN_DATA, json.dumps(msg))


def redis_read_data(repo_name):
    jsonify_clean_data = redis_client.blpop(REDIS_KEY_CLEAN_DATA_RETURN.format(repo_name))[1]
    return json.loads(jsonify_clean_data)


@app.route("/git/<owner>/<repo>")
def main(owner=None, repo=None):
    with tracer.start_span('main-context') as main_span:
        repo_name = "{}/{}".format(owner, repo)
        main_span.set_tag("repo_name", repo_name)
        repo_contributors = requests.get(GET_DATA_FROM_REPO_URL.format(repo_name)).json()
        redis_push_data(repo_contributors, repo_name)
        data = redis_read_data(repo_name)
        return flask.jsonify(**data, indent=2)


if __name__ == "__main__":
    app.run(threaded=False, port=8000)

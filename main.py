import json

import flask
import redis
import requests
from flask import Flask
from opentracing import Format
from opentracing.ext import tags

from tracer import init_tracer

GET_DATA_FROM_REPO_URL = "http://localhost:8001/proxy-github/{}"
REDIS_KEY_CLEAN_DATA = "clean-data-from-git"
REDIS_KEY_CLEAN_DATA_RETURN = "clean-data-from-git-{}"

app = Flask(__name__)
tracer = init_tracer("gateway")
redis_client = redis.Redis()


def http_get(span, url):
    span.set_tag(tags.HTTP_METHOD, 'GET')
    span.set_tag(tags.HTTP_URL, url)
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    headers = {}
    tracer.inject(span, Format.HTTP_HEADERS, headers)
    r = requests.get(url, headers=headers)
    return r.json()


def redis_push_data(span, data, repo_name):
    msg = {}
    span.set_tag("QUEUE_NAME", REDIS_KEY_CLEAN_DATA)
    span.set_tag(tags.SPAN_KIND, "producer")
    headers = {}
    tracer.inject(span, Format.TEXT_MAP, headers)
    msg["headers"] = headers
    msg["queue_to_return_msg"] = REDIS_KEY_CLEAN_DATA_RETURN.format(repo_name)
    msg["data"] = data
    redis_client.rpush(REDIS_KEY_CLEAN_DATA, json.dumps(msg))


def redis_read_data(repo_name):
    jsonify_clean_data = redis_client.blpop(REDIS_KEY_CLEAN_DATA_RETURN.format(repo_name))[1]
    return json.loads(jsonify_clean_data)


@app.route("/git/<owner>/<repo>")
def main(owner=None, repo=None):
    with tracer.start_span('main-context') as main_span:
        repo_name = "{}/{}".format(owner, repo)
        main_span.set_tag("repo_name", repo_name)
        with tracer.start_span('get-data-from-github-proxy', child_of=main_span) as span_get_data:
            repo_contributors = http_get(span_get_data, GET_DATA_FROM_REPO_URL.format(repo_name))
            print(repo_contributors)
        with tracer.start_span('push-data-to-clean-redis', child_of=main_span) as span_push_redis:
            redis_push_data(span_push_redis, repo_contributors, repo_name)
        with tracer.start_span('read-data-from-clean-redis', child_of=main_span) as span_read_redis:
            data = redis_read_data(repo_name)
        # contributors_commits = get_contributors_to_commit(repo_contributors)
        return flask.jsonify(**data, indent=2)


if __name__ == "__main__":
    app.run(threaded=False, port=8000)

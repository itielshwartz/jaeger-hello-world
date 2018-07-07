import json

import redis
from opentracing import Format
from opentracing.ext import tags

from bad_things import bad_thing_1
from tracer import init_tracer

tracer = init_tracer("clean-github-data")

redis_client = redis.Redis()
REDIS_KEY_CLEAN_DATA = "clean-data-from-git"
REDIS_KEY_CLEAN_DATA_RETURN = "clean-data-from-git-{}"


def clean_github_data():
    while True:
        raw_msg = redis_client.blpop(REDIS_KEY_CLEAN_DATA)[1]
        msg = json.loads(raw_msg)
        repo_contributors = msg["data"]
        queue_to_return_msg = msg["queue_to_return_msg"]
        headers = msg["headers"]
        span_ctx = tracer.extract(Format.TEXT_MAP, headers)
        span_tags = {tags.SPAN_KIND: "consumer"}
        with tracer.start_span("extracting_contributors_to_commit", child_of=span_ctx, tags=span_tags) as span:
            contributors_to_commit = {}
            span.log_kv({"repo_contributors_size": len(contributors_to_commit)})
            for contribute in repo_contributors:
                bad_thing_1()
                username = contribute["author"]["login"]
                contributors_to_commit[username] = sum((week["c"] for week in contribute["weeks"]))
            redis_client.rpush(queue_to_return_msg, json.dumps(contributors_to_commit))


if __name__ == "__main__":
    clean_github_data()

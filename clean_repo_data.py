import json

import redis

from bad_things import bad_thing_1

redis_client = redis.Redis()
REDIS_KEY_CLEAN_DATA = "clean-data-from-git"
REDIS_KEY_CLEAN_DATA_RETURN = "clean-data-from-git-{}"


def clean_github_data():
    while True:
        raw_msg = redis_client.blpop(REDIS_KEY_CLEAN_DATA)[1]
        msg = json.loads(raw_msg)
        repo_contributors = msg["data"]
        queue_to_return_msg = msg["queue_to_return_msg"]
        contributors_to_commit = {}
        for contribute in repo_contributors:
            bad_thing_1()
            username = contribute["author"]["login"]
            contributors_to_commit[username] = sum((week["c"] for week in contribute["weeks"]))
        redis_client.rpush(queue_to_return_msg, json.dumps(contributors_to_commit))


if __name__ == "__main__":
    clean_github_data()

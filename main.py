import flask
import requests
from flask import Flask

from bad_things import bad_thing_0, bad_thing_1

get_repo = "https://api.github.com/repos/{}/stats/contributors"
app = Flask(__name__)


def get_repo_contributors(repo_and_owner):
    url = get_repo.format(repo_and_owner)
    bad_thing_0(url)
    return requests.get(url)


def clean_github_data(repo_contributors):
    contributors_to_commit = {}
    bad_thing_1()
    for contribute in repo_contributors:
        username = contribute["author"]["login"]
        contributors_to_commit[username] = sum((week["c"] for week in contribute["weeks"]))
    return contributors_to_commit


@app.route("/git/<owner>/<repo>")
def main(owner=None, repo=None):
    repo_name = "{}/{}".format(owner, repo)
    repo_contributors = get_repo_contributors(repo_name).json()
    contributors_commits = clean_github_data(repo_contributors)
    return flask.jsonify(**contributors_commits, indent=2)


if __name__ == "__main__":
    app.run(threaded=False, port=8000)

import flask
import requests
from flask import Flask

from bad_things import bad_thing_0

get_repo = "https://api.github.com/repos/{}/stats/contributors"
app = Flask(__name__)


@app.route("/proxy-github/<owner>/<repo>")
def get_repo_contributors(owner=None, repo=None):
    owner_and_repo = "{}/{}".format(owner, repo)
    github_request_url = get_repo.format(owner_and_repo)
    bad_thing_0(github_request_url)
    resp = requests.get(github_request_url)
    return flask.jsonify(resp.json())


if __name__ == "__main__":
    app.run(threaded=False, port=8001)

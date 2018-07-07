import flask
import requests
from flask import Flask
from opentracing_instrumentation.request_context import get_current_span, span_in_context

from bad_things import bad_thing_0, bad_thing_1
from tracer import init_tracer

get_repo = "https://api.github.com/repos/{}/stats/contributors"
app = Flask(__name__)

tracer = init_tracer("gateway")


def get_repo_contributors(repo_and_owner):
    with tracer.start_span("get_repo_contributors", child_of=get_current_span()) as span:
        url = get_repo.format(repo_and_owner)
        span.set_tag("github_request_url", url)
        bad_thing_0(url)
        return requests.get(url)


def clean_github_data(repo_contributors):
    with tracer.start_span("clean_github_data", child_of=get_current_span()) as span:
        contributors_to_commit = {}
        bad_thing_1()
        span.log_kv({"repo_contributors_size": len(contributors_to_commit)})
        for contribute in repo_contributors:
            username = contribute["author"]["login"]
            contributors_to_commit[username] = sum((week["c"] for week in contribute["weeks"]))
        return contributors_to_commit


@app.route("/git/<owner>/<repo>")
def main(owner=None, repo=None):
    with tracer.start_span('main-context') as span:
        repo_name = "{}/{}".format(owner, repo)
        span.set_tag("repo_name", repo_name)
        with span_in_context(span):
            repo_contributors = get_repo_contributors(repo_name).json()
            contributors_commits = clean_github_data(repo_contributors)
            return flask.jsonify(**contributors_commits, indent=2)


if __name__ == "__main__":
    app.run(threaded=False, port=8000)

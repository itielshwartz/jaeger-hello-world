import flask
import requests
from flask import Flask, request
from opentracing import Format
from opentracing.ext import tags

from bad_things import bad_thing_0
from tracer import init_tracer

get_repo = "https://api.github.com/repos/{}/stats/contributors"
app = Flask(__name__)
tracer = init_tracer("github-proxy")


@app.route("/proxy-github/<owner>/<repo>")
def get_repo_contributors(owner=None, repo=None):
    span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
    span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
    with tracer.start_span("getting-repo-data-from-github", child_of=span_ctx, tags=span_tags) as span:
        owner_and_repo = "{}/{}".format(owner, repo)
        github_request_url = get_repo.format(owner_and_repo)
        span.set_tag("github_request_url", github_request_url)
        bad_thing_0(github_request_url)
        resp = requests.get(github_request_url)
        return flask.jsonify(resp.json())


if __name__ == "__main__":
    app.run(threaded=False, port=8001)

Step 5 Tags and Logs
====================

In this part we are going to add tags and logs to our web-app.

---

1. We added log to our span:
    ```python
    span.log_kv({"repo_contributors_size": len(contributors_to_commit)})
    ```

2. Then we added new span for both functions (while refrence thd main span):
    ```python
    span.set_tag("github_request_url", github_request_url)
    ```

To run
------

* Run the server
    ```bash
    python main.py
    ```
* Try and access both pages at the same time:
* http://127.0.0.1:8000/git/fluent/fluentd
* http://127.0.0.1:8000/git/pallets/flask

Ok now we can check the jaeger UI!
* Check the Jaeger UI at http://localhost:16686

Great not we can also wee what's the url of the bad request -
https://api.github.com/repos/fluent/fluentd/stats/contributors

`Mystery solved!`

But didn't we talked about distbuted system?

Next step
---------
[Step 6 - Distribute single span](https://github.com/itielshwartz/jaeger-hello-world/tree/step-6-distribute-single-span)

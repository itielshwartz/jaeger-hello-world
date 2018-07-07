Step 4 Multiple spans
=====================

In this part we are going to add multiple spans to our web-app.

---

1. We added the span to our app context (so we can refrence it in other functions)
    ```python
    with span_in_context(span):
    ```

2. Then we added new span for both functions (while refrence thd main span):
    ```python
    with tracer.start_span("clean_github_data", child_of=get_current_span()) as span:
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

Great not we can see what function took more time `get_repo_contributors`!

But which request caused it?

Next step
---------
[Step 5 - Tags and logs](https://github.com/itielshwartz/jaeger-hello-world/tree/step-5-tags-and-logs)

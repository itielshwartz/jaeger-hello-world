Step 7 Distribute multiple spans
================================

In this part we moved our trace data across all of our service.

This allow us to track a single request across all of the services we are using.

What was done
-------------
1.We added the trace to the requests header:
```python
    span.set_tag(tags.HTTP_METHOD, 'GET')
    span.set_tag(tags.HTTP_URL, url)
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    headers = {}
```
2.We use those headers in the other server:
```python
    span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
    span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
    with tracer.start_span("getting-repo-data-from-github", child_of=span_ctx, tags=span_tags) as span:
```
3.We add the trace to the redis request:
```python
    span.set_tag("QUEUE_NAME", REDIS_KEY_CLEAN_DATA)
    span.set_tag(tags.SPAN_KIND, "producer")
    headers = {}
    tracer.inject(span, Format.TEXT_MAP, headers)
```
4.We use those headers in the redis consumer:
```python
    headers = msg["headers"]
    span_ctx = tracer.extract(Format.TEXT_MAP, headers)
    span_tags = {tags.SPAN_KIND: "consumer"}
    with tracer.start_span("extracting_contributors_to_commit", child_of=span_ctx, tags=span_tags) as span:
```


To run
------

* Run the servers
    ```bash
    (python main.py & python get_repo_data.py & python clean_repo_data.py)
    ```
* Try and access both pages at the same time:
* http://127.0.0.1:8000/git/fluent/fluentd
* http://127.0.0.1:8000/git/pallets/flask

Ok now we can check the jaeger UI!
* Check the Jaeger UI at http://localhost:16686

For the first time we can see a full trace with data from coming from multiple services.
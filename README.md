Step 7 Distribute multiple spans
================================

In this part we moved our trace data across all of our service.

This allow us to track a single request across all of the services we are using.


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
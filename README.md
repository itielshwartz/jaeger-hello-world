Step 6 Distribute single span
=============================

In this part we seprated our **HUGE** monolith into microservices.
* Microservice A - main the gateway
* Microservice B - the github proxy - get the repo data
* Microservice C - clean the github data

`Client -Http-> service A -Http-> Service B -> Service A -Redis-> Service B -Redis-> Service A -> Client`


To run
------

* Run the server
    ```bash
    (python main.py & python get_repo_data.py & python clean_repo_data.py)
    ```
* Try and access both pages at the same time:
* http://127.0.0.1:8000/git/fluent/fluentd
* http://127.0.0.1:8000/git/pallets/flask

Ok now we can check the jaeger UI!
* Check the Jaeger UI at http://localhost:16686

Sadly we see only one service (the main)...

But again **didn't we talked about distbuted system?**

Next step
---------
[Step 7 - Multiple spans](https://github.com/itielshwartz/jaeger-hello-world/tree/step-7-distribute-multiple-spans)

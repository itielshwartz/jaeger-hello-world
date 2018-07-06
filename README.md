Step 3 Adding jaeger
====================

In this part we are going to add jaeger to our web-app.

---

1. We added `tracer.py` -> a jaeger client basic config.

2. Then we added it to the start of our web-server :
    ```python
        with tracer.start_span('main-context') as span:
    ```

To run
------

* Run the jaeger all-in-one docker:
    ```bash
    docker run -d -p5775:5775/udp -p6831:6831/udp -p6832:6832/udp \
      -p5778:5778 -p16686:16686 -p14268:14268 -p9411:9411 \
      jaegertracing/all-in-one:1.5.02
     ```
* Run the server
    ```bash
    python main.py
    ```
* Try and access both pages at the same time:
* http://127.0.0.1:8000/git/fluent/fluentd
* http://127.0.0.1:8000/git/pallets/flask

Ok now we can check the jaeger UI!
* Check the Jaeger UI at http://localhost:16686

We can see one request took much more time then the other -
But why?

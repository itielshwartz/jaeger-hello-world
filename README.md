Step 2 the monolith going wild
==============================

In this part we add two simple functions to our main app:
```python
from bad_things import bad_thing_0, bad_thing_1
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

Ok both requests seems slow... but why?

Next step
---------
[Step 3 - Adding Jaeger](https://github.com/itielshwartz/jaeger-hello-world/tree/step-3-adding-jaeger)

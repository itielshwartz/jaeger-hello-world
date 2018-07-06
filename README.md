Step 1 the monolith
===================

In this part all we have is a simple flask server.

The server get the a owner and and github repo.

It return a Json with the username: number of commits for all of the repo commiters.

To run
------

* Run the server
    ```bash
    python main.py
    ```
* Check it out:
* http://127.0.0.1:8000/git/fluent/fluentd
* http://127.0.0.1:8000/git/pallets/flask
Jaeger hello world
==================

This tutorial is a full walkthrough about using jaeger.

It is based on the (great) [opentracing-tutorial](https://github.com/yurishkuro/opentracing-tutorial/tree/master/python).

Game plan
---------

First we will build a monolith demo app.
And will graduely improve it by adding more logs, tracking and jaeger capabilties.

Prerequisites
-------------

* Clone the repo
    ```bash
    git clone git@github.com:itielshwartz/jaeger-hello-world.git
    ```
* Have a docker installed
* Have a virtulenv installed
     ```bash
        python3 -m venv venv && source venv/bin/activate
     ```
 * Install the requirements
     ``` bash
        pip install requirements.txt
    ```
            
The walkthrough
---------------
[Step 1 - The monolith](https://github.com/itielshwartz/jaeger-hello-world/tree/step-1-the-monolith)

[Step 2 - The monolith going wild](https://github.com/itielshwartz/jaeger-hello-world/tree/step-2-the-monolith-going-wild)

[Step 3 - Adding Jaeger ](https://github.com/itielshwartz/jaeger-hello-world/tree/step-3-adding-jaeger)

[Step 4 - Multiple spans](https://github.com/itielshwartz/jaeger-hello-world/tree/step-4-multiple-spans)

[Step 5 - Tags and logs](https://github.com/itielshwartz/jaeger-hello-world/tree/step-5-tags-and-logs)

[Step 6 - Distribute single span](https://github.com/itielshwartz/jaeger-hello-world/tree/step-6-distribute-single-span)

[Step 7 - Multiple spans](https://github.com/itielshwartz/jaeger-hello-world/tree/step-7-distribute-multiple-spans)



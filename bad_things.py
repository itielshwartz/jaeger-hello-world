import time


def bad_thing_0(github_request_url):
    print(len(github_request_url) % 2)
    if len(github_request_url) % 2 == 0:
        time.sleep(5)


def bad_thing_1():
    pass

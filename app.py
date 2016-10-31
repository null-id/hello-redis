#!/usr/bin/env python
# coding=utf-8

from redis import Redis
from flask import Flask

app = Flask(__name__)
redis = Redis(host="127.0.0.1", port=6379)

@app.route("/<int:id>")
def page(id):
    redis.incr(str(id))
    return "page with id {0} views {1} time(s)".format(id, redis.get(str(id)))


if __name__ == "__main__":
    app.debug=True
    app.run()

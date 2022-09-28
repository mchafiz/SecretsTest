#!/usr/bin/python
# coding: utf-8
from flask import Flask
import config
import requests
import psycopg2
import redis

app = Flask(__name__)

@app.route('/req_1')
def req_one():
    # hardcoded api secret in obvious header
    headers = {'X-API-KEY' : 'CkSaSTFTEJ4BSpSAULQJBvpc586JhCxT'}
    results = requests.get('https://bonjarber.com/', headers=headers)
    return results.text


@app.route('/pos_2')
def pos_2():
    # config secret in postgres connection
    conn = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="vsecret")
    return conn

@app.route('/red_1')
def red_one():
    # config secret in redis connection
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, password=config.SOURCE_2)
    return redis_db

@app.route('/red_2')
def red_2():
    # hardcoded secret in redis connection
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, password='redis')
    return redis_db

@app.route('/')
def entry_point():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
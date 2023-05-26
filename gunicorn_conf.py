import os
import multiprocessing

bind = '0.0.0.0:8000'
loglevel = 'debug'
errorlog = '-'
accesslog = '-'

workers = os.environ.get('WORKERS', 2)
preload = True
reload = True
worker_class = os.environ.get('WORKER_CLASS', 'gevent')
keepalive = 60
timeout = int(os.environ.get('GUNICORN_TIMEOUT', 30))  # 30 is standard default

access_log_format = '{Client-IP: %({X-Real-IP}i)s, Request-time: %(L)s, Request-date: %(t)s, HTTP-Status: "%(r)s", HTTP-Status-Code: %(s)s, Response-length: %(b)s, Http-Referrer: %(f)s, User-Agent: %(a)s}'
import multiprocessing

bind = "0.0.0.0:80"
worker_class = "uvicorn.workers.UvicornWorker"
workers = multiprocessing.cpu_count()
threads = 2

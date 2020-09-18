import docker 
from celery import Celery



app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379/0')
client = docker.from_env()


@app.task
def create():

    container = client.containers.run("bfirsh/reticulate-splines", detach=True)
    
    return  client.containers.list()

@app.task
def get_all_containers():
    return  client.containers.list()

@app.task
def stop(containerName):
    for container in client.containers.list():
        if container.name == containerName:
            container.stop()
            
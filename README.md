# peewee-flask-demo

### Building our Container
```
docker build -t flask-demo:latest .
```

### Running our Container
```
docker stop flask-app

docker run -d -p 5000:5000 flask-demo

docker run --rm -d --name flask-app -p 5000:5000 --privileged --user root flask-demo
```

### View Container
```
docker ps
```

### View Logs
```
docker logs flask-app
```

### Viewing Application
View [app](http://127.0.0.1:5000) local machine by visiting `127.0.0.1:5000`


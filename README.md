# Docker Training

## Flask Demo

Run the demo:

```
docker run -d -p 80:5000 skipperkongen/flaskdemo
open http://localhost
```

Build and run the demo

```
cd flaskdemo
docker build . -t flaskdemo
docker run -d -p 80:5000 flaskdemo
# open http://localhost
```

### monitor the network I/O on the flaskdemo container

Run an alpine container with attached network interface:

```
# Get ID of running flaskdemo container
docker ps
# Open shell in alpine and attach other container's network interface
docker run -it --net container:<id-of-other> alpine
```

In alpine container's shell

```
# apk add ngrep
# ngrep -tpd any
```

# Introduction

## VM vs Docker

- Virtual machine runs on hypervisor (vmware or vitualbox)
- VM's are slow, needs full OS, takes lot of resources
- Docker runs on host Operating system, provides isolation to run multiple apps and lightweight
- Fast and takes up lesshardware resources

## Architecture
- Docker runs on client server architecture, connects to server (Docker Engine) via REST API
- Container is just like a process on Operating system, which connects to hardware via common kernel

## Docker commands
- Download image from hub, Start a container,if not found locally automatically pulls from dockerhub and runs it
    > docker pull alpine

    > docker run image
- list running containers with info such as cotainer_id, Imagename, status, ports
    > docker ps

    > docker ps -a
- Stop container 
    > docker stop container_id or name
- permanently remove stopped container
    > docker rm beautiful_liskov

    > docker container remove beautiful_liskov
- list local images of docker
    > docker images
- removes docker image
    > docker rmi ubuntu

    > docker image remove ubuntu
- execute commands on container
    > docker exec beautiful_liskov cat /etc/hosts

## Other Features
- portmapping using -p while running docker, 80 of host is mapped to 5000 of container
    >docker run -p 80:5000
- volume mapping, saving data on host, if container is deleted
    >docker run -v opt/data:/var/lib/mysql
- inspect details of the container json format
    >docker inspect b843ceb491f6
- run container in background in detached mode
    > docker run -d image

    > docker logs container_id

## Dockerfile 
Contains instructions to build an image
- FROM -> to import from docker hub 
- COPY -> copy files from local directory to container
- ADD -> Same as copy but also supports url and decompress the compressed files(zip)
- WORKDIR -> SET Working directory
- CMD -> command to run on container
- RUN -> executiong OS commands(On terminal)
- ENV -> Setting up environment variables
- EXPOSE -> Documenting on which port the container will eventually run
- USER - user that should run the application

## Creating Docker Image
- install docker
- docker build -t hello-docker .
    - -t is for tag
    - hello-docker is name for repository
    - . specifies to take files from current directory
- docker images -> lists all the docker images on system
- docker run hello-docker

## Docker commands
- docker ps     -> see running containers
- docker ps -a  -> we can see stopped containers as well
- docker run ubuntu -> runs ubuntu on container, pulls from docker hub if not preent on local machine
- docker run -it ubuntu -> interactive terminal mode
    - echo hello world
    - whoami

## Docker Image
- Dockerfile packages our application to an image, which contains
    - an operating system
    - runtime environment eg.python or node
    - application files
    - third party libraries
    - environment varibles
    
## Container
- Container is a process which runs image
    - Provides an isolated environment for executing applications
    - can be stopped and restarted
    - just an OS process, but has its own file system provided by image
    - An image can have multiple containers and each container is isloated from others
---
# Linux 
## Linux File system
- / -> root
    - /bin -> contains binary files/programs
    - /boot -> files necessary for boot
    - /dev -> files for devices
    - /etc -> editable text configs
    - /home -> home directory for all users
    - /root -> home directory of root user only root user can access
    - /lib -> software libraries
    - /var  -> Variables
    - /proc -> contains files representing running processes

## Linux commands
Run ubuntu on interactive terminal mode
>docker run -it ubuntu
- apt -> advance package tool (package manager)
- apt update -> updates repository database
- apt install python3
- apt autoremove python3 -> removes packages along with installed dependencies
- echo, ls, pwd, cd, cat, less, more, > , <
- mkdir, rm, mv, cp, touch
- head, tail, less, more
- find -> recursively lists all files in current directory
    - find -type d -name fi*
    - find / -type f -name "*.py" > pyfiles.txt
- mkdir test ; cd test ; echo done -> multiple commands in one line
- && to stop if one command fails, || executes next only if first fails
- ls /bin | less
- grep (global regular expreession print), i for case insensitive
    - grep -i hello file.txt
    - grep -ir hello . ->recursive searching for hello in all files of current directory
- users and groups
    - useradd -m alice
    - >docker exec -it 433100e81f4c bash
    - usermod -s /bin/bash alice
    - > docker exec -it -u alice 433100e81f4c bash
    - add user bob (interactive)
    - userdel bob
    - groupadd developers
    - usermod -G developers alice
    - groups alice
    - chmod ugo+x hello.sh
- ps -> running processes
    - pid -> process Id
    - TTY -> telety tells if any terminal interface is used
    - pts - psuedo terminal
    - kill pid -> kills process
- printenv -> all the evironmet variables
    - prinenv PATH
    - export user=alice
    - printenv user
    - echo $user
    - .bashrc -> permanent user env variables
    - *user=alice >> .bashrc*   -> adding permanent env variable
    - source ~/.bashrc  -> reflecting changes without starting new term session
    - $user -> prints alice
---
# Docker
Create a simple flask app
- app.py
- requirements.txt
- Dockerfile
- .dockerignore
## Dockerfile
Below contents of Dockerfile

```
FROM python:3.9.4-alpine3.12
RUN addgroup app && adduser -S -G app app
USER app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

- Creating a group and user and running application with user for security, users list stored in /etc/passwd and groups in /etc/group
- Creating group app and creating system user with primary group as app
- RUN is a build instruction (executed while building an image)
- CMD is Runtime instruction (executed while starting container)
    - Shell form 
        >CMD python app.py
    - Exec form -> Fast as it does not start any shell process (Preferred)

        > CMD ["python", "app.py"]
    - if multiple CMD instructions are set only last one is executed

- ENTRYPOINT same as CMD & have 2 forms as CMD
    - if multiple ENTRPOINT instructions are set only last one is executed

        > ENTRYPOINT ['python", "app.py"]
    - Can be overridden while starting container
        > docker run -it --entrypoint sh suspicious_wilbur

## DockerImage
- An image is a collection of layers, A new layer is created after each instruction is executed
- When we rebuild the image, if nothing is changed the layer is taken from layer cache
- if a slight modification is found that instruction and all below are reexcuted completely and layers are rebuilt.

    ```
    #Dockerfile
    FROM python:3.9.4-alpine3.12
    RUN addgroup app && adduser -S -G app app
    USER app
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["python", "app.py"]
    ```

- build time can be saved by taking requirements above copying other application files, since they might change frequently

## Removing Images Containers
### Dangling images
- the images created after modifying the existing image, and have no name.can be removed by
    > docker image prune
- All the stopped contaners can be removed by
    > docker container prune
### Images
- to remove saved images
    > docker image rm image_id/image_name

    > docker rmi image_id/image_name
- multiple images can be deleted by giving space after each name
- prunes all stopped containers, all the networks not used by any container, dangling images, build cache
    > docker system prune

## Tags
- tags can be used as version identifier
    > docker build -t web-app .

    > docker buld -t web-app:1 .
- Both images have same image id but different tag, tagged image can be removed
    > docker image rm web-app:1
- Tagging after image is build
    > docker tag web-app:latest web-app:new

    > docker tag web-app:3 web-app:latest

## Sharing images
- create a repository on dockerhub
    ```
    > docker build -t web-app:3 .
    > docker tag web-app:3 ganeshchennuri/web-app:3
    > docker login
    > docker push ganeshchennuri/web-app:3
    ```
### Saving and loading images
- Image can be saved as compressed file
    > docker image save --help

    > docker image save -o web-app.tar web-app:3 

- Images can be loaded from compressed files

    >docker image load web-app.tar

## Containers
- running containers
    > docker run web-app:3

- runing in detached mode
    > docker run -d web-app:3

- specifying name for container
    > docker run --name flaskapp web-app:3
- logs
```
    > docker logs --help
    > docker logs container_id 
    > docker logs -f container_id -> realtime logs
    > docker logs -n container_id -> last 10 logs
    > docker logs -t container_id -> shows timestamp
```
- port publishing
    > docker run -d -p 80:5000 --name flask-app web-app:3
- executing commands in running container
    > docker exec -it flask-app sh

- starting and stopping containers, docker run starts new container
    > docker stop flask-app

    docker start -> starts and existing container

    > docker start flask-app

- removing
    > docker conatiner remove/rm container_id

    > docker rm flask-app
    
    force remove running container
    > docker rn -f flask-app

- delete stopped containers
    > docker container prune

- Other Features for linux container
    > docker ps -a | grep flask

## Networking

- By default comes with 3 networking drivers bridge, host & none. Network is created after runnng docker compose
    > docker network ls
    1. Bridge -> internal network created by docker on host 172.17.0.1/255, all containers assgned ip in same series, can be accessed on host by port mapping
    2. none - all the containers are completely isolated, no external network
    3. host - ports are directly mapped to host, so we cannot run same application multiple times, since portnumbers would be same and points to host directly
- we can set network while running container, by default it takes bridge
    > docker run ubuntu --network=host

- we can create a network with different subnet
    > docker network create --driver bridge --subnet 182.0.0/16 private_network
- inspecting conainer we can see network type, ip & mac address
    >docker inspect container_name
- Docker comes with embedded dns server, contains name and ip of the containers. Each container has component called dnsresolver, maps ip of the container.

## File System
```
/var/lib/docker/
  |- aufs
  |- containers
  |- images
  |_ volumes
```
- image is built by layers i.e image layers (read-only), when we run an image a container layer is ran on top of image.
- Deleting containers, data inside containers also deleted

## Volumes   
voume mount can be used to save data from container on host,
bind mount can be used to mount directory from host to container
> docker volume create app-data

> docker volume inspect app-data

Output shows driver as local, for cloud it would be different, mount point shows storage path of volume on host machine

```
[
    {
        "CreatedAt": "2021-04-29T13:10:14Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/app-data/_data",
        "Name": "app-data",
        "Options": {},
        "Scope": "local"
    }
]
```

if volume is not created already it will be automatically created with root user permissions and only read access available to our app user
> docker run -d --name web -p 5000:5000 -v app-data:/app/data web-app:latest

Antoher way of mounting volumes is, mounting db from data/mysql on host to container
> docker run --mount type=bind source=/data/mysql,target=/var/lib/mysql mysql

Copying files to and from containers

> docker cp dc1a835adbfb:/app/data/data.txt .

> docker cp f.txt dc1a835adbfb:/app/data

## Storage drivers
- AUFS(ubuntu), ZFS, BTRFS, Device Mapper, Overlay, Ovrlay2
### Sharing source code

    By using bind mapping we can share codemwith application running on container, without rebuilding image or copying files to container.
    for applications like react where hot reloading feature is available changes are reflected

> docker run -d -p 80:5000 -v $(pwd):/app web-app

## Docker Engine

- Docker daemon -> background process that manages docker objects (images, containers, volumes, network)
- REST API (Interface talking to daemon)
- Docker CLI (cli uses Rest api to talk to deamon), cli can be used on any host
    > docker -H=12.123.1.2:2375 run nginx

### namespaces
- Containers uses namspaces to isolate workspaces (pid, network, mount,etc)
- Suppose ngnix server is ran on container & it tkes PID 1 on container, it is mapped on host to different PID but same service
### cgroups
Docker has no limit of usage of hardware resources on host, can be restricted by cgroups
> docker run --cpus=0.5 ubuntu

> docker run --memory=100m ubuntu

#### Note
- removing all containers and images at once,backquoted statements run as commands
    > docker stop `docker container ls -q`

    > docker container rm -f $(docker container ls -aq)

    > docker image rm -f $(docker image ls -q)

## Docker Compose
Applications have front-end, backend and database services which needs to be run on different ports and need to execute multiple commands to build or run that image

```
version: "3.8"
services:
    web: 
        build: ./frontned
        ports: 
            - 3000:3000
    api: 
        build: ./backend
        ports: 
            - 3001:3001
    db: 
        image: mongo:4.0-xenial
        environment:
            DB_URL: mongodb://db/vidly
        volumes:
            - vidly:/data/db           
volumes:
    vidly: 
```

- we can name anything for services, build path should have Dockerfile or image can be used,to pull from dockerhub
- ports can be specfied host to container
- environment variables defined
- volume mapping can be done for any directory inside container, but volume should be created at same level as services in yaml file

### Building images
- using docker compose we can execute same commands, but instead of one we are executing on whole i.e includes all the services

    > docker-compose build

    > docker-compose up

    or
    > docker-compose up -d --build

- stopping containers
    > docker-compose down

### logs
- we can see logs of all the containers at one place
    > docker-compose logs 
- we can see logs of individual containers as well
    > docker logs -f api_container_id

### sharing source-code
- We can share source code with containers -v host:container
All the dependencies should also be installed on host machine so that it should detect changes and reflect into container.

    eg : nodemon for react app
```
api: 
    build: ./backend
    ports: 
        - 3001:3001
    environment:
        DB_URL: mongodb://db/vidly
    volumes:
        - ./backend:/app
```
### networking
> docker exec -it -u root web_container_id sh
    
    `ping api` -> works only with root user and works since all containers in same network

### Database migration

migration should be done at the start of the application, we can overide CMD of Dockerfile in docker-compose.yml
```
api: 
    build: ./backend
    ports: 
        - 3001:3001
    environment:
        DB_URL: mongodb://db/vidly
    volumes:
        - ./backend:/app
    command: ./wait-for db:27017 && migrate-mongo up && npm start
```
all the commands can be clubber into shell script and run at once

> command: ./docker-entrypoint.sh

```
#!/bin/sh

echo "Waiting for MongoDB to start..."
./wait-for db:27017 

echo "Migrating the databse..."
npm run db:up 

echo "Starting the server..."
npm start 
```

### tests
```
 webtest: 
    image: react-app_web
    volume: ./frontend:/app
    command : npm tests
apitests:
    build: ./backend
    environment:
        DB_URL: mongodb://db/vidly
    command: ./docker-entrypoint.sh
```
### Deployment

- Single host deployment
- CLusters (Docker Swarm, Kubernetes)

# Container Orchestration
When a container fails we need to detect the failure and run another container to serve users, if the host itslef fails we need multiple hosts to keep ths system up.
- Docker Swarm -> Easy to setup but lacks advance features
- Kubernetes (Google) -> bit difficult to setup but have advanced features and most popular
- Mesos (apache) -> difficult to setup but has lots of advanced features

## Docker Swarm
- swarm manager and multiple workers (nodes) on different hosts(with docker)
    ```
    > docker swarm init
    > docker swarm join --token <token>
    ```
- docker swarm automatically manages workers, run command on manager to create multiple worker replicas, port mapping networking and all docker command can be used
    > docker service create --repiicas=3 my-web-server

## Kubernetes
Running replicas on images, scaling up can be done with one command,
we can roll update to all the nodes 1 at a time, and can be rolled back of any problem occurs

- Kubernetes consists on clusters (multiple node replicas)
- Master looks on nodes in a cluster
- Components of Kuberneetes
    - API Server (frontend to kubernetes)
    - etcd (distriuted stroage on all nodes)
    - scheduler (distributes the nodes to newly created containers)
    - controller (responsible for noticing and making changes if node failure occurs)
    - controller runtime (software used to run container Docker)
    - kubelet (agent that runs on each node)
- kubectl (control or commandline tool for kubernetes) 
```
> kubectl run --replicas=2000 my-web-server
> kubectl scale --replicas=2000 my-web-server
> kubectl rolling-update my-web-server --image:web-server:2
> kubectl rolling-update my-web-server --rollback

> kubectl get nodes
> kubectl cluster info
```
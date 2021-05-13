# Multi-Arch Building
## Install QEMU
* Read this stuff:
    https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/
* display the host architecture:
```console
usr@pc:~$ uname -m 
x86_64
```
* run an executable made for aarch64 on x86_64:
```console
usr@pc:~$ docker run --rm -t arm64v8/ubuntu uname -m
#standard_init_linux.go:211: exec user process caused "exec format error"
```
* notice the above command doesnt work...
* install qemu garbage:
```console
usr@pc:~$ sudo apt-get install qemu binfmt-support qemu-user-static
##  Installs qemu and friends
usr@pc:~$ docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
##  Does some registration nonsense with docker
usr@pc:~$ docker run --rm -t arm64v8/ubuntu uname -m
##  test out running arm stuff on x86
```
## Building For ARM on x86
You have to do this or else you're gonna be building on arm and thats  crazy slow and terrible.
* Read this: https://docs.docker.com/docker-for-mac/multi-arch/
```console
usr@pc:~$ docker buildx ls

NAME/NODE DRIVER/ENDPOINT STATUS  PLATFORMS
default * docker
  default default         running linux/amd64, linux/arm64, linux/arm/v7, linux/arm/v6
```
```console
usr@pc:~$ docker buildx create --name mybuilder --use
##  Please name it something better than mybuilder, ex: "multiarch"
usr@pc:~$ docker buildx insptect --boostrap
##  Config boilerplate
```
```console
usr@pc:~$ sudo docker buildx build --platform linux/amd64,linux/arm64/v8 -t gibsoncratus/flask-hub-public:latest --push .
```
#### Command Notes:
    aarch64 and amd64 are the same thing. look it up
    see the --push, that pushes the images immediatly under this one tag
        for some reason when you buildx, the images are not saved locally
            presumably because it could be like 10+ images
        
## Deploy Remotely
* view your build manifest
```console
usr@pc:~$ sudo docker buildx imagetools inspect gibsoncratus/flask-hub-public:latest
Name:      docker.io/gibsoncratus/flask-hub-public:latest
MediaType: application/vnd.docker.distribution.manifest.list.v2+json
Digest:    sha256:cead989631fbd4b346282433814ed9bdf5765f8b47d6b473ab848826fb70cc5a
           
Manifests: 
  Name:      docker.io/gibsoncratus/flask-hub-public:latest@sha256:ae350c169e4c5db99f4e0d49defe862b82e54e9fcea73cf590dc26d55b81ad3b
  MediaType: application/vnd.docker.distribution.manifest.v2+json
  Platform:  linux/amd64
             
  Name:      docker.io/gibsoncratus/flask-hub-public:latest@sha256:5fcb9d9a1fb0b50bf70ea84e8ca8bb32b1710ce4e9aae6fb0657939af2543d33
  MediaType: application/vnd.docker.distribution.manifest.v2+json
  Platform:  linux/arm64
```
* Check out how it has the platforms we requested.
* now when you go pull it on another computer, if the specific arch is available, it will pull the right one automagically. Lets try it.
* ssh into an arm machine thats connected to the internet
```console
usr@pc:~$ sudo docker login
usr@pc:~$ sudo docker pull gibsoncratus/flask-hub-public:latest
usr@pc:~$ sudo docker run --name flask-hub-inst -v$PWD/app:/app -p5000:5000 gibsoncratus/flask-hub-public:latest
##  this might show an error, but it might work despite the error
```
* go into your browser to http://10.0.0.94:5000/
    * obviously your device has a different IP

Good Job~
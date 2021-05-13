# FLASK-HUB
This demo demonstrates the following:
 * how to use docker hub
 * build a docker application
 * deploy a docker application
 * build a docker application for multiple architectures
 * deploy a docker application on arm64/v8, compiled from amd64 
 * access the website remotely

##  Steps
### Testing Locally
1. test your application locally
1. get an account on docker hub
1. build your docker image version
1. run your local docker image

### Pushing To Docker Hub
1. make a docker repo
1. build your docker image
1. push your docker image
1. try to pull your docker image on another computer

### Multi-Arch Compilation
1. try to compile for arm64 from amd64 (it will fail)
1. use buildx to compile the webapp for amd64 and arm64v8 from amd64

### Remote Deployment
1. pull it on arm64 device
1. deploy on arm64 device
1. connect to website from browser on other device on network

Good Job~
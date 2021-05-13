# Basics
## Testing Locally
```console
usr@pc:~$ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 990-935-107
```
* Go to the url http://0.0.0.0:5000/ in browser to see your site.

## Building for Docker
* Get an account on docker hub.
    * I think you can figure this out.
* Build your application like this:
```console
usr@pc:~$ sudo docker build -t gibsoncratus/flask-hub-public:latest .
```
    Command Notes:
    * docker username: gibsoncratus
        * Yours will be different
    * Everything in docker requires login
        * You can use "docker login" / "docker logout"
    * ":latest" is the build tag. 
        * You can make however many of these you want. 
        * Use it for versioning. 
    * the "." at the end of the command indicates the current working directory
        * You should be running these build commands inside the same 
        folder as the Dockerfile

* View your images after you build them:

```console
usr@pc:~$ sudo docker images
##lists your built and downloaded docker images
usr@pc:~$ sudo docker image rm
##removes an image
usr@pc:~$ sudo docker irm
##alias for "docker image rm"
```

## Testing Locally As Docker Container
```console
usr@pc:~$ sudo docker run --name flask-hub-inst -v$PWD/app:/app -p5000:5000 gibsoncratus/flask-hub-public:latest
```

    Command Notes:
    * Each container needs a unique name
        * Name it or else docker gives it a fucked up UUID name.
    * "-p5000:5000" is port exposing for the webapp
    * -v tells docker to make the app file a consistent volume
        * I dont believe live lazy reloading works without this.

* Go to the url http://0.0.0.0:5000/ in browser to see your site.

Good Job~

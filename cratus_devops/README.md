# Local-Remote Hybrid Setup
## Basic Setup of AssetRxEdge on Remote Device
1. Setup your Xavier/edge device with a fresh ubuntu install.
1. pull the cratus arxe-egui repo on the remote device
    ```console
    usr@edge:~$ git clone https://gibsoncratus@bitbucket.org/cratus/arxe-api.git
    ```
1. Now we are gonna install some of the dependencies for running AssetRxEdge. And Fetch the docker containers and whatnot. 
The script you are about to run also makes a linux system service that will manage AssetRxEdge. It will restart your edge device, 
and when it reboots, at 10.0.0.44:3000 (use your edge device ip though) in the browser you can see your deployed AssetRxEdge. 
    ```console
    usr@edge:~$ cd arxe-egui
    ##  go into the folder of the repo u just pulled
    usr@edge:~$ sudo ./setup.sh
    ##  run the setup script
    ```
# Speedy Reload Mode for Development
## Setting up the Edge Device
We are gonna mount the backend folder that the edge AssetRxEdge instance uses from your dev PC. That way they are in sync.
1. Make sure ssh is installed on both the local machine (ex: desktop pc) and remote machine (ex: Jetson Xavier).
    ```console
    usr@edge:~$ sudo apt-get install sshfs
    usr@pc:~$ sudo apt-get install sshfs
    usr@pc:~$ sudo apt-get install openssh-server
    ##  this installs the server.
    ##  #   you only need this on the local host
    ##  #   youll see in a bit why
    ```
1. go ahead and disable the AssetRxEdge service on the edge device.
We do this so that it stops sniffing the files we're about to share between our edge device and dev pc.
    ```console
    usr@edge:~$ sudo systemctl stop cratustech
    ##  go loop up systemctl: start, stop, restart, etc
    ```
1. Check here to see where our AssetRxEdge backend is.
    ```console
    usr@edge:~$ sudo ls /.cratustech/json_output
    ##  see its showing your files, nice
    ```
1. Move that shit out of the way because we are gonna remote mount our own backend store here instead.
    ```console
    usr@edge:~$ sudo mv /.cratustech/json_output/ /.cratustech/json_output_back
    ## move that trash
    usr@edge:~$ sudo mkdir /.cratustech/json_output
    ##  make a fresh blank folder for mounting to
    ```
1. Okay, now go ahead and clone the cratus repo on your dev pc.
    ```console
    usr@pc:~$ git clone https://gibsoncratus@bitbucket.org/cratus/arxe-api.git
    usr@pc:~$ ls arxe-egui
    ##  notice we have no server folder. fuck
    ```
1. Switch to the dev branch in git, bc we need the server folder.
    ```console
    usr@pc:~$ git branch
    usr@pc:~$ git checkout dev
    usr@pc:~$ git branch
    ##  see look, you changed branches
    usr@pc:~$ ls arxe-egui
    ##  notice we have a server folder now. yay
    ```
1. On your edge device, try to ssh to your dev pc.
    ```console
    usr@edge:~$ ssh edgeusr@pc
    ##  make sure this works
    ##  accept the key store or whatever
    ```
1. If that worked you can mount the local dev server folder over to the edge device folder we made earlier.
    ```console
    usr@edge:~$ sudo sshfs gibson@10.0.0.98:/home/gibson/CratusRepos/arxe-egui/server/json_output /.cratustech/json_output
    usr@edge:~$ sudo ls /.cratustech/json_output
    ##  check it out, you are sharing backends now
    ```
    if you accidentally mounted the wrong folder or messed up the command, you may get some error about "missing mountpoint" or something. Try this 
    ```console
    usr@edge:~$ sudo fusermount -u /.cratustech/json_output
    ##  resets that mountpoint
    ```
    Then go back up to the top of this step, and remount.
1. Now turn the AssetRxEdge service back on.
    ```console
    usr@edge:~$ sudo systemctl start cratustech
    ```
## Setting up the Local Build to refer to the Edge Backend
## ~~~~(which is now mounted via sshfs to local folder)
You have to tweak some config on the build files to get your locally hosted server to use the edge device instance. 
1. find these 2 files.
    1. arxe-egui/server/server.js
    1. arxe-egui/src/helpers/AxiosHelper.js

1. In the whereami() function in arxe-egui/src/helpers/AxiosHelper.js
    ```js
    export function whereami() {

        var res = window.location.origin.toString();
        var n = res.length;
        var res1 = res.substring(0, n - 5);
        console.log("whereami ", res1);

        if (res1 == 'http://localhost') {
            // res1 = "http://10.0.0.100"
            //ENGİN sen kullanırken buradaki commenti silerek kullan
            // res1 = "http://192.168.1.139"
        }
        var tmpserial = getSerial(serialNumber);
        console.log("whereami tmpserial ", tmpserial, res1);
        return res1;
    };
    ```
    You have to change where the local server is connecting to.
    ```js
    if (res1 == 'http://localhost') {
        res1 = "http://10.0.0.100" //<-- PUT YOUR EDGE DEVICE IP HERE
    }
    ```
1. In the arxe-egui/server/server.js file, you have to set the following two variables. These variables are used by the server to know where to connect.
    ```js
    const JSON_OUTPUT_PATH = "/home/gibson/CratusRepos/arxe-egui/server/json_output";
    //  this one should be the location of your json_output folder in your local dev code folder. Remember you cloned the git earlier, and switched to dev branch so you would have the "server" folder. Well now we are using it.
    const CUSTOM_API_BASE_URL = "http://10.0.0.100"; 
    //  This one should be the ip of your edge device
    ```
    There is no knowing what they are set to before. Just remember to set these to the normal settings before you build and upload your docker image to the docker hub.
    ```js
    const JSON_OUTPUT_PATH = '/app/json_output';
    const CUSTOM_API_BASE_URL = 'http://localhost';
    ```
    For now, use your dev settings:
    ```js
    const JSON_OUTPUT_PATH = "/home/gibson/CratusRepos/arxe-egui/server/json_output";
    const CUSTOM_API_BASE_URL = "http://10.0.0.100"; 
    ```
1. Now you need to start the local server. In the terminal navigate to the arxe-egui folder of the git repo you cloned earlier. 
Then run the run.sh. 
    ```console
    usr@edge:~$ ./run.sh
    ```
    If you look inside that you will see its really short, 3 lines. 
    ```bash
    #!/bin/sh

    npm run server &
    sleep 10
    npm start 
    ```
    npm run server just starts a server from the "server" folder. We had to switch to the dev branch for that. 
    npm start begins the application.

1. Go to them and test it. In the browser go to 10.0.0.100:3000 (edge device ip though), and another tab at http://localhost:3000. 
You will notice that if you change microservices on remote, it doesn't sync with local, but if you refresh the page it works. 
If you want to add or remove functionality from the gui you can code it up, and hit save, and you will find your changes viewable immediatly from the localhost tab. 

There you go. Now you can dev quickly.
I do not yet know the limitations here. 
If you crash the edge service or get the application in an unrecoverable state in the gui, you may need to disable the service on the edge device via systemctl, and disable and reenable some docker containers with your dockerfu. When the app is restarted, it should recreate them based on the mutual json_output folder I believe. 
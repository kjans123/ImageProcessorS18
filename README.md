# ImageProcessorS18 &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/master/LICENSE) &middot; [![Build Status](https://travis-ci.org/kjans123/ImageProcessorS18.svg?branch=master)](https://travis-ci.org/kjans123/ImageProcessorS18) &middot; [![Documentation Status](https://readthedocs.org/projects/imageprocessors18-cps/badge/?version=latest)](http://imageprocessors18-cps.readthedocs.io/en/latest/?badge=latest)

### ONLINE README: http://imageprocessors18-cps.readthedocs.io/en/latest/

### Description

* The Crunchwrap Pizza Image Processor can be used to take in one or more .jpg images or a .zip archive of images in order for the user to run histogram equalization, log compression, constrast stretching, or reverse video operations on the image(s) they upload. This repository includes starter code for a ReactJSX app frontend that allows image upload, download, and display; starter code for a Mongo Database to store user information; and server code that processes the selected images and returns them to the frontend.
<img src="https://user-images.githubusercontent.com/24235476/39473111-2f73adf8-4d1b-11e8-8d19-27a584e2de02.png" width="400">
<img src="https://user-images.githubusercontent.com/24235476/39473272-f597002a-4d1b-11e8-909f-f64c91fc566e.png" width="400">

### Getting Started

## Initial Setup
First you will need to clone this repository to your local machine. Install all of the required python dependencies using:
```
pip install -r requirements.txt
```
and make sure to activate your virtual environment before continuing. ```source venv/bin/activate ```

   ***NOTE: if Tkinter throws a Not Found error, you will need to use this command: ``` apt-get install python-tk```***
    
## Database
To get started running the database (if you want to run your own database), use the below command in the same directory as the ProcessServer.py file ```(~/ImageProcessorS18/server)```
```
sudo docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```
and on line 33 in the ProcessServer.py file edit
```
connect("mongodb://vcm-3594.vm.duke.edu:27017/image_process_app")
```
with the name you want assign to your database:
```
connect("mongodb://vcm-3594.vm.duke.edu:27017/<your_database_name_here>")
```

## Server
In order to run the server, make sure that you are within the server folder before starting
```
cd ~/ImageProcessorS18/server
```
You can run the server on your local computer using gunicorn:
```
gunicorn --bind 0.0.0.0:5000 ProcessServer:app
```
* App
The...

### License

ImageProcessorS18 is [MIT licensed](./LICENSE).

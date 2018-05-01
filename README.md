# ImageProcessorS18 &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/master/LICENSE) &middot; [![Build Status](https://travis-ci.org/kjans123/ImageProcessorS18.svg?branch=master)](https://travis-ci.org/kjans123/ImageProcessorS18)

### ONLINE README: put online readme link here

### Description

* The Crunchwrap Pizza Image Processor can be used to take in one or more .jpg images or a .zip archive of images in order for the user to run histogram equalization, log compression, constrast stretching, or reverse video operations on the image(s) they upload. This repository includes starter code for a ReactJSX app frontend that allows image upload, download, and display; starter code for a Mongo Database to store user information; and server code that processes the selected images and returns them to the frontend.
![image text](https://user-images.githubusercontent.com/24235476/39473111-2f73adf8-4d1b-11e8-8d19-27a584e2de02.png)


### Getting Started
First you will need to clone this repository to your local machine. Install all of the required python dependencies using:
```
pip install -r requirements.txt
```
and make sure to activate your virtual environment before continuing.
* Database
To get started running the database....

* Server
In order to run the server, make sure that you are within the server folder before beginning.
```
cd server
```
You can run the server on your local computer using gunicorn:
```
gunicorn --bind 0.0.0.0:5000 ProcessServer:app
```
* App
The...

### License

ImageProcessorS18 is [MIT licensed](./LICENSE).

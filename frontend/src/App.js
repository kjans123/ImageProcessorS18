import React from 'react';
import AppBar from 'material-ui/AppBar';
import Button from 'material-ui/Button';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import Paper from 'material-ui/Paper';
import TextField from 'material-ui/TextField';
import { InputLabel } from 'material-ui/Input';
import { MenuItem } from 'material-ui/Menu';
import { FormControl } from 'material-ui/Form';
import Select from 'material-ui/Select';
import axios from 'axios';
import Dropzone from 'react-dropzone';
import FileSaver from 'file-saver';

var styles = {
    "backgroundStyle": {
        "backgroundImage": "url(https://user-images.githubusercontent.com/24235476/38747932-7ffdd550-3f1a-11e8-8ecf-ad2c3f6d3d69.jpg)",
        "backgroundRepeat": "round",
        "backgroundSize": "200px 200px",
    },
    "appBarStyle": {
        "marginBottom": "10px",
        "backgroundColor": "#001A57",
    },
    "appBarStyle2": {
        "marginBottom": "10px",
        "backgroundColor": "#A1B70D",
    },
    "paperStyle": {
        "height": "660px",
        "width": "1000px",
        "marginLeft": "200px",
        "marginTop": "30px",
        "textAlign": "center",
        "display": "inline-block",
        "padding": "10px",
    },
    "paperStyle2": {
        "height": "210px",
        "width": "205px",
        "display": "inline-block",
        "padding": "10px",
        "backgroundColor": "#001A57"
    },
    "paperStyle3": {
        "height": "1000px",
        "width": "1000px",
        "marginLeft": "200px",
        "marginTop": "30px",
        "textAlign": "center",
        "display": "inline-block",
        "padding": "10px",
    },
    "textFieldStyle": {
        "marginTop": "10px",
        "width": "180px",
    },
    "buttonStyle": {
        "backgroundColor": "#001A57",
        "marginTop": "30px",
        "color": "white",
    },
    "containerStyle": {
        "border": "3px",
        "borderStyle": "solid",
        "borderColor": "#001A57",
        "padding": "1em",
        "color": "#001A57",
    },
    "tableStyle": {
        "padding": "1em",
        "color": "#001A57",
    },
    "formStyle": {
        "width": "200px",
    },
    "formStyle2": {
        "width": "100px",
    },
    "errorStyle": {
        "marginTop": "20px",
        "marginBottom": "20px",
        "backgroundColor": "#E83635",
        "color": "white",
    },
    "headerStyle": {
        "border": "3px",
        "borderStyle": "solid",
        "borderColor": "white",
        "color": "white",
    },
    "upFieldStyle": {
        "backgroundColor": "gray",
        "color": "white",
        "height": "100px",
    },
}

class App extends React.Component {
    constructor() {
      super();
      this.state = {
          "userID": "",
          "id": null,
          "errorText": "",
          "currentImageString": "",
          "header": "",
          "listImages": [],
          "up": null,
          "confirmMsg": "",
          "processingTechnique": "",
          "proc": null,
          "postReady": "",
          "downloadExt": "",
          "ext": null,
          "downloadEnable": "",
          //response variables
          "userEmail": "",
          "procMethod": "",
          "uploadTime": "",
          "actionTime": "",
          "picSize": "",
          "outputTable": [],
          "postB64Str": null,
      };
    }

    //handles text field changes
    //displays error message for inadequate submissions
    onTextFieldChange = (event) => {
        this.setState({"userID": event.target.value});
        if (event.target.value.includes(" ")) {
            this.setState({"errorText": "Invalid email: No spaces allowed"})
        } else if (event.target.value.includes("@" && ".")) {
            this.setState({"errorText": ""})
            this.setState({"id": 1})
        } else {
            this.setState({"errorText": "Invalid email: example@address.com"})
        }
    }

    //handles image uploads to dropzone and creates array of base64 strings
    onUpload = (files) => {
        console.log(files.length)
        const listFiles = []
        for (let i = 0; i<files.length; i++) {
            const reader = new FileReader();
            reader.readAsDataURL(files[i]);
            reader.onloadend = () => {
            this.setState({"currentImageString": reader.result.split(',')[1]});
            this.setState({"header": reader.result.split(',')[0]});
            //will need header for output
            /*
            this.setState({"wComma": this.state.header.concat(",")})
            this.setState({"wHeader": this.state.wComma.concat(this.state.currentImageString)})
            console.log(this.state.wComma)
            console.log(this.state.wHeader)
            */
            listFiles.push(this.state.currentImageString);
            this.setState({"listImages": listFiles})
            //console.log(this.state.listImages[0])
            //console.log(this.state.header)
            this.setState({confirmMsg: "https://user-images.githubusercontent.com/24235476/39205822-cbc38b80-47c9-11e8-93fb-a5122f2b92fb.png"});
            }
            reader.onerror = (error) => {
                this.setState({confirmMsg: "Oops. An upload error has occured."});
            }
        }
        this.setState({"up": 1});
    }

    handleProcessChange = (event) => {
        this.setState({"processingTechnique": event.target.value});
        this.setState({"proc": 1})
    }

    postData = () => {
        var condition = this.state.id + this.state.up + this.state.proc + this.state.ext
        if (condition === 4) {
            this.setState({"postReady": ""})
            var urlString = "http://vcm-3594.vm.duke.edu:5000/process"
            var data = {
                "user_email": this.state.userID,
                "pre_b64_string": this.state.listImages,
                "proc_method": this.state.processingTechnique,
                "file_type": this.state.downloadExt,
                "header": this.state.header,
            }
            axios.post(urlString, data).then( (response) => {
                console.log(response);
                var displayPictures = []
                //data from backend for display
                this.setState({"userEmail": response.data.user_email});
                console.log(this.state.userEmail)
                this.setState({"procMethod": response.data.proc_method});
                this.setState({"uploadTime": response.data.upload_time});
                this.setState({"actionTime": response.data.action_time});
                this.setState({"picSize": response.data.pic_size});
                /*
                //push for pic table display
                for (let i=0; i < response.new_info.pre_b64_string.length; i++) {
                displayPictures.push({
                    "pre": response.data.pre_b64_string[i],
                    "preHist": response.data.pre_histogram[i],
                    "post": response.data.post_b64_string[i],
                    "postHist": response.data.post_histograms[i]
                });
                console.log(displayPictures)
                this.setState({"outputTable": displayPictures})
            }
            *//*
                this.setState({preB64Str: response.data.pre_b64_string[0]});

                this.setState({preHist: response.data.pre_histogram[0]});
                */
                this.setState({postB64Str: response.data.post_b64_string[0]});
                console.log(this.state.postB64Str)
                /*
                this.setState({postHist: response.data.post_histograms[0]});
                */
            });
        }
        else {
            this.setState({"postReady": "All four fields are required in order for image to be processed"})
        }
    }

    handleFileChange = (event) => {
        this.setState({"downloadExt": event.target.value});
        this.setState({"ext": 1})
        if (this.state.downloadExt === "JPEG") {
            this.setState({"downloadEnable": false})
            console.log(this.state.downloadEnable)
        }
        else if (this.state.downloadExt === "PNG") {
            this.setState({"downloadEnable": false})
        }
        else if (this.state.downloadExt === "TIFF") {
            this.setState({"downloadEnable": false})
        }
        else {
            this.setState({"downloadEnable": true})
        }
    }

    onDownload = () => {
        var urlGetString = "http://vcm-3594.vm.duke.edu:5000/download"
        axios.get(urlGetString).then( (response) => {
                console.log(response);
                this.setState({listOrNo: response.new_info.post_b64_string})
                this.setState({singleImage: response.new_info.post_b64_string})
                this.setState({zipImage: response.new_info.b64_zip_out})
                if (this.state.listOrNo.length > 1) {
                    this.setState({downloadEnable: ""});
                    var img = this.state.listImages[0]
                    var byteString = atob(img.split(',')[1]);
                    var mimeString = img.split(',')[0].split(':')[1].split(';')[0]
                    var ab = new ArrayBuffer(byteString.length);
                    var ia = new Uint8Array(ab);
                    for (var i = 0; i < byteString.length; i++) {
                        ia[i] = byteString.charCodeAt(i);
                    }
                    var blob = new Blob([ab], {type: mimeString});
                    FileSaver.saveAs(blob, "image.jpeg");
                }

            })
        if (this.state.downloadExt === "JPEG") {
            this.setState({downloadEnable: ""});
            var img = this.state.listImages[0]
            var byteString = atob(img.split(',')[1]);
            var mimeString = img.split(',')[0].split(':')[1].split(';')[0]
            var ab = new ArrayBuffer(byteString.length);
            var ia = new Uint8Array(ab);
            for (var i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            var blob = new Blob([ab], {type: mimeString});
            FileSaver.saveAs(blob, "image.jpeg");
        }
        else if (this.state.downloadExt === "PNG") {
            this.setState({downloadEnable: ""});
            var img = this.state.listImages[0]
            var byteString = atob(img.split(',')[1]);
            var mimeString = img.split(',')[0].split(':')[1].split(';')[0]
            var ab = new ArrayBuffer(byteString.length);
            var ia = new Uint8Array(ab);
            for (var i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            var blob = new Blob([ab], {type: mimeString});
            FileSaver.saveAs(blob, "image.png");
        }
        else if (this.state.downloadExt === "TIFF") {
            this.setState({downloadEnable: ""});
            var img = this.state.listImages[0]
            var byteString = atob(img.split(',')[1]);
            var mimeString = img.split(',')[0].split(':')[1].split(';')[0]
            var ab = new ArrayBuffer(byteString.length);
            var ia = new Uint8Array(ab);
            for (var i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            var blob = new Blob([ab], {type: mimeString});
            FileSaver.saveAs(blob, "image.tif");
        }
        else {
            this.setState({"downloadEnable": "Cannot download a file with no extension. Please select a file type in order to download image."})
        }
    }

  render() {
    return (
      <body style={styles.backgroundStyle}>
      <AppBar position="static" style={styles.appBarStyle}>
          <Toolbar>
              <Typography variant="title" color="inherit">
                  Crunchwrap Pizza Image Processor &#127790;
              </Typography>
          </Toolbar>
      </AppBar>
      <Paper position="static" style={styles.paperStyle}>
        <AppBar position="static" style={styles.appBarStyle}>
            <Toolbar>
                <Typography variant="title" color="inherit">
                    Welcome User
                </Typography>
            </Toolbar>
        </AppBar>
          <TextField
              value={this.state.userID}
              style={styles.textFieldStyle}
              placeholder="Enter your email address"
              onChange={this.onTextFieldChange}/>
            <div style={styles.errorStyle}>
              {this.state.errorText}
            </div>
          <Paper position="static" style={styles.paperStyle2}>
          <section>
          <div className="dropzone" align="center">
          <Dropzone
            accept="image/jpeg, .zip"
            onDrop={this.onUpload}>
            <p>
            <font color="white">
            Drop some files here, or click to select files
            <br></br>
            (.jpg and .zip only)
            </font>
            </p>
            <img src= {this.state.confirmMsg} alt="" height="40%" width="80%"/>
          </Dropzone>
          </div>
          </section>
          </Paper>
          <div>
          <br></br>
            <FormControl style={styles.formStyle}>
            <InputLabel style={{"color": "#001A57"}}><b>Processing Technique</b></InputLabel>
            <Select
                value={this.state.processingTechnique}
                onChange={this.handleProcessChange}
                >
                <MenuItem value="">
                <em>None</em>
              </MenuItem>
              <MenuItem value={"Histogram Equalization"}>Histogram Equalization</MenuItem>
              <MenuItem value={"Contrast Stretching"}>Contrast Stretching</MenuItem>
              <MenuItem value={"Log Compression"}>Log Compression</MenuItem>
              <MenuItem value={"Reverse Video"}>Reverse Video</MenuItem>
            </Select>
            </FormControl>
          <div style={{"color": "#001A57"}}>
          <br></br>
          <p><b>What file type would you like to download your image as after processing?</b></p>
          <FormControl style={styles.formStyle2}>
          <InputLabel style={{"color": "#001A57"}}><b>File Type</b></InputLabel>
          <Select
              value={this.state.downloadExt}
              onChange={this.handleFileChange}
              >
              <MenuItem value="">
              <em>None</em>
            </MenuItem>
            <MenuItem value={"JPEG"}>JPEG</MenuItem>
            <MenuItem value={"PNG"}>PNG</MenuItem>
            <MenuItem value={"TIFF"}>TIFF</MenuItem>
          </Select>
          </FormControl>
          </div>
          </div>
          <div>
          <Button variant="raised" style={styles.buttonStyle}
              onClick={this.postData}>
              Process
          </Button>
          </div>
          <div style={styles.errorStyle}>
            {this.state.postReady}
          </div>
      </Paper>
      <Paper style={styles.paperStyle3}>
      <AppBar position="static" style={styles.appBarStyle}>
          <Toolbar>
              <Typography variant="title" color="inherit">
                  Processed Output
              </Typography>
          </Toolbar>
      </AppBar>
      <img src= {this.state.postB64Str} alt= "" height="50%" width="50%"/>
          <p style={styles.containerStyle} align="left">
          User: <font color="#E83635">{this.state.userEmail}</font>
          <br></br>
          Process: <font color="#E83635">{this.state.procMethod}</font>
          <br></br>
          <p style={styles.containerStyle} align="left">
            <table style={styles.tableStyle}>
                <tr>
                    <th>Original Image</th>
                    <th>Histogram</th>
                    <th>Processed Image</th>
                    <th>Histogram</th>
                </tr>

                /*
                {this.state.outputTable.map(e =>{
                    return(
                        <tr>
                            <td><img src= {e.pre} alt= "" height="50%" width="50%"/></td>
                            <td><img src= {e.preHist} alt= "" height="50%" width="50%"/></td>
                            <td><img src= {e.post} alt= "" height="50%" width="50%"/></td>
                            <td><img src= {e.postHist} alt= "" height="50%" width="50%"/></td>
                        </tr>
                    );
                })}
                */
            </table>
          </p>
          Uploaded: <font color="#E83635">{this.state.uploadTime}</font>
          <br></br>
          Process Time: <font color="#E83635">{this.state.actionTime}</font>
          <br></br>
          Size: <font color="#E83635">{this.state.picSize}</font>
          </p>
          <div>
          <Button variant="raised" style={styles.buttonStyle}
              onClick={this.onDownload}>
              Download Images
          </Button>
          <div style={styles.errorStyle}>
            {this.state.downloadEnable}
          </div>
          </div>
      </Paper>
    </body>
    );
  }
}

export default App;

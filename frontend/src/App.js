import React from 'react';
import AppBar from 'material-ui/AppBar';
import Button from 'material-ui/Button';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import Paper from 'material-ui/Paper';
import TextField from 'material-ui/TextField';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import Input, { InputLabel } from 'material-ui/Input';
import { MenuItem } from 'material-ui/Menu';
import { FormControl, FormHelperText } from 'material-ui/Form';
import Select from 'material-ui/Select';
import ReactDOM from 'react-dom';
import DropzoneComponent from 'react-dropzone-component';
import {UploadField} from '@navjobs/upload';
import axios from 'axios';

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
    "paperStyle": {
        "height": "460px",
        "width": "1000px",
        "marginLeft": "200px",
        "marginTop": "30px",
        "textAlign": "center",
        "display": "inline-block",
        "padding": "10px",
    },
    "paperStyle2": {
        "height": "190px",
        "width": "325px",
        "display": "inline-block",
        "padding": "10px",
        "backgroundColor": "#001A57"
    },
    "paperStyle3": {
        "height": "500px",
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
          "errorText": "",
          "processingTechnique": "",
          "currentImageString": "",
          "downloadExt": "",
          "imgStr": "",
          "userOutput": "",
          "confirmMsg": "",
      };
    }

    handleProcessChange = (event) => {
        this.setState({"processingTechnique": event.target.value});
    }

    handleFileChange = (event) => {
        this.setState({"downloadExt": event.target.value});
    }

    onTextFieldChange = (event) => {
        this.setState({"userID": event.target.value});
        if (event.target.value.includes(" ")) {
            this.setState({"errorText": "Invalid email: No spaces allowed"})
        } else if (event.target.value.includes(".")) {
            this.setState({"errorText": ""})
        } else if (event.target.value.includes("@")) {
            this.setState({"errorText": ""})
        } else {
            this.setState({"errorText": "Invalid email: example@address.com"})
        }
    }

    onUpload = (files) => {
        const reader = new FileReader()
        const file = files[0]
        reader.readAsDataURL(file);
        reader.onloadend = () => {
            console.log(reader.result);
            this.setState({currentImageString: reader.result});
            this.setState({confirmMsg: "https://user-images.githubusercontent.com/24235476/39205822-cbc38b80-47c9-11e8-93fb-a5122f2b92fb.png"})
        }
    }

    postData = () => {
        var urlString = "http://0.0.0.0:5000/simple"
        var data = {
            "user_email": this.state.userID,
            "b64_string": this.state.currentImageString,
            "proc_method": this.state.processingTechnique,
        }
        axios.post(urlString, data).then( (response) => {
            console.log(response);
            this.setState({imgStr: response.data.image_string});
            this.setState({userOutput: response.data.user_id});
            console.log(this.state.imgStr)
        });
    }

  render() {
    return (
      <body style={styles.backgroundStyle}>
      <AppBar position="static" style={styles.appBarStyle}>
          <Toolbar>
              <Typography variant="title" color="inherit">
                  Crunchwrap Pizza Image Processor
              </Typography>
          </Toolbar>
      </AppBar>
      <Paper position="static" style={styles.paperStyle}>
          <TextField
              value={this.state.userID}
              style={styles.textFieldStyle}
              placeholder="Enter your email address"
              onChange={this.onTextFieldChange}/>
          <div style={styles.errorStyle}>
            {this.state.errorText}
          </div>
          <Paper position="static" style={styles.paperStyle2}>
            <h3 style={styles.headerStyle}>Upload your image below</h3>
            <UploadField onFiles={this.onUpload} align="center">
                <div style={styles.upFieldStyle}>
                Upload JPEG or .zip of JPEGs here
                <br></br>
                    <img src= {this.state.confirmMsg} alt="" height="50%" width="50%"/>
                </div>
            </UploadField>
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
          </div>
          <div>
          <Button variant="raised" style={styles.buttonStyle}
              onClick={this.postData}>
              PROCESS
          </Button>
          </div>
      </Paper>
      <Paper style={styles.paperStyle3}>
          <p style={styles.containerStyle} align="left">
          User: <font color="#E83635">{this.state.userOutput}</font>
          <br></br>
          Previous processes:
          <br></br>
          <p style={styles.containerStyle} align="left">
          <img src= {this.state.imgStr} alt="..." height="30%" width="30%"/>
          </p>
          Uploaded:
          <br></br>
          Process Time:
          <br></br>
          Size:
          </p>
          <div style={{"color": "#001A57"}}>
          Download as: &ensp;
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
          <div>
          <Button variant="raised" style={styles.buttonStyle}>
              Download
          </Button>
          </div>
      </Paper>
    </body>
    );
  }
}

export default App;

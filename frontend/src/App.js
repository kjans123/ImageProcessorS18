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
        "height": "3000px",
        "width": "1000px",
        "marginLeft": "200px",
        "marginTop": "30px",
        "textAlign": "center",
        "display": "inline-block",
        "padding": "10px",
    },
    "textFieldStyle": {
        "marginTop": "30px",
        "width": "180px",
    },
    "selectFieldStyle": {
        "width": "150px",
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
        "color": "white"
    }
}

class App extends React.Component {
    constructor() {
      super();
      this.state = {
          age: '',
          name: 'hai',
          "userID": "",
          "errorText": "",
      };
    }

    handleChange = (event) => {
        this.setState({ [event.target.name]: event.target.value});
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

  render() {
      const { classes } = this.props
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
          <div>
          <br></br>
          <form autoComplete="off">
            <FormControl style={styles.formStyle}>
            <InputLabel><b>Processing Technique</b></InputLabel>
            <Select
                value={this.state.age}
                onChange={this.handleChange}
                inputProps={{
                    name: 'age',
                    id: 'age-simple',
                }}
                >
                <MenuItem value="">
                <em>None</em>
              </MenuItem>
              <MenuItem value={10}>Histogram Equalization</MenuItem>
              <MenuItem value={20}>Contrast Stretching</MenuItem>
              <MenuItem value={30}>Log Compression</MenuItem>
              <MenuItem value={40}>Reverse Video</MenuItem>
            </Select>
            </FormControl>
          </form>
          </div>
          <div>
          <Button variant="raised" style={styles.buttonStyle}>
              PROCESS
          </Button>
          </div>
          <p style={styles.containerStyle} align="left">
          User:
          <br></br>
          Previous processes:
          <br></br>
          <p style={styles.containerStyle} align="center">
          Insert pics and histograms here as a material ui table
          </p>
          Uploaded:
          <br></br>
          Process Time:
          <br></br>
          Size:
          </p>
          Download as: &ensp;
            <FormControl style={styles.formStyle2}>
            <InputLabel><b>File Type</b></InputLabel>
            <Select
                value={this.state.age}
                onChange={this.handleChange}
                inputProps={{
                    name: 'age',
                    id: 'age-simple',
                }}
                >
                <MenuItem value="">
                <em>None</em>
              </MenuItem>
              <MenuItem value={10}>JPEG</MenuItem>
              <MenuItem value={20}>PNG</MenuItem>
              <MenuItem value={30}>TIFF</MenuItem>
            </Select>
            </FormControl>
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

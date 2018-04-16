import React from 'react';
import AppBar from 'material-ui/AppBar';
import Button from 'material-ui/Button';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import Paper from 'material-ui/Paper';
import TextField from 'material-ui/TextField';
{/*import SelectField from 'material-ui/SelectField';*/}
{/*import MenuItem from 'material-ui/MenuItem';*/}

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
    }
}

class App extends React.Component {
    constructor() {
      super();
      this.state = {
          value: 1,
      };
    }

    handleChange = (event, index, value) => this.setState({value});

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
              style={styles.textFieldStyle}
              placeholder="Enter your email address"/>
          <div>
          <br></br>
          *Select Field will go here once material-ui stops bugging*
          {/*<SelectField
            floatingLabelText="Processing Technique"
            value={this.state.value}
            onChange={this.handleChange}
          >
            <MenuItem value={1} primaryText="Histogram Equalization" />
            <MenuItem value={2} primaryText="Contrast Stretching" />
            <MenuItem value={3} primaryText="Log Compression" />
            <MenuItem value={4} primaryText="Reverse Video" />
          </SelectField>*/}
          </div>
          <div>
          <Button variant="raised" style={styles.buttonStyle}>
              Select Image
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
          Download as *Select field will go here*
          {/*<SelectField
            floatingLabelText="File type"
            value={this.state.value}
            onChange={this.handleChange}
          >
            <MenuItem value={1} primaryText="JPEG" />
            <MenuItem value={2} primaryText="PNG" />
            <MenuItem value={3} primaryText="TIFF" />
          </SelectField>*/}
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

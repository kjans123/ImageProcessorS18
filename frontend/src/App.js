import React from 'react';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import Paper from 'material-ui/Paper';
import TextField from 'material-ui/TextField';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem'

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
          <SelectField
            floatingLabelText="Processing Technique"
            value={this.state.value}
            onChange={this.handleChange}
          >
            <MenuItem value={1} primaryText
      </Paper>
    </body>
    );
  }
}

export default App;

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import * as AWS from 'aws-sdk'

AWS.config.update({
  region: '<region>',
  endpoint: 'dynamodb.us-east-2.amazonaws.com',
  accessKeyId: '<accessKeyId>',
  secretAccessKey: '<secretAccessKey>'
});

const rootElement = document.getElementById("root");

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  rootElement
);

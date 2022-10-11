import React from "react";
import ReactDOM from "react-dom";
// import { ApolloProvider } from "react-apollo";
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';
// import { client } from "./api/apollo/client";
// import client from "./api/apollo/index";

import { BrowserRouter } from "react-router-dom";

import "font-awesome/css/font-awesome.min.css";
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbreact/dist/css/mdb.css";
import "./index.css";

import App from "./App";
import * as serviceWorker from "./serviceWorker";
import { createStore } from "redux";

import { Provider } from "react-redux";
import appReducer from "./redusers/index.js";

const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/',
  cache: new InMemoryCache(),
});

const store = createStore(appReducer);

ReactDOM.render(
  <ApolloProvider client={client}>
    <BrowserRouter>
      <Provider store={store}>
        <App />
      </Provider>
    </BrowserRouter>
  </ApolloProvider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

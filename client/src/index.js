import React from 'react';
import ReactDOM from 'react-dom';
import HomeContainer from './containers/HomeContainer'
import './index.css'

const App = () => {
  return (
    <HomeContainer/>
  )
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

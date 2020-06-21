import React from 'react';
import Classifer from './containers/Classifier/Classifier';
import Header from './components/Header/Header';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header/>
      <Classifer/>
    </div>
  );
}

export default App;

import React from 'react';
import './App.css';
import Particlejs from './Particlejs'; 
import Home from './pages/Home';
import Student from './pages/Student';
import HigherStudies from './pages/higherstudies/HigherStudies';
import Error from './pages/Error';
import {Switch, Route} from "react-router-dom";
import HsGraph from './pages/higherstudies/HsGraph';
import HsData from './pages/higherstudies/HsData';

function App(){
  return (
    <div>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route exact path="/student">
          <Student />
        </Route>
        <Route exact path="/student/higherstudies">
          <HigherStudies />
        </Route>
        <Route exact path="/student/higherstudies/graph">
          <HsGraph />
        </Route>
        <Route exact path="/student/higherstudies/data">
          <HsData />
        </Route>
        <Route exact path="/student/placements">
          <HigherStudies />
        </Route>
        <Route exact path="/student/activities">
          <HigherStudies />
        </Route>
        <Route exact path="/student/achievements">
          <HigherStudies />
        </Route>
        <Route path="/">
          <Error />
        </Route>
      </Switch>
    {/* <Particlejs /> */}
    </div>
  );
}

export default App;

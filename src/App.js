import React from 'react';
import './App.css';
import Particlejs from './Particlejs'; 
import Home from './pages/Home';
import Student from './pages/Student';
import Error from './pages/Error';
import {Switch, Route} from "react-router-dom";
import HigherStudies from './pages/higherstudies/HigherStudies';
import Placements from './pages/placements/Placements';
import CompetetiveExams from './pages/competetiveexams/CompetetiveExams';
import Internships from './pages/internships/Internships';
import Activities from './pages/activities/Activities';
import Achievements from './pages/achievements/Achievements';
import Conference from './pages/conference/Conference';
import Journal from './pages/journal/Journal';
import FundedProjects from './pages/fundedprojects/FundedProjects';

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
        <Route exact path="/student/placements">
          <Placements />
        </Route>
        <Route exact path="/student/activities">
          <Activities />
        </Route>
        <Route exact path="/student/achievements">
          <Achievements />
        </Route>
        <Route exact path="/student/competetiveexams">
          <CompetetiveExams />
        </Route>
        <Route exact path="/student/internships">
          <Internships />
        </Route>
        <Route exact path="/student/conference">
          <Conference />
        </Route>
        <Route exact path="/student/journal">
          <Journal />
        </Route>
        <Route exact path="/student/fundedprojects">
          <FundedProjects />
        </Route>
        <Route path="/">
          <Error />
        </Route>
      </Switch>
    <Particlejs />
    </div>
  );
}

export default App;

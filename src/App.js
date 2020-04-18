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
import Faculty from './pages/Faculty';

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
        <Route exact path="/faculty">
          <Faculty />
        </Route>
        <Route exact path="/faculty/book">
          <Faculty />
        </Route>
        <Route exact path="/faculty/book_chapter">
          <Faculty />
        </Route>
        <Route exact path="/faculty/conference_paper">
          <Faculty />
        </Route>
        <Route exact path="/faculty/consultancy">
          <Faculty />
        </Route>
        <Route exact path="/faculty/courses_handled">
          <Faculty />
        </Route>
        <Route exact path="/faculty/faculty">
          <Faculty />
        </Route>
        <Route exact path="/faculty/faculty_conference_symposia">
          <Faculty />
        </Route>
        <Route exact path="/faculty/faculty_guest_lecture">
          <Faculty />
        </Route>
        <Route exact path="/faculty/faculty_patent">
          <Faculty />
        </Route>
        <Route exact path="/faculty/faculty_qualification">
          <Faculty />
        </Route>
        <Route exact path="/faculty/faculty_research">
          <Faculty />
        </Route>
        <Route exact path="/faculty/faculty_service">
          <Faculty />
        </Route>
        <Route exact path="/faculty/faculty_workshop_fdp">
          <Faculty />
        </Route>
        <Route exact path="/faculty/funded_projects">
          <Faculty />
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

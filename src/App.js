import React from 'react';
import './App.css';
import Particlejs from './Particlejs'; 
import Home from './pages/Home';
import Error from './pages/Error';
import Begin from './pages/Begin';
import LinkGen from './pages/linkGen/LinkGen';
import Upload from './pages/-stud-anal/Upload';
import {Switch, Route} from "react-router-dom";
// student pages 
import Student from './pages/Student';
import HigherStudies from './pages/-student-pages/HigherStudies';
import Placements from './pages/-student-pages/placements/Placements';
import CompetetiveExams from './pages/-student-pages/competetiveexams/CompetetiveExams';
import Internships from './pages/-student-pages/Internships';
import Activities from './pages/-student-pages/Activities';
import Achievements from './pages/-student-pages/Achievements';
import Conference from './pages/-student-pages/Conference';
import Journal from './pages/-student-pages/Journal';
import FundedProjects from './pages/-student-pages/FundedProjects';
//faculty pages
import Faculty from './pages/Faculty';
import Book from './pages/-faculty-pages/Book';
import BookChapter from './pages/-faculty-pages/BookChapter';
import ConferencePaper from './pages/-faculty-pages/ConferencePaper';
import Consultancy from './pages/-faculty-pages/consultancy/Consultancy';
import CoursesHandled from './pages/-faculty-pages/courses_handled/CoursesHandled';
import FacConfSymp from './pages/-faculty-pages/FacConfSymp';
import Fac from './pages/-faculty-pages/faculty/Fac';
import FacGuestLec from './pages/-faculty-pages/FacGuestLec';
import FacultyPatent from './pages/-faculty-pages/FacultyPatent';
import FacultyQuali from './pages/-faculty-pages/FacultyQuali';
import FacultyResearch from './pages/-faculty-pages/FacultyResearch';
import FacultyService from './pages/-faculty-pages/FacultyService';
import FacWorkFDP from './pages/-faculty-pages/FacWorkFDP';
import FundedProj from './pages/-faculty-pages/FundedProj';
//non teaching staff pages
import NonTeach from './pages/NonTeach';
import NTstaff from './pages/-non-teaching-pages/NTStaff/NTstaff';
import NTach from './pages/-non-teaching-pages/StaffAch/NTach';
import NTserv from './pages/-non-teaching-pages/StaffServ/NTserv';


function App(){
  return (
    <div>
      <Switch>
        <Route exact path="/">
          <Begin />
        </Route>
        <Route exact path="/home">
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
          <Book />
        </Route>
        <Route exact path="/faculty/book_chapter">
          <BookChapter />
        </Route>
        <Route exact path="/faculty/conference_paper">
          <ConferencePaper />
        </Route>
        <Route exact path="/faculty/consultancy">
          <Consultancy />
        </Route>
        <Route exact path="/faculty/courses_handled">
          <CoursesHandled />
        </Route>
        <Route exact path="/faculty/faculty">
          <Fac />
        </Route>
        <Route exact path="/faculty/faculty_conference_symposia">
          <FacConfSymp />
        </Route>
        <Route exact path="/faculty/faculty_guest_lecture">
          <FacGuestLec />
        </Route>
        <Route exact path="/faculty/faculty_patent">
          <FacultyPatent />
        </Route>
        <Route exact path="/faculty/faculty_qualification">
          <FacultyQuali />
        </Route>
        <Route exact path="/faculty/faculty_research">
          <FacultyResearch />
        </Route>
        <Route exact path="/faculty/faculty_service">
          <FacultyService />
        </Route>
        <Route exact path="/faculty/faculty_workshop_fdp">
          <FacWorkFDP />
        </Route>
        <Route exact path="/faculty/funded_projects">
          <FundedProj />
        </Route>
        <Route exact path="/nonteaching">
          <NonTeach />
        </Route>
        <Route exact path="/nonteaching/non_teaching_staff">
          <NTstaff />
        </Route>
        <Route exact path="/nonteaching/staff_achievement">
          <NTach />
        </Route>
        <Route exact path="/nonteaching/staff_service">
          <NTserv />
        </Route>
        <Route exact path="/generate_link">
          <LinkGen />
        </Route>
        <Route exact path="/student-anal">
          <Upload />
        </Route>
        <Route path="/">
          <Error message="Page doesn't exist" />
        </Route>
      </Switch>
    <Particlejs />
    </div>
  );
}

export default App;

import React from 'react';
import '../Home.css';
// import axios from 'axios';
class HsGraph extends React.Component {

 constructor(props) {
    super(props); 
    this.state = {
      x:'country',
      y:'nos',
      dep: 'all',
      year: '2019',
      MyComponent: true
    };

    this.handleChangex = this.handleChangex.bind(this);
    this.handleChangey = this.handleChangey.bind(this);
    this.handleChangedep = this.handleChangedep.bind(this);
    this.handleChangeyear = this.handleChangeyear.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChangex(event) {
    this.setState({x: event.target.value});
  }
  handleChangey(event) {
    this.setState({y: event.target.value}); 
  }
  handleChangedep(event) {
    this.setState({dep: event.target.value});
  }
  handleChangeyear(event) {
    this.setState({year: event.target.value}); 
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log("making request")
  
    //fetch("/HS1graph")
    // fetch('/result')
    //   .then(response => {
    //     console.log(response)
    //     return response.json()
    //   })
    //   .then(json => {
    //   console.log=(json)
    //   this.setState({playerName: json[0]})
    //   })

  }

  render() {
    if(this.state.MyComponent)
      return (
        <div className="mainbox">
          <div className="card1">
            <form onSubmit="" method="post">
              <div>
                <h3>Choose parameters</h3>
                <div className="together">
                  <h5>x:</h5>
                  <select id="x" name="x" onChange={this.handleChangex}>
                    <option value="country">country</option>
                    <option value="yearOfPassing">year of passing</option>
                    <option value="departmentId">department</option>
                    <option value="course">course</option>
                    <option value="program">program</option>
                  </select>
                </div>
                <div className="together">
                  <h5>y:</h5>
                  <select id="y" name="y" onChange={this.handleChangey}>
                    <option value="noOfStud">no. of students</option>
                  </select>
                </div>
                <div className="together">
                  <h5>year:</h5>
                  <select id="year" name="year" onChange={this.handleChangeyear}>
                    <option value="all">all</option>
                    <option value="2019">2019</option>
                    <option value="2018">2018</option>
                    <option value="2017">2017</option>
                    <option value="2016">2016</option>
                    <option value="2015">2015</option>
                  </select>
                </div>
                <div className="together">
                  <h5>department:</h5>
                  <select id="dep" name="dep" onChange={this.handleChangedep}>
                    <option value="all">all</option>
                    <option value="cse">computer science</option>
                    <option value="is">information science</option>
                    <option value="ece">electronics and communication</option>
                    <option value="ee">electrical engineering</option>
                    <option value="cv">civil engineering</option>
                    <option value="bt">biotechnology</option>
                    <option value="ch">chemical engineering</option>
                    <option value="im">industrial management</option>
                    <option value="it">information technology</option>
                    <option value="mba">MBA</option>
                    <option value="me">mechanical engineering</option>
                    <option value="ml">medical electronics</option>
                    <option value="te">telecommunication</option>
                  </select>
                </div>
              </div>
              <button className="butt" type="submit" onSubmit={async () => {
                const data={
                  dep:this.state.dep,
                  year:this.state.year,
                  tab:"higher_studies",
                  x:this.state.x,
                  y:this.state.y
                };
                const response = await fetch("/fields", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                  },
                  body: JSON.stringify(data)
                })
                if (response.ok) {
                this.setState({ MyComponent: false })
                }
              }}> 
              GO 
              </button>
            </form>
          </div>
        </div>
    );
    else
    return(
      <div className="mainbox"> 
      <img src="http://127.0.0.1:5000/graph" alt="error"></img>
      </div>
    )
  }

}


export default HsGraph;
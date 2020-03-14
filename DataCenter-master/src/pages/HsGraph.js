import React from 'react';
import './Home.css';
import axios from 'axios';
class HsGraph extends React.Component {

 constructor(props) {
    super(props); 
    this.state = {
      x:'country',
      y:'country',
      MyComponent: true
    };

    this.handleChangex = this.handleChangex.bind(this);
    this.handleChangey = this.handleChangey.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChangex(event) {
    this.setState({x: event.target.value});
  }
  handleChangey(event) {
    this.setState({y: event.target.value}); 
  }


  handleSubmit(event) {
    event.preventDefault();
    console.log("making request")
    const data={
      x:this.state.x,
      y: this.state.y,
    }
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
            <form method="get">
                <label>Choose the x and y values:</label>
                
                <select id="x" name="x" onChange={this.handleChangex}> 
                    <option value="country">country</option>
                    <option value="noOfStud">no. of students</option>
                    <option value="departmentid">department</option>
                </select>
                <select id="y" name="y" onChange={this.handleChangey}>
                    <option value="country">country</option>
                    <option value="noOfStud">no. of students</option>
                    <option value="departmentid">department</option>
                </select>

              {/*<DropdownButton id="x" title="x-value">
                <Dropdown.Item hrefx="#/action-1">country</Dropdown.Item>
                <Dropdown.Item href="#/action-2">no. of students</Dropdown.Item>
                <Dropdown.Item href="#/action-3">department</Dropdown.Item>
              </DropdownButton>
              <DropdownButton id="y" title="y-value">
                <Dropdown.Item href="#/action-1">country</Dropdown.Item>
                <Dropdown.Item href="#/action-2">no. of students</Dropdown.Item>
                <Dropdown.Item href="#/action-3">department</Dropdown.Item>
              </DropdownButton>*/}

                <button className="butt" type="submit" onClick={async () => {
            // const data={
            //   x:this.state.x,
            //   y:this.state.y,
            // };
            // const response = await fetch("/fields", {
            //   method: "POST",
            //   headers: {
            //     "Content-Type": "application/json"
            //   },
            //   body: JSON.stringify(data)
            // })
            // if (response.ok) {
              this.setState({MyComponent:false})
            }}> GO </button>
            </form>
          </div>
        </div>
    );
    else
    return(
      <div className="mainbox"> 
     
      <img src={"http://127.0.0.1:5000/HS2graph?x="+this.state.x+"&y="+this.state.y} alt="error"></img>
      <a href={"http://127.0.0.1:5000/HS2graph?x="+this.state.x+"&y="+this.state.y} download> click to download
      </a>
      </div>
    )
  }

}


export default HsGraph;
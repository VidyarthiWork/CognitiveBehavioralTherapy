import React, { Component } from "react";
import axios from "axios";

class App extends Component {
 constructor(props) {
  super(props);
  this.state = { value: "" };

  this.handleChange = this.handleChange.bind(this);
  this.handleSubmit = this.handleSubmit.bind(this);
 }

 handleChange(event) {
  this.setState({ value: event.target.value });
 }

 handleSubmit(event) {
  alert("A name was submitted: " + this.state.value);
  event.preventDefault();
  if (this.state.value) {
   axios.put(`/api/test/{this.state.value}`, this.state);
   return;
  }
 }

 render() {
  return (
   <form onSubmit={this.handleSubmit}>
    <label>
     Name:
     <input type="text" value={this.state.value} onChange={this.handleChange} />
    </label>
    <input type="submit" value="Submit" />
   </form>
  );
 }
}

export default App;

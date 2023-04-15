// Only run this after running the Flask process
// Either through a HTML page or directly with node
import axios from "axios";


const base_url = 'http://localhost:5000'; //  The URL on which the flask application runs

//  Function containing a GET request
const testGet = () => {
  axios.get(`${base_url}/async/get`) // by default this is asynchronous
    .then(response => { //  then block tells the process what to do once the promise is fulfilled
      console.log(response.data); //  The respone object's data field contains the JSON sent by the backend
    })
    .catch(error => {
      console.log(error.code); // The error object's code contains a quick one word description of the error
    });
}
//  analogous function for post
const testPost = () => {
  axios.post(`${base_url}/async/post`, { data: 'POST TEST' }) // Post contains data
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error.code)
    })
}

testGet();
testPost();



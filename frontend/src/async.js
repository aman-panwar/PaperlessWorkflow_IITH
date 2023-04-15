import axios from "axios";

const base_url = 'http://localhost:5000';

const testGet = () => {
  axios.get(`${base_url}/async/get`)
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error.code);
    });
}

const testPost = () => {
  axios.post(`${base_url}/async/post`, { data: 'POST TEST' })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error.code)
    })
}

testGet();
testPost();



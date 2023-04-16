const baseURL = 'http://localhost:8000'

document.getElementById('get_form').addEventListener('submit', event => {
  event.preventDefault();

  const param1 = document.getElementById('param1Value').value;
  const param2 = document.getElementById('param2Value').value;

  const params = {
    'param1': param1,
    'param2': param2,
  };

  axios.get(`${baseURL}/get_process`, { params })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    })
})

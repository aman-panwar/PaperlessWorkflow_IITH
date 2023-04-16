const baseURL = 'http://localhost:8000'

document.getElementById('post_form').addEventListener('submit', event => {
  event.preventDefault();

  const formData = new FormData(event.target);
  console.log(formData)
  axios.post(`${baseURL}/post_process`, formData)
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error.code);
    })
})

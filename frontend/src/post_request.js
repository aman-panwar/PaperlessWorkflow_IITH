const baseURL = "http://localhost:5000";
document.getElementById('postform').addEventListener('submit', (event) => {
  event.preventDefault();
  const form = new FormData(event.target);
  axios.post(`${baseURL}/form/submit`, form)
    .then(response => {
      alert(response.data)
    })
    .catch(error => {
      console.log(error);
    })
})


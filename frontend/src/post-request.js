
window.onload = () => {
  document.getElementById('post-form').addEventListener('submit', (event) => {
    form = FormData(event.target);
    console.log(form)
  })
}

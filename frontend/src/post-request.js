window.onload = () => {
  document.getElementById('postform').addEventListener('submit', (event) => {
    const form = FormData(event.target);
    console.log(form);
  })
}

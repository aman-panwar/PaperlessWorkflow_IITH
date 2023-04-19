import axios from "../node_modules/axios"

document.getElementById('postform').addEventListener('submit', (event) => {
  event.preventDefault();
  const form = new FormData(event.target);
  const formdata = Object.fromEntries(form);
  console.log(formdata);
})

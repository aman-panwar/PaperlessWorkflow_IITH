document.getElementById('postform').addEventListener('submit', (event) => {
  event.preventDefault();
  const form = new FormData(event.target);
})

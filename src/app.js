const form = document.querySelector('#definition-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  fetch('/get-definition', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(definition => {
    // Display the definition to the user
  })
  .catch(error => console.error(error));
});

document.getElementById('registrationForm').addEventListener('submit', function(event) {
  var password = document.getElementById('password').value;
  if (password.length < 8) {
    event.preventDefault(); // Prevent form submission
    alert('Password must be at least 8 characters long!');
  }
});
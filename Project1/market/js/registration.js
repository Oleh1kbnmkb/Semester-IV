$(document).ready(function() {
  $('#registrationForm').submit(function(e) {
    e.preventDefault();
    var form = $(this);
    var url = form.attr('action');
    var data = form.serialize();

    $.ajax({
      type: 'POST',
      url: url,
      data: data,
      success: function(response) {
        $('#registrationMessage').text('Registration successful!');
        form[0].reset();
      },
      error: function(error) {
        $('#registrationMessage').text('Registration failed.');
      }
    });
  });
});

$('#toggle_header').click(() => {
  if ($('HEADER').hasClass('red')) {
    $('HEADER').toggleClass('green');
  } else if ($('HEADER').hasClass('green')) {
    $('HEADER').toggleClass('red');
  }
});

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.ajax({ url: url })
  .done((req) => {
    const greeting = req.hello;
    $('#hello').text(greeting);
  });

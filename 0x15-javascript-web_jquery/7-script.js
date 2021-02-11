const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.ajax({ url: url })
  .done((req) => {
    $('#character').text(req.name);
  });

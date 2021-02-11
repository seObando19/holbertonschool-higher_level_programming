const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.ajax({ url: url })
  .done((req) => {
    const res = req.results;

    for (const idx in res) {
      $('UL#list_movies').append(`<li>${res[idx].title}</li>`);
    }
  });

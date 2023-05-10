$(document).ready(() => {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  let response = null;

  $.ajax({
    method: 'GET',
    async: false,
    url: url,
    success: (data) => {
      response = data.hello;
    },
    error: () => {
      response = 'Error fetching data';
    }
  });

  if (response) {
    $('#hello').text(response);
  }
});


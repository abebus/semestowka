socket.on('connect', function() {console.log('Connected to the server')});

socket.on('message', function(message) {
    console.log('Received a message: ' + message)
    socket.emit('message', 'Привет серверу!');
});

socket.on('clicked', function() {
  const button = document.getElementById('change_login');

  console.log('clicked');
  document.getElementById("username_field").innerHTML = "send clicked";

  onClickHandler(button);
});

$('#change_login').click(function () {
            const button = document.getElementById('change_login');

  console.log('clicked');
  document.getElementById("username_field").innerHTML = "send clicked";

  onClickHandler(button);
        })

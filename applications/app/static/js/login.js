async function getDataAsync(url)
{
  let response = await fetch(url);
  let data = await response.json()
  return data;
}


var app = new Vue({
  'el': '#login-app',
  'data': {
    'username': '',
    'password': '',
    'passwordType': 'password',
    'message': ''
  },
  'methods': {
    'loginOnClick': function () {
      this.message = '';
      // data = JSON.stringify({'username': this.username, 'password': this.password});
      // resp = request('POST', '/api/auth', [['Content-Type', 'application/json']], data);
      fetch('/api/auth', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'username': this.username, 'password': this.password})
      }).then(r => r.json())
        .then(data => {
          if (data.status == 'OK') {
            console.log('XXXX', data)
            window.location = '/';
          } else {
            console.log('ERROR', data)
            this.message = 'The username or password is incorrect';
          }
      });
    },
  	'showPassword': function () {
      if (this.passwordType == 'password') {
        this.passwordType = 'text';
      } else {
        this.passwordType = 'password';
      }
    }
  }
});

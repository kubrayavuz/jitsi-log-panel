var app = new Vue({
  'el': '#login-app',
  'data': {
    'username': '',
    'password': '',
    'passwordType': 'password'
  },
  'methods': {
    'loginOnClick': function () {
      data = JSON.stringify({'username': this.username, 'password': this.password});
      resp = request('POST', '/api/auth', [['Content-Type', 'application/json']], data);
      resp = JSON.parse(resp);
      if (resp.status == 'OK') {
        window.location = '/';
      } else {
        alert('Kullanıcı adı ya da parola hatalı');
      }
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

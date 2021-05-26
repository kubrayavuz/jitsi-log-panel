var app = new Vue({
  'el': '#login-app',
  'data': {
    'username': '',
    'password': '',
    'passwordType': 'password',
    'message': '',
  },
  'methods': {
    loginOnClick: function () {
      this.message = "";
      data = {'username': this.username, 'password': this.password}
      request('post', '/api/auth', data).then(data => {
        data.status == 'OK' ? window.location = "/" :
                              this.message = "Kullanıcı adı ya da parola hatalı"
      })
    },
    showPassword: function () {
      if (this.passwordType == "password") {
        this.passwordType = "text";
      } else {
        this.passwordType = "password";
      }
    },
  },
});

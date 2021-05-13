var app = new Vue({
  'el': '#login-app',
  'data': {    
  	'passwordType': 'password'
  },
  'methods': {
  	'showPassword': function () {
      if (this.passwordType == 'password') {
        this.passwordType = 'text';
      } else {
        this.passwordType = 'password';
      }
    }
  }
});

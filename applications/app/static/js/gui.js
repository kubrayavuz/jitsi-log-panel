var app = new Vue({
  'el': '#app',
  'data': {
    'menuList': [
      { 'name': 'Konferans', 'iconClass': 'people_alt' },
      { 'name': 'Network', 'iconClass': 'signal_cellular_alt' },
    ],
    'selectedMenu': 'Konferans',
  },
  'methods': {
    logoutOnClick: function () {
      request('delete', '/api/auth', null).then(data => {
        data.status == 'OK' ? window.location = "/login" :
                              this.message = "Oturum sonlandırılamadı"
      })
    },
  },
});

var app = new Vue({
  el: '#app',
  data: {    
  	menuList: [
      { 'name': 'Conference', 'iconClass': 'people_alt' },
      { 'name': 'Network', 'iconClass': 'signal_cellular_alt'}
    ],
    selectedMenu: 'Conference'
  }
});

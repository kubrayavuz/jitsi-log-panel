function request(method, location, headers, data) {
    r = new XMLHttpRequest();
    r.open(method, location, false);
    for (var i = headers.length - 1; i >= 0; i--) {
        r.setRequestHeader(headers[i][0], headers[i][1]);
    }
    r.send(data);
    response = r.responseText;
    return response;
}


function async_request(method, location, headers, data, callback) {
  var r = new XMLHttpRequest();
  r.open(method, location);
  header_keys = Object.keys(headers);
  for (var i = header_keys.length - 1; i >= 0; i--) {
    r.setRequestHeader(header_keys[i], headers[header_keys[i]]);
  }
  r.onreadystatechange = function() {
    if (r.readyState == 4){
        callback(r.responseText);
    }
  };
  r.send(data);
}

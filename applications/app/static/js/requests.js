function request(method, url, data) {
  return axios({
    method: method,
    url: url,
    data: data,
    timeout: 4000
  })
  .then((response) => response.data)
  .catch(err => console.log(err))
}

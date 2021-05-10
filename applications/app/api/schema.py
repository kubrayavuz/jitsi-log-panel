from schema import Schema, Use

LOGIN_SCHEMA = Schema({
    'username': Use(str),
    'password': Use(str)
})

PASSWORD_SCHEMA = Schema({
    'password': Use(str),
    'old_password': Use(str),
})
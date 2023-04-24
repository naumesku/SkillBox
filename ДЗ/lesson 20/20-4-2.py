server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
for i,s in server_data.items():
    print (i,':')
    for k,v in s.items():
        print('\t', k, ':', v)
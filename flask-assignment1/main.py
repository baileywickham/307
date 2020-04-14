from flask import Flask, request, jsonify

app = Flask(__name__)
users = {
        'users_list' :
        [
            {
                'id' : 'xyz789',
                'name' : 'Charlie',
                'job': 'Janitor',
                },
            {
                'id' : 'abc123',
                'name': 'Mac',
                'job': 'Bouncer',
                },
            {
                'id' : 'ppp222',
                'name': 'Mac',
                'job': 'Professor',
                },
            {
                'id' : 'yat999',
                'name': 'Dee',
                'job': 'Aspring actress',
                },
            {
                'id' : 'zap555',
                'name': 'Dennis',
                'job': 'Bartender',
                }
            ]
        }

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    # implimented as an OR
    if request.method == 'GET':
        if id :
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
    elif request.method == 'DELETE':
        if id :
            for user in users['users_list']:
                if user['id'] == id:
                    del user



@app.route('/users', methods=['POST'])
@app.route('/')
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username :
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users

    elif request.method == 'POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        return resp



if __name__ == "__main__":
    app.run(port=8080)

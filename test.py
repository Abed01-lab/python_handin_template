from flask import Flask, jsonify, abort, request

app = Flask(__name__)

@app.route('/flask_app/')
def index():
    return "Hello, World from flask server!"



towns = [
    {
        'id': 1,
        'code' : 3000,
        'name': 'Helsingør'
    },
    {
        'id': 2,
        'code' : 3070,
        'name': 'Snekkersten'
    },
    {
        'id': 3,
        'code' : 3060,
        'name': 'Espergærde'
    },    
    {
        'id': 4,
        'code' : 3100,
        'name': 'Hornbæk'
    },
    {
        'id': 5,
        'code' : 3140,
        'name': 'Ålsgård'
    }
]

@app.route('/towns/', methods=['GET'])
def get_towns():
    return jsonify({'towns: ': towns} )

@app.route('/town/<int:town_id>', methods=['GET'])
def get_town(town_id):
    town = [town for town in towns if town['id'] == town_id]
    if len(town) ==0:
        abort(404)
    return jsonify({'town: ': town})
    
@app.route('/town/', methods=['POST'])
def create_town():
    if not request.json or not 'code' in request.json:
        abort(404)
    town = {
        'id' : towns[-1]['id'] + 1,
        'code': request.json['code'],
        'name' : request.json['name']
    }
    towns.append(town)
    return jsonify({'towns :' : towns})

@app.route('/town/<int:town_id>', methods=['PUT'])
def update_town(town_id):
    town = [town for town in towns if town['id'] == town_id]
    if len(town) == 0:
        abort
    if not request.json or not 'code' in request.json:
        abort(404)
    towns[town_id]['code'] = request.json.get('code')
    towns[town_id]['name'] = request.json.get('name')
    return jsonify({'town: ': towns[town_id]})

@app.route('/town/<int:town_id>', methods=['DELETE'])
def delete_town(town_id):
    town = [town for town in towns if town['id'] == town_id]
    if len(town) == 0:
        abort(404)
    towns.remove(town[0])
    return jsonify({'towns :' : towns})


if __name__ == '__main__':
    app.run(debug=True)
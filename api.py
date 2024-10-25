from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/users/', methods=['GET'])
def returnUserInfo():
    id = request.args.get("id", type=int)
    id = int(id)
    users = {
    1: {"name": "Alex",
        "age": 25
    },
    2: {"name": "Max",
        "age": 28
    },
    3: {"name": "Egor",
        "age": 15
    }
}
    return jsonify(users[id])
pass
if __name__ == "__main__":
 app.run(debug=True)

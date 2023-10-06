from flask import Flask, request, jsonify

app = Flask(__name__)

data = [
    {"id": 1, "name": "Bon-chan"},
    {"id": 2, "name": "Robin"},
    {"id": 3, "name": "Sogeking"}
]

# GET all data
@app.route("/data", methods=["GET"])
def get_all_data():
    return jsonify(data)

# GET data by ID
@app.route("/data/<int:id>", methods=["GET"])
def get_data_by_id(id):
    result = next((item for item in data if item["id"] == id), None)
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Data not found"}), 404

# GET data by Name
@app.route("/data/name/<string:name>", methods=["GET"])
def get_data_by_name(name):
    result = next((item for item in data if item["name"] == name), None)
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Data not found"}), 404

# Update data by ID
@app.route('/data/update/<int:id>/<new_name>', methods=['PUT', 'GET', 'POST'])
def update_name_by_id(id, new_name):   
    if new_name is None:
        return jsonify({"message": "New name not provided"}), 400

    for item in data:
        if item['id'] == id:
            item['name'] = new_name
            return jsonify({"message": f"Name for ID {id} updated successfully to {new_name}"})

    return jsonify({"message": "Data not found"}), 404

if __name__== '__main__':
    app.run(debug=True)

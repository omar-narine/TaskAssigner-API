from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'db': 'tasks_db'}
db = MongoEngine(app)

class Task(db.Document):
    id = db.StringField(required=True, unique=True)
    taskTitle = db.StringField(required=True)
    taskDueDate = db.DateTimeField(required=True)
    taskDescription = db.StringField(required=True)
    taskStatus = db.StringField(required=True)

@app.route('/addTask', methods=['POST'])
def add_task():
    task = Task(**request.get_json())
    task.save()
    return jsonify(task.to_json()), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.objects.all()
    return jsonify([task.to_json() for task in tasks])

@app.route('/task/<id>', methods=['GET'])
def get_task(id):
    task = Task.objects.get_or_404(id=id)
    return jsonify(task.to_json())

@app.route('/task/<id>', methods=['PATCH'])
def update_task(id):
    task = Task.objects.get_or_404(id=id)
    task.update(**request.get_json())
    return jsonify(task.to_json())

@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.objects.get_or_404(id=id)
    task.delete()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
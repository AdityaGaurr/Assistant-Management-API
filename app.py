from flask import Flask, jsonify, request
from models import db, Assistant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assistants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# POST /assistant: Create a new assistant
@app.route('/assistant', methods=['POST'])
def create_assistant():
    data = request.get_json()
    new_assistant = Assistant(
        name=data['name'],
        email=data['email'],
        mobile=data['mobile'],
        salary=data['salary'],
        city=data['city'],
        country=data['country'],
        department=data['department'],
        role=data['role']
    )
    db.session.add(new_assistant)
    db.session.commit()
    return jsonify({'id': new_assistant.id})

# GET /assistant/<assistant_id>: Retrieve an assistant
@app.route('/assistant/<int:id>', methods=['GET'])
def get_assistant(id):
    assistant = Assistant.query.get(id)
    if not assistant:
        return jsonify({'message': 'Assistant not found'}), 404
    return jsonify({
        'id': assistant.id,
        'name': assistant.name,
        'email': assistant.email,
        'mobile': assistant.mobile,
        'salary': assistant.salary,
        'city': assistant.city,
        'country': assistant.country,
        'department': assistant.department,
        'role': assistant.role
    })

# PUT /assistant/<assistant_id>: Update an assistant
@app.route('/assistant/<int:id>', methods=['PUT'])
def update_assistant(id):
    assistant = Assistant.query.get(id)
    if not assistant:
        return jsonify({'message': 'Assistant not found'}), 404
    data = request.get_json()
    assistant.name = data.get('name', assistant.name)
    assistant.email = data.get('email', assistant.email)
    assistant.mobile = data.get('mobile', assistant.mobile)
    assistant.salary = data.get('salary', assistant.salary)
    assistant.city = data.get('city', assistant.city)
    assistant.country = data.get('country', assistant.country)
    assistant.department = data.get('department', assistant.department)
    assistant.role = data.get('role', assistant.role)
    db.session.commit()
    return jsonify({'message': 'Assistant updated'})

# DELETE /assistant/<assistant_id>: Delete an assistant
@app.route('/assistant/<int:id>', methods=['DELETE'])
def delete_assistant(id):
    assistant = Assistant.query.get(id)
    if not assistant:
        return jsonify({'message': 'Assistant not found'}), 404
    db.session.delete(assistant)
    db.session.commit()
    return jsonify({'message': 'Assistant deleted'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
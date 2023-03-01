"""Flask app for Cupcakes"""
from flask import Flask, render_template, jsonify,request, redirect, render_template
from models import db, connect_db, Cupcake
 
app = Flask(__name__)

app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.app_context().push()
connect_db(app)

@app.route('/')
def root():
    """Renders homepage"""
    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    """Retrieves data about all cupcakes"""
    all_cakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_single_cupcake(cupcake_id):
    """Retrieves data about a single cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.to_dict())

@app.route('/api/cupcakes',methods=["POST"])
def create_cupcake():
    """Creates a cupcake"""
    data = request.json
    new_cake = Cupcake(flavor=data['flavor'],
                       size=data['size'],
                       rating=data['rating'],
                       image=data['image'])
    db.session.add(new_cake)
    db.session.commit()
    json_response = jsonify(cupcake = new_cake.to_dict())
    return (json_response,201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods =["PATCH"])
def update_cupcake(cupcake_id):
    """Updates current cupcake from data and return new data"""

    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.image = data['image']
    cupcake.rating = data['rating']

    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict())

@app.route('/api/cupcakes/<int:cupcake_id>',methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Deletes cupcake and returns confirmation"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Cupcake Deleted!')
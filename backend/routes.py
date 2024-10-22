from app import app, db
from flask import request, jsonify
from models import Ani
import jikan_service as j

# Get all Ani
@app.route("/api/ani",methods=["GET"])
def get_ani():
    anis = Ani.query.all()
    result = [ani.to_json() for ani in anis]
    return jsonify(result)

# Create an anime
@app.route("/api/ani",methods=["POST"])
def create_ani():
    try:
        data = request.json
        
        title = data.get('title')
        rating = data.get("rating")
        description = data.get("description")
        
        new_ani = Ani(title=title, rating=rating, description=description)
        
        db.session.add(new_ani)
        
        db.session.commit()
        
        return jsonify({"msg":"Anime created successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
        #Fetch anime title

# Delete an anime from user list
@app.route("/api/ani/<int:id>", methods=["DELETE"])
def delete_anime(id):
    try:
        ani = Ani.query.get(id)
        if ani is None:
            return jsonify({"error":"Anime is not in list."}), 404
        
        db.session.delete(ani)
        db.session.commit()
        
        return jsonify({"msg":"Anime Deleted."})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
    
# Update anime
@app.route("/api/ani/<int:id>", methods=["PATCH"])
def update_ani(id):
    try:
        ani = Ani.query.get(id)
        if ani is None:
            return jsonify({"error":"Anime is not in list."}), 404
        
        data = request.json
        
        ani.rating = data.get("rating", ani.rating)
        
        db.session.commit()
        return jsonify(ani.to_json())
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
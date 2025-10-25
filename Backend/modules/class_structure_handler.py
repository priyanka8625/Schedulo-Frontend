from flask import jsonify
from config import db

# Collection for class structure
class_structure_collection = db['class_structure']

def save_class_structure(data):
    """
    Saves the class structure by overwriting the previous one.
    Expected data format:
    {
        "sy": [{"div": "A", "batches": 2}, ...],
        "ty": [{"div": "A", "batches": 2}, ...],
        "be": [{"div": "A", "batches": 2}, ...]
    }
    """

    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        # Delete existing structure
        class_structure_collection.delete_many({})

        # Insert new structure
        class_structure_collection.insert_one(data)

        return jsonify({"message": "Class structure saved successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

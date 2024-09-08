from flask import  jsonify

class Message:
    def isExist(*Args):
        for arg in Args:
            if not arg:
                return False, jsonify({"error": "name and email are required!"}), 400
            else:
                return True, "", 200

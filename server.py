# from flask import Flask, jsonify
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)  # Allow frontend requests

# @app.route('/run-script', methods=['GET'])
# def run_script():
#     try:
#         result = subprocess.run(["python3", "classifying_infant_cry_type_A.py"], capture_output=True, text=True)
#         #result = subprocess.run(["python3", "hello.py"], capture_output=True, text=True)
#         return jsonify({"message": "Script executed", "output": result.stdout})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        # Make sure the script path is correct
        result = subprocess.run(["python3", "classify_crying_type.py"], capture_output=True, text=True)
        
        # If there's any error in the script, it will be captured in stderr
        if result.stderr:
            return jsonify({"error": result.stderr}), 500

        # Return the script's output (stdout)
        return jsonify({"message": "Script executed successfully", "output": result.stdout})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
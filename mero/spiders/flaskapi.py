import json
from flask import Flask ,jsonify
import os

PORT = int(os.environ.get("PORT", 5000))


class flask_api():

    def returndata(self,data):
        
        
        app=Flask(__name__)
        @app.route('/',methods=['GET'])
        def hello():
            return jsonify(data)
        app.run(host='0.0.0.0',port=PORT)


# if __name__ == "__main__":
#     app.run()
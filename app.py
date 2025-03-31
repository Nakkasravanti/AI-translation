# from flask import Flask, render_template, request, jsonify
# from models.translation import translate_text

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/translate", methods=["POST"])
# def translate():
#     data = request.json
#     text = data.get("text", "")
#     target_lang = data.get("target_lang", "en")
#     translated_text = translate_text(text, target_lang)
#     return jsonify({"translated_text": translated_text})

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template, request, jsonify
# from models.translation import translate_text

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/translate', methods=['POST'])
# def translate():
#     data = request.get_json()
#     text = data.get('text')
#     target_lang = data.get('target_lang')

#     if not text or not target_lang:
#         return jsonify({'error': 'Invalid input'}), 400

#     translated_text = translate_text(text, target_lang)
#     return jsonify({'translated_text': translated_text})

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, render_template, request, jsonify
from models.translation import translate_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    target_lang = data.get('target_lang')

    if not text or not target_lang:
        return jsonify({'error': 'Invalid input'}), 400

    translated_text = translate_text(text, target_lang)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

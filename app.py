from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

chat_bot = 

@app.route('/')
def home():
	return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chat_bot.get_response(userText))

if __name__ == '__main__':
	app.run(debug=True)
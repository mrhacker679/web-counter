from flask import Flask, redirect, render_template

app = Flask(__name__)
visitor_count = 0

@app.route('/')
def home():
        global visitor_count
        visitor_count += 1
        return render_template('home.html', visitor_count=visitor_count)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

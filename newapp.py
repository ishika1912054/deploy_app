from flask import Flask, jsonify, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='templates')

db = mysql.connector.connect(
    host="DESKTOP-S51A0MK",
    user="Ishika_Mittal",
    password="I$h!k@178",
    database="works"
)

@app.route('/api/word', methods=['GET'])
def get_word():
    cursor = db.cursor()
    cursor.execute("SELECT word FROM words")
    result = cursor.fetchone()
    cursor.close()
    if result:
        word = result[0]
    else:
        word = "Word not found"
    return jsonify({'word': word})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        word = request.form.get('word')
        cursor = db.cursor()
        cursor.execute("UPDATE words SET word = %s", (word,))
        db.commit()
        cursor.close()
        return 'Word updated successfully'
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)

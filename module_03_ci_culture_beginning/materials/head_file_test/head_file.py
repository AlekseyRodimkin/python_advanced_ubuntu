import flask

app = flask.Flask(__name__)


@app.route('/headfile/<string:filename>')
def make_new_file(filename: str) -> str:
    with open(filename, 'a') as file:
        pass
    return f'File {filename} created!'


if __name__ == '__main__':
    app.run(debug=True)
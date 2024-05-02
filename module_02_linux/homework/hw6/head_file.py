from flask import Flask
import os

app = Flask(__name__)


@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    """
    Возвращает первые size символов файла.
    :param: size: int - количество символов.
    :param: relative_path: str - путь к файлу.
    :return: str - первые size символов файла.
    """
    abs_path = os.path.abspath(os.path.join('..', relative_path))
    read_text = ''
    with open(abs_path, "r") as f:
        read_text = f.read(size)
    return f"<b>{abs_path}<b/> {size}<br>{read_text}"


if __name__ == "__main__":
    app.run(debug=True)

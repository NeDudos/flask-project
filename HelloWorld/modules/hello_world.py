from flask import Blueprint

hello_world_bp = Blueprint('hellow_world', __name__)

@hello_world_bp.route('/')
def hello_world():
    return '<h1>Hello, World!</h1> \n <button type="button" class="btn btn-dark" onclick="process(1);">Нажать 1</button>'
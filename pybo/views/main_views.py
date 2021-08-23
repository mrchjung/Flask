from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
#blueprint 의 이름을 역추적.
#url_for('blueprint명.함수',매개변수)
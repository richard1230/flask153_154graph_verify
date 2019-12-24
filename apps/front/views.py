from flask import (
    Blueprint,
    views,
    render_template,
    make_response,
    Response,
    Flask,

)
from utils.captcha import Captcha
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw

bp = Blueprint("front", __name__)  # url_prefix='cms'表示一个前缀,这里不需要


@bp.route('/')
def index():
    return 'front index'


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    out = BytesIO()
    # with open("{}.png".format(image),'rb') as f:
    #     image = f.read()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    # print(resp)
    # resp = Response(resp,mimetype="image/png")
    # resp.context_type = 'image/png'
    resp.headers['Content-Type'] = 'image/jpg'

    return resp


class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))

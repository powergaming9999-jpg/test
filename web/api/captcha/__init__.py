from flask import request
from flask import jsonify

from web.app import app, limiter



@limiter.limit('1 per second')
@app.route('/api/v1/captcha', methods=['GET'])
def route_captcha():
    return jsonify({'error': True, 'message': 'Captcha is disabled'}), 410

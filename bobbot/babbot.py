from datetime import date, timedelta
from flask import request, jsonify

from schapi import *

from bobbot import app


keyboard = {
        'type': 'buttons',
        'buttons': ['오늘 급식', '내일 급식', '모래 급식']
    }


def meal(region, school_code, year, month, day):
    meal_dict = SchoolAPI(region, school_code).get_by_date(year, month, day)
    message = helper(meal_dict, 'breakfast')
    message += helper(meal_dict, 'lunch')
    message += helper(meal_dict, 'dinner')
    return message


def helper(meal_dict, key):
    return '[{0}]\n{1}\n\n'.format(key, '\n'.join(meal_dict[key] or '정보가 없습니다.\n\n'))


@app.route('/keyboard')
def keyboard():
    return jsonify(keyboard)


@app.route('/message')
def message():
    content = request.get_json()['content']

    now = date.today()
    if content == '내일 급식':
        now += timedelta(days=1)
    elif content == '모레 급식':
        now += timedelta(days=2)
    year, month, day = now.timetuple()

    message = meal(region, school_code, year, month, day)

    return jsonify({
        'message': {
            'type': 'text',
            'text': message
        },
        'keyboard': keyboard
    })

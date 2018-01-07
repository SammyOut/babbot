from datetime import date, timedelta
from flask import Flask, request, jsonify

from schapi import *

SEOUL = 'stu.sen.go.kr'
BUSAN = 'stu.pen.go.kr'
DAEGU = 'stu.dge.go.kr'
INCHEON = 'stu.ice.go.kr'
GWANGJU = 'stu.gen.go.kr'
DAEJEON = 'stu.dje.go.kr'
ULSAN = 'stu.use.go.kr'
SEJONG = 'stu.sje.go.kr'
GYEONGGI = 'stu.cbe.go.kr'
KANGWON = 'stu.kwe.go.kr'
CHUNGBUK = 'stu.cbe.go.kr'
CHUNGNAM = 'stu.cne.go.kr'
JEONBUK = 'stu.jbe.go.kr'
JEONNAM = 'stu.jne.go.kr'
GYEONGBUK = 'stu.gbe.go.kr'
GYEONGNAM = 'stu.gne.go.kr'
JEJU = 'stu.jje.go.kr'

region = ''
school_code = ''

main_keyboard = {
        'type': 'buttons',
        'buttons': ['오늘 급식', '내일 급식', '모래 급식']
    }

app = Flask(__name__)


def meal(year, month, day):
    global region
    global school_code
    meal_dict = SchoolAPI(region, school_code).get_by_date(year, month, day)
    message = helper(meal_dict, 'breakfast')
    message += helper(meal_dict, 'lunch')
    message += helper(meal_dict, 'dinner')
    return message


def helper(meal_dict, key):
    return '[{0}]\n{1}\n\n'.format(key, '\n'.join(meal_dict[key] or '정보가 없습니다.'))


@app.route('/keyboard')
def keyboard():
    return jsonify(main_keyboard)


@app.route('/message')
def message():
    content = request.get_json()['content']

    now = date.today()
    if content == '내일 급식':
        now += timedelta(days=1)
    elif content == '모레 급식':
        now += timedelta(days=2)
    year, month, day = now.timetuple()

    message = meal(year, month, day)

    return jsonify({
        'message': {
            'type': 'text',
            'text': message
        },
        'keyboard': main_keyboard
    })


def bot(region_input, school_code_input, host=None, port=None):
    global region
    global school_code

    region = region_input
    school_code = school_code_input

    app.run(host=host, port=port)

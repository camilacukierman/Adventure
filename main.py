from bottle import route, run, template, static_file, request
import random
import json
import pymysql
import os

connectivity = pymysql.connect(host="localhost",
                               user="root",
                               password="",
                               db="adventure",
                               cursorclass=pymysql.cursors.DictCursor)
# current_q = 1
# username = 'Yippy'
# try:
#     with connectivity.cursor() as cursor:
#a
#         sql = " INSERT INTO users (name, energy_total, bodytemp_total, id_q) VALUES ('{}', 100, 100, 1)".format(username)
#
#         print("blah")
#         cursor.execute(sql)
#         options = cursor.fetchall()
#
#         print(options)
#
# except:
#     print("failed")




@route("/", method="GET")
def index():
    return template("adventure.html")


@route("/start", method="POST")
def start():
    username = request.POST.get("user")
    current_adv_id = request.POST.get("adventure_id")

    # name = {"name":''}
    with connectivity.cursor() as cursor:
        user = get_user(cursor, username)
        #print(user)
        if user is None:
            print("something")
            user = init_user(cursor, username)

        question_row, options = get_data(cursor, 1, username)


    current_story_id = 0  # todo change


# todo add the next step based on db
    return json.dumps({"user": user['name'],
                   "adventure": current_adv_id,
                   "current": user['id_q'],
                   "text": question_row['text_q'],
                   "image": question_row['image'],
                   "options": options
                   })


def init_user(cursor, username):
    sql = "INSERT INTO users (name, energy_total, bodytemp_total, id_q) VALUES (\'{}\', 100, 100, 1)".format(username)
    cursor.execute(sql)
    user = get_user(cursor, username)
    connectivity.commit()
    return user


def get_data(cursor, result, username):
    # get infos of current user to use and updqate in every step
    sql = "SELECT * FROM questions WHERE id_q={}".format(result)
    cursor.execute(sql)
    question_row = cursor.fetchone()

    sql = "SELECT * FROM answers WHERE id_q={}".format(result)
    cursor.execute(sql)
    options = cursor.fetchall()

    return question_row, options

#
def get_user(cursor, username):
    sql = "SELECT * FROM users WHERE name='{}'".format(username)
    cursor.execute(sql)
    user = cursor.fetchone()
    print(user)
    return user
    # connectivity.commit()



@route("/story", method="POST")
def story():
    username = request.POST.get("user")
    current_adv_id = request.POST.get("adventure")
    next_story_id = request.POST.get("next")
    energy_change= request.POST.get("energy_change")
    bodytemp_change= request.POST.get("bodytemp_change")
    print(bodytemp_change, energy_change)

    # update_user(...)
    with connectivity.cursor() as cursor:
        question, options = get_data(cursor, next_story_id, username)
        bodytemp_total, energy_total = calc_measurments(cursor,bodytemp_change, energy_change, username)
    # next_steps_results = []
    # random.shuffle(options)  #todo change - used only for demonstration purpouses

    # todo add the next step based on db
    return json.dumps({"user": username,
                       "adventure": current_adv_id,
                       "current": next_story_id,
                       "text": question['text_q'],
                       "image": question['image'],
                       "options": options,
                       "energy_total": energy_total,
                       "bodytemp_total": bodytemp_total
                       })


def calc_measurments(cursor, bodytemp_change, energy_change, username):
    user = get_user(cursor, username)
    bodytemp_total = int(user['bodytemp_total']) + int(bodytemp_change)
    energy_total = int(user['energy_total']) + int(energy_change)
    print(bodytemp_total, energy_total)
    return bodytemp_total, energy_total


# "adventure": current_adv_id,
# "text": "New scenario! What would you do?",
# "image": "choice.jpg",
# "options": next_steps_results

@route('/js/<filename:re:.*\.js$>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=9000)
    # run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))



if __name__ == '__main__':
    main()

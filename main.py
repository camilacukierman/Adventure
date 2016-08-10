from bottle import route, run, template, static_file, request
import random
import json
import pymysql

connectivity = pymysql.connect(host="sql6.freesqldatabase.com",
                               user="sql6130708",
                               password="THC8Cqs1Kq",
                               db="sql6130708",
                               cursorclass=pymysql.cursors.DictCursor)

try:
    with connectivity.cursor() as cursor:
        sql = "SELECT * FROM users WHERE name={}".format(username)
        cursor.execute(sql)
        user1 = cursor.fetchall()
        print(user1)
except:
    print("falied")


@route("/", method="GET")
def index():
    return template("adventure.html")


@route("/start", method="POST")
def start():
    username = request.POST.get("name")
    current_adv_id = request.POST.get("adventure_id")

    # name = {"name":''}
    with connectivity.cursor() as cursor:
        user = get_user(cursor, username)
        if user is None:
            init_user(cursor, username)

        user, question, options = init_data(cursor,  username)
    connectivity.close()

    return json.dumps({"name": user1["name"],

                       })

    user_id = user[id]
    current_story_id = 0  # todo change
    next_steps_results = [
        {"id": 1, "option_text": "I fight it"},
        {"id": 2, "option_text": "I give him 10 coins"},
        {"id": 3, "option_text": "I tell it that I just want to go home"},
        {"id": 4, "option_text": "I run away quickly"}
    ]

    # todo add the next step based on db
    return json.dumps({"name": user['name'],

                       })


def init_user(cursor, username):
    insert_sql = " INSERT INTO 'users'( 'name','current_q') VALUES ({0},\'{1}\')".format(username, 1)
    cursor.execute(insert_sql)
    connectivity.commit()


def init_data(cursor,  username):
    # get infos of current user to use and updqate in every step
    user1 = get_user(cursor, username)

    sql = "SELECT * FROM users WHERE name={}".format(username)
    cursor.execute(sql)
    user1 = cursor.fetchall()

    question = get_question(cursor, user1['current_q'])

    sql = "SELECT * FROM questions  WHERE question_id IS user[current_q]".format(username)
    cursor.execute(sql)
    result = cursor.fetchall()

    options = get_options(cursor, user1['current_q'])

    sql = "SELECT * FROM users WHERE name={}".format(username)
    cursor.execute(sql)
    result = cursor.fetchall()

    return user1, question, options


def get_user(cursor, username):
    insert_sql = " INSERT INTO 'users'( 'name','current_q') VALUES ({0},\'{1}\')".format(username, 1)
    cursor.execute(insert_sql)
    connectivity.commit()

    #
    # sql = "SELECT * FROM users WHERE name={}".format(username)
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # return result


@route("/story", method="POST")
def story():
    user_id = request.POST.get("user")
    current_adv_id = request.POST.get("adventure")
    next_story_id = request.POST.get("next")  # this is what the user chose - use it!
    update_user(...)
    result, question, options = init_data(cursor, result, username)
    next_steps_results = [
        {"id": 1, "option_text": "I run!"},
        {"id": 2, "option_text": "I hide!"},
        {"id": 3, "option_text": "I sleep!"},
        {"id": 4, "option_text": "I fight!"}
    ]
    random.shuffle(next_steps_results)  # todo change - used only for demonstration purpouses

    # todo add the next step based on db
    return json.dumps({"user": result[""],
                       "adventure": current_adv_id,
                       "text_q": result["text_q"],
                       "image": result["image"],
                       "options": next_steps_results
                       })


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


if __name__ == '__main__':
    main()

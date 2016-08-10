from bottle import route, run, template, static_file, request
import random
import json
import pymysql

connectivity = pymysql.connect(host="localhost",
                               user="root",
                               password="",
                               db="mydb",
                               cursorclass=pymysql.cursors.DictCursor)
current_q = 1
username = 'Ilana'
try:
    with connectivity.cursor() as cursor:

        sql = "SELECT * FROM answers WHERE id_q={}".format(current_q)

        print("blah")
        cursor.execute(sql)
        options = cursor.fetchall()
        firstop = options[0]['text_ans']
        print(firstop)
        secop = options[1]['text_ans']
        print(secop)
        thop = options[2]['text_ans']
        print(thop)
        print(options)
except:
    print("failed")


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

    sql = "SELECT * FROM users WHERE name='{}'".format(username)
    cursor.execute(sql)
    user1 = cursor.fetchall()
    current_q = user1[0]['id_q']

    sql = "SELECT * FROM questions WHERE id_q={}".format(current_q)
    cursor.execute(sql)
    question_row = cursor.fetchall()
    image = question_row[0]['image']
    text = question_row[0]['text_q']

    sql = "SELECT * FROM answers WHERE id_q={}".format(current_q)
    cursor.execute(sql)
    options = cursor.fetchall()

    return user1, question_row, options


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

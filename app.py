import random
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request
import mysql.connector as connector
from time import time
import array

con = connector.connect(host='localhost', port='3306', user='root',
                        password='jamesbond', database='newdb')
app = Flask(__name__)
dev = "ENV"

if dev == "ENV":
    app.debug = True


class randomPassGen:
    def generating(self):
        MAX_LEN = 8

        # declare arrays of the character that we need in out password
        # Represented as chars to enable easy string concatenation
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                             'z']

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                             'Z']

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                   '*', '(', ')', '<']
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        password = ""
        for x in temp_pass_list:
            password = password + x
        return password


class eMailing:
    def __init__(self, toemail, info):
        self.toemail = toemail
        self.info = info

    def joker(self):
        email = EmailMessage()
        email['from'] = 'James Bond'
        email['to'] = self.toemail
        email['subject'] = "Feedback"

        email.set_content(self.info)
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("kakagems26@gmail.com", "vdrgjucmalsyrndw")
            smtp.send_message(email)


@app.route('/signInSir', methods=['GET', 'POST'])
def leh():
    global goat
    global UderID
    if request.method == 'POST':
        UsernaMee = request.form['usernamee']
        pASworD = request.form['passw']
        UderID = UsernaMee
        if UsernaMee == '' or pASworD == '':
            return render_template('signin.html', mess="Enter all the Fields")
        try:
            query = "select * FROM loginpassword WHERE UserID = '{}'".format(UsernaMee)
            cur = con.cursor()
            cur.execute(query)
            for row in cur:
                goat = row[1]
            if goat == pASworD:
                return render_template('index.html')
            else:
                return render_template('signin.html', mess="Incorrect Password")
        except:
            print("hello here is the error occured")
            return render_template('signin.html', mess="No Candidate")


@app.route("/passfetch", methods=['GET', 'POST'])
def hello_worldo():
    global team
    global ayt
    global ewrPass
    global t1
    global tempPass
    global roll

    if request.method == 'POST':
        roll = request.form['usernamet']
        guess = request.form['radio112']
        print(guess)
        z1 = randomPassGen()
        w1 = z1.generating()
        tempPass = w1
        print(w1)
        if guess == 'option1':
            try:
                query = "select * FROM feedCredential WHERE RollNo = '{}'".format(roll)
                cur = con.cursor()
                cur.execute(query)

                for row in cur:
                    team = row[3]
                    ayt = row[0]
                roll = ayt

                query = "select * from loginpassword WHERE UserID='{}'".format(ayt)
                if ayt == ' ;asaoweekfwjeroq34jr9034rjepwd':
                    return render_template('forgetpass.html', mess="No User Exist By This Roll Number")

                ayt = ' ;asaoweekfwjeroq34jr9034rjepwd'
                cur = con.cursor()
                cur.execute(query)
                for roww in cur:
                    ewrPass = roww[1]
                info = "Your Updated Password After Verification will be: " + str(w1)
                b1 = eMailing(team, info)
                b1.joker()
                # return render_template('signin.html', mess="OTP Send At Your Email Address " + str(team))
                t1 = time()
                return render_template('timing.html', mess="Password Send At Your Email Address " + str(team))
            except:
                return render_template('forgetpass.html', mess="No User Exist By This Roll Number")
        else:
            try:
                query = "select * from loginpassword WHERE UserID='{}'".format(roll)

                cur = con.cursor()
                cur.execute(query)

                for roww in cur:
                    ewrPass = roww[1]



                query = "select * FROM feedCredential WHERE UserId = '{}'".format(roll)
                cur = con.cursor()
                cur.execute(query)
                for row in cur:
                    team = row[3]
                    ayt = row[2]

                if ayt == ' ;asaoweekfwjeroq34jr9034rjepwd':
                    return render_template('forgetpass.html', mess="No User Exist By This User ID")

                info = "Your Roll Number: " + str(ayt) + "\nYour Updated Password After Verification will be: " + str(w1)
                ayt = ' ;asaoweekfwjeroq34jr9034rjepwd'
                b2 = eMailing(team, info)
                b2.joker()
                t1 = time()
                # return render_template('signin.html', mess="OTP Send At Your Email Address " + str(team))
                return render_template('timing.html', mess="Password Send At Your Email Address " + str(team))
            except:
                return render_template('forgetpass.html', mess="No User Exist By This UserId")


@app.route('/submitpass', methods=['GET', 'POST'])
def ytr():
    if request.method == 'POST':
        passwrdn = request.form['entr']
        t2 = time()
        if (t2 - t1) > 60:
            return render_template('timing.html', mess='Your session has expired ')
        else:
            if passwrdn == tempPass:
                query = "UPDATE loginpassword SET Password ='{}'WHERE UserId = '{}'".format(tempPass, roll)
                yep = con.cursor()
                yep.execute(query)
                con.commit()
                return render_template('index.html')
            else:
                return render_template('timing.html', mess='Wrong Password')


@app.route('/signUpSir', methods=['GET', 'POST'])
def pandaop():
    if request.method == 'POST':
        UsernaME = request.form['username']
        pASSword = request.form['pass']
        RepASSword = request.form['Repass']
        print(type(pASSword))
        print(type(RepASSword))
        if UsernaME == "" or pASSword == "" or RepASSword == "":
            return render_template('signup.html', mess="Please Enter all Fields")
        if pASSword != RepASSword:
            return render_template('signup.html', mess="Re-Entered Password is not matching")
        else:
            try:
                query = "insert into loginpassword(UserID,Password)values('{}','{}')".format(UsernaME, pASSword)
                yep = con.cursor()
                yep.execute(query)
                con.commit()
                return render_template('signin.html')
            except:
                return render_template('signup.html', mess="UserName Already Taken")


@app.route("/")
def hello_world():
    return render_template('login_du.html')


@app.route("/emailpassS", methods=['GET', 'POST'])
def lo_tree():
    return render_template('forgetpass.html')


@app.route('/ok', methods=['GET', 'POST'])
def fir():
    return render_template("signin.html")


@app.route('/yu', methods=['GET', 'POST'])
def ji():
    return render_template('signup.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        Roll_Number = request.form['roll_no']
        emaill = request.form['email']
        course = request.form['service']
        rating = request.form['rating']
        message = request.form['message']

        if name == '' or Roll_Number == '' or emaill == '' or course == 'Select Course' or rating == 'Select Rating' or message == '':
            return render_template('index.html', mess=" Please Enter all required Fields ")
        else:
            try:
                query = "select * from feedCredential WHERE UserId='{}'".format(UderID)
                cur = con.cursor()
                cur.execute(query)
                print("hekko1")
                for roww in cur:
                    rlln = roww[2]
                print("hekko1")
                if rlln == Roll_Number:
                    cur = con.cursor()
                    cur.execute("""
                       UPDATE feedCredential
                       SET UserName=%s, RollNo=%s, email=%s, Course=%s,Rating=%s,FeedBACK=%s
                       WHERE UserId=%s
                    """, (name, Roll_Number, emaill, course, rating, message, UderID))
                    print("hekko1")
                    con.commit()
                    print("hekko2")
                    info = "Name : " + str(name) + "\nRoll Number : " + str(Roll_Number) + "\nEmail : " + str(
                        emaill) + "\nRating : " + str(rating) + "\nFeedback : " + str(message)
                    thanking = " \n\n\n We Have Updated Your Feedback 😊"
                    print("hekko1")
                    gott = info + thanking

                    b3 = eMailing(emaill, gott)
                    b3.joker()
                    print("hekko5")
                    return render_template('commonV.html',
                                           mess="You Have Already Submitted The Form,However It is Updated By Latest Provided Data")
                else:
                    return render_template('index.html', mess="Roll Number Is Invalid")
            except:
                try:
                    quer = "insert into feedCredential(UserId,UserName,RollNo,email,Course,Rating,FeedBACK)values('{}','{}','{}','{}','{}','{}','{}')". \
                        format(UderID, name, Roll_Number, emaill, course, rating, message)
                    yepp = con.cursor()
                    yepp.execute(quer)
                    con.commit()
                    info = "Name : " + str(name) + "\nRoll Number : " + str(Roll_Number) + "\nEmail : " + str(
                        emaill) + "\nRating : " + str(rating) + "\nFeedback : " + str(message)
                    thanking = "<b> \n\n\nThanks For Your Feedback </b>"
                    gott = info + thanking

                    b4 = eMailing(emaill, gott)
                    b4.joker()
                    return render_template('commonV.html', mess="Your Feedback Is Appreciated")
                except:
                    return render_template('commonV.html', mess="jai Shri Ram")


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
    )

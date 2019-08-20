import os
import shutil
from docutils.nodes import table, author
from hgext.fsmonitor.pywatchman import client

from db import cryptoDB


from stem.control import Controller
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Hi BotMaster:)  <a href="/logout">Logout</a>'

def show_tables():
    tables = {'elmundo', 'eldiario'}
    out = ""
    out += "<h1>Bot list</h1>"
    out += '<link rel="stylesheet" href="/static/tables.css" type="text/css">'
    out += '<h3>Hi BotMaster!  <a href="/logout">Logout</a></h3>'

    for table_name in tables:
        rows = cryptoDB.get_all_users(table_name)
        out += "<h2> Bots created in " + table_name + "</h2>"
        out += '<div class="table-wrapper">'
        out += '<table class="fl-table">'
        out += "    <thead>"
        out += "    <tr>"
        out += "        <th>User ID</th>"
        out += "        <th>Username</th>"
        out += "        <th>Pwd</th>"
        out += "        <th>E-mail</th>"
        out += "    </tr>"
        out += "    </thead>"

        for row in rows:
            out += "<tr>"
            for i in range(0,4):
                out += "<td>" + str(row[i]) + "</td>"
            out += "</tr>"
        out += "      <tbody>"
        out += "    </table>"
        out += "</div>"

    return out

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return show_tables()
    return render_template('login.html', error=error)


@app.route("/logout")
def logout():
    def logout():
        session['logged_in'] = False

    return index()

print(' * Connecting to tor')

with Controller.from_port() as controller:
  controller.authenticate()

  # All hidden services have a directory on disk. Lets put ours in tor's data
  # directory.

  hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', '/tmp'), 'hello_world')

  # Create a hidden service where visitors of port 80 get redirected to local
  # port 5000 (this is where Flask runs by default).

  print(" * Creating our hidden service in %s" % hidden_service_dir)
  result = controller.create_hidden_service(hidden_service_dir, 80, target_port = 5000)

  # The hostname is only available when we can read the hidden service
  # directory. This requires us to be running with the same user as tor.

  if result.hostname:
    print(" * Our service is available at %s, press ctrl+c to quit" % result.hostname)
  else:
    print(" * Unable to determine our service's hostname, probably due to being unable to read the hidden service directory")

  try:
    app.run()
  finally:
    # Shut down the hidden service and clean it off disk. Note that you *don't*
    # want to delete the hidden service directory if you'd like to have this
    # same *.onion address in the future.

    print(" * Shutting down our hidden service")
    controller.remove_hidden_service(hidden_service_dir)
    shutil.rmtree(hidden_service_dir)

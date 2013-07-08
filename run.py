from bottle import route, run, template, request, get, post
import listdocs
import getpass
from tabulate import tabulate

@route('/')
def login_prompt():
    return template('templates/login.tpl')

@route('/login', method='POST')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    global spreadclient
    spreadclient = listdocs.spreadserv.SpreadsheetsService()
    spreadclient.email = username
    spreadclient.password = password
    spreadclient.ProgrammaticLogin()
    global spreadsheet_feed
    spreadsheet_feed = spreadclient.GetSpreadsheetsFeed()
    set_spreadid = ''
    global processed_ids
    processed_ids = listdocs.get_spreadsheet_ids(spreadsheet_feed, spreadclient)
    return template('templates/mainmenu.tpl', processed_ids=processed_ids, spreadsheet_feed=spreadsheet_feed)

@route('/set_spreadsheet', method='POST')
def set_workingsheet():
    try:
        command = set_spreadid + ' ' + set_workid
        listdocs.set_spreadsheet(command)
        table = listdocs.sheet_read(spreadclient)[0]
        keys = listdocs.sheet_read(spreadclient)[1]
        row_list = listdocs.sheet_read(spreadclient)[2]
        return template('templates/console.tpl', table=table, keys=keys, row_list=row_list)
    except:
        global set_spreadid
        set_spreadid = request.forms.get('set_spreadid')
        global set_workid
        set_workid = request.forms.get('set_workid')
        command = set_spreadid + ' ' + set_workid
        listdocs.set_spreadsheet(command)
        table = listdocs.sheet_read(spreadclient)[0]
        keys = listdocs.sheet_read(spreadclient)[1]
        row_list = listdocs.sheet_read(spreadclient)[2]
        return template('templates/console.tpl', table=table, keys=keys, row_list=row_list)

@route('/insert_row', method="GET")
def insert_data():
    cols = listdocs.make_columns(spreadclient)
    import pdb; pdb.set_trace()
    return template('templates/insert.tpl', cols=cols)

@route('/created_row', method="POST")
def created_row():
    new_row = {}
    cols = listdocs.make_columns(spreadclient)
    for key in cols:
        new_row[key] = request.forms.get(key)
    listdocs.insert_row(new_row, set_spreadid, set_workid, spreadclient)
    return set_workingsheet()

@route('/update_row', method="GET")
def updateing_row():
    import pdb; pdb.set_trace()
    return set_workingsheet()
     
 
run(host='localhost', port=8080, debug=True)

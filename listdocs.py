import gdata.docs.service as docserv
import gdata.spreadsheet.service as spreadserv
import getpass
from tabulate import tabulate

def get_spreadsheet_ids(spreadsheet_feed, spreadclient):
    spread_keys = []
    spread_ids = []
    group = []
    out = []
    for spreadsheet in spreadsheet_feed.entry:
        spread_keys.append(spreadsheet.id.text.rsplit('/', 1)[1])
    for i in range(len(spreadsheet_feed.entry)):
        curkey = spread_keys[i]
        worksheet_feed = spreadclient.GetWorksheetsFeed(curkey)
        for worksheet in worksheet_feed.entry:
            group.append(worksheet.id.text.rsplit('/', 1)[1])
        spread_ids.append(group)
        group = []
        spread_needs = zip(spread_keys, spread_ids)
    for key, value in spread_needs:
        out.append(' ' + str(key) + ' ' + str(value))
    return out

def print_spreadsheets_ids(processed_ids):
    for i in range(len(spreadsheet_feed.entry)):
        print spreadsheet_feed.entry[i].title.text + processed_ids[i]

def sheet_read(spreadclient):
    feed = spreadclient.GetListFeed(set_spreadid, set_workid)
    keys = feed.entry[0].custom.keys()
    row_sub_list = []
    row_list = []
    for row in feed.entry:
        row_sub_list = []
        for key in row.custom.keys():
	    row_sub_list.append(row.custom[key].text)
        row_list.append(row_sub_list)
    table = tabulate(row_list, headers= keys)         
    return [table, keys, row_list]

def set_spreadsheet(command):
    working_sheet = command.split()
    global set_spreadid
    set_spreadid = working_sheet[0]
    global set_workid
    set_workid = working_sheet[1]

def make_columns(spreadclient):
    feed = spreadclient.GetListFeed(set_spreadid, set_workid)
    splitted_columns = feed.entry[0].custom.items()
    col = []
    for i in range(len(splitted_columns)):
        col.append(splitted_columns[i][0])
    return col

def enter_columns(cols):
    new_row = {}
    for col in cols:
        new_row[col] = raw_input(col + ' ')
    return new_row

def insert_row(row, set_spreadid, set_workid, spreadclient):
    spreadclient.InsertRow(row, set_spreadid, set_workid)

def update_row(command):
    feed = spreadclient.GetListFeed(set_spreadid, set_workid)
    old_row = int(command.split()[1]) - 1
    cols = make_columns()
    new_row = enter_columns(cols)
    spreadclient.UpdateRow(feed.entry[old_row], new_row)

def delete_row(command):
    feed = spreadclient.GetListFeed(set_spreadid, set_workid)
    row_to_del = int(command.split()[1]) - 1
    spreadclient.DeleteRow(feed.entry[row_to_del])

if __name__ == "__main__":
    command = ''
    while command != 'q':
        print '\nCommands:'
        print 'q = quit'
        print 'g = get'
        print 's = spreadsheet ids'
        print 'set [spreadsheet id] [worksheet id] = set a worksheet to work on'
        print 'read = read worksheet'
        print 'insert = insert row'
        print 'update [row #] = update specified row'
        print 'delete [row #] = deletes specified row'
        command = raw_input('Command: ')
        print '------------------------'
        if command == 'g':
            get_list()
        elif command == 's':
            processed_ids = get_spreadsheet_ids()
            print_spreadsheets_ids(processed_ids)
        elif command == 't':
            test()
        elif 'set' in command:
            set_spreadsheet(command)
        elif 'read' in command.split():
            sheet_read()
        elif 'insert' in command:
            cols = make_columns()
            row = enter_columns(cols)
            insert_row(row)
        elif 'update' in command:
            update_row(command)
        elif 'delete' in command:
            delete_row(command)
        elif command == 'q':
            break
        else:
            print "invalid command"

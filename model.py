import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
id_number= 0

def init():
    global entries
    try:

        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []
    print(entries)

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, id_number
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "id_number": id_number}
    id_number += 1
    print(id_number)
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(clicked_id):
    global entries, GUESTBOOK_ENTRIES_FILE, id_number
    # print("IDNUM : " clicked_id)
    # entry = {"author": name, "text": text, "timestamp": time_string, "id_number": id_number}
    # indexed_number = 0
    for ele in entries:
        if int(clicked_id) == ele["id_number"]:
            try:
                entries.remove(ele)
                break
            except:
                pass
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("error!")
    print(entries)



        # if int()
        # print("the selected index is: ")
        # print(indexed_number)
        # print("entry i is: ")
        # print(i)
        # print("the id number is:")
        # print(i["id_number"])
        # print("the selected number is: ")
        # print(id_n)
        # if i['id_number'] == id_n:
        #     print("yay, it's the same!")
        #     entries.delete(entries[indexed_number])
        #     break
        # indexed_number += 1
    # print(entries)

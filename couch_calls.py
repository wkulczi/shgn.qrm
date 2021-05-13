import couchdb

couch = None
db = None
db_name = None

def init(couch_db_url= 'http://test:test@127.0.0.1:5984', database_name = 'mockups'):
    global couch, db, db_name
    db_name=database_name
    couch = couchdb.Server(couch_db_url)
    try:
        db = couch[database_name]
    except couchdb.http.ResourceNotFound:
        print("[EX] Database not founc, creating new db with name: {}".format(db_name))
        db = couch.create(db_name)

def get_timestamp():
    from datetime import datetime
    now = datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M:%S"))

def add_record(_value, _type):
    doc = {'value': _value, 'type': _type, 'date': get_timestamp()}
    db.save(doc) #todo ustaw timestamp jako id

def get_records_manually(_type):
    try:
        resultlist = list()
        for doc in db.find({'selector': {'type': _type}}):
            resultlist.append({'date':doc['date'], 'value':doc['value']})
        return resultlist
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        return []

def get_records_from_view(_type):
    try:
        resultlist = []
        for doc in db.view('testdesigndoc/'+_type):
            print(doc)
            resultlist.append({'date':doc.key, 'value':doc.value})
        return resultlist
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        return []
        
def get_records_by_key(_type, reverse_results=True):
    result = []
    if (_type=='temp'):
        result = get_records_from_view('temp-view')
        if not result:
            result = get_records_manually(_type)
    elif (_type =='light'):
        result = get_records_from_view('light-view')
        if not result:
            result = get_records_manually(_type)
    if reverse_results:
        return result[::-1]
    else:
        return result

def clear_db():
    del couch[db_name]

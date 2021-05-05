import couchdb

couch = None
db = None
db_name = None

def init(couch_db_url= 'http://admin:admin@127.0.0.1:5984', database_name = 'mockups'):
    global couch, db, db_name
    db_name=database_name
    couch = couchdb.Server(couch_db_url)
    try:
        db = couch[database_name]
    except couchdb.http.ResourceNotFound:
        print("[EX] Database not founc, creating new db with name: {}".format(db_name))
        db = couch.create(db_name)

def get_timestamp():
    import time
    ts = time.gmtime()
    return str(time.strftime("%Y-%m-%d %H:%M:%S", ts))

def add_record(_value, _type):
    doc = {'value': _value, 'type': _type, 'date': get_timestamp()}
    db.save(doc) #todo ustaw timestamp jako id

def get_records(_type):
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

def clear_db():
    del couch[db_name]
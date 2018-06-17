import Config.DataSource as ds
import hashlib
import uuid


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


# TO BE IN LOGIN HANDLER FILE
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def handle_register(username, password):
    # GET THE DATABASE
    data_source = ds.DataSource()
    db = data_source.getDB()

    # GET THE REQUIRED COLLECTION
    db_users = db['users']

    # QUERY THE COLLECTION INTO CURSOR
    users = db_users.find()
    usernames = []

    if users.count() != 0:
        # GET ALL USERNAMES
        for user in users:
            usernames.append(user['user_name'])

        # CHECK IF USERNAME IS DUPLICATE
        if (username in usernames):
            data_source.close()
            return {"message": "Duplicate User Name"}

        # GENERATE NEW ID
        users.rewind()
        id = users.sort([("_id", -1)]).limit(1)[0]["_id"] + 1
    else:
        id = 1;

    # HASH THE PASSWORD
    hex_password_dig = hash_password(password)

    # INSERT THE DATA
    data = {"_id": id, "user_name": username, "password": hex_password_dig}
    id_ret = db_users.insert_one(data).inserted_id

    # END
    if (id_ret != None):
        data_source.close()
        return {"message": "Data Inserted"}

import Config.DataSource as ds
import hashlib
import random
import base64


class Auth:

    def __init__(self):
        self.token = ''

    def __init__(self, token):
        assert isinstance(token, str)
        self.token = token

    # TO BE IN LOGIN HANDLER FILE
    def check_password(self,hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def generate_token(self):
        x = random.randint(1000, 99000)
        token = hashlib.sha3_256(str(x).encode()).hexdigest()
        self.token = token

    def store_server_session(self):
        # GET THE DATABASE
        data_source = ds.DataSource()
        db = data_source.getDB()

        # GET THE REQUIRED COLLECTION
        db_users = db['users']
        # INSERT TOKEN
        db_users.insert_one({"token": self.token})

    def delete_server_session(self):
        # GET THE DATABASE
        data_source = ds.DataSource()
        db = data_source.getDB()

        # GET THE REQUIRED COLLECTION
        db_users = db['users']
        # DELETE TOKEN
        db_users.delete_one({"token": self.token})

    def start_server_session(self):
        self.generate_token()
        self.store_server_session()
        self.throw_auth_token()

    def throw_auth_token(self):
        return {"token":self.token}

    def close_server_session(self):
        self.delete_server_session()
        return {"message": "Logged out Successfully"}


    def authenticate_user(self,credentials):

        result=None

        cred_dec=self.decode_auth_header(credentials)
        username=cred_dec["username"]
        password=cred_dec["password"]

        # GET THE DATABASE
        data_source = ds.DataSource()
        db = data_source.getDB()

        # GET THE REQUIRED COLLECTION
        db_users = db['users']

        #MAKE QUERY DOCUMENT
        query={"user_name":username}

        # QUERY THE COLLECTION INTO CURSOR
        users = db_users.find(query)

        for user in users:
            if self.check_password(user['password'],password):
                #AUTHENTICATED
                self.start_server_session()
                self.throw_auth_token()
            else:
                return {"token":"UNAUTHORIZED"}


    def decode_auth_header(self,cred):
        decoded=base64.b64decode(cred).decode()
        cnt=0;
        for char in decoded:
            if(char==':'):
                break
            cnt=cnt+1

        username=decoded[:cnt]
        password=decoded[cnt+1:]

        return {"username":username, "password":password}




#Outside of class
def is_authorized(token):
    # GET THE DATABASE
    data_source = ds.DataSource()
    db = data_source.getDB()

    # GET THE REQUIRED COLLECTION
    db_tokens = db['auth_tokens']

    query = {"token":token}
    retrieved = db_tokens.find_one()

    if retrieved is not None:
        return True
    else:
        return False














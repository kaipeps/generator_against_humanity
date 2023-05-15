from db.db import sql
import bcrypt

def create_user(first_name, last_name, email, password):
    password_digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql('INSERT INTO users(first_name, last_name, email, password_digest, is_admin) VALUES(%s, %s, %s, %s, FALSE) RETURNING *', [first_name, last_name, email, password_digest])

def find_user_by_email(email):
    users = sql('SELECT * FROM users WHERE email = %s', [email])
    if len(users) > 0:
        return users[0]
    else:
        return None

def find_user_by_id(id):
    users = sql('SELECT * FROM users WHERE user_id = %s', [id])
    return users[0]

def generate_author_name(author_id):
    users_names = sql(f'SELECT first_name, last_name FROM users WHERE user_id = {author_id}')
    author_name = users_names[0]
    author_name = author_name['first_name'] + ' ' + author_name['last_name']
    return author_name

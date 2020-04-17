# pip install flask-bcrypt
from flask_bcrypt import Bcrypt

# Generate password Hash
bcrypt = Bcrypt()
password = bcrypt.generate_password_hash('testing').decode('utf-8')
print(password)

# Generate different Hash every time you generate password (can't use hash table to hack password)
# bcrypt.check_password_hash(pw_hash, password) return True if match
match = bcrypt.check_password_hash(password, 'fakepassword')
print(match)

match = bcrypt.check_password_hash(password, 'testing')
print(match)
import bcrypt


class Hash:
    def check_hash(password, hashed_password):
        return bcrypt.checkpw(password.encode("UTF-8"), hashed_password)

    def get_hash(password, salt):
        return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt(salt))

admin_list = [('ADMIN1', 'admin1'), ('ADMIN2', 'admin2'), ('ADMIN3', 'admin3')]


def user_name(username, user_password):
    for item in admin_list:
        if item[0] == username and item[1] == user_password:
            return True
    else:
        return False



def save():
    with open(r"file\user.csv", 'a') as file_users:
        users = file_users.write('\n' + new_user)
        print("Data successfully added!")
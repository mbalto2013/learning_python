def username_generator(first_name, last_name):
    rs_first_name = first_name[:3] if len(first_name) >= 3 else first_name
    rs_last_name = last_name[:4] if len(last_name) >= 4 else last_name
    user_name = rs_first_name + rs_last_name
    return(user_name)
    
def password_generator(user_name):
    password = user_name[-1] + user_name[0:-1]
    #+ user_name[1:-1]
    print(password)



password_generator("AbeSimp")
#print(username_generator('Abe', 'Simpson'))


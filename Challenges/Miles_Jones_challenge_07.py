def stored_passwords(passCheck):
    badPass = ('123456','123456789','12345','qwerty',
               'password','12345678','111111','123123',
               '1234567890','1234567','qwerty123','000000',
               '1q2w3e','aa12345678','abc123','password1',
               '1234','qwertyuiop','123321','password123',
               '1q2w3e4r5t','iloveyou','654321','666666',
               '987654321','123','123456a','qwe123',
               '1q2w3e4r','7777777','1qaz2wsx','123qwe',
               'zxcvbnm','121212','asdasd','a123456',
               '555555','dragon','112233','123123123',
               'monkey','11111111','qazwsx','159753',
               'asdfghjkl','222222','1234qwer','qwerty1',
               '123654','123abc')


    if passCheck in badPass:
        found = f"{passCheck} at index {badPass.index(passCheck)}. Your password is too common.  Please consider changing it."
        return found
    else:
        notFound = "This is a strong password"
        return notFound


        

def getUserPass():
    userName = input("Please enter a username: ")
    while True:
        userPass = input("Please enter a password: ")
        result = stored_passwords(userPass)
        print(result)
        if result == "This is a strong password":
            break
    


def main():
    getUserPass()


if __name__ == "__main__":
    main()
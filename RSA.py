import md5



####Calculate the MD5 Hash Value of the Following String
##m = md5.new()
##m.update("12lsdfahlwfhiqwefuqwguifhsfgjksagf2qiuofwqieurihfiasfhdqpweiqoweyiqoryquiwdfg3")
##m1= m .hexdigest()
##


##Simple Non-Secure Numerical Only RSA Function

def resarsaencfunc():
    try:
            m = int(input('Input Some Random Number')) #5
            e = int(input('Input Some Random Number')) #5321
            n = int(input('Input Some Random Number')) #15 # n =10545437.0
            func_value= m**e%n
            return func_value
    except:
        print "Input is Not a Valid Number"

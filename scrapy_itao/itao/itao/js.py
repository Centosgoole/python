import time,random

def get_collback():
    salt = int(time.time() * 1000)
    randomstr = str(random.random()).replace(".", '')
    callback = "jQuery" + "183" + randomstr + "_" + str(salt)
    return str(callback)

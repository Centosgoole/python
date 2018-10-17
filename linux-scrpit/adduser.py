import random,string,os

def main():
    user_file = open("./emlusers.txt").read().split(",")
    for i in range(len(user_file)):
        user = user_file[i]
        passwd= ''.join(random.sample(string.ascii_letters + string.digits, 10))
        chickuser = os.system("useradd {}".format(user))
        if chickuser == 0:
            os.system("echo {} |passwd --stdin {}".format(passwd,user))
            with open(r"./emailinfo.txt","a+") as f:
                f.write(user+","+passwd+"\n")
                print("adduser:{}/{}---Done----({}/{})".format(user,passwd,i,len(user_file)))
        else:
			pass
            continue
            
if __name__ =="__main__":
    main()

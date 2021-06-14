import re
while 1:
    email=input("Unesite Vas e-mail: (ime.prezime@fpmoz.sum.ba) ")
    eduid=input("Unesite Vas EduID: (IPrezimeX@sum.ba) ")
    prezime=email[email.index(".")+1:email.index("@")]
    regex="^([a-zA-Z]+).([a-zA-Z]+)(@fpmoz.sum.ba)$"
    regex2="^([a-zA-Z]+)[0-9]*(@sum.ba)$"
    rez1=re.match(regex,email)
    rez2=re.match(regex2,eduid)
    if rez1:
        print("E-mail formalno validan...")
        if rez2:
            print("EduID formalno validan...")
            if (prezime in eduid[1:len(prezime)+1]) and (email[0]==eduid[0]) and (prezime not in eduid[len(prezime)+1:]):
                print("Unos potpuno validan!")
                break
            else:
                print("Unosi se ne podudaraju!")
                break
        else:
            print("Unos EduID nije validan!")
    else:
        print("Unos mail-a nije validan!")
    break

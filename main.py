    # 1-uyga vazifa
mystr = "Alijon"
myit = iter(mystr)
print(next(myit)) # A
print(next(myit)) # l
print(next(myit)) # i
print(next(myit)) # j
print(next(myit)) # o
print(next(myit)) # n


    # 2-uyga vazifa
username=input("USERNAME")
password=input("PASSWORD")
email=input("EMAIL")
parol=input("PAROL")
_username="Alijon"
_password="123456789"
_email="alijonrashidov011gmail.com"
_parol="alijon"

if "1" in email:
    print("Email to'g'ri kiritildi")
    if"A" in username:
        print("Username to'g'ri kiritildi")
        print("Yaxshimisiz Admin")
    else:
        print("Ma'lumotlar xato kiritildi")

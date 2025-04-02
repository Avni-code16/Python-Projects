# A simple email slicer program in python
# it splits into username and domain name

def email_slicer(email):
    if "@" not in email:
        return "Invalid email format"

    username, domain = email.split("@")
    return f"Username: { username} \n Domain: {domain}"

e_mail = input("Please enter email ID : ")
print(email_slicer(e_mail))

email = "Amit_ml@gmail.edu"


if email.count("@") == 1 and "." in email.split("@")[1]:

    username = email.split("@")[0]

    
    domain_part = email.split("@")[1]
    domain = domain_part.rsplit(".", 1)[0]

    
    if email.endswith(".com"):
        domain_type = "Commercial Domain"
    elif email.endswith(".edu"):
        domain_type = "Educational Domain"
    else:
        domain_type = "Other Domain"

    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Domain Type: {domain_type}")
else:
    print("Invalid email")
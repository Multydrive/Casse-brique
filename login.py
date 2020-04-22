class Login():

    def register():
        print ("Inscription")
        username = input("Entrez le nom d'utilisateur ")
        password = input("Entrez le mot de passe ")
        file = open("accountfile.txt","a")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write("\n")
        file.close()
        if login():
            print("Connecté")
        else:
            print("Echec lors de la connexion")

    def login():
        print("Connexion")
        username = input("Entrez le nom d'utilisateur ")
        password = input("Entrez le mot de passe ")
        for line in open("accountfile.txt","r").readlines(): # Read the lines
            login_info = line.split() # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password == login_info[1]:
                print("Correct credentials!")
                return True
        print("Incorrect credentials.")
        return False

    register()

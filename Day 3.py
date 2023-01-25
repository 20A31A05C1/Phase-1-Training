# Dictionaries
for i in range (1):
    d = {
        'key1': input("Enter key 1:- "),
        'key2': input("Enter key 2:- ")
    }
    print(d)

# Update values
l = []
d = {}
for i in range (1):
    d.update({
        'key1': input("Enter key 1:- "),
        'key2': input("Enter key 2:- ")
    })
    l.append(d)
print(l)

# Username and Password
for i in range (1):
    d = {
        'Username': input("Username:-  "),
        'Password': input("Password:-  ")
    }
    print(d)

# Username and Password Validation
db = [{'nishi@gmail.com': 'abcd1234'},
      {'naina@gmail.com': 'asdf1234'},
      {'cse@gmail.com': 'qwerty1234'},
      {'mdp@gmail.com': 'hello1234'},
      {'pragati@gmail.com': 'pragati@123'}
      ]
username = input("Enter the username")
password = input("Enter the password")
temp = {username : password}
if temp in db:
    print("Found")
else:
    print("Not found")

# Password validation

# Define a dictionary to store the username and password
credentials = {"username": "admin", "password": "password123"}

# Prompt the user to enter their username and password
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Check if the entered username and password match the stored values
if entered_username == credentials["username"] and entered_password == credentials["password"]:
    print("Access granted!")
else:
    print("Access denied. Incorrect username or password.")

# Matrix Addition


    def add_matrices(mat1, mat2):
        # Get the dimensions of the matrices
        rows = len(mat1)
        cols = len(mat1[0])

        # Initialize the result matrix with zeroes
        result = [[0 for j in range(cols)] for i in range(rows)]

        # Perform the addition
        for i in range(rows):
            for j in range(cols):
                result[i][j] = mat1[i][j] + mat2[i][j]

        return result


    # Example usage
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    result = add_matrices(mat1, mat2)
    print(result)  # [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

# Fibonacci series














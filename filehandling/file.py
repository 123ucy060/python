
#file write, read, append

# Writing to a file (overwrites existing content)

file = open("book.txt", "w")

file.write("Login Success - User: admin\n")
file.write("Login Failed - User: guest\n")
file.write("IP Blocked - 192.168.1.10\n")

file.close()



#reading from a file

file = open("book.txt", "r")
content = file.read()
print(content)
file.close()



#appending to a file (adds content to the end of the file)

file = open("book.txt", "a")

file.write("Suspicious Activity - IP: 10.0.0.5\n")

file.close()


#csv file operations(comma separated values)
# writing to a csv file   
import csv

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Status"])
    writer.writerow(["admin", "Success"])
    writer.writerow(["guest", "Failed"])


# reading from a csv file
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



#json file operations (JavaScript Object Notation)
# writing to a json file
import json

aler = {
    "user": "admin",
    "ip": "192.168.1.5",
    "status": "suspicious"
}

with open("alert.json", "w") as file:
    json.dump(aler, file)



# reading from a json file
with open("alert.json", "r") as file:
    data = json.load(file)
    print(data)

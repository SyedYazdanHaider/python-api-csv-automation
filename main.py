import requests
print(requests.__version__)
url = "https://jsonplaceholder.typicode.com/users"
response  = requests.get(url)
users = response.json()

#print(users[1]["name"])

with open("users.csv","w") as file:
    file.write("name,username,email,city\n")

    for x in range(len(users)):
        user = users[x]
        file.write(f"{user['name']},{user['username']},{user['email']},{user['address']['city']}\n")


with open("users.csv","r") as file,open("result2.txt","w") as writeFile:
    file.readline()
    cities = set()
    cityList = []
    count = 0

    for line in file:
        name,username,email,city = line.strip().split(",")
        cityList.append(city)
        cities.add(city)
        count+=1
    
    writeFile.write(f"Total Users: {count}\nUnique cities: {len(cities)}\nCities list: {cityList}")

with open("result2.txt","r") as readfile:
    print(readfile.read())

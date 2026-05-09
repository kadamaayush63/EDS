team={}
for i in range(11):
    name=input("Enter player Name: ")
    height=int(input("Enter height : "))
    team[name]=height
captain=max(team)
print(team)
print(captain)
print(team[captain])

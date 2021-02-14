current_users = ['Sasha', 'Vera', 'Admin', 'Troll', 'Kolyan']
new_users = ['Tolyan', 'Sasha', 'Troll', 'Ann', 'Mike']
current_users = [name.lower() for name in current_users]  
print(current_users) 
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user)
        print("Menyai imya")
    else:
        print("Grac")

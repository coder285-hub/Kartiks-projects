file_name = input("Enter the name of the file: ")
file_extension=file_name.rsplit(".",1)[1]
if file_extension.lower() in ['gif', 'jpg', 'jpeg', 'png']:
    print("image/",file_extension)
elif file_extesnion.lower()in


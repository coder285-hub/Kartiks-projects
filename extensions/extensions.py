file_name = input("Enter the name of the file: ")
file_extension=file_name.rsplit(".",1)[1]
if file_extension.lower() in ['gif', 'jpg', 'jpeg', 'png']:
    print(f"image/{file_extension}")
elif file_extension.lower() in ['pdf', 'txt', 'zip']:
    print(f"application/{file_extension}")
else:
    print("application/octet-stream")


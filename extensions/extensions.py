file_name = input("Enter the name of the file: ")
file_extension=file_name.rsplit(".",1)[1] if '.' in file_name else ''
if file_extension.lower() in ['gif', 'jpg', 'jpeg', 'png']:
    if file_extension == 'jpg':
        file_extension = 'jpeg'
    print(f"image/{file_extension.lower()}")
elif file_extension.lower() in ['pdf', 'zip']:
    print(f"application/{file_extension.lower()}")
elif file_extension.lower()==txt:
    print("text/plain")
else:
    print("application/octet-stream")


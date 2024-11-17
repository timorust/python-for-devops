def readFile(file_path):
    try:
        file = open(file_path, "r")
        data = file.read()
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("An I/O error occurred")
    else:
        print("File content:")
        print(data)
    finally:
        print("Closing the file")
        try:
            file.close()
        except NameError:
            print("File was not opened, cannot close")

readFile("close.txt")

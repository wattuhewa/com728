def search(file_path):
    print("Searching.....")
    with open(file_path) as file:
        for line in file.readlines():
            print(f"Looked in {line.strip()}")
    print("....Done")

def run():
    search("c:/data/files/txt/locations.txt")

run()

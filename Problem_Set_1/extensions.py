
def main():
    file = input("Filename: ").lower().strip()

    media_types = {

        ".gif": "image/media",
        ".zip": "files/application",
        ".jpg": "image/media",
        ".jpeg": "image/media",
        ".png": "image/media",
        ".pdf": "text/document",
        ".txt": "text/document"
    }
    for ext, media in media_types.items():
        if file.endswith(ext):
            print(media)
            return
    print("application/octet-stream")

main()
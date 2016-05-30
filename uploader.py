import easygui
import webbrowser
from imgurpython import ImgurClient

CLIENT_ID = 'CLIENT_ID_HERE'
CLIENT_SECRET = 'CLIENT_SECRET_HERE'
path = easygui.fileopenbox()
album = None

def upload(client):
    config = {
		'title': 'Uploaded with EZPZU by didey.',
    }
    print("Image is being uploaded...")
    image = client.upload_from_path(path, anon=False)
    print()

    return image


if __name__ == '__main__':
    client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
    image = upload(client)
    print("Image posted.")
    with open("images.txt", "a") as links:
        links.write(image['link'] + "\n")
    webbrowser.open_new_tab(image['link'])



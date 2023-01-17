
# NOTE: Internet connection required


import os
import requests
import webbrowser
import openai

from io import BytesIO
from PIL import Image


# If you want to open an image in browser set "in_browser" on True
in_browser: bool = False


# Here you have to enter your own api key
# openai.api_key = "your api key"
# To find your api key you need to go to https://beta.openai.com/overview, then sign up / log in
# Then click on your profile (upper right corner) and enter "View API keys" and generate a new API key
openai.api_key = "your api key"


def check_where_to_open(data: dict):
    if in_browser == True:
       open_in_browser(data["img_url"])

    elif in_browser == False:
        open_in_system(data["img_data"], data["img_name"])


def open_in_browser(img_url):
    webbrowser.open_new_tab(img_url)

def open_in_system(img_data, img_name):
    img = Image.open(BytesIO(img_data))
    img.show()


def genarate_an_image(prompt, i):
    img_res = "256x256"
    img_name = prompt

    try:
        print(f'\nGenerating image {i + 1}: "{prompt}"...')

        response = openai.Image.create(prompt=prompt, n=1, size=img_res)
        img_url = response["data"][0]["url"]
        img_data = requests.get(img_url).content

        print("Done")

        return {
            "img_url": img_url,
            "img_data": img_data,
            "img_name": img_name
        }

    except openai.error.OpenAIError as e:
        print(f"ERROR: {e}\nHTTP STATUS: {e.http_status}")


# main
if __name__ == "__main__":
    # Getting input from the user
    # Here we ask about the subject of the picture
    prompt = input("Please enter the topic of the image: ")

    # And here for the number of images
    # The number you enter must be a positive integer
    amount_of_images = int(input("Please enter the number of generated images: "))

    # image resolution
    # All possible sizes: "256x256", "512x512", "1024x1024"
    image_res = "512x512"

    for i in range(amount_of_images):
        img = genarate_an_image(prompt, i)
        check_where_to_open(img)

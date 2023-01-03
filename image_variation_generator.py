
# NOTE: Internet connection required

from io import BytesIO
from PIL import Image
import webbrowser
import openai


# Here you have to enter your own api key
# openai.api_key = "your api key"
# To find your api key you need to go to https://beta.openai.com/overview, then sign up / log in
# Then click on your profile (upper right corner) and enter "View API keys" and generate a new API key
openai.api_key = "your api key"

# Here we ask about the number of images
# The number you enter must be a positive integer
user_range = int(input("Please enter the number of generated images: "))

# image resolution
# All possible sizes: "256x256", "512x512", "1024x1024"
image_res = "512x512"

try:
    for i in range(0, user_range):
        print(f"\nGenerating image {i + 1}...")

        # Read the image file from disk and resize it
        # Here you have to enter your image which you want to make a variation
        # image = Image.open("image.png")
        # Format can be any
        image = Image.open("image.png")
        width, height = 256, 256
        image = image.resize((width, height))

        # Convert the image to a BytesIO object
        byte_stream = BytesIO()
        image.save(byte_stream, format='PNG')
        byte_array = byte_stream.getvalue()

        response = openai.Image.create_variation(
            image=byte_array,
            n=1,
            size=image_res
        )
        image_url = response["data"][0]["url"]

        print(f"Image {i + 1}: {image_url}\n")
        # Opening the generated image in a browser
        # You can use "webbrowser.open_new_tab()" as well
        webbrowser.open_new_tab(image_url)

except openai.error.OpenAIError as e:
    print(f"ERROR: {e}\nHTTP STATUS: {e.http_status}")

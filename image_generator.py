
# NOTE: Internet connection required

import webbrowser
import openai


# Here you have to enter your own api key
# openai.api_key = "your api key"
# To find your api key you need to go to https://beta.openai.com/overview, then sign up / log in
# Then click on your profile (upper right corner) and enter "View API keys" and generate a new API key
openai.api_key = "your api key"

# Getting input from the user
# Here we ask about the subject of the picture
user_prompt = input("Please enter the topic of the image: ")
# And here for the number of images
# The number you enter must be a positive integer
user_range = int(input("Please enter the number of generated images: "))

try:
    for i in range(0, user_range):
        print(f"\nGenerating image {i + 1}...")

        response = openai.Image.create(
            prompt=user_prompt,
            n=1,                          
            size="512x512" # all possible sizes: "256x256", "512x512", "1024x1024"
        )
        image_url = response["data"][0]["url"]

        print(f"Image {i + 1}: {image_url}\n")
        # Opening the generated image in a browser
        # You can use "webbrowser.open_new_tab()" as well
        webbrowser.open_new_tab(image_url)

except openai.error.OpenAIError as e:
    print(f"ERROR: {e}\nHTTP STATUS: {e.http_status}")

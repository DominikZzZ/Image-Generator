
# NOTE: Internet connection required


import webbrowser
import openai


# Here you have to enter your own api key
# openai.api_key = "api key"
# To find your api key you need to go to https://beta.openai.com/overview, then sign up / log in
# Then click on your profile (upper right corner) and enter "View API keys" and generate a new API key
openai.api_key = "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"

user_prompt = input("Please enter the topic of the image: ")
user_range = int(input("Please enter the number of generated images: "))

for i in range(0, user_range):
    print(f"\nGenerating image {i + 1}...")

    response = openai.Image.create(
        prompt=user_prompt,
        n=1,                          
        size="256x256" # all possible sizes: "256x256", "512x512", "1024x1024"
    )
    image_url = response["data"][0]["url"]

    print(f"{i + 1}: {image_url}\n")
    # Opening the generated image in a browser
    # You can use "webbrowser.open_new_tab()" as well
    webbrowser.open_new_tab(image_url)
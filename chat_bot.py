import google.generativeai as genai

API_KEY = "AIzaSyB_93Pb6mwqdas4nX4tTLkDu48fLjwSVGA"

genai.configure(api_key=API_KEY)

mod = genai.GenerativeModel("gemini-2.0-flash")

Me = input("Enter Your Name : ")

Name = input("Name Your Bot : ")

print("Chat with",Name,"!!!","Type bye to exit")

chat = mod.start_chat()


while True :
    text_input = input(f"{Me} : ")
    if text_input.lower() == 'bye' :
        break
    response = chat.send_message("Hello")
    print(  Name, ":",response.text)

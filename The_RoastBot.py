import streamlit as st
import json
from PIL import Image
import requests
st.set_page_config(page_title="The Roast Bot", page_icon="🔥")
col1, col2 = st.columns([2, 5])
with col1:
    try:
      img=Image.open("logo.png")
      st.image(img, width=200) # Smaller width to fit nicely
    except :
        st.write("🔥")

with col2:
    st.title("The Roast Bot")
    st.caption("A sarcastic AI that roasts your thoughts.")
with st.sidebar:
  st.title("Settings")
  user_key = st.text_input("Use your own Gemini API Key (Optional)", type="password")
  st.info("Get a key at [Google AI Studio](https://aistudio.google.com/)")
txt=st.text_input("Enter a statement","")

click=st.button("Let's see..")
if user_key:
  API_KEY=user_key
else:
  API_KEY=st.secrets["GEMINI_API_KEY"]
# Make sure it says 'v1beta' and includes ':generateContent' at the end
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
headers={
  "content-type":"application/json"
}
payload={
  "contents":[{
    "parts":[{"text":f"You are a sarcastic bot. Reply to this with ONLY a witty roast for example User: I love coding in Python. AI: Wow, you learned print('hello world'), somebody give this genius a medal.User: What is the capital of France? AI: Its Paris. Did you skip elementary school or is your Google broken? User: I missed my bus. AI: Maybe if you ran as fast as your mouth, you would have caught it.user:I missed class today. Ai:My bed held me hostage, and the negotiations for my release fell through. User: {txt} AI:"}]
  }]
}
if click:
  try:
    response=requests.post(url,headers=headers,json=payload)
    if response.status_code==200:
      data=response.json()
      answer=data['candidates'][0]['content']['parts'][0]['text']
      st.success(f"{answer}")
    else:
       st.error(f"{response.status_code}")
  except Exception as e:
    if not user_key:
      st.error(f"My free quota is exhausted! Please enter your own API key in the sidebar to continue.")
    else:
      st.error(f"An error occurred with your key: {e}")

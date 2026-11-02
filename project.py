
import streamlit as st
import openai
import os
from dotenv import load_dotenv


load_dotenv()


st.set_page_config(page_title="SmartAI Assistant", page_icon="🤖", layout="wide")


st.sidebar.title("🔑 API Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")


if api_key:
    openai.api_key = api_key
else:
    openai.api_key = os.getenv("OPENAI_API_KEY")


st.title("🤖 SmartAI Content Assistant")
st.write("Upwork Portfolio Project - Powered by Python & OpenAI")
st.markdown("---")


option = st.selectbox(
    "What would you like to do today?",
    ("Create Content (Blog/Social Media)", "Summarize Long Text", "Change Writing Tone")
)


if option == "Create Content (Blog/Social Media)":
    st.subheader("📝 AI Content Generator")
    topic = st.text_input("Enter the topic or prompt:")
    platform = St.selectbox("Select Platform:", ["Blog Post", "LinkedIn", "Twitter/X", "Facebook"])
    
    if st.button("Generate Content"):
        if not openai.api_key:
            st.error("Please provide an OpenAI API Key in the sidebar!")
        elif not topic:
            st.warning("Please enter a topic.")
        else:
            with st.spinner("AI is thinking..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini", 
                        messages=[
                            {"role": "system", "content": f"You are an expert content writer for {platform}."},
                            {"role": "user", "content": f"Write a catchy and engaging post about: {topic}"}
                        ]
                    )
                    st.success("Generated successfully!")
                    st.write(response.choices[0].message['content'])
                except Exception as e:
                    st.error(f"Error: {e}")


elif option == "Summarize Long Text":
    st.subheader("🔍 Text Summarizer")
    text_to_sum = st.text_area("Paste your long article or text here:", height=200)
    
    if st.button("Summarize"):
        if not openai.api_key:
            st.error("Please provide an OpenAI API Key!")
        elif not text_to_sum:
            st.warning("Please paste some text.")
        else:
            with st.spinner("Summarizing..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant that summarizes text concisely in bullet points."},
                            {"role": "user", "content": f"Summarize the following text:\n\n{text_to_sum}"}
                        ]
                    )
                    st.success("Summary Generated!")
                    st.write(response.choices[0].message['content'])
                except Exception as e:
                    st.error(f"Error: {e}")


elif option == "Change Writing Tone":
    st.subheader("🎭 Tone Transformer")
    original_text = st.text_area("Enter your original text:", height=150)
    tone = st.selectbox("Select Target Tone:", ["Professional", "Casual/Friendly", "Humorous/Funny", "Persuasive (Sales)"])
    
    if st.button("Transform Tone"):
        if not openai.api_key:
            st.error("Please provide an OpenAI API Key!")
        elif not original_text:
            st.warning("Please enter some text.")
        else:
            with st.spinner("Transforming..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": f"Rewrite the text to sound completely {tone}."},
                            {"role": "user", "content": original_text}
                        ]
                    )
                    st.success("Transformed Text:")
                    st.write(response.choices[0].message['content'])
                except Exception as e:
                    st.error(f"Error: {e}")

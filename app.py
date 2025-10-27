import streamlit as st
import openai

st.set_page_config(page_title="AI Love Letter Generator 💌", page_icon="💘")

st.title("💌 AI Love Letter Generator")
st.write("Surprise someone special with a personalized AI-generated love letter 💖")

# Input fields
name = st.text_input("Enter her name 💕")
vibe = st.selectbox("Choose a tone:", ["Romantic", "Funny", "Cute", "Poetic", "Filmy"])
reason = st.text_area("Why do you like her? 💫")

if st.button("Generate Love Letter 💌"):
    if not name or not reason:
        st.warning("Please fill in all fields 😊")
    else:
        with st.spinner("Writing your love letter... 💭"):
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            prompt = f"Write a {vibe.lower()} love letter for a girl named {name}. The sender likes her because {reason}. Make it sweet and natural."
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                letter = response.choices[0].message["content"]
                st.success("Here’s your AI-written love letter 💌")
                st.write(letter)
            except Exception as e:
                st.error("Error generating letter 😢 — check your API key or usage.")

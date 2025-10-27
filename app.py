import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="💘 AI Love Letter Generator", page_icon="💌")

st.title("💌 AI Love Letter Generator")
st.write("Generate a personalized AI love letter for someone special 💕")

# Inputs
name = st.text_input("Enter her name 💖")
tone = st.selectbox("Choose a tone 💫", ["Romantic", "Cute", "Poetic", "Funny", "Filmy"])
reason = st.text_area("Why do you like her? 🌸")

# Configure API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

if st.button("Generate Love Letter 💌"):
    if not name or not reason:
        st.warning("Please fill all fields 💬")
    else:
        with st.spinner("Writing your love letter... 💭"):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")  # Supported model
                prompt = f"""
                Write a {tone.lower()} love letter for a girl named {name}.
                The sender likes her because {reason}.
                Make it emotional, poetic, and heart-touching.
                """
                response = model.generate_content(prompt)
                st.success("Here’s your AI-written love letter 💌")
                st.markdown(f"### 💖 Love Letter to {name}")
                st.write(response.text)
            except Exception as e:
                st.error("Error generating letter 😢")
                st.exception(e)

# Footer
st.markdown("---")
st.markdown("<center>Made with 💖 by Tarunjit</center>", unsafe_allow_html=True)

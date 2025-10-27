import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="💌 AI Love Letter Generator", page_icon="💘")

# Title
st.title("💘 AI Love Letter Generator")
st.write("Surprise someone special with a personalized AI-generated love letter 💕")

# Input fields
name = st.text_input("Enter her name 💖")
tone = st.selectbox("Choose a tone 💫", ["Romantic", "Cute", "Poetic", "Funny", "Filmy"])
reason = st.text_area("Why do you like her? 🌸")

# Configure Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

if st.button("Generate Love Letter 💌"):
    if not name or not reason:
        st.warning("Please fill all fields 💬")
    else:
        with st.spinner("Writing your love letter... 💭"):
            prompt = f"""
            Write a {tone.lower()} love letter for a girl named {name}.
            The sender likes her because {reason}.
            Make it emotional, poetic, and sweet.
            """
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                st.success("Here’s your AI-written love letter 💌")
                st.write(response.text)
            except Exception as e:
                st.error("Error generating letter 😢")
                st.write(e)

# Footer
st.markdown("---")
st.markdown("<center>Made with 💖 by Tarunjit</center>", unsafe_allow_html=True)

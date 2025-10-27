# app.py
import streamlit as st
from google import genai
import os

st.set_page_config(page_title="💌 AI Love Letter Generator", page_icon="💘")

st.title("💌 AI Love Letter Generator")
st.write("Generate a personalized AI love letter for someone special 💕")

# Inputs
name = st.text_input("Enter her name 💖")
tone = st.selectbox("Choose a tone 💫", ["Romantic", "Cute", "Poetic", "Funny", "Filmy"])
reason = st.text_area("Why do you like her? 🌸")

# Get API key from Streamlit secrets and set it as env var for the genai client
api_key = st.secrets.get("GEMINI_API_KEY", "")
if not api_key:
    st.warning("GEMINI_API_KEY not found in Streamlit secrets. Add it under Settings → Secrets.")
else:
    # For safety we also set it to environment so genai client can pick it up if needed
    os.environ["GEMINI_API_KEY"] = api_key

if st.button("Generate Love Letter 💌"):
    if not name or not reason:
        st.warning("Please fill all fields 💬")
    else:
        with st.spinner("Writing your love letter... 💭"):
            try:
                # Create genai client (explicitly pass api_key)
                client = genai.Client(api_key=api_key)

                # Choose a supported model (gemini-2.5-flash is current as of docs)
                model_name = "gemini-2.5-flash"

                prompt = (
                    f"Write a {tone.lower()} love letter for a girl named {name}. "
                    f"The sender likes her because {reason}. Make it emotional, poetic, and sweet."
                )

                # Call the generate_content helper
                response = client.models.generate_content(model=model_name, contents=prompt)

                # The SDK returns an object with .text() or .text depending on version.
                # Try to access the returned text robustly:
                letter = None
                # newer SDK sometimes provides response.text or response.outputs...
                if hasattr(response, "text"):
                    # if response.text is callable (some SDK versions)
                    try:
                        letter = response.text
                    except Exception:
                        letter = str(response.text)
                elif hasattr(response, "outputs"):
                    # outputs is a list of objects with .text()
                    try:
                        letter = "".join([o.text for o in response.outputs if hasattr(o, "text")])
                    except Exception:
                        letter = str(response)
                else:
                    letter = str(response)

                st.success("Here’s your AI-written love letter 💌")
                st.markdown(f"### 💖 Love Letter to {name}")
                st.write(letter)

            except Exception as e:
                st.error("Error generating letter 😢")
                st.exception(e)

# Footer
st.markdown("---")
st.markdown("<center>Made with 💖 by Tarunjit</center>", unsafe_allow_html=True)

import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Custom CSS for new attractive layout
st.markdown("""
    <style>
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
        color: #f4f4f9;
        font-family: 'Montserrat', sans-serif;
    }

    .header {
        text-align: center;
        color: #ffffff;
        font-size: 42px;
        font-weight: 700;
        padding: 20px 0;
    }

    .subheader {
        text-align: center;
        color: #f4f4f9;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .result-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        color: #ffffff;
        font-size: 18px;
    }

    .stButton>button {
        background-color: #4caf50;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #45a049;
    }

    .footer {
        text-align: center;
        margin-top: 60px;
        color: #f4f4f9;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# Application Title
st.markdown('<h1 class="header"> 🌍 Language Translator</h1>', unsafe_allow_html=True)

# Layout - Split into two columns
col1, col2 = st.columns(2)

with col1:
    # User input for word/sentence
    word = st.text_input("Enter a word or sentence to translate:")

with col2:
    # Language search input
    search = st.text_input("Search for a language:")

    # Filter the languages based on the search term
    language_options = [language for language in LANGUAGES.values() if search.lower() in language.lower()]

    if not language_options:
        st.write("No languages match your search.")
    else:
        # Selectbox to choose the target language
        target_language = st.selectbox("Select the target language:", language_options)

# Translate button and display results
if word:
    # Detect the input language
    detected_language = translator.detect(word).lang
    detected_language_name = LANGUAGES[detected_language].capitalize()

    st.markdown(f"<p><b>Detected Language: </b>{detected_language_name}</p>", unsafe_allow_html=True)

    # Add a button to trigger the translation
    if st.button("Translate"):
        # Get the code of the selected language
        target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]
        translated = translator.translate(word, dest=target_language_code)

        # Display detected language and translated text
        st.markdown(f'<div class="result-box">Input Language: {detected_language_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">Translated Text in {target_language}: {translated.text}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">Built with ❤️ using Streamlit</p>', unsafe_allow_html=True)

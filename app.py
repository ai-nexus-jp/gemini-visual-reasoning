import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv
from src.gemini_logic import check_object_with_gemini

# Load environment variables
load_dotenv()

# Branding and Page Config
st.set_page_config(
    page_title="Gemini Vision Explorer",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for branding
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
    }
    h1 {
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Gemini Vision Explorer")
st.markdown("### Detect objects and their context in scenes using Gemini 2.5")
st.markdown("---")

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")
    # Try to get key from environment variable
    env_api_key = os.getenv("GOOGLE_API_KEY")
    
    api_key_input = st.text_input(
        "Enter Google API Key",
        value=env_api_key if env_api_key else "",
        type="password",
        help="Your Google Gemini API Key. To avoid entering this every time, set it in a .env file."
    )
    model_name = st.selectbox("Select Model", ["gemini-2.5-flash"])
    
    st.markdown("---")
    st.markdown("### Custom Instructions")
    custom_prompt = st.text_area(
        "Optional: Describe what to look for (e.g., 'The blue bottle, not the red one')",
        help="Add specific details or constraints for the AI."
    )
    
    st.markdown("---")
    st.markdown("Built with ❤️ by [Your Name]")


# Main UI
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Target Object")
    target_file = st.file_uploader("Upload Target Image", type=["jpg", "png", "jpeg"], key="target")
    if target_file:
        target_image = Image.open(target_file)
        st.image(target_image, caption="Target Object", width="stretch")

with col2:
    st.subheader("2. Scene Image")
    scene_file = st.file_uploader("Upload Scene Image", type=["jpg", "png", "jpeg"], key="scene")
    if scene_file:
        scene_image = Image.open(scene_file)
        st.image(scene_image, caption="Scene to Analyze", width="stretch")

st.markdown("---")

# Execution button
if st.button("Analyze Images"):
    if not api_key_input:
        st.error("Please enter your Google API Key in the sidebar.")
    elif not target_file or not scene_file:
        st.warning("Please upload both the Target Object and Scene images.")
    else:
        with st.spinner("Analyzing..."):
            # Convert uploaded files to images for the API
            result = check_object_with_gemini(api_key_input, model_name, target_image, scene_image, custom_prompt)
            
            # Display result
            st.success("Analysis Complete!")
            st.code(result, language='json')

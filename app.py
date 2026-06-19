import streamlit as st

from src.llm.llm_service import generate_srs
from src.llm.prompts import build_srs_prompt
from src.extraction.json_parser import parse_llm_json
from src.storage.json_manager import save_json


st.set_page_config(
    page_title = "AI Powered SRS Generator",
    layout="wide",
    page_icon="📄"
)

st.title("AI Powered SRS Generator")
st.write(
    """
    Generate Software Requirement Specification (SRS) documents
    automatically using AI
    """
)

project_scope = st.text_area(
    "Enter Project Scope",
    height=200,
    placeholder="Enter text here"
)

generate_btn = st.button("Generate SRS")


if generate_btn:
    if project_scope.strip() == "":
        st.error("Please enter project scope")
    elif len(project_scope.strip().split()) < 15:
        st.warning("Input too less to create a report")
    else:
        with st.spinner(
            "Extracting Requirements..."
        ):
            
            prompt = build_srs_prompt(project_scope)

            result = generate_srs(prompt)

            extracted_data = (
                parse_llm_json(result)
            )

            filepath = save_json(extracted_data)

        st.success("Extraction Complete")
        st.subheader("Structured JSON")
        st.json(
            extracted_data
        )
        st.write(
            f"Saved to: {filepath}"
        )

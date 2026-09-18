
import streamlit as st
from groq import Groq
import os

# Page settings
st.set_page_config(
    page_title="AI Learning Hub",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Hub")
st.write("Learn smarter with AI!")

st.header("📚 Student Learning Assistant")

# Student level
level = st.selectbox(
    "Select your level",
    [
        "Primary School",
        "Middle School",
        "High School",
        "College",
        "Adult"
    ]
)

# Subject
subject = st.text_input(
    "Enter subject",
    placeholder="e.g. Biology, Mathematics, English"
)

# Topic
topic = st.text_input(
    "Enter topic",
    placeholder="e.g. Photosynthesis"
)

# Response style
style = st.selectbox(
    "How should AI explain?",
    [
        "Very Simple",
        "Simple",
        "Detailed"
    ]
)

# Response size
response_size = st.selectbox(
    "Response size",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

# API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.warning("⚠️ Groq API key is missing.")

# Generate button
if st.button("✨ Generate Explanation"):

    if not api_key:
        st.error("Please add your GROQ_API_KEY first.")

    elif not subject or not topic:
        st.warning("Please enter both subject and topic.")

    else:
        try:
            client = Groq(api_key=api_key)

            prompt = f"""
You are an AI learning assistant.

Student level: {level}
Subject: {subject}
Topic: {topic}
Explanation style: {style}
Response size: {response_size}

Explain the topic clearly according to the student's level.

Include:
- Easy explanation
- Important points
- One simple example
- A short practice question
"""

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            answer = response.choices[0].message.content

            st.success("✅ Explanation generated!")
            st.markdown(answer)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

import streamlit as st
import re

# Page Settings
st.set_page_config(
    page_title="Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)

# Title
st.title("🛡️ Phishing Email Detector")

st.write("Detect suspicious phishing emails using rule-based analysis.")

# Text Area
email_text = st.text_area(
    "Paste Email Content Here",
    height=250
)

# Phishing Keywords
phishing_keywords = [
    "urgent",
    "verify",
    "bank",
    "password",
    "click here",
    "login",
    "lottery",
    "winner",
    "free",
    "account suspended",
    "update now"
]

# Analyze Button
if st.button("Analyze Email"):

    score = 0
    detected = []

    # Convert text to lowercase
    text = email_text.lower()

    # Keyword Detection
    for word in phishing_keywords:
        if word in text:
            score += 10
            detected.append(word)

    # URL Detection
    urls = re.findall(r'https?://\S+|www\.\S+', email_text)

    if urls:
        score += 20

    # Result Logic
    st.subheader("Analysis Result")

    if score >= 50:
        st.error("⚠️ Phishing Email Detected")
    elif score >= 20:
        st.warning("⚠️ Suspicious Email")
    else:
        st.success("✅ Safe Email")

    # Score Display
    st.write(f"### Risk Score: {score}")

    # Detected Keywords
    if detected:
        st.write("### Suspicious Keywords Found:")
        for item in detected:
            st.write(f"- {item}")

    # URL Display
    if urls:
        st.write("### Suspicious Links Found:")
        for url in urls:
            st.write(f"- {url}")

    # No Input Handling
    if email_text.strip() == "":
        st.warning("Please paste email content.")
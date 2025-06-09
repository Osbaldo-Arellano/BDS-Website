import streamlit as st

st.set_page_config(page_title="Digital Security for BDS", layout="centered")

st.title("🔐 Digital Security for BDS (Boycott, Divestment, Sanctions)")

st.markdown("### What Should BDS Be Concerned About?")

concerns_definitions = {
    "Surveillance & Doxxing": "Monitoring activists or exposing their private information to harm them.",
    "Metadata Collection": "Metadata can leak information like who you contact, when, and where.",
    "Platform Censorship (Facebook, Instagram, etc.)": "The suppression of content related to BDS on social media platforms due to political pressure.",
    "Device Seizure by Authorities": "Law enforcement or border patrol confiscating phones or laptops without a warrant."
}

for label, definition in concerns_definitions.items():
    if st.checkbox(label):
        st.info(label + ": " + definition)



# Accordion for recommended tool
with st.expander(" Recommended Tool:🛠️ Encrypted Messaging App - Signal "):
    st.markdown("""
    Signal is a free, open-source encrypted messaging app used by journalists and activists.

    ### 🥷🏿 Features
    - End-to-end encryption by default
    - Minimal metadata retention
    - Open-source
    - Disappearing messages\
    - Available Anywhere - Windows, Linux, iOS, Android, and MacOS
    """)

with st.expander("🔐 How Signal Protects BDS Members"):
    st.markdown("""
    - **Confidentiality**: Only sender and receiver can read messages.
    - **Anonymity**: No one, including the Signal Foundation, can read your messages or listen to your calls..
    - **No Metadata Logging**: Signal stores almost no user data.
    - **Large Group Chats**:  Signal supports as many as 1,000 people in a single chat. 
    """)

with st.expander("📲 How to Use Signal"):
    st.markdown("""
    1. Download Signal from the [official site](https://signal.org/download/)
    2. Register with a phone number (use a burner if needed)
    3. Add trusted contacts
    4. Enable disappearing messages and screen lock
    """)

with st.expander("👍 Pros and 👎 Cons"):
    st.markdown("""
    **Pros:**
    - Popular among activists
    - Regular security updates
    - Designed for user privacy

    **Cons:**
    - Requires phone number to register

    **NOTE:**
    Tools like Signal are most effective when widely adopted across a movement.
    """)

st.markdown("""
### 🧠 Final Thought
BDS's power lies in collective action. We need to protect every member with collective privacy.

📥 [Click here to download Signal](https://signal.org/download/)
""")

st.info("💡 Tip: Schedule privacy trainings to ensure all members are using Signal correctly.")
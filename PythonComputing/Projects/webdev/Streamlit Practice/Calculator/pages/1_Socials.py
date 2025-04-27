import streamlit as st

st.set_page_config(
    page_title="Socials",
    page_icon="📱"
)

st.write("# Socials")
st.write("## Follow us on social media")

columns = st.columns(4, gap="small")
if len(columns) == 4:
    col1, col2, col3, col4 = columns
else:
    st.write("Not enough columns returned. Expected 4.")


col1.link_button(label="Instagram", url="https://instagram.com", help="Follow us on Instagram", use_container_width=True)
col2.link_button(label="Youtube", url="https://youtube.com", help="Follow us on Youtube", use_container_width=True)
col3.link_button(label="Github", url="https://github.com", help="Follow us on GitHub", use_container_width=True)
col4.link_button(label="LinkedIn", url="https://linkedin.com", help="Follow us on LinkedIn", use_container_width=True)



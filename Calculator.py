import streamlit as st

st.set_page_config(
    page_title="Calculator",
    page_icon="🧮"
)   

# H1
st.write("# Calculator")
st.write("## Calculate stuff")

cin = st.text_area("Crunch your numbers here", "10*10")

st.write("Result:")
st.write(f"# {eval(cin)}")

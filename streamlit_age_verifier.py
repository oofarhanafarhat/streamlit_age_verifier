import streamlit as st

st.title(" Age Verifier App")

age_input = st.number_input("Enter your age:", min_value=-100, max_value=150, step=1)

if st.button("Check Age"):
    if age_input >= 60:
        st.success("You are a senior citizen.")
        st.info("You are respected and valuable for us. Please share your life experience and guide us.")
    elif age_input >= 18:
        st.success("You are an adult.")
        st.success("You can make your own decisions.")
        st.info("Welcome! Make your life meaningful and responsible.")
        st.info("Remember to take care of your health and well-being.")
    elif age_input >= 0:
        st.warning("You are a minor.")
        st.info("Enjoy your childhood, but always keep learning!")
    else:
        st.error("Invalid age. Age cannot be negative.")
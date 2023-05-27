import streamlit as st
from streamlit-chat import message

st.title('EasyLanguage')

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right
import streamlit as st
import time
st.set_page_config(page_title="Trend NXT AI", page_icon="🤖")
st.title("Trend NXT AI")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
i=-1
if prompt :=st.chat_input("whats up?"):
    i+=1
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    
    
    if prompt =="hey":
        response1 = "Hello! I am your personal fashion assistant. How may i help you today?"
    if prompt == "You remember the black jeans i bought last month?":
        response1 = "Do you mean The Mango Dark shade, no fade, flared, mid-rise, black jeans?"
    if prompt == "Yes that one":
        response1 = "How may i help you with it?"
    if prompt == "What kind of tshirt should i wear with it?":
        response1 = "Since your jeans have a classic black color and a flattering flared cut, you've got a lot of options for tops! Here are a few ideas depending on the look you're going for: \n\n •Solid colored t-shirt: A crisp white tee or a black crewneck tee are always failsafe options. You can also go for a grey tee or a jewel tone like emerald green or sapphire blue.\n\n•Graphic t-shirt:  A graphic tee with a cool print or a band tee can add a touch of personality to your outfit.\n\n•Striped t-shirt:  A classic striped tee in black and white or navy and white is a laid-back yet polished choice. \n\nYou can choose one of these depending on the requirement."
    if prompt == "Which one will be the best for a casual outing?":
        response1 = "Out of the options listed, for a casual, a  solid colored t-shirt or a graphic t-shirt would be the best choices. Here's why: \n\n •Lightweight and breathable: A t-shirt made from cotton or linen will keep you cool and comfortable in the warm weather.\n\n •Relaxed style: A t-shirt offers a casual and laid-back vibe, perfect for a relaxed outing.\n\n •Versatility: You can easily dress it up or down with accessories like a statement necklace, a scarf, or a denim jacket."
    else:
        response1 = "Server is down right now"
    response = f"AI : {response1}"
    
    
    with st.chat_message("assistant"):
        time.sleep(2)
        st.markdown(response)
        
    st.session_state.messages.append({"role":"assistant","content":response})
    
    
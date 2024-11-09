import streamlit as st
import openai

# Initialize the OpenAI API key
openai.api_key = 'your-openai-api-key-here'  # Replace with your actual API key

# Streamlit interface
def main():
    st.title("GPT Chat Interface")
    
    # Session state to store chat history
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Display existing chat messages
    for msg in st.session_state['messages']:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # User input
    user_input = st.chat_input("Ask a question or type a message...")
    if user_input:
        # Display user message
        st.session_state['messages'].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Generate response from GPT
        with st.spinner("Generating response..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": msg["role"], "content": msg["content"]} for msg in st.session_state['messages']
                ]
            )
            assistant_response = response["choices"][0]["message"]["content"]
            
            # Display assistant response
            st.session_state['messages'].append({"role": "assistant", "content": assistant_response})
            with st.chat_message("assistant"):
                st.markdown(assistant_response)

if __name__ == "__main__":
    main()

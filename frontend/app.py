import streamlit as st
import requests

st.set_page_config(page_title="LLM Chatbot", page_icon="🤖")

st.title("LLM Chatbot 🤖")
st.markdown("Ask any question to the chatbot using Groq API!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form("chat_form"):
    user_input = st.text_input("You:", key="user_input", placeholder="Type your question here...")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip() != "":
    try:
        res = requests.post("http://localhost:8000/chat", json={"message": user_input})
        res_json = res.json()

        bot_reply = res_json.get("response", "No response")
        execution_time = res_json.get("execution_time", "N/A")
        token_usage = res_json.get("token_usage", {})
        model_time = res_json.get("model_total_time", "N/A")

        # ✅ Store all 5 values
        st.session_state.chat_history.append((user_input, bot_reply, execution_time, model_time, token_usage))

    except Exception as e:
        st.error(f"Error: {e}")

st.subheader("Conversation History")
for i, (user_msg, bot_msg, exec_time, model_time, tokens) in enumerate(reversed(st.session_state.chat_history), 1):
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Bot:** {bot_msg}")

    st.caption(f"⚡ **Execution Time (Backend)**: {exec_time} seconds")
    st.caption(f"🧠 **Model Time (Groq)**: {model_time} seconds")

    if tokens:
        st.markdown("📊 **Tokens Used:**")
        st.markdown(f"- Prompt Tokens: `{tokens.get('prompt_tokens', 'N/A')}`")
        st.markdown(f"- Completion Tokens: `{tokens.get('completion_tokens', 'N/A')}`")
        st.markdown(f"- Total Tokens: `{tokens.get('total_tokens', 'N/A')}`")

    st.markdown("---")

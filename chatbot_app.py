import streamlit as st
from openai import OpenAI
import json
import numpy as np


# Initialize OpenAI client
client = OpenAI(api_key="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")

# Load decision tree JSON
with open('decision_tree.json', 'r') as f:
    decision_tree = json.load(f)

# Function to get next question from the decision tree
def get_next_question(current_node):
    if isinstance(current_node, dict):
        if 'question' in current_node:
            return current_node['question'], list(current_node['options'].keys())
        elif 'result' in current_node:
            return current_node['result'], None
    return None, None

# Modified function to navigate tree with multiple selections
def navigate_tree_multi(current_node, selected_options):
    results = []
    for option in selected_options:
        if 'options' in current_node and option in current_node['options']:
            next_node = current_node['options'][option]
            # Handle TAME/DASH results
            if isinstance(next_node, dict) and 'result' in next_node:
                if next_node['result'] in ['TAME', 'DASH']:
                    results.append(decision_tree[next_node['result']])
                else:
                    results.append(next_node)
            else:
                results.append(next_node)
    return results

# Keep interpret_user_input function for future use
def interpret_user_input(user_input, options, current_question):
    system_prompt = """You are a logistics software product recommendation assistant. Your role is to:
1. Match user responses to predefined options for a product recommendation system
2. Understand logistics industry terminology and requirements
3. Consider the context of the current question when interpreting responses
4. Only respond with an exact match from the available options or 'None' if no good match exists

Core products:
- TAME: For freight forwarders, 3PLs, manufacturers, distributors, and ports
- DASH: For couriers and hauliers

Focus on understanding the user's business needs and matching them to the most appropriate option."""

    prompt = f"""Current question: {current_question}
Available options: {', '.join(options)}
User response: {user_input}

Select the most appropriate option from the available choices. Only respond with the exact option text or 'None' if no good match exists."""
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=50
    )
    
    return response.choices[0].message.content.strip()

# Function to reset session state
def reset_session_state():
    st.session_state.current_nodes = [decision_tree['root']]  # Now a list of current nodes
    st.session_state.history = []
    st.session_state.recommendations = []
    st.rerun()

# Streamlit app
st.title("Fero's Product Recommender")
st.markdown("""
This assistant will help you find the perfect software solution for your logistics business needs.
Please answer a few questions about your requirements.
""")

# Initialize session state
if 'current_nodes' not in st.session_state:
    st.session_state.current_nodes = [decision_tree['root']]  # Now a list
if 'history' not in st.session_state:
    st.session_state.history = []
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = []

# Display history
if st.session_state.history:
    with st.expander("Previous Responses", expanded=False):
        for item in st.session_state.history:
            st.write(item)

# Process each current node
all_next_nodes = []
for current_node in st.session_state.current_nodes:
    question, options = get_next_question(current_node)
    
    if question and options:
        st.write(f"Question: {question}")
        
        # Create checkboxes for multiple selection
        selected_options = []
        cols = st.columns(min(3, len(options)))
        for idx, option in enumerate(options):
            with cols[idx % 3]:
                if st.checkbox(option, key=f"checkbox_{option}_{id(current_node)}"):
                    selected_options.append(option)
        
        # Add a "Continue" button for this set of options
        if selected_options and st.button("Continue", key=f"continue_{id(current_node)}"):
            # Store selections in history
            st.session_state.history.append(f"Q: {question}\nA: {', '.join(selected_options)}")
            
            # Navigate to next nodes
            next_nodes = navigate_tree_multi(current_node, selected_options)
            
            # Process results and next steps
            for node in next_nodes:
                if isinstance(node, dict) and 'result' in node:
                    if node['result'] not in ['TAME', 'DASH']:
                        if node['result'] not in st.session_state.recommendations:
                            st.session_state.recommendations.append(node['result'])
                    else:
                        all_next_nodes.append(decision_tree[node['result']])
                else:
                    all_next_nodes.append(node)
            
            if all_next_nodes:
                st.session_state.current_nodes = all_next_nodes
                st.rerun()

# Display final recommendations
if st.session_state.recommendations:
    st.write("---")
    st.write("Summary of Recommendations:")
    for rec in st.session_state.recommendations:
        st.success(f"Recommended Solution: {rec}")

# Add a reset button at the bottom
if st.button("Reset and Start Over", key="reset_bottom"):
    reset_session_state()
# app.py

import streamlit as st
from questions import questions
from mapping import recommend_modules, module_descriptions

def main():
    st.set_page_config(page_title="Logistics Solutions Recommendation Engine", layout="wide")
    st.title("Logistics Solutions Recommendation Engine")
    st.write("Answer the following questions to receive tailored module recommendations for your business.")

    # Initialize or retrieve responses
    if 'responses' not in st.session_state:
        st.session_state.responses = {}

    responses = st.session_state.responses

    # Iterate over the questions
    for question in questions:
        qid = question['id']
        qtext = question['question']
        qtype = question['type']
        options = question.get('options', [])

        # Conditional Logic for Skipping Questions
        # Example: Skip vehicle types question if they don't own a fleet
        if qid == 8 and responses.get(7) != 'Own Fleet':
            continue
        # Add other conditional skips as needed

        # Display the question based on its type
        if qtype == 'multiple':
            responses[qid] = st.multiselect(qtext, options, default=responses.get(qid, []))
        elif qtype == 'single':
            responses[qid] = st.selectbox(qtext, options, index=options.index(responses.get(qid)) if responses.get(qid) else 0)
        elif qtype == 'yesno':
            responses[qid] = st.radio(qtext, ('Yes', 'No'), index=0 if responses.get(qid) == 'Yes' else 1)
        elif qtype == 'text':
            responses[qid] = st.text_input(qtext, value=responses.get(qid, ''))

        # Add a divider for better visual separation
        st.markdown("---")

    # When the user clicks the "Get Recommendations" button
    if st.button("Get Recommendations"):
        modules = recommend_modules(responses)
        if modules:
            st.success("Based on your responses, we recommend the following modules:")
            for module in modules:
                description = module_descriptions.get(module, 'Description not available.')
                st.markdown(f"### {module}")
                st.write(description)
        else:
            st.warning("No specific modules recommended based on your responses.")

if __name__ == "__main__":
    main()

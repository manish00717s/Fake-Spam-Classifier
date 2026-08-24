"""
Spam Classifier Web Application
Streamlit-based UI for real-time spam detection
"""

import streamlit as st
import pickle
import os
from preprocessing import preprocess_text

# Page config
st.set_page_config(page_title="Spam Classifier", page_icon="🚨", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .spam { color: #e74c3c; font-weight: bold; }
    .ham { color: #2ecc71; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🚨 SMS Spam Classifier")
st.markdown("Detect spam messages using Machine Learning")

# Load models
@st.cache_resource
def load_models():
    model_path = os.path.dirname(__file__)
    parent_path = os.path.dirname(model_path)
    
    with open(os.path.join(parent_path, 'models', 'tfidf_vectorizer.pkl'), 'rb') as f:
        vectorizer = pickle.load(f)
    
    with open(os.path.join(parent_path, 'models', 'spam_classifier_model.pkl'), 'rb') as f:
        model = pickle.load(f)
    
    return vectorizer, model

try:
    vectorizer, model = load_models()
    
    # Sidebar info
    with st.sidebar:
        st.header("📊 Model Info")
        st.markdown("""
        - **Algorithm**: Multinomial Naive Bayes
        - **Accuracy**: 97.14%
        - **Precision**: 100%
        - **Dataset**: 5,572 SMS messages
        """)
    
    # Main interface
    user_input = st.text_area("📝 Enter message:", placeholder="Type a message...", height=100)
    
    if st.button("🔍 Check Message", use_container_width=True):
        if user_input.strip():
            # Preprocess
            cleaned = preprocess_text(user_input)
            
            # Vectorize
            X_input = vectorizer.transform([cleaned])
            
            # Predict
            prediction = model.predict(X_input)[0]
            probability = model.predict_proba(X_input)[0]
            
            st.markdown("---")
            
            if prediction == 1:
                st.error("🚨 **SPAM DETECTED**")
                st.metric("Spam Probability", f"{probability[1]*100:.1f}%")
            else:
                st.success("✅ **LEGITIMATE MESSAGE**")
                st.metric("Ham Probability", f"{probability[0]*100:.1f}%")
            
            with st.expander("See preprocessing details"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Original:**")
                    st.info(user_input)
                with col2:
                    st.write("**Cleaned:**")
                    st.info(cleaned)
        else:
            st.warning("Please enter a message")

except Exception as e:
    st.error(f"Error loading models: {str(e)}")
    st.info("Ensure .pkl files exist in ../models/ directory")

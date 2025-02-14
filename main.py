import streamlit as st
import google.generativeai as genai
genai.configure(api_key="enter_your_apikey")
# Configure the Streamlit page
st.set_page_config(page_title="AI Code Reviewer", layout="centered")

st.title("💬 An AI Code Reviewer")
st.write("Enter your Python code here ...")

# Text area for user to enter Python code
code_input = st.text_area("Python Code", height=200, placeholder="Paste your Python code here...")

# Function to generate AI-based code review
def get_code_review(code):
    """Function to send code to GoogleAI API and return feedback."""
    try:
        model = genai.GenerativeModel("gemini-pro")  # Adjust model as needed
        response = model.generate_content(
            f"""Review the following Python code and provide a bug report along with the corrected version:
            {code}

            Response format:
            **Bug Report**
            - List of identified issues in the code.
            
            **Fixed Code**
            - Provide the corrected version of the code.
            """
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Generate button
if st.button("Generate"):
    if code_input.strip():
        with st.spinner("Analyzing your code..."):
            review_result = get_code_review(code_input)
        
        st.subheader("📝 Code Review")
        
        # Extract bug report and fixed code
        if "**Fixed Code**" in review_result:
            bug_report, fixed_code = review_result.split("**Fixed Code**", 1)
        else:
            bug_report = review_result
            fixed_code = "No fixed code provided."
        
        st.markdown("### 🐞 Bug Report")
        st.write(bug_report.strip())  # Display bug report
        
        st.markdown("### ✅ Fixed Code")
        st.code(fixed_code.strip(), language="python")  # Display fixed code in code block
    else:
        st.warning("⚠️ Please enter some code before submitting.")

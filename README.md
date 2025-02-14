# -AI-Code-Reviewer  

## 📌 Overview
The **AI Code Reviewer** is a web-based application built using **Streamlit** and **Google Gemini AI** to analyze Python code. It provides a **bug report** and **fixed code** suggestions based on AI-powered insights.

## 🚀 Features
- 📝 **Code Analysis:** Detects errors and provides feedback.
- 🐞 **Bug Report:** Identifies issues in the provided Python code.
- ✅ **Fixed Code:** Suggests corrections with an improved version of the code.
- 🎨 **Customizable UI:** Modify background styles and themes as needed.
- 🌐 **Runs on Custom Ports:** Flexibility to change the running port.

## 🛠️ Installation
Installation

To set up the project, follow these steps:

1.Clone the repository:

use the git clone 

2.Navigate to the project directory:

cd main.py

3.Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate

## 🔥 Usage
### 1️⃣ Run the Streamlit App
streamlit run main.py  
By default, Streamlit runs on port **8501**. To change the port:
  
streamlit run app.py --server.port 8502


### 2️⃣ Enter Your Python Code
- Paste your Python code into the text area.
- Click on **Generate Review** to analyze the code.
- View **Bug Report** and **Fixed Code** suggestions.


## 📌 Dependencies
- **Streamlit** (For UI)
- **Google Generative AI SDK** (For AI-based code review)
- **Python 3.8+**




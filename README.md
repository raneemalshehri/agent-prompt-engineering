# 🔐 Password Agent with LangChain + Streamlit

This project is a secure password utility powered by LangChain and OpenAI, wrapped in a user-friendly Streamlit app. It can:

✅ Evaluate password strength

🔐 Generate strong, customizable passwords

The LangChain agent selects the appropriate tool based on your natural language input.


# 🚀 Features

Check Password Strength
Get feedback on how secure your password is.

Generate Passwords
Generate a strong password with optional settings: length, symbols, numbers, and uppercase letters.

# 🧰 Tech Stack
LangChain

OpenAI API

Streamlit

Python 3.10+


# 📦 Requirements
Install the required packages:

pip install streamlit langchain openai python-dotenv

Make sure to set your OpenAI API key in the .env file!


# 🧪 Example Usage
agent.run("Is 'password123' secure?")
## Output: Weak password.

agent.run("Generate a strong password for my banking website.")
## Output: e.g. "K8#sP2l!9qTz"

agent.run("I need a 16-character password without symbols.")
## Output: e.g. "fR8zH2kL9mQwTuXe"

agent.run("Is 'Tr0ub4dor&3' a good password?")
## Output: Strong password 💪


# 📁 File Structure
├── app.py               # Streamlit app

├── password_agent.ipynb  # Main notebook with LangChain agent and tools

├── .env                  # Environment file to store OpenAI API key

└── README.md             # Project documentation


# 📝 How to Run
1. Clone the repository:
```bash
git clone https://github.com/raneemalshehri/agent-prompt-engineering.git
cd agent-prompt-engineering
```
2. Install the required packages:
```bash
pip install langchain openai
```
3. Set your OpenAI API key:

Create a .env file in the root directory and add:
```bash
OPENAI_API_KEY=your-api-key
```
4. Run the agent:
```bash
streamlit run app.py




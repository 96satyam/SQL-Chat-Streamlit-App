# 🦜 LangChain: Chat with SQL DB
This project is a Streamlit-based application that allows users to interact with SQL databases using natural language queries powered by LangChain and Groq’s Llama3-8b-8192 model.

## 🚀 Features
Supports SQLite and MySQL Databases – Connect to either a local SQLite database (student.db) or a remote MySQL database.

Conversational SQL Agent – Ask questions in natural language and get responses generated dynamically.

Seamless Integration with LangChain – Uses SQLDatabaseToolkit and create_sql_agent for efficient query execution.

Secure API Key Handling – Requires a Groq API Key for LLM-based query interpretation.

Interactive UI with Streamlit – Simple and user-friendly interface for database interactions.

## 🏗️ Tech Stack
Python 🐍

Streamlit 🎨

LangChain 🧠

SQLite / MySQL 🗄️

SQLAlchemy 🏗️

Groq (Llama3-8b-8192) 🤖

🔧 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/chat-with-sql.git
cd chat-with-sql
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up Environment Variables
Create a .env file and add your Groq API Key:

ini
Copy
Edit
GROQ_API_KEY=your_api_key_here
4️⃣ Run the Application
bash
Copy
Edit
streamlit run app.py
### ⚙️ How It Works
Select a Database – Choose between SQLite (student.db) or MySQL.

Enter MySQL Credentials (if applicable) – Provide host, user, password, and database name.

Enter API Key – Securely authenticate using your Groq API Key.

Ask Questions – Use natural language to query your database and get AI-generated responses.

### 📝 Example Queries
"Show me the top 10 students by grade."

"How many students enrolled in 2024?"

"List all courses with more than 50 students."

### 🎯 Future Enhancements
Add support for PostgreSQL and other relational databases.

Implement user authentication for secured access.

Improve error handling and query optimization.

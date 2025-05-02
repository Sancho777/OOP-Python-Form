# 🧾 Registration Form with FastAPI + HTML Element Abstraction

This project showcases how to build a **registration form web application** using:

- 🐍 Python (OOP for HTML elements)
- ⚡ FastAPI (web backend)
- 🎨 Bootstrap 5 (for styling)
- 📦 Uvicorn (ASGI server)

All HTML elements (`input`, `select`, `a`, `img`, `div`, `form`) are modeled using Python classes to demonstrate **object-oriented programming (OOP)** principles in a real-world web context.

---

## 📌 Features

✅ Object representation of HTML elements
✅ Clean and modular HTML generation using Python classes
✅ Responsive and styled registration form
✅ Displays submitted data on a confirmation page
✅ Centralized layout with consistent styling
✅ Easy to run locally

---

## 🛠️ HTML Elements as Python Classes

Each HTML element used in the form is represented by a Python class:

class HTMLElement:
def **init**(self, tag: str, attrs: dict = None, content: str = "", self_closing=False):
...
def render(self) -> str:
...

Specialized Elements
Input(HTMLElement) – supports type, name, placeholder, etc.

Select(HTMLElement) – handles <option> children.

A(HTMLElement) – for links/buttons.

Img(HTMLElement) – for image tags.

Div(HTMLElement) – for layout and form groups.

Form(HTMLElement) – complete form wrapper.

📄 Form Overview
📥 Registration Form Fields:
Name (Text input)

Email (Email input)

Country (Select dropdown)

Profile Picture (Image placeholder)

Submit Button

✅ Submit Page
After submission, it shows:

Entered name

Entered email

Selected country

A confirmation message

Both pages are centered, styled with a light background, and Bootstrap form classes.

🚀 How to Run

1. Clone the repo / Create main file
   Save this project in a file called main.py.

bash
mkdir FormPy && cd FormPy

# save main.py here

2. Create & activate virtual environment (optional but recommended)

bash
python -m venv venv

# On Windows

venv\Scripts\activate

# On Mac/Linux

source venv/bin/activate

3. Install dependencies

bash
pip install fastapi uvicorn

4. Run the server

bash
uvicorn main:app --reload --port 3000
Visit: <http://localhost:3000>

📁 Folder Structure (if using images)

cpp

FormPy/
├── main.py
├── static/
│ └── logo.png
└── README.md

Use the static/ folder for images if you add one in the future.

```

```

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from html_elements import Form as HtmlForm, Div, Input, Select, Img, HTMLElement

app = FastAPI()

# Serve /static
app.mount("/static", StaticFiles(directory="static"), name="static")


def build_registration_form() -> str:
    form = HtmlForm(
        action="/submit",
        method="post",
        enctype="multipart/form-data",
        **{"class": "registration-form"}
    )

    form_fields = Div(**{"class": "form-fields"})

    # Name field
    name_group = Div(**{"class": "form-group"})
    name_group.add_child(HTMLElement("label").add_child("Name:") or "")
    name_group.add_child(Input(name="name", input_type="text", placeholder="Enter your name", **{"class": "form-control"}))
    form_fields.add_child(name_group)

    # Email field
    email_group = Div(**{"class": "form-group"})
    email_group.add_child(HTMLElement("label").add_child("Email:") or "")
    email_group.add_child(Input(name="email", input_type="email", placeholder="Enter your email", **{"class": "form-control"}))
    form_fields.add_child(email_group)

    # Country select
    country_group = Div(**{"class": "form-group"})
    country_group.add_child(HTMLElement("label").add_child("Country:") or "")
    select = Select(name="country", **{"class": "form-control"})
    select.add_option("United States", "us")
    select.add_option("Canada", "ca")
    select.add_option("United Kingdom", "uk")
    select.children[-1].attrs["selected"] = "selected"
    select.add_option("Australia", "au")
    country_group.add_child(select)
    form_fields.add_child(country_group)

    # Profile Picture
    pic_group = Div(**{"class": "form-group"})
    pic_group.add_child(HTMLElement("label").add_child("Profile Picture:") or "")
    pic_group.add_child(Img("/static/logo.png", alt="profile", **{"class": "h-16"}))
    form_fields.add_child(pic_group)

    # Submit button
    submit_group = Div(**{"class": "form-group"})
    submit = Input(input_type="submit", value="Register", **{"class": "btn btn-primary"})
    submit_group.add_child(submit)
    form_fields.add_child(submit_group)

    form.add_child(form_fields)
    return form.render()


@app.get("/", response_class=HTMLResponse)
async def get_form():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registration</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #f0f4f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .form-container {{
                background: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                width: 100%;
                max-width: 400px;
            }}
            .form-group {{
                margin-bottom: 1rem;
            }}
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1 class="text-center mb-4">Registration Form</h1>
            {build_registration_form()}
        </div>
    </body>
    </html>
    """
    return html



@app.post("/submit", response_class=HTMLResponse)
async def submit_form(
    name: str = Form(...),
    email: str = Form(...),
    country: str = Form(...)
):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Submission Successful</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #f0f4f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .form-container {{
                background: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                width: 100%;
                max-width: 400px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="form-container">
            <h2 class="mb-3">✅ Registration Successful!</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Country:</strong> {country}</p>
            <a href="/" class="btn btn-primary mt-3">Back to Form</a>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

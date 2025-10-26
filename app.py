from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

CSV_PATH = os.path.join(os.path.dirname(__file__), "enquiries.csv")
FIELDNAMES = [
    "name",
    "nationality",
    "phone",
    "email",
    "dateOfTravel",
    "cityOfResidence",
    "vocationType",
    "consent"
]

def ensure_csv_exists():
    """Create CSV with header if it doesn't exist."""
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def append_enquiry(data: dict):
    """Append one enquiry dict to CSV."""
    ensure_csv_exists()
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        # ensure only the expected keys are written (avoid extras)
        row = {k: data.get(k, "") for k in FIELDNAMES}
        writer.writerow(row)

def read_all_enquiries():
    """Return list of dict rows from CSV (excluding header)."""
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

@app.route("/", methods=["GET"])
def index():
    # Render the HTML you already wrote (save it as templates/index.html)
    return render_template("index.html")

@app.route("/submit_enquiry", methods=["POST"])
def submit_enquiry():
    # Collect fields from the form
    form = request.form
    data = {
        "name": form.get("name", "").strip(),
        "nationality": form.get("nationality", "").strip(),
        "phone": form.get("phone", "").strip(),
        "email": form.get("email", "").strip(),
        "dateOfTravel": form.get("dateOfTravel", "").strip(),
        "cityOfResidence": form.get("cityOfResidence", "").strip(),
        "vocationType": form.get("vocationType", "").strip(),
        # checkbox: if present in form it means checked, else empty
        "consent": "yes" if form.get("consent") in ["on", "yes", "true", "1"] else "no"
    }

    append_enquiry(data)

    # After saving, redirect to results page that displays all enquiries
    return redirect(url_for("results"))

@app.route("/results", methods=["GET"])
def results():
    enquiries = read_all_enquiries()
    # enquiries is a list of dicts; pass to template
    return render_template("result.html", enquiries=enquiries)

if __name__ == "__main__":
    # Run with: python app.py
    app.run(debug=True)

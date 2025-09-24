from flask import Flask, render_template, request

app = Flask(__name__)

# ---- Simple phishing detection logic ----
def is_phishing(text):
    keywords = ["urgent", "verify", "suspend", "reset", "password", "confirm", "bank", "secure"]
    for kw in keywords:
        if kw.lower() in text.lower():
            return True
    if "@" in text or len(text) > 120:
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    status = None
    if request.method == "POST":
        text = request.form["email"]
        if is_phishing(text):
            result = "⚠️ Suspicious! Classified as phishing.\n👉 Suggested Response: Quarantine email, block links, notify SOC."
            status = "danger"  # red
        else:
            result = "✅ Looks safe (no phishing detected)."
            status = "success"  # green
    return render_template("index.html", result=result, status=status)

if __name__ == "__main__":
    app.run(debug=True)

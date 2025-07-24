from flask import Flask, render_template, request
import pickle
import pandas as pd

# ── load model + encoders once at startup
with open("shopper_tree.pkl", "rb") as f:
    bundle = pickle.load(f)

model = bundle["model"]
encoders = bundle["encoders"]
feature_order = bundle["feature_order"]

app = Flask(__name__)

def preprocess(form_data):
    """
    Convert incoming HTML form fields into the model‑ready DataFrame row.
    `form_data` is the immutable dict returned by Flask `request.form`.
    """
    # convert strings → Python types
    sample = {k: (v if v not in ["True", "False"] else v == "True")
              for k, v in form_data.items()}

    df = pd.DataFrame([sample])

    # encode categoricals
    for col in df.columns:
        if col in encoders:
            df[col] = encoders[col].transform(df[col])

    # align column order and fill any missing numeric columns with 0
    df = df.reindex(columns=feature_order).fillna(0)
    return df

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        X_new = preprocess(request.form)
        pred_num = model.predict(X_new)
        prediction = encoders["Revenue"].inverse_transform(pred_num)[0]
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
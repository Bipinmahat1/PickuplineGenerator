from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os

load_dotenv()

app = Flask(__name__)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        line_type = data.get("lineType", "funny")

        prompt = (
    f"You are an expert pickup line generator."
    f"Create a completely unique, clever, and creative {line_type.lower()} pickup line that "
    f"you have never used before. Respond ONLY with the pickup line, no explanations."
    )

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Give me a pickup line."}
            ],
            max_tokens=500,
            temperature=1.2
        )
        pickup_line = response.choices[0].message.content.strip()
        return jsonify({'pickup_line': pickup_line})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)

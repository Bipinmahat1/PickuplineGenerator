# 💘 Pickup Line Generator 

A web-based Pickup Line Generator powered by **OpenAI's GPT-4**. Users can select the style of pickup line whether it's **funny, flirty, cheesy, bold, simple, nerdy, or romantic** and the app generates a creative pickup line on demand.

Built with **Python Flask** for the backend, **OpenAI API** for AI-powered text generation, and a sleek responsive frontend using **HTML, CSS, and JavaScript**.

---

## 🚀 Features

- 🎯 Generate creative pickup lines in various styles.
- 🔥 Powered by GPT-4 for intelligent, witty, and unique responses.
- 🎨 Beautiful, clean, and responsive UI.
- ✅ Dynamic dropdown for pickup line types.
- 🔐 API key is managed securely via a `.env` file.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI:** OpenAI GPT-4 API
- **Environment Management:** Python Dotenv

---

## 📦 Installation & Running Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/pickup-line-generator.git
cd pickup-line-generator
```

## 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
## 3️⃣ Set Up Environment Variables
```bash
OPENAI_API_KEY=your-openai-api-key
```
## 4️⃣ Run the App
```bash
python pickupLines.py
```
## 5️⃣ Open in Browser
```bash
http://127.0.0.1:5000
```


## 📂 Project Structure
```bash
pickup-line-generator/
│
├── static/               # CSS files
├── templates/            # HTML templates
├── .env                  # API key (ignored in Git)
├── .gitignore            # Ignored files
├── pickupLines.py        # Flask app
├── requirements.txt      # Python dependencies
└── README.md             # Project README
```
## ✨ Future Improvements

- Deploy to Render, Vercel, or Heroku.

- Add text-to-speech for reading pickup lines aloud.

- Add copy to clipboard or share to social media features.

- Implement dark/light mode toggle.

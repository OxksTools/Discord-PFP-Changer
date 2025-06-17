# Discord Profile Picture Changer

> A multi-threaded Discord avatar changer using random images and tokens.  
> Built and maintained by [OxksTools](https://github.com/OxksTools)

---

## ✅ Features

- Change avatars for multiple accounts at once
- Randomly selects avatars from local `avatars/` folder
- Uses Discord tokens
- Fast multithreaded execution
- Color-coded console output

---

## 📁 Project Structure

```
discord-pfp-changer/
│
├── avatars/
│   ├── avatar1.png
│   └── avatar2.jpg
│
├── tokens.txt
├── main.py
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/OxksTools/discord-pfp-changer.git
cd discord-pfp-changer
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

> Required modules: `requests`, `colorama`

### 3. Add Tokens
Create a file called `tokens.txt` and place one Discord token per line:
```
mfa.yourToken1Here
mfa.yourToken2Here
```

### 4. Add Avatars  
Place `.png` or `.jpg` files in the `avatars/` folder.

### 5. Run the Script
```bash
python main.py
```

You'll be prompted for how many profiles you want to change.

---

## 📌 Output Example
```bash
Enter amount of profiles to change > 3
[SUCCESS] Profile updated for token: mfa.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[SUCCESS] Profile updated for token: mfa.yyyyyyyyyyyyyyyyyyyyyyyyyyyyy
[ERROR]    Status code: 400
```

---

## ⚠️ Disclaimer

- This tool is for **educational and personal use only**.
- Use **only on accounts you own** or have **explicit permission** to access.
- **Abuse** of Discord's API may result in bans or rate-limiting.

---

## 📬 Contact & Support

- GitHub: [OxksTools](https://github.com/OxksTools)
- Custom work: `!Hazza#0001` (Discord)

---

## 🛠️ License

This project is licensed under the [MIT License](LICENSE).

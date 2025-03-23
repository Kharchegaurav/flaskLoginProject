### **📌 Project Explanation: Flask Login System with Firebase Authentication**  

This project is a **login system** built using **Flask (Python)** for the backend, **Firebase** for authentication, **PostgreSQL** (previously used, now replaced by Firebase), and **HTML, CSS, JS** for the frontend.

---

## **📂 Project File Structure and Responsibilities**
```
📁 WebPage
│── 📁 static/            # Contains CSS, JS, Images
│── 📁 templates/         # Contains HTML files
│   │── index.html        # Login page
│── app.py                # Main Flask backend
│── firebase_config.json  # Firebase credentials
│── requirements.txt      # Dependencies
│── .venv/                # Virtual environment (installed packages)
│── Procfile (Optional)   # If deploying to Heroku
```

---

## **📌 File Breakdown & What Each One Does**
### **1️⃣ `app.py` → Flask Backend**
**Handles:**  
✅ Running the Flask app  
✅ Connecting to **Firebase Authentication**  
✅ Processing user login requests  
✅ Managing session tokens for logged-in users  
✅ Redirecting to a **dashboard** after successful login  

🔹 **Important Functions in `app.py`**  
- `hello_world()`: Handles login requests (validates user with Firebase)  
- `dashboard()`: Displays a welcome message after login  
- `logout()`: Clears session and logs out the user  

---

### **2️⃣ `index.html` → Frontend Login Page**
**Handles:**  
✅ Collecting user **email** and **password**  
✅ Sending login data to **Flask (`app.py`)**  
✅ Displaying **error messages** if login fails  
✅ Redirecting to **dashboard** after successful login  

🔹 **Key Parts in `index.html`**  
- **`<form>`**: Sends login data using `POST`  
- **`flash messages`**: Displays login errors  
- **Bootstrap & FontAwesome**: Styling  

---

### **3️⃣ `firebase_config.json` → Firebase Credentials**
**Handles:**  
✅ Connecting Flask app to Firebase  
✅ Storing project API keys securely  

🔹 **Why Needed?**  
- It allows the Flask app to **communicate with Firebase Authentication**  

---

### **4️⃣ `static/` → Stores Frontend Assets**
**Contains:**  
📁 `css/` → Styling files (Bootstrap, custom styles)  
📁 `js/` → JavaScript functions (form validation, UI effects)  
📁 `images/` → Icons, background images  

---

## **🔄 Login Flow (How It Works)**
1️⃣ User enters **email** & **password** in `index.html`  
2️⃣ The form sends a `POST` request to Flask (`app.py`)  
3️⃣ Flask **validates credentials** using Firebase Authentication  
4️⃣ If successful → User is redirected to **dashboard**  
5️⃣ If failed → **Error message is shown**  

---

## **🔹 Next Steps**
✅ If everything is working fine, you can now **deploy it online** using **Heroku, Render, or AWS**! 🚀  

Let me know if you need **further improvements or debugging!** 😊


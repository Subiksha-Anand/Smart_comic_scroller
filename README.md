```markdown
# 📖 Smart Comic Scroller - Hands-Free Comic Reader

Welcome to the **Smart Comic Scroller**, a voice-enabled comic book reader that allows you to enjoy comics without lifting a finger. This project combines **OpenCV**, **pyttsx3**, and **keyboard automation** to provide a **hands-free experience** while reading comic pages.



---

## 🚀 Features

- ✅ Hands-free comic page navigation
- 🗣️ Voice feedback using `pyttsx3`
- ⏭️ Auto-scrolls or changes pages at your voice command or key triggers
- 🖼️ Supports image-based comic reading (JPG, PNG)
- 🪄 Clean, minimal interface for immersive comic viewing
- 💾 Comes with a Windows EXE file — no need to install Python!

---

## 🖼️ How It Works

The script loads all the image files (comic pages) from a specified folder and displays them one by one. You can control the scrolling using:

- Predefined keys (like `n` for next, `q` for quit)
- Voice commands (future enhancement)
- Optional timer-based automatic scroll (if integrated)

---
## 🎯 Key Features

- ✋ **Hand Gesture Control**  
  - 👋 Palm: Scroll up/down based on hand position  
  - 👍 Thumbs Up: Go to next chapter  
  - 👎 Thumbs Down: Go to previous chapter  
  - 🤟 Rock Sign: Toggle between Gesture and Voice Mode  

- 🎙️ **Voice Command Control** (when in Voice Mode)  
  - “Scroll down”, “Scroll up”, “Stop scrolling”  
  - “Next chapter”, “Previous chapter”

## 📁 Folder Structure

```

Hands\_free\_comic\_reader/
│
├── comic\_reader.py        # Main script
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── dist/
│   └── SmartComicReader.exe   # Compiled EXE (Windows)
└── comic\_pages/
├── page1.jpg
├── page2.jpg
└── ...

````

---

## 💻 How to Run (Python Users)

### 🔧 Requirements

Install required libraries:

```bash
pip install -r requirements.txt
````

### ▶️ Run the script

```bash
python comic_reader.py
```

Make sure to update the path in the script to the folder containing your comic images.

---

## 🧊 EXE Version for Windows

🎉 You can use the **ready-to-run `.exe` file** without installing Python or any packages!

### 📦 Download the EXE

> 👉 [Download SmartComicReader.exe from the `dist` folder](https://github.com/Subiksha-Anand/Smart_comic_scroller/tree/master/dist)

Steps:

1. Download the `.exe` file.
2. Double-click to launch the comic reader.
3. Make sure you have some images in the specified folder.

**Note**: If Windows SmartScreen gives a warning:

* Click **More info → Run anyway**

---



## 🧰 Built With

* Python 🐍
* OpenCV (`cv2`) 📷
* `pyttsx3` 🔊
* `keyboard` ⌨️
* Git LFS (for hosting large EXE files) 🪪

---

## 🌐 Repository Info

* Source Code: [main branch](https://github.com/Subiksha-Anand/Smart_comic_scroller/tree/main)
* EXE File: [master branch > dist/](https://github.com/Subiksha-Anand/Smart_comic_scroller/tree/master/dist)

---

## ✨ Credits

This project was ideated and built as part of a creative AI internship experience. Huge thanks to  CHATGPT for guidance and debugging wisdom 👴🔥

---

## 📬 Contact

If you liked this project or want to collaborate:

* 📧 [Subiksha Anand](mailto:subikshamatcs@gmail.com)
* 🔗 [GitHub: @Subiksha-Anand](https://github.com/Subiksha-Anand)

---



# 🖐️ Hands-Free Comic Reader using Eye Blink Detection 👁️

A computer vision-based comic reader that enables hands-free scrolling using real-time **eye blink detection**. Designed for accessibility, convenience, and innovation, this app is ideal for comic book lovers, readers with disabilities, and anyone who wants a futuristic reading experience.

---

## 📌 Features

- 👀 **Blink-Based Scrolling**: Scroll through comic pages by blinking your eyes.
- 📂 **Drag & Drop Interface**: Simply drag a folder of images (comic pages) into the app.
- 🧠 **AI-Powered Eye Detection**: Utilizes MediaPipe and OpenCV for real-time facial landmark tracking.
- 🖥️ **Desktop App (.exe)**: Packaged as a standalone executable with GUI.
- 🛠️ **User-Friendly GUI**: Intuitive interface built with `Tkinter`.
- 🔒 **Privacy Friendly**: All processing happens locally; no webcam data is stored or sent.

---

## 🚀 Demo

> ✨ Download the `.exe` file from [Releases] (https://github.com/Subiksha-Anand/Smart_comic_scroller/blob/main/dist/test.exe) and try the app without installing Python or dependencies!

https://user-images.githubusercontent.com/yourusername/demo-preview.gif

---

## 🏗️ How It Works

1. **Facial Landmark Detection**: Uses MediaPipe’s `FaceMesh` to detect eye landmarks.
2. **Blink Detection Logic**:
   - Calculates Eye Aspect Ratio (EAR) to detect a blink.
   - A blink triggers scroll-down.
3. **Image Viewer**:
   - Loads comic pages from a folder.
   - Displays them one-by-one in a scrollable canvas.
4. **Threading**: Ensures camera feed and UI remain responsive in parallel.

---

## 🧪 Tech Stack

| Component            | Library/Tool         |
|---------------------|----------------------|
| GUI                 | Tkinter              |
| Eye Detection       | MediaPipe, OpenCV    |
| Image Processing    | PIL (Pillow)         |
| Packaging           | PyInstaller          |
| Threading           | Python `threading`   |
| Git LFS             | For uploading `.exe` |

---

## 📸 Screenshots

| 👁️ Blink Detection | 🗂️ Folder Upload |
|---------------------|------------------|
| ![blink](screenshots/blink.png) | ![folder](screenshots/folder_upload.png) |

---

## 🛠️ Installation (For Developers)

```bash
git clone https://github.com/Subiksha-Anand/Smart_comic_scroller.git
cd Smart_comic_scroller
pip install -r requirements.txt
python main.py

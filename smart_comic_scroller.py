import cv2
import mediapipe as mp
import pyautogui
import time
import speech_recognition as sr
import threading
import pyttsx3
import tkinter as tk
from tkinter import ttk

auto_scroll_direction = None  # 'up', 'down', or None
auto_scroll_thread = None

def smart_comic_control():
    # Voice engine for feedback
    global cap
    global mode
    engine = pyttsx3.init()
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    # Scroll control variables

    auto_scroll_stop_event = threading.Event()
    scroll_speed = 600

    # Gesture detection setup
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    # Webcam
    cap = cv2.VideoCapture(0)

    # Scroll timing
    scroll_delay = 0.5
    last_scroll_time = 0

    # Mode
    mode = "Gesture"

    # Voice recognition
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # === Auto scroll ===
    def auto_scroll():
        global auto_scroll_direction
        while not auto_scroll_stop_event.is_set():
            if auto_scroll_direction == 'down':
                pyautogui.scroll(-100)
            elif auto_scroll_direction == 'up':
                pyautogui.scroll(100)
            time.sleep(0.1)

    # === Hand gesture detection helpers ===
    def is_palm_open(landmarks):
        finger_tips = [8, 12, 16, 20]
        return sum(1 for tip in finger_tips if landmarks[tip].y < landmarks[tip - 2].y) >= 3

    def is_thumbs_up(landmarks):
        return (
            landmarks[4].y < landmarks[3].y < landmarks[2].y and
            all(landmarks[tip].y > landmarks[tip - 2].y for tip in [8, 12, 16, 20])
        )

    def is_thumbs_down(landmarks):
        return (
            landmarks[4].y > landmarks[3].y > landmarks[2].y and
            all(landmarks[tip].y > landmarks[tip - 2].y for tip in [8, 12, 16, 20])
        )

    def is_rock_sign(landmarks):
        return (
            landmarks[4].y < landmarks[3].y and
            landmarks[8].y < landmarks[6].y and
            landmarks[12].y > landmarks[10].y and
            landmarks[16].y > landmarks[14].y and
            landmarks[20].y < landmarks[18].y
        )

    # === Voice recognition ===
    def recognize_voice():
        
        global mode, auto_scroll_direction, auto_scroll_thread
        while True:
            if mode == "Voice":
                try:
                    with mic as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=4)
                        command = recognizer.recognize_google(audio).lower()
                        print("Voice Command:", command)

                        if "scroll down" in command:
                            speak("Auto scrolling down")
                            auto_scroll_direction = 'down'
                            auto_scroll_stop_event.clear()
                            if auto_scroll_thread is None or not auto_scroll_thread.is_alive():
                                auto_scroll_thread = threading.Thread(target=auto_scroll)
                                auto_scroll_thread.daemon = True
                                auto_scroll_thread.start()

                        elif "scroll up" in command:
                            speak("Auto scrolling up")
                            auto_scroll_direction = 'up'
                            auto_scroll_stop_event.clear()
                            if auto_scroll_thread is None or not auto_scroll_thread.is_alive():
                                auto_scroll_thread = threading.Thread(target=auto_scroll)
                                auto_scroll_thread.daemon = True
                                auto_scroll_thread.start()

                        elif "stop scrolling" in command:
                            print("Voice Command: stop auto scroll")
                            auto_scroll_stop_event.set()
                            auto_scroll_direction = None  # Clear direction


                        elif "next chapter" in command:
                            pyautogui.click(1015, 136)
                            speak("Next chapter")

                        elif "previous chapter" in command:
                            pyautogui.click(890, 137)
                            speak("Previous chapter")

                except Exception as e:
                    print("Voice error:", e)
                    continue

    # Start voice recognition in background
    threading.Thread(target=recognize_voice, daemon=True).start()

    # === Main Loop ===
    while True:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret or frame is None:
            print("❌ Failed to read from webcam")
            break
        h, w, _ = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        # Draw gesture zones
        cv2.rectangle(frame, (0, int(h * 0.75)), (w, h), (0, 255, 0), 2)  # Bottom zone
        cv2.rectangle(frame, (0, 0), (w, int(h * 0.25)), (255, 0, 0), 2)  # Top zone

        # Show mode text
        cv2.putText(frame, f"Mode: {mode}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 255) if mode == "Voice" else (0, 255, 0), 2)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                wrist_y = hand_landmarks.landmark[0].y * h

                if is_rock_sign(hand_landmarks.landmark):
                    mode = "Voice" if mode == "Gesture" else "Gesture"
                    print("🤟 Toggled Mode →", mode)
                    speak(f"{mode} Mode")
                    time.sleep(1)

                if mode == "Gesture":
                    if is_thumbs_up(hand_landmarks.landmark):
                        pyautogui.click(1015, 136)
                        print("👍 Thumbs Up → Next Chapter")
                        time.sleep(1.2)

                    elif is_thumbs_down(hand_landmarks.landmark):
                        pyautogui.click(890, 137)
                        print("👎 Thumbs Down → Previous Chapter")
                        time.sleep(1.2)

                    elif is_palm_open(hand_landmarks.landmark):
                        if wrist_y > h * 0.75 and time.time() - last_scroll_time > scroll_delay:
                            pyautogui.scroll(-scroll_speed)
                            last_scroll_time = time.time()
                            print("⬇️ Palm at Bottom → Scroll Down")

                        elif wrist_y < h * 0.25 and time.time() - last_scroll_time > scroll_delay:
                            pyautogui.scroll(scroll_speed)
                            last_scroll_time = time.time()
                            print("⬆️ Palm at Top → Scroll Up")

        cv2.imshow("Comic Control with Gestures + Voice", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

def start_scroller():
    threading.Thread(target=smart_comic_control, daemon=True).start()

def stop_scroller():
    if 'cap' in globals() and cap.isOpened():
        cap.release()
        cv2.destroyAllWindows()
        print("Webcam released.")
    else:
        print("Webcam was not running.")


# Simple GUI
app = tk.Tk()
app.title("Smart Comic Scroller 🧠📖")
app.geometry("300x200")

ttk.Label(app, text="Smart Comic Scroller", font=("Arial", 14)).pack(pady=10)

ttk.Button(app, text="▶ Start", command=start_scroller).pack(pady=10)
ttk.Button(app, text="⏹ Stop", command=stop_scroller).pack(pady=5)

app.mainloop()


import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
import pytesseract
import speech_recognition as sr
import pyttsx3
import sympy as sp
import re
import cv2
from PIL import Image, ImageTk
import threading

# Create a window
root = tk.Tk()
root.title("Math Arithmetic Equation Solver")
root.config(bg="light blue")

# pyttsx3
engine = pyttsx3.init()

# opencv
cap = cv2.VideoCapture(0)

# To preprocess and input
def preprocess_equation(equation):
    # Replace 'x' with '*' for multiplication
    equation = equation.replace('x', '*').replace('X', '*')
    
    equation = re.sub(r'[^0-9+\-*/().]', '', equation)
    
    # Remove any extraneous spaces
    equation = equation.replace(" ", "")
    
    return equation

# To solve math equations
def solve_math_problem(problem_text):
    try:
        # For math expressions
        equation = preprocess_equation(problem_text)
        cleaned_problem = re.sub(r'[^\d+\-*/().*]', '', equation)
        expr = sp.sympify(cleaned_problem)
        result = sp.N(expr)
        # To remove unnecessary zeros
        formatted_result = format(float(result), ".15g").rstrip('0').rstrip('.') if '.' in format(float(result), ".15g") else format(float(result), ".15g")
        return formatted_result
    except sp.SympifyError as e:
        print(f"Error parsing the math problem: {e}")
        return "Invalid mathematical expression"
    except Exception as e:
        print(f"Error solving math problem: {e}")
        return "Unable to solve the problem"

# Function to recognize equation on an image
def perform_ocr(image):
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error performing OCR: {e}")
        return ""

# To handle voice input using SpeechRecognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your math problem:")
        audio = recognizer.listen(source)
        try:
            problem_text = recognizer.recognize_google(audio)
            print("You said:", problem_text)
            
            # Replace spoken words for brackets with appropriate characters
            problem_text = problem_text.lower()
            problem_text = problem_text.replace("open bracket", "(")
            problem_text = problem_text.replace("close bracket", ")")
            
            # Balance unmatched open brackets
            open_brackets = problem_text.count("(")
            close_brackets = problem_text.count(")")
            if open_brackets > close_brackets:
                problem_text += ")" * (open_brackets - close_brackets)
            
            math_entry.delete(0, tk.END)
            math_entry.insert(0, problem_text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Function to handle file selection and recognition of text from image
def select_file_and_ocr():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        text_from_image = perform_ocr(Image.open(file_path))
        if text_from_image:
            math_entry.delete(0, tk.END)
            math_entry.insert(0, text_from_image)

# To handle solving the math problem
def solve_problem():
    problem_text = math_entry.get()
    if problem_text:
        result = solve_math_problem(problem_text)
        result_text = f"Result: {result}"  # Using formatted result without trailing zeros
        result_label.config(text=result_text)
        root.after(500, announce_result, result_text)

# Function to announce the result using speaker(pyttsx3)
def announce_result(result_text):
    def speak():
        engine.say(result_text)
        engine.runAndWait()
    
    # Run the speak function in a separate thread 
    threading.Thread(target=speak).start()

# To update the webcam feed in the new window
def update_webcam_feed():
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        webcam_label.imgtk = imgtk
        webcam_label.configure(image=imgtk)
        webcam_window.after(10, update_webcam_feed)

# Function to capture an image from the webcam
def capture_image():
    ret, frame = cap.read()
    if ret:
        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        text_from_image = perform_ocr(pil_image)
        if text_from_image:
            math_entry.delete(0, tk.END)
            math_entry.insert(0, text_from_image)
            solve_problem()


# Function to open the webcam window
def open_webcam_window():
    global webcam_window, webcam_label
    webcam_window = tk.Toplevel(root)
    webcam_window.title("Webcam Feed")
    webcam_label = tk.Label(webcam_window)
    webcam_label.pack()
    capture_button = tk.Button(webcam_window, text="Capture Image", command=capture_image)
    capture_button.pack(pady=10)
    update_webcam_feed()

# Below is the program to create GUI elements for the main window

myFont = font.Font(size=11)

# Arrange GUI elements
math_label = tk.Label(root, text="Enter the math problem:", bg="light blue")
math_label.pack(pady=10)

math_entry = tk.Entry(root, width=50, font=myFont)
math_entry.pack(pady=10)

voice_button = tk.Button(root, text="Give Voice Input", command=recognize_speech, font=myFont)
voice_button.pack(pady=5)


ocr_button = tk.Button(root, text="  Select Image  ", command=select_file_and_ocr, font=myFont)
ocr_button.pack(pady=5)


webcam_button = tk.Button(root, text="Open Webcam Window", command=open_webcam_window, font=myFont)
webcam_button.pack(pady=5)


result_label = tk.Label(root, text="", font=myFont, bg="light blue")
result_label.pack(pady=10)


solve_button = tk.Button(root, text="Solve", command=solve_problem, font=myFont)
solve_button.pack(pady=10)


# Run the main loop
root.mainloop()

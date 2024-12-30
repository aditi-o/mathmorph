# mathmorph
# Math Arithmetic Equation Solver  

This project is an intuitive and user-friendly multimedia-powered math solver, capable of accepting arithmetic equations through multiple input modes—voice, images, and live camera feed. Built with Python, it leverages powerful libraries like **Tkinter**, **Pytesseract**, **SpeechRecognition**, **pyttsx3**, and **SymPy** to create a seamless, interactive experience for solving math problems.  

## Features  
- **Multimedia Input:** Accept equations via:  
  - **Voice Commands:** Speak your equation aloud, and the application will process it.  
  - **Image Recognition:** Upload an image or capture one via webcam, and the application extracts and solves the equation.  
  - **Manual Text Entry:** Type your equation directly into the application.  
- **Real-time Solution:** Solves equations instantly and displays precise results.  
- **Audio Feedback:** Announces the solution using a text-to-speech engine, making it accessible and engaging.  
- **Live Webcam Feed:** Capture equations directly from the camera for instant processing.  
- **Equation Preprocessing:** Automatically formats and cleans input equations for accurate solving.  

## Technologies Used  
- **Graphical User Interface (GUI):** Built with Tkinter for an interactive layout.  
- **OCR:** Uses Pytesseract to extract text from images.  
- **Speech Recognition:** Converts voice input into text for equation solving.  
- **Math Parsing and Solving:** Employs SymPy for accurate equation parsing and computation.  
- **Text-to-Speech:** Utilizes pyttsx3 to provide audible results.  
- **Webcam Integration:** Implements OpenCV for real-time camera input.  

## How It Works  
1. **Choose Input Method:**  
   - Enter the equation manually, select an image file, or capture an equation from the webcam.  
   - For voice input, simply speak the equation.  
2. **Process the Equation:**  
   - The input is preprocessed to ensure accurate parsing.  
   - For voice input, it handles spoken words like "open bracket" and balances unmatched brackets.  
3. **Solve and Announce:**  
   - The equation is solved in real-time using SymPy.  
   - The result is displayed on-screen and announced through the speaker.  

## Applications  
- **Educational Tools:** For students and teachers to quickly solve and verify equations.  
- **Accessibility:** Supports individuals with visual or physical impairments by using voice and audio features.  
- **Productivity Enhancement:** Reduces time spent on manual calculations or equation solving.  

This innovative tool makes solving arithmetic equations effortless, interactive, and accessible to everyone.

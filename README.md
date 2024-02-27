# Enhanced Quiz App with Sound Effects

## Overview
Welcome to the Enhanced Quiz App project! This Python application takes quiz-taking to the next level by incorporating dynamic question fetching, object-oriented design, an interactive GUI, and now, immersive sound effects. Test your knowledge with an added auditory dimension!

## Files
1. **data.py**
   - Utilizes the `requests` library to fetch quiz questions from the Open Trivia Database API.
   - Defines parameters for the API request.
   - Parses the JSON response and extracts the question data.

2. **main.py**
   - Imports necessary modules (`Question`, `question_data`, `QuizBrain`, `QuizInterface`).
   - Creates a list of `Question` instances from the fetched question data.
   - Initializes a `QuizBrain` with the question list and a `QuizInterface` to present the quiz to the user.

3. **question_model.py**
   - Defines the `Question` class with attributes for question text and correct answer.

4. **quiz_brain.py**
   - Implements the `QuizBrain` class, managing the flow of the quiz, tracking the user's score, and checking answers.
   - Uses the `html` module to unescape HTML entities in question text.

5. **ui.py**
   - Implements the graphical user interface using the `tkinter` library.
   - Displays questions, buttons for true/false answers, provides visual feedback, and now includes engaging sound effects.
   - Utilizes a color theme for a visually pleasing design.

## Sound Effects
- The enhanced version of the Quiz App introduces sound effects for a more immersive experience. The sound effects complement the user interface and contribute to an engaging quiz atmosphere.

## How to Run
1. Ensure you have Python installed on your system.
2. Run `main.py` to start the Enhanced Quiz App.
3. Enjoy the quiz, experience the sound effects, and challenge your knowledge!

## Dependencies
- `requests` library
- `tkinter` library (for GUI)
- Ensure your system supports playing sound files

## Special Thanks
A sincere thank you to Anela Yu for her continuous inspiration and guidance throughout the development of this project!

## Acknowledgments
- Open Trivia Database API (https://opentdb.com/)

Feel free to explore, contribute, or provide feedback. Let the quiz, with its enhanced features, be both an educational and enjoyable experience! 🚀🔊💻

#PythonProject #QuizApp #OpenTriviaAPI #ProgrammingFun #SoundEffects #TechCommunity

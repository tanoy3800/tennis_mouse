### Project Title
**Tennis Mouse Tracking Game**

### Project Description
The **Tennis Mouse Tracking Game** is an interactive, fast-paced arcade-style game where players control a paddle to bounce multiple balls back and forth. The game utilizes mouse movement to track the paddle's position on the screen, and the objective is to hit as many balls as possible without letting them fall off the screen. The game increases in difficulty over time as the balls' speed and direction change, providing an engaging experience for the player.

#### Features:
- **Mouse-controlled Paddle**: The paddle's position is controlled in real-time based on the mouse's movement.
- **Multiple Balls**: The game can feature more than one ball at a time, each with its own random movement.
- **Dynamic Speed**: As the game progresses, the balls' speed and movement become faster, creating a challenging environment.
- **Collision Detection**: Balls bounce off walls and the paddle, with angles and directions modified for added complexity.
- **Score Tracking**: Players earn points by successfully hitting balls with the paddle, with the score being displayed on the screen.
- **Game Over**: The game ends when any ball falls below the screen, displaying the final score.

### How to Install and Run the Project
To run the **Tennis Mouse Tracking Game**, follow these steps:
1. **Install Python**:
   - Ensure Python 3.x is installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**:
   - The game uses the `turtle` and `pyautogui` libraries. Install them by running the following commands in your terminal or command prompt:
     ```
     pip install pyautogui
     ```

3. **Download the Game Code**:
   - Download or clone the Python code for the **Tennis Mouse Tracking Game** to your local machine.

4. **Run the Program**:
   - Open a terminal or command prompt, navigate to the folder containing the game code, and run the Python file:
     ```
     python tennis_game.py
     ```
     
Problem I personaly found to run the **Tennis Mouse Tracking Game**:
1. **Unable to import 'pyautogui'**:
   - ModuleNotFoundError: No module named 'pyautogui' is the message I got when I first try to test how pyautigui work. This can be solve by change your Interpreter into Recommended path in vscode, by click the python version at the bottom right.

### Usage
Once the program is running, follow these steps to interact with the game:

1. **Control the Paddle**:
   - Use your mouse to move the paddle up, down, left, and right. The paddle will follow the mouse's position in real-time.

2. **Hit the Balls**:
   - The objective is to keep the balls from falling off the screen. Bounce the balls back by positioning the paddle correctly. Each successful hit increases your score.

3. **Game Over**:
   - The game will end when any ball crosses the bottom of the screen. Your score will be displayed, and the game will stop.

#### Sample Interaction:
- When you run the game, you'll see the white paddle and balls appear on the screen. The score will be displayed at the top.
- The balls will bounce around the screen. Move the paddle with your mouse to keep them in play.
- After hitting a ball, the speed of the game will increase, making it harder to control the paddle.

For a demonstration, [you can click this to vision the game in action]().

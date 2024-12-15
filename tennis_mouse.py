import turtle
import pyautogui
import random
import time
import math

class TennisGame:
    def __init__(self, num_balls:int=1):
        self.screen = turtle.Screen()
        self.screen.title("Tennis Mouse Tracking Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.num_balls = num_balls
        self.balls = []
        self.ball_speed = 2
        self.speed_increase_percentage = 1.05

        self.create_balls()  # Create balls for the game

        # Create paddle
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=6)
        self.paddle.penup()
        self.paddle.goto(0, -250)

        self.score = 0  # Initialize score

        # Display score
        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.goto(0, 240)
        self.score_display.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

        self.draw_walls()  # Draw game walls

        self.play_game()  # Start the game loop

    def create_balls(self):
        """Create balls and initialize their speed and directions."""
        for _ in range(self.num_balls):
            ball = turtle.Turtle()
            ball.shape("circle")
            ball.color("white")
            ball.penup()
            ball.speed(0)
            ball.goto(0, 0)

            # Assign initial random direction and speed
            speed = self.ball_speed
            ball.dx = speed * random.choice([1, -1])
            ball.dy = speed * random.choice([1, -1])

            self.balls.append(ball)

    def move_paddle(self):
        """Move the paddle based on the mouse position."""
        x, y = pyautogui.position()  # Get current mouse position
        x = x - 960  # Adjust for center of the screen
        y = (-y) + 565  # Adjust y-coordinate to match screen

        # Keep paddle within screen bounds
        if x > 350:
            x = 350
        elif x < -350:
            x = -350

        if y > 250:
            y = 250
        elif y < -250:
            y = -250

        self.paddle.setx(x)
        self.paddle.sety(y)

    def move_balls(self):
        """Move each ball, check for collisions, and adjust ball's position."""
        for ball in self.balls:
            # Scale the movement for high-speed balls
            movement_scale = 1
            if abs(ball.dx) > 5:  # If the ball is moving fast
                movement_scale = 0.5  # Make smaller movements to prevent skipping

            # Move the ball in smaller steps
            ball.setx(ball.xcor() + ball.dx * movement_scale)
            ball.sety(ball.ycor() + ball.dy * movement_scale)

            # Handle wall collisions
            if ball.xcor() > 390 or ball.xcor() < -390:
                ball.dx *= -1  # Reverse direction on horizontal wall

            if ball.ycor() > 290:
                ball.dy *= -1  # Reverse direction on upper wall
                self.randomize_ball_angle(ball)

            # Paddle collision detection
            if (ball.ycor() > self.paddle.ycor() - 10 and ball.ycor() < self.paddle.ycor() + 10) and \
               abs(ball.xcor() - self.paddle.xcor()) < 50:
                if ball.dy < 0:  # Only reverse if the ball is moving downwards
                    ball.dy *= -1
                    self.adjust_ball_angle(ball)
                    self.score += 1  # Increase score for successful hit

            # Game over if the ball falls below the screen
            if ball.ycor() < -290:
                self.game_over()

    def randomize_ball_angle(self, ball):
        """Randomly change the ball's angle after hitting the top wall."""
        angle = random.randint(30, 75)
        direction = random.choice([1, -1])

        angle_rad = angle * (math.pi / 180)  # Convert angle to radians

        # Reassign ball speed and direction after randomization
        speed = self.ball_speed
        ball.dx = speed * direction * math.cos(angle_rad)
        ball.dy = speed * -abs(math.sin(angle_rad))

    def adjust_ball_angle(self, ball):
        """Adjust the ball's angle after hitting the paddle to add variation."""
        variation = random.uniform(0.2, 1.0)
        ball.dy = abs(ball.dy)  # Make sure the ball is moving upwards after hitting paddle

        if ball.xcor() > self.paddle.xcor():  # Ball hits right side of paddle
            direction = -1
            ball.dx = (ball.dx * variation) * direction
        elif ball.xcor() < self.paddle.xcor():  # Ball hits left side of paddle
            direction = 1
            ball.dx = (ball.dx * variation) * direction
        else:
            ball.dx = (ball.dx * variation)  # No horizontal deviation if center hit

        # Increase ball speed after hitting the paddle
        ball.dx *= self.speed_increase_percentage
        ball.dy *= self.speed_increase_percentage
        self.ball_speed *= self.speed_increase_percentage  # Increase global speed

    def draw_walls(self):
        """Draw the walls surrounding the game area."""
        wall_thickness = 10

        # Lower wall
        lower_wall = turtle.Turtle()
        lower_wall.hideturtle()
        lower_wall.speed(0)
        lower_wall.color("red")
        lower_wall.pensize(wall_thickness)
        lower_wall.penup()
        lower_wall.goto(-400, -290)
        lower_wall.pendown()
        lower_wall.goto(400, -290)

        # Upper wall
        upper_wall = turtle.Turtle()
        upper_wall.hideturtle()
        upper_wall.speed(0)
        upper_wall.color("white")
        upper_wall.pensize(wall_thickness)
        upper_wall.penup()
        upper_wall.goto(-400, 290)
        upper_wall.pendown()
        upper_wall.goto(400, 290)

        # Left wall
        left_wall = turtle.Turtle()
        left_wall.hideturtle()
        left_wall.speed(0)
        left_wall.color("white")
        left_wall.pensize(wall_thickness)
        left_wall.penup()
        left_wall.goto(-400, -290)
        left_wall.pendown()
        left_wall.goto(-400, 290)

        # Right wall
        right_wall = turtle.Turtle()
        right_wall.hideturtle()
        right_wall.speed(0)
        right_wall.color("white")
        right_wall.pensize(wall_thickness)
        right_wall.penup()
        right_wall.goto(400, -290)
        right_wall.pendown()
        right_wall.goto(400, 290)

    def game_over(self):
        """Handle the game over scenario when a ball goes below the screen."""
        for ball in self.balls:
            ball.dx = 0  # Stop ball movement
            ball.dy = 0
            ball.hideturtle()  # Hide the ball
        self.paddle.hideturtle()  # Hide the paddle

        # Display the game over message
        game_over_text = turtle.Turtle()
        game_over_text.hideturtle()
        game_over_text.color("white")
        game_over_text.penup()
        game_over_text.goto(0, 0)
        game_over_text.write(f"Game Over! Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def play_game(self):
        """Start the game loop to continuously move the paddle and balls."""
        while True:
            self.move_paddle()  # Move the paddle based on mouse position
            self.move_balls()  # Move the balls and check for collisions

            # Update the score display
            self.score_display.clear()
            self.score_display.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

            self.screen.update()  # Update the screen with new positions
            time.sleep(0.01)  # Control the game speed

if __name__ == "__main__":
    num_balls = int(input("Enter number of balls: "))  # Ask for the number of balls
    game = TennisGame(num_balls)  # Start the game with the specified number of balls

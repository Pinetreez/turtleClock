
import turtle
import time

# Switch to Logo mode - Up = 0 degrees, then go clockwise
turtle.mode("logo")

# Single-Hand Length
HOUR_HAND = 190

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

# Create a Turtle object
face = turtle.Turtle(visible=False)
face.speed(5)  # Set the drawing speed
hand = turtle.Turtle(visible=False)

# Function to draw a clock face with hand
def draw_clock_face():
    
    # List of Roman numerals for the clock hours
    roman_numerals = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]

# Draw the clock numbers and balls
    for i in range(12):
        hour = roman_numerals[i]  # Use Roman numeral from the list
        face.penup()
        face.goto(0, 0)
        face.setheading(i * 30)  # angle in degrees
        face.forward(200)
        face.pendown()
        face.setheading(180)
        face.penup()
        face.forward(25)
        face.color("DarkOrange3")
    
        # Adjust the position of the numbers at 3 and 9 o'clock
        if i == 3 or i == 9:
            face.setx(face.xcor() - 8)  # Move to the left slightly
    
        face.write(str(hour), align="center", font=("Arial", 13, "normal"))


    # Draw the minute dots
    for x in range(720):
        face.penup()
        face.goto(0, 0)
        face.setheading(x/2)  # angle in degrees (720 seconds = 360 degrees)
        face.forward(200)
        face.pendown()
        if x % 60 == 0:
            face.dot(10, "DarkOrange3")
        elif x % 30 == 0:
            face.dot(7, "DarkSeaGreen3")  
        elif x % 15 == 0:
            face.dot(5, "DarkGoldenRod4")
        elif x % 5 == 0:
            face.dot(3, "azure")
        face.setheading(180)
        

    
# Function to draw clock hand
def draw_clock_hand():

    current_time = time.localtime()
    # Clear previous hands
    hand.clear()

    # Calculate angles for the hand
    hour_angle = (current_time.tm_hour % 12) * 30 + current_time.tm_min * 0.5
    


    # Draw the hour hand 
    hand.penup()
    hand.goto(0, 0)
    hand.pendown()
    hand.color("DarkOrange")
    hand.setheading(hour_angle)
    hand.pensize(3)
    hand.forward(HOUR_HAND)

# Function to update the clock continuously
def update_clock():
    draw_clock_face()
    while True:
        draw_clock_hand()  # Draw the clock hand based on the current time
        screen.update()  # Update the screen
        time.sleep(1)  # Wait for 1 second before updating the clock again

# Main program
if __name__ == "__main__":
    
      # Call the function to draw the clock face
    update_clock()  # Call the function to draw the clock hand
    # Close the window when clicked
    screen.exitonclick()
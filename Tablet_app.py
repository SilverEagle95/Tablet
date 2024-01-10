import tkinter as tk
from tkinter import Canvas, Button, PhotoImage, messagebox
import cv2
import numpy as np
import base64
import pygame
import os
from tkinter import filedialog
import time
from gtts import gTTS
import ursina

# tic-tac-toe
def tic_tac_tou():
    import tkinter as tk
    from tkinter import messagebox
    import random

    # Function to check for a win or tie
    def check_win():
        for i in range(3):
            if (buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != " ") or \
                    (buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != " ") or \
                    (buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != " ") or \
                    (buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != " "):
                messagebox.showinfo("Winner!", f"Player {buttons[i][i]['text']} wins!")
                return True
        if all(buttons[i][j]['text'] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("Tie Game", "It's a tie!")
            return True
        return False

    # Function for the computer's move
    def computer_move():
        empty_buttons = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]['text'] == " "]
        if empty_buttons:
            row, col = random.choice(empty_buttons)
            buttons[row][col]['text'] = "O"
            check_win()

    # Function to handle button click
    def on_click(row, col):
        if buttons[row][col]['text'] == " " and not check_win():
            buttons[row][col]['text'] = "X"
            if not check_win():
                computer_move()

    # Function to restart the game
    def restart_game():
        for i in range(3):
            for j in range(3):
                buttons[i][j]['text'] = " "
        check_win()

    # Create the main window
    root = tk.Tk()
    root.title("Tic-Tac-Toe vs Computer")

    # Create a 2D list to hold the buttons
    buttons = [[None for _ in range(3)] for _ in range(3)]

    # Create buttons and add them to the window
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2,
                                      command=lambda i=i, j=j: on_click(i, j))
            buttons[i][j].grid(row=i, column=j)

    # Create a restart button
    restart_button = tk.Button(root, text="Restart", command=restart_game)
    restart_button.grid(row=3, column=1, pady=10)

    # Start the GUI loop
    root.mainloop()


# Guessing game
def guessing_game():
    import tkinter as tk
    from tkinter import messagebox
    import random

    class GuessingGame:
        def __init__(self, master):
            self.master = master
            self.master.title("Colorful Guessing Game")
            self.master.geometry("300x200")
            self.master.configure(bg='#FFD700')  # Set background color to gold

            self.target_number = random.randint(1, 100)

            self.feedback_label = tk.Label(self.master, text="Enter your guess:", font=('Helvetica', 12), bg='#FFD700')
            self.feedback_label.pack()

            self.guess_entry = tk.Entry(self.master, font=('Helvetica', 12))
            self.guess_entry.pack()

            self.guess_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess,
                                          font=('Helvetica', 12), bg='#32CD32', fg='white')
            self.guess_button.pack()

            self.result_label = tk.Label(self.master, text="", font=('Helvetica', 12), bg='#FFD700')
            self.result_label.pack()

        def check_guess(self):
            try:
                user_guess = int(self.guess_entry.get())
                self.give_feedback(user_guess)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")

        def give_feedback(self, guess):
            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.", fg='#FF6347')  # Set text color to tomato
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.", fg='#FF6347')
            else:
                self.result_label.config(text=f"Congratulations! You guessed the correct number {self.target_number}.",
                                         fg='#008080')  # Set text color to teal
                self.reset_game()

        def reset_game(self):
            self.target_number = random.randint(1, 100)
            self.guess_entry.delete(0, tk.END)
            self.result_label.config(text="", fg='#FFD700')  # Reset text color

    if __name__ == "__main__":
        root = tk.Tk()
        game = GuessingGame(root)
        root.mainloop()


# Timer
def Timer():
    import tkinter as tk
    from tkinter import ttk
    import time

    class TimerApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Modern Timer")
            self.root.geometry("400x200")
            self.root.resizable(False, False)

            self.is_running = False
            self.start_time = None

            self.style = ttk.Style()
            self.style.configure("TButton", padding=10, font=("Helvetica", 12))

            self.label_var = tk.StringVar()
            self.label_var.set("00:00:00")

            self.label = ttk.Label(root, textvariable=self.label_var, font=("Helvetica", 24))
            self.label.pack(pady=20)

            self.start_button = ttk.Button(root, text="Start", command=self.start_timer)
            self.start_button.pack(side=tk.LEFT, padx=10)

            self.stop_button = ttk.Button(root, text="Stop", command=self.stop_timer)
            self.stop_button.pack(side=tk.LEFT, padx=10)

            self.reset_button = ttk.Button(root, text="Reset", command=self.reset_timer)
            self.reset_button.pack(side=tk.LEFT, padx=10)

            self.update_timer()

        def start_timer(self):
            if not self.is_running:
                self.is_running = True
                self.start_time = time.time() - self.elapsed_time()

                self.start_button["state"] = "disabled"
                self.stop_button["state"] = "enabled"
                self.reset_button["state"] = "enabled"

                self.update_timer()

        def stop_timer(self):
            if self.is_running:
                self.is_running = False

                self.start_button["state"] = "enabled"
                self.stop_button["state"] = "disabled"
                self.reset_button["state"] = "enabled"

        def reset_timer(self):
            self.is_running = False
            self.start_time = None

            self.start_button["state"] = "enabled"
            self.stop_button["state"] = "disabled"
            self.reset_button["state"] = "disabled"

            self.update_timer()

        def elapsed_time(self):
            if self.start_time is None:
                return 0
            return time.time() - self.start_time

        def update_timer(self):
            if self.is_running:
                self.label_var.set(self.format_time(self.elapsed_time()))
                self.root.after(1000, self.update_timer)

        @staticmethod
        def format_time(seconds):
            minutes, seconds = divmod(int(seconds), 60)
            hours, minutes = divmod(minutes, 60)
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    if __name__ == "__main__":
        root = tk.Tk()
        app = TimerApp(root)
        root.mainloop()


# magic game
def magic_game():
    import tkinter as tk
    import random

    root = tk.Tk()
    root.title("Magic Ball")
    root.geometry("600x800")
    root.config(bg="dark blue")

    def shaking():
        answer_list = ["No", "Yes", "Maybe", "I dont think so", "Nuh-uh", "Ofcourse"]
        random_answer = random.sample(answer_list, k=1)
        title.config(text=random_answer)

    title = tk.Label(root, text="Shake the magic ball!", height=5, width=80, font=100, bg="black", fg="purple")
    title.pack()

    shake_button = tk.Button(root, text="Shake!", bg="purple", font=70, width=40, command=lambda: shaking())
    shake_button.pack()

    root.mainloop()

# fireworks
def fireworks():
    import pygame
    from random import randint, uniform, choice
    import math

    vector2 = pygame.math.Vector2
    trails = []
    fade_p = []

    GRAVITY_FIREWORK = vector2(0, 0.3)
    GRAVITY_PARTICLE = vector2(0, 0.07)
    DISPLAY_WIDTH = DISPLAY_HEIGHT = 800
    BACKGROUND_COLOR = (20, 20, 30)
    FIREWORK_SPEED_MIN = 17
    FIREWORK_SPEED_MAX = 20
    FIREWORK_SIZE = 5
    PARTICLE_LIFESPAN = 70
    X_SPREAD = 0.8
    Y_SPREAD = 0.8
    PARTICLE_SIZE = 4
    MIN_PARTICLES = 100
    MAX_PARTICLES = 200
    X_WIGGLE_SCALE = 20
    Y_WIGGLE_SCALE = 10
    EXPLOSION_RADIUS_MIN = 10
    EXPLOSION_RADIUS_MAX = 25
    COLORFUL = True
    TRAIL_LIFESPAN = PARTICLE_LIFESPAN / 2
    TRAIL_FREQUENCY = 10
    TRAILS = True

    # Initialize Pygame mixer
    pygame.init()
    pygame.mixer.init()

    # Load sound effects
    explosion_sound = pygame.mixer.Sound(
        "C:\\Users\\alizb\\Downloads\\Sound Effects  Fireworks.mp3")  # Replace with the actual file path

    class Firework:
        def __init__(self):
            self.colour = tuple(randint(0, 255) for _ in range(3))
            self.colours = tuple(tuple(randint(0, 255) for _ in range(3)) for _ in range(3))

            self.firework = Particle(randint(0, DISPLAY_WIDTH), DISPLAY_HEIGHT, True, self.colour)
            self.exploded = False
            self.particles = []

        def update(self, win: pygame.Surface) -> None:
            if not self.exploded:
                self.firework.apply_force(GRAVITY_FIREWORK)
                self.firework.move()
                self.show(win)
                if self.firework.vel.y >= 0:
                    self.exploded = True
                    self.explode()
            else:
                for particle in self.particles:
                    particle.update()
                    particle.show(win)

        def explode(self):
            amount = randint(MIN_PARTICLES, MAX_PARTICLES)
            if COLORFUL:
                self.particles = [Particle(self.firework.pos.x, self.firework.pos.y, False, choice(self.colours)) for _
                                  in
                                  range(amount)]
            else:
                self.particles = [Particle(self.firework.pos.x, self.firework.pos.y, False, self.colour) for _ in
                                  range(amount)]
            explosion_sound.play()  # Play the explosion sound

        def show(self, win: pygame.Surface) -> None:
            x = int(self.firework.pos.x)
            y = int(self.firework.pos.y)
            pygame.draw.circle(win, self.colour, (x, y), self.firework.size)

        def remove(self) -> bool:
            if not self.exploded:
                return False

            for p in self.particles:
                if p.remove:
                    self.particles.remove(p)

            return len(self.particles) == 0

    class Particle(object):
        def __init__(self, x, y, firework, colour):
            self.firework = firework
            self.pos = vector2(x, y)
            self.origin = vector2(x, y)
            self.acc = vector2(0, 0)
            self.remove = False
            self.explosion_radius = randint(EXPLOSION_RADIUS_MIN, EXPLOSION_RADIUS_MAX)
            self.life = 0
            self.colour = colour
            self.trail_frequency = TRAIL_FREQUENCY + randint(-3, 3)

            if self.firework:
                self.vel = vector2(0, -randint(FIREWORK_SPEED_MIN, FIREWORK_SPEED_MAX))
                self.size = FIREWORK_SIZE
            else:
                self.vel = vector2(uniform(-1, 1), uniform(-1, 1))
                self.vel.x *= randint(7, self.explosion_radius + 2)
                self.vel.y *= randint(7, self.explosion_radius + 2)
                self.size = randint(PARTICLE_SIZE - 1, PARTICLE_SIZE + 1)
                self.move()
                self.outside_spawn_radius()

        def update(self) -> None:
            self.life += 1
            if self.life % self.trail_frequency == 0:
                trails.append(Trail(self.pos.x, self.pos.y, False, self.colour, self.size))
            self.apply_force(
                vector2(uniform(-1, 1) / X_WIGGLE_SCALE, GRAVITY_PARTICLE.y + uniform(-1, 1) / Y_WIGGLE_SCALE))
            self.move()

        def apply_force(self, force: pygame.math.Vector2) -> None:
            self.acc += force

        def outside_spawn_radius(self) -> bool:
            distance = math.sqrt((self.pos.x - self.origin.x) ** 2 + (self.pos.y - self.origin.y) ** 2)
            return distance > self.explosion_radius

        def move(self) -> None:
            if not self.firework:
                self.vel.x *= X_SPREAD
                self.vel.y *= Y_SPREAD
            self.vel += self.acc
            self.pos += self.vel
            self.acc *= 0
            self.decay()

        def show(self, win: pygame.Surface) -> None:
            x = int(self.pos.x)
            y = int(self.pos.y)
            pygame.draw.circle(win, self.colour, (x, y), self.size)

        def decay(self) -> None:
            if self.life > PARTICLE_LIFESPAN:
                if randint(0, 15) == 0:
                    self.remove = True
            if not self.remove and self.life > PARTICLE_LIFESPAN * 1.5:
                self.remove = True

    class Trail(Particle):
        def __init__(self, x, y, is_firework, colour, parent_size):
            Particle.__init__(self, x, y, is_firework, colour)
            self.size = parent_size - 1

        def decay(self) -> bool:
            self.life += 1
            if self.life % 100 == 0:
                self.size -= 1
            self.size = max(0, self.size)
            self.colour = (min(self.colour[0] + 5, 255), min(self.colour[1] + 5, 255), min(self.colour[2] + 5, 255))
            if self.life > TRAIL_LIFESPAN:
                ran = randint(0, 15)
                if ran == 0:
                    return True
            if not self.remove and self.life > TRAIL_LIFESPAN * 1.5:
                return True
            return False

    def update(win: pygame.Surface, fireworks: list, trails: list) -> None:
        if TRAILS:
            for t in trails:
                t.show(win)
                if t.decay():
                    trails.remove(t)
        for fw in fireworks:
            fw.update(win)
            if fw.remove():
                fireworks.remove(fw)
        pygame.display.update()

    def main():
        win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        clock = pygame.time.Clock()
        fireworks = []
        running = True

        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button click
                    fireworks.append(Firework())
                    explosion_sound.play()  # Play the explosion sound when creating a new firework

            win.fill(BACKGROUND_COLOR)
            update(win, fireworks, trails)

        pygame.quit()
        quit()

    main()


# Translator
def translator_app():
    import tkinter as tk
    from googletrans import Translator, LANGUAGES
    from gtts import gTTS
    import os
    import pygame

    class TranslatorApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Simple Translator")

            # Input language dropdown
            self.input_language_label = tk.Label(master, text="Select Input Language:")
            self.input_language_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

            self.input_languages = list(LANGUAGES.values())
            self.input_language_var = tk.StringVar()
            self.input_language_var.set(self.input_languages[0])

            self.input_language_menu = tk.OptionMenu(master, self.input_language_var, *self.input_languages)
            self.input_language_menu.grid(row=0, column=1, padx=10, pady=10)

            # Selected input language label
            self.selected_input_label = tk.Label(master, text="Selected Input Language:")
            self.selected_input_label.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

            # Entry for input
            self.input_text_label = tk.Label(master, text="Enter Text:")
            self.input_text_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

            self.input_text = tk.Entry(master, width=40)
            self.input_text.grid(row=1, column=1, padx=10, pady=10)

            # Output language dropdown
            self.output_language_label = tk.Label(master, text="Select Output Language:")
            self.output_language_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

            self.output_language_var = tk.StringVar()
            self.output_language_var.set(self.input_languages[1])

            self.output_language_menu = tk.OptionMenu(master, self.output_language_var, *self.input_languages)
            self.output_language_menu.grid(row=2, column=1, padx=10, pady=10)

            # Selected output language label
            self.selected_output_label = tk.Label(master, text="Selected Output Language:")
            self.selected_output_label.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)

            # Button to trigger translation
            self.translate_button = tk.Button(master, text="Translate", command=self.translate_text)
            self.translate_button.grid(row=2, column=3, padx=10, pady=10)

            # Voice button
            self.voice_button = tk.Button(master, text="Play Translation", command=self.play_translation)
            self.voice_button.grid(row=2, column=4, padx=10, pady=10)

            # Voice select button
            self.voice_select_button = tk.Button(master, text="Voice Select", command=self.play_input_text)
            self.voice_select_button.grid(row=2, column=5, padx=10, pady=10)

            # Output label
            self.output_label = tk.Label(master, text="Translated Text:")
            self.output_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

            # Text widget to display output
            self.output_text = tk.Text(master, height=5, width=40)
            self.output_text.grid(row=3, column=1, padx=10, pady=10)

        def translate_text(self):
            translator = Translator()
            input_text = self.input_text.get()
            input_lang = self.input_language_var.get()
            output_lang = [k for k, v in LANGUAGES.items() if v == self.output_language_var.get()][0]
            translated_text = translator.translate(input_text, src=input_lang, dest=output_lang).text
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, translated_text)

            # Update selected language labels
            self.selected_input_label.config(text="Selected Input Language: " + input_lang)
            self.selected_output_label.config(text="Selected Output Language: " + output_lang)

        def play_translation(self):
            translated_text = self.output_text.get(1.0, tk.END).strip()
            if translated_text:
                output_lang_code = [k for k, v in LANGUAGES.items() if v == self.output_language_var.get()][0]
                tts = gTTS(translated_text, lang=output_lang_code)
                tts.save("translation.mp3")
                self.play_audio("translation.mp3")

        def play_input_text(self):
            input_text = self.input_text.get()
            if input_text:
                input_lang_code = [k for k, v in LANGUAGES.items() if v == self.input_language_var.get()][0]
                tts = gTTS(input_text, lang=input_lang_code)
                tts.save("input_text.mp3")
                self.play_audio("input_text.mp3")


        def play_audio(self, filename):
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

    if __name__ == "__main__":
        root = tk.Tk()
        app = TranslatorApp(root)
        root.mainloop()


# bank app
def bank_app():
    import tkinter as tk
    from tkinter import messagebox
    from matplotlib import pyplot as plt

    class FinancialTrackerApp:
        """
        A tkinter-based application for tracking financial expenses and incomes.

        Attributes:
        - root: tk.Tk
            The main window of the application.
        - expenses: dict
            A dictionary to store the expenses, categorized by their categories.
        - incomes: list
            A list to store the incomes.
        """

        def __init__(self):
            """
            Constructor to initialize the FinancialTrackerApp class.

            Initializes the main window, expenses dictionary, and incomes list.
            """

            # Creating the main window
            self.root = tk.Tk()
            self.root.title("Financial Tracker")

            # Initializing the expenses dictionary and incomes list
            self.expenses = {}
            self.incomes = []

        def add_expense(self, category: str, amount: float):
            """
            Adds an expense to the expenses dictionary.

            Parameters:
            - category: str
                The category of the expense.
            - amount: float
                The amount of the expense.

            Raises:
            - ValueError:
                Raises an error if the amount is negative.
            """

            # Checking if the amount is negative
            if amount < 0:
                raise ValueError("Expense amount cannot be negative.")

            # Adding the expense to the expenses dictionary
            if category in self.expenses:
                self.expenses[category] += amount
            else:
                self.expenses[category] = amount

        def add_income(self, amount: float):
            """
            Adds an income to the incomes list.

            Parameters:
            - amount: float
                The amount of the income.

            Raises:
            - ValueError:
                Raises an error if the amount is negative.
            """

            # Checking if the amount is negative
            if amount < 0:
                raise ValueError("Income amount cannot be negative.")

            # Adding the income to the incomes list
            self.incomes.append(amount)

        def show_summary(self):
            """
            Displays a summary of the expenses and incomes using matplotlib.

            Creates a pie chart to visualize the expenses by category,
            and a bar chart to visualize the incomes over time.
            """

            # Pie chart for expenses by category
            categories = list(self.expenses.keys())
            amounts = list(self.expenses.values())

            plt.figure(figsize=(8, 6))
            plt.pie(amounts, labels=categories, autopct='%1.1f%%')
            plt.title("Expenses by Category")
            plt.show()

            # Bar chart for incomes over time
            plt.figure(figsize=(8, 6))
            plt.plot(range(1, len(self.incomes) + 1), self.incomes)
            plt.xlabel("Time")
            plt.ylabel("Income")
            plt.title("Incomes over Time")
            plt.show()

        def run(self):
            """
            Runs the financial tracker application.

            Starts the main event loop of the tkinter application.
            """

            self.root.mainloop()

    # Example usage of the FinancialTrackerApp class:

    # Creating an instance of the FinancialTrackerApp
    app = FinancialTrackerApp()

    # Adding expenses
    try:
        app.add_expense("Food", 100)
        app.add_expense("Travel", 50)
        app.add_expense("Entertainment", 80)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

    # Adding incomes
    try:
        app.add_income(1000)
        app.add_income(500)
        app.add_income(800)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

    # Showing the summary
    app.show_summary()

    # Running the application
    app.run()


# tod-o app
def todo_app():
    import tkinter as tk
    from tkinter import messagebox

    def add_task():
        task = entry.get()
        if task:
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Please type here something!")

    def delete_task():
        try:
            selected_task_index = listbox.curselection()[0]
            listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Error", "Please select a task to delete!")

    def mark_done():
        try:
            selected_task_index = listbox.curselection()[0]
            task = listbox.get(selected_task_index)
            listbox.itemconfig(selected_task_index, {'bg': 'light grey', 'fg': 'grey'})
        except IndexError:
            messagebox.showwarning("Error", "Please select a task to mark it up!")

    # Tkinter window create
    root = tk.Tk()
    root.title("Todo App")

    # Task +
    frame_add_task = tk.Frame(root)
    frame_add_task.pack(pady=10)

    label = tk.Label(frame_add_task, text="Feladat:")
    label.pack(side=tk.LEFT)

    entry = tk.Entry(frame_add_task, width=30)
    entry.pack(side=tk.LEFT)

    add_button = tk.Button(frame_add_task, text="Hozzáadás", command=add_task)
    add_button.pack(side=tk.LEFT)

    # Feladatok listája
    listbox = tk.Listbox(root, width=50, height=10, selectbackground='light blue')
    listbox.pack(pady=20)

    # Törlés és megjelölés gombok
    frame_buttons = tk.Frame(root)
    frame_buttons.pack()

    delete_button = tk.Button(frame_buttons, text="Törlés", command=delete_task)
    delete_button.pack(side=tk.LEFT)

    done_button = tk.Button(frame_buttons, text="Megjelölés", command=mark_done)
    done_button.pack(side=tk.LEFT)

    # Tkinter start
    root.mainloop()


# begginer info
def beginner_infotk():
    import tkinter as tk
    from tkinter import messagebox
    import time

    def show_info():
        info_text = """
        print = function
        input = function
        str(string) = change string & type
        int(integer) = number type
        import = keyword
        lower = function
        find = function
        return = keyword

        Press at the menu "Infos" to see how those thing works
        """
        messagebox.showinfo("Infos", info_text)

    def run_project():
        result_text = """
        print('Hello!')
        The code: Hello!

        input_name = input('What's your name?: ')
        The code, Whatever you write here you can edit it with some more codes!

        variable_str = str(8)
        print(varaible_str+1)
        The code: 81, Becasue the 'variable_str' is a type, not a number!

        variable_int = int(8)
        print(varaible_int+1)
        A kód: 9, Because the int type converts 'str' to a number

        import time
        time.sleep(1)
        print('Hi')
        Wait 1 second and run the code: Hi, but it could be 'import random' or something else

        variable_case = 'HEllo WorLD'
        variable_case.lower()
        the code: hello world

        variable_find = 'I like cats and dogs'
        variable_find.find('cat')
        The code: 7

        'return' returns special codes
        """
        messagebox.showinfo("Project code", result_text)

    def on_exit():
        root.destroy()

    root = tk.Tk()
    root.title("Programing for begginers")

    info_button = tk.Button(root, text="Infos", command=show_info)
    info_button.pack(pady=10)

    project_button = tk.Button(root, text="Project running", command=run_project)
    project_button.pack(pady=10)

    exit_button = tk.Button(root, text="Leave", command=on_exit)
    exit_button.pack(pady=10)

    root.mainloop()


# weather
def weather_app():
    import tkinter as tk
    from PIL import Image, ImageTk
    import requests
    from io import BytesIO

    def get_weather(city):
        api_key = "5c34e4e67062d63c99605bd9f2b293ca"  # Replace with your OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            weather_info = f"The weather in {city} is {weather_description.lower()}, with a temperature of {temperature}°C."
            result_label.config(text=weather_info, fg="#2ecc71")  # Set text color to a shade of green for success
        else:
            error_message = f"Oops! Something went wrong: {data['message']}"
            result_label.config(text=error_message, fg="#e74c3c")  # Set text color to a shade of red for error

    # GUI setup
    root = tk.Tk()
    root.title("Creative Weather App")
    root.geometry("400x300")  # Adjust the window size

    city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 14),
                          fg="#3498db")  # Use a shade of blue for label text color
    city_label.pack(pady=5)

    city_entry = tk.Entry(root, font=("Helvetica", 14))
    city_entry.pack(pady=5)

    get_weather_button = tk.Button(root, text="Get Weather", command=lambda: get_weather(city_entry.get()),
                                   bg="#f39c12", fg="#ffffff",
                                   font=("Helvetica", 14))  # Use an orange color for the button
    get_weather_button.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=300,
                            fg="#9b59b6")  # Use a shade of purple for result text color
    result_label.pack(pady=5)

    root.configure(bg="#34495e")  # Set background color to a dark shade of blue

    root.mainloop()


# Extra 3D cube
def Cube_3dcoll():
    import tkinter as tk
    from math import sin, cos, radians

    class RotatingCube:
        def __init__(self, root, size=100):
            self.root = root
            self.root.title("Rotating 3D Cube")

            self.size = size
            self.angle_x = 0
            self.angle_y = 0

            self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
            self.canvas.pack()

            # Center of the canvas
            self.center = (self.canvas.winfo_reqwidth() // 2, self.canvas.winfo_reqheight() // 2)

            self.draw_cube()

            self.root.bind("<KeyPress>", self.key_press)
            self.root.bind("<KeyRelease>", self.key_release)

            self.rotate_cube()

        def draw_cube(self):
            # Define cube vertices
            vertices = [
                (-self.size, -self.size, -self.size),
                (self.size, -self.size, -self.size),
                (self.size, self.size, -self.size),
                (-self.size, self.size, -self.size),
                (-self.size, -self.size, self.size),
                (self.size, -self.size, self.size),
                (self.size, self.size, self.size),
                (-self.size, self.size, self.size)
            ]

            # Rotate vertices around the y-axis
            rotated_vertices = []
            for vertex in vertices:
                x, y, z = vertex
                new_x = x * cos(radians(self.angle_x)) - z * sin(radians(self.angle_x))
                new_z = x * sin(radians(self.angle_x)) + z * cos(radians(self.angle_x))
                rotated_vertices.append((new_x, y, new_z))

            # Rotate vertices around the x-axis
            final_rotated_vertices = []
            for vertex in rotated_vertices:
                x, y, z = vertex
                new_y = y * cos(radians(self.angle_y)) - z * sin(radians(self.angle_y))
                new_z = y * sin(radians(self.angle_y)) + z * cos(radians(self.angle_y))
                final_rotated_vertices.append((x, new_y, new_z))

            # Project vertices onto 2D space and translate to the center
            projected_vertices = [(x + self.center[0], y + self.center[1]) for x, y, z in final_rotated_vertices]

            # Draw the filled cube
            cube_polygon = [
                projected_vertices[0], projected_vertices[1], projected_vertices[2], projected_vertices[3],
                projected_vertices[7], projected_vertices[6], projected_vertices[5], projected_vertices[4]
            ]
            self.canvas.create_polygon(cube_polygon, fill="green", outline="black", tags="cube")

        def rotate_cube(self):
            self.angle_x += 2  # Adjust the rotation speed if needed
            self.angle_y += 2  # Adjust the rotation speed if needed
            self.draw_cube()
            self.root.after(30, self.rotate_cube)

        def key_press(self, event):
            if event.keysym in {"w", "a", "s", "d"}:
                self.root.bind("<KeyRelease-{}>".format(event.keysym), self.key_release)
                self.root.after(30, lambda: self.move_cube(event.keysym))

        def key_release(self, event):
            if event.keysym in {"w", "a", "s", "d"}:
                self.root.unbind("<KeyRelease-{}>".format(event.keysym))

        def move_cube(self, key):
            if key == "w":
                self.size += 5
            elif key == "s":
                self.size -= 5
            elif key == "a":
                self.angle_x -= 5
            elif key == "d":
                self.angle_x += 5
            elif key == "e":
                self.angle_y -= 5
            elif key == "q":
                self.angle_y += 5
            self.draw_cube()

    if __name__ == "__main__":
        root = tk.Tk()
        app = RotatingCube(root)
        root.mainloop()




# memory game (.place)
def memor_game1():
    import tkinter as tk
    from tkinter import messagebox
    import random

    class MemoryGame:
        def __init__(self, root, rows, columns):
            self.root = root
            self.root.title("Memory Game")

            self.rows = rows
            self.columns = columns
            self.buttons = []
            self.first_button = None
            self.second_button = None

            self.create_board()

        def create_board(self):
            # Create a list of pairs of random numbers
            numbers = [i // 2 for i in range(self.rows * self.columns)]
            random.shuffle(numbers)
            self.board = [numbers[i:i + self.columns] for i in range(0, len(numbers), self.columns)]

            # Create buttons for each grid element
            for i in range(self.rows):
                row_buttons = []
                for j in range(self.columns):
                    button = tk.Button(self.root, text="", width=5, height=2, command=lambda i=i, j=j: self.flip(i, j))
                    button.grid(row=i, column=j)
                    row_buttons.append(button)
                self.buttons.append(row_buttons)

        def flip(self, i, j):
            # Handle button click event
            button = self.buttons[i][j]
            if button.cget("text") == "":
                # If the button is not flipped, show its value
                button.config(text=str(self.board[i][j]))

                if self.first_button is None:
                    self.first_button = (i, j)
                else:
                    self.second_button = (i, j)
                    self.check_match()

        def check_match(self):
            # Check if the two flipped buttons have the same value
            i1, j1 = self.first_button
            i2, j2 = self.second_button

            if self.board[i1][j1] == self.board[i2][j2]:
                # Change color to green for matching buttons
                self.buttons[i1][j1].config(bg="green", state=tk.DISABLED)
                self.buttons[i2][j2].config(bg="green", state=tk.DISABLED)
            else:
                # Reset the text of non-matching buttons
                self.buttons[i1][j1].config(text="")
                self.buttons[i2][j2].config(text="")

            # Reset the first and second buttons
            self.first_button = None
            self.second_button = None

            # Check if all buttons are disabled (game over)
            if all(button.cget("state") == tk.DISABLED for row in self.buttons for button in row):
                messagebox.showinfo("Game Over", "Congratulations! You've matched all pairs.")

    if __name__ == "__main__":
        root = tk.Tk()
        game = MemoryGame(root, rows=4, columns=4)
        root.mainloop()


# (.place) celander
def celendar1():
    import tkinter as tk
    from datetime import datetime

    class CalendarApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Calendar App")

            self.create_widgets()
            self.update_datetime()  # Call the update_datetime method initially

        def create_widgets(self):
            # Date and Time Display
            self.datetime_label = tk.Label(self.master, text="", font=("Helvetica", 20))
            self.datetime_label.pack(padx=20, pady=20)

        def update_datetime(self):
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.datetime_label.config(text=current_datetime)
            self.master.after(1000, self.update_datetime)  # Schedule the next update in 1000 milliseconds (1 second)

    if __name__ == "__main__":
        root = tk.Tk()
        app = CalendarApp(root)
        root.mainloop()


# excel with python
def excel_python():
    import tkinter as tk
    from tkinter import messagebox
    from openpyxl import Workbook

    class ExcelApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Excel-like App")

            self.table_data = [['' for _ in range(5)] for _ in range(5)]  # Initialize a 5x5 table data

            # Create the table
            self.create_table()

            # Create a button to save to Excel
            save_button = tk.Button(master, text="Save to Excel", command=self.save_to_excel)
            save_button.grid(row=6, column=0, columnspan=5, pady=10)

        def create_table(self):
            for i in range(5):
                for j in range(5):
                    entry = tk.Entry(self.master, width=12)
                    entry.grid(row=i, column=j)
                    entry.insert(tk.END, self.table_data[i][j])
                    entry.bind('<FocusOut>', lambda event, i=i, j=j: self.update_table_data(event, i, j))

        def update_table_data(self, event, i, j):
            widget = event.widget
            self.table_data[i][j] = widget.get()

        def save_to_excel(self):
            workbook = Workbook()
            sheet = workbook.active

            for i, row in enumerate(self.table_data, start=1):
                sheet.append(row)

            try:
                workbook.save("excel_output.xlsx")
                messagebox.showinfo("Success", "Data saved to excel_output.xlsx")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    if __name__ == "__main__":
        root = tk.Tk()
        app = ExcelApp(root)
        root.mainloop()


# nootebook
def nootebook():
    import tkinter as tk
    from tkinter import filedialog

    def print_text():
        input_text = entry.get()
        print("You entered:", input_text)

    def save_text():
        input_text = entry.get()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            with open(file_path, 'w') as file:
                file.write(input_text)
            print(f"Text saved to: {file_path}")

    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                entry.delete(0, tk.END)
                entry.insert(0, content)
            print(f"Opened file: {file_path}")

    # Create the main window
    root = tk.Tk()
    root.title("Python Tkinter Notebook")

    # Create a text widget
    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    # Create a button to print the text
    print_button = tk.Button(root, text="Print Text", command=print_text)
    print_button.pack(side=tk.LEFT, padx=5)

    # Create a button to save the text
    save_button = tk.Button(root, text="Save", command=save_text)
    save_button.pack(side=tk.LEFT, padx=5)

    # Create a button to open a file
    open_button = tk.Button(root, text="File Search", command=open_file)
    open_button.pack(side=tk.LEFT, padx=5)

    # Start the Tkinter main loop
    root.mainloop()


# spiderman kawaii
def spiderman_kawaii():
    import turtle as t

    t.speed(13)  # Painting speed control
    t.bgcolor("#990000")
    t.pensize(10)
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.circle(-120)
    t.penup()
    t.circle(-120, -60)
    t.pendown()
    t.pensize(5)
    t.right(50)
    t.circle(70, 55)
    t.right(85)
    t.circle(75, 58)
    t.right(90)
    t.circle(70, 55)
    t.right(90)
    t.circle(70, 58)

    # body
    t.penup()
    t.pensize(10)
    t.goto(80, 15)
    t.pendown()
    t.seth(92)
    t.fd(135)
    t.seth(125)
    t.circle(30, 135)
    t.seth(190)
    t.fd(50)
    t.seth(125)
    t.circle(30, 135)
    t.seth(275)
    t.fd(90)

    # Arm 1
    t.penup()
    t.pensize(10)
    t.goto(92, -150)
    t.seth(240)
    t.pendown()
    t.fd(80)
    t.left(10)
    t.circle(-28, 185)

    # Arm 2
    t.penup()
    t.goto(0, 50)
    t.seth(0)
    t.pensize(10)
    t.circle(-120, -60)
    t.seth(200)
    t.pendown()
    t.fd(72)
    t.left(20)
    t.circle(30, 150)
    t.left(20)
    t.fd(20)
    t.right(15)
    t.fd(10)
    t.pensize(5)
    t.fillcolor("#3366cc")
    t.begin_fill()
    t.seth(92)
    t.circle(-120, 31)
    t.seth(200)
    t.fd(45)
    t.left(90)
    t.fd(52)
    t.end_fill()
    t.fd(-12)
    t.right(90)
    t.fd(40)
    t.penup()
    t.right(90)
    t.fd(18)
    t.pendown()
    t.right(86)
    t.fd(40)
    t.penup()
    t.goto(-152, -86)
    t.pendown()
    t.left(40)
    t.circle(35, 90)
    # Body coloring
    t.penup()
    t.goto(-80, 116)
    t.seth(10)
    t.pensize(5)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#3366cc")
    t.fd(155)
    t.seth(-88)
    t.fd(37)
    t.seth(195)
    t.fd(156)
    t.end_fill()
    t.penup()
    t.goto(-75, 38)
    t.seth(15)
    t.pendown()
    t.begin_fill()
    t.fd(158)
    t.seth(-88)
    t.fd(55)
    t.seth(140)
    t.circle(120, 78)
    t.end_fill()
    # Arm 1 To color
    t.penup()
    t.fillcolor("#3366cc")
    t.pensize(5)
    t.goto(75, -170)
    t.pendown()
    t.begin_fill()
    t.seth(240)
    t.fd(30)
    t.right(90)
    t.fd(17)
    t.end_fill()
    t.fd(10)
    t.left(80)
    t.fd(55)
    t.penup()
    t.left(90)
    t.fd(15)
    t.pendown()
    t.left(85)
    t.fd(55)
    t.penup()
    t.goto(43, -225)
    t.left(84)
    t.pendown()
    t.circle(60, 51)
    t.speed(0)

    # Body vertical lines
    for i in range(3):
        t.penup()
        t.goto(-70 + i * 15, 135)
        t.seth(-90)
        t.pendown()
        t.pensize(5)
        t.fd(15 - 2 * i)

    for i in range(3):
        t.penup()
        t.goto(36 + i * 15, 156)
        t.seth(-90)
        t.pendown()
        t.pensize(5)
        t.fd(15 - 2 * i)
        a = -60
        b = 70

    for i in range(4):
        t.penup()
        t.goto(a, b)
        a = a + 40
        b = b + 10
        t.seth(-90)
        t.pendown()
        t.pensize(5)
        t.fd(26)

    def oo(li, jing):
        t.penup()
        t.goto(0, 50)
        t.seth(0)
        t.circle(-120, li)
        t.pendown()
        t.right(jing)
        t.pensize(5)
        oo(-60, 110)
        t.fd(130)
        oo(-28, 96)
        t.fd(140)
        oo(9, 89)
        t.fd(144)
        oo(42, 70)
        t.fd(160)
        oo(80, 60)
        t.fd(130)
        t.penup()
        t.goto(-80, -40)
        t.right(160)
        t.pendown()
        t.right(50)
        t.circle(70, 45)
        t.right(75)
        t.circle(70, 38)
        t.right(50)
        t.circle(70, 45)
        t.right(90)
        t.circle(70, 48)
        t.penup()
        t.goto(-53, -70)
        t.pendown()
        t.left(40)
        t.circle(70, 30)
        t.right(50)
        t.circle(70, 20)
        t.right(50)
        t.circle(70, 38)
        t.right(70)
        t.circle(70, 24)
        t.penup()
        t.goto(-19, -105)
        t.left(72)
        t.pendown()
        t.fd(22)
        t.right(60)
        t.fd(22)
        oo(-140, 80)
        t.circle(-90, 120)
        t.penup()
        oo(140, 100)
        t.circle(90, 13)
        t.pendown()

    t.right(-50)
    t.circle(70, 45)
    t.right(75)
    t.circle(70, 38)
    t.right(50)
    t.circle(70, 36)
    t.penup()
    t.goto(22, -185)
    t.right(70)
    t.pendown()
    t.fd(72)
    t.penup()
    t.goto(-40, -182)
    t.right(38)
    t.pendown()
    t.fd(70)
    t.speed(10)
    # The left eye
    t.penup()
    t.pensize(7)
    t.goto(-15, -110)
    t.seth(0)
    t.pendown()
    t.pensize(10)
    t.begin_fill()
    t.left(130)
    t.fd(110)
    t.right(250)
    t.circle(90, 60)
    t.circle(40, 120)
    t.fillcolor("#F5FFFA")
    t.end_fill()

    # Right eye
    t.penup()
    t.goto(5, -110)
    t.pendown()
    t.begin_fill()
    t.right(30)
    t.fd(110)
    t.right(-250)
    t.circle(-90, 60)
    t.circle(-40, 120)
    t.end_fill()
    t.done()


# spiderman art
def spider_man_art():
    from sketchpy import library as lib
    sketch = lib.tom_holland()
    sketch.draw()



# digital clock
def clock():
    import tkinter as tk
    from time import strftime

    class DigitalClock:
        def __init__(self, root):
            self.root = root
            self.root.title("Digital Clock")

            self.label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
            self.label.pack(anchor='center')

            self.update_time()

        def update_time(self):
            time_string = strftime('%H:%M:%S %p')
            self.label.config(text=time_string)
            self.root.after(1000, self.update_time)

    if __name__ == "__main__":
        root = tk.Tk()
        app = DigitalClock(root)
        root.mainloop()


# white text animation
def white_text():
    import pygame
    import sys
    import random
    import time

    pygame.init()

    # Képernyő mérete
    WIDTH, HEIGHT = 800, 600

    # Színek
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Inicializálja a betűstílust
    font = pygame.freetype.Font(None, 50)

    def render_text_3d(text, depth):
        surface, rect = font.render(text, (255, 255, 255))

        # Átméretezi a szöveget, hogy a mélység hatását létrehozza
        scaled_surface = pygame.transform.scale(surface, (surface.get_width() + depth, surface.get_height() + depth))

        return scaled_surface

    def create_heart():
        heart_size = random.randint(10, 30)
        heart_surface = pygame.Surface((heart_size, heart_size), pygame.SRCALPHA)
        pygame.draw.polygon(heart_surface, WHITE, [(heart_size // 2, 0), (0, heart_size), (heart_size, heart_size)])
        pygame.draw.circle(heart_surface, WHITE, (heart_size // 4, heart_size // 4), heart_size // 4)
        pygame.draw.circle(heart_surface, WHITE, (heart_size - heart_size // 4, heart_size // 4), heart_size // 4)
        return heart_surface

    def main():
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("3D font cool")

        clock = pygame.time.Clock()

        text_input = ""
        depth = 0

        hearts = []

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        text_input = ""
                    else:
                        text_input += event.unicode
                        hearts.append((create_heart(), time.time()))

            screen.fill(BLACK)

            # Rajzolja meg a háttérben lévő 3D hatást
            depth_surface = render_text_3d(text_input, depth)
            screen.blit(depth_surface,
                        ((WIDTH - depth_surface.get_width()) // 2, (HEIGHT - depth_surface.get_height()) // 2))

            # Rajzolja meg a fehér szíveket
            for heart, timestamp in hearts:
                elapsed_time = time.time() - timestamp
                if elapsed_time < 1:
                    heart_rect = heart.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
                    screen.blit(heart, heart_rect)

            # Frissítse a képernyőt
            pygame.display.flip()

            # Tisztítsa meg a képernyőt a fehér szívek után
            screen.fill(BLACK)

            # Állítsa be a képkocka sebességét
            clock.tick(60)

            # Növelje a mélység értékét
            depth += 1
            if depth > 50:
                depth = 0

    if __name__ == "__main__":
        main()


# heart animation
def heart_animation():
    import turtle
    import random

    def draw_heart(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("red")
        turtle.begin_fill()
        turtle.left(50)
        turtle.forward(10)
        turtle.circle(7, 200)
        turtle.right(140)
        turtle.circle(7, 200)
        turtle.forward(10)
        turtle.end_fill()
        turtle.penup()

    def draw_emoji(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        emojis = ["💐", "🍫", "😘"]
        turtle.color("black")
        turtle.write(random.choice(emojis), align="center", font=("Arial", 12, "normal"))
        turtle.penup()

    def firework():
        turtle.speed(0)
        turtle.hideturtle()
        turtle.bgcolor("black")

        for _ in range(50):
            x = random.randint(-300, 300)
            y = random.randint(-200, 200)
            draw_heart(x, y)
            draw_emoji(x, y - 20)

        turtle.done()

    firework()


# mp3 player
def mp3_player():
    import tkinter as tk
    from tkinter import filedialog
    from pygame import mixer

    class MP:
        def __init__(self, win):
            # Create Tkinter window
            win.geometry('200x200')
            win.title('Music Player')
            win.resizable(0, 0)

            # StringVar to change button text later
            self.play_restart = tk.StringVar()
            self.pause_resume = tk.StringVar()
            self.play_restart.set('Play')
            self.pause_resume.set('Pause')

            # The buttons and their positions
            load_button = Button(win, text='Load', width=10, font=('Arial', 20), command=self.load)
            load_button.place(x=100, y=40, anchor='center')

            play_button = Button(win, text="Play",textvariable=self.play_restart, width=10, font=('Arial', 20), command=self.play)
            play_button.place(x=100, y=80, anchor='center')

            pause_button = Button(win, text="Pause",textvariable=self.pause_resume, width=10, font=('Arial', 20), command=self.pause)
            pause_button.place(x=100, y=120, anchor='center')

            stop_button = Button(win, text='Stop', width=10, font=('Arial', 20), command=self.stop)
            stop_button.place(x=100, y=160, anchor='center')

            self.music_file = False
            self.playing_state = False

        def load(self):
            self.music_file = filedialog.askopenfilename()
            print("Loaded: ", self.music_file)
            self.play_restart.set('Play')

        def play(self):
            if self.music_file:
                mixer.init()
                mixer.music.load(str(self.music_file))
                mixer.music.play()
                self.playing_state = False
                self.play_restart.set('Restart')
                self.pause_resume.set('Pause')

        def pause(self):
            if not self.playing_state:
                mixer.music.pause()
                self.playing_state = True
                self.pause_resume.set('Resume')
            else:
                mixer.music.unpause()
                self.playing_state = False
                self.pause_resume.set('Pause')

        def stop(self):
            mixer.music.stop()

    root = tk.Tk()
    MP(root)
    root.mainloop()


# coordinates
def coordinatep():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    def main():
        x = float(input("X: "))
        y = float(input("Y: "))
        z = float(input("Z: "))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(x, y, z, c='r', marker='o')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

    if __name__ == "__main__":
        main()

# file manager
def file_managar():
    import os
    import shutil
    import tkinter as tk
    from tkinter import filedialog

    class FileManagerApp:
        def __init__(self, root):
            self.root = root
            self.root.title("File Manager")

            self.create_widgets()

        def create_widgets(self):
            # Buttons
            self.list_files_button = tk.Button(self.root, text="List Files", command=self.list_files)
            self.list_files_button.pack(pady=10)

            self.create_directory_button = tk.Button(self.root, text="Create Directory", command=self.create_directory)
            self.create_directory_button.pack(pady=10)

            self.delete_file_button = tk.Button(self.root, text="Delete File", command=self.delete_file)
            self.delete_file_button.pack(pady=10)

            self.move_file_button = tk.Button(self.root, text="Move File", command=self.move_file)
            self.move_file_button.pack(pady=10)

        def list_files(self):
            directory = filedialog.askdirectory(title="Select Directory")
            if directory:
                print("Files in {}: \n".format(directory))
                for filename in os.listdir(directory):
                    print(filename)

        def create_directory(self):
            directory = filedialog.askstring("Create Directory", "Enter directory name:")
            if directory:
                try:
                    os.makedirs(directory)
                    print("Directory '{}' created successfully.".format(directory))
                except FileExistsError:
                    print("Directory '{}' already exists.".format(directory))

        def delete_file(self):
            filename = filedialog.askopenfilename(title="Select File to Delete")
            if filename:
                try:
                    os.remove(filename)
                    print("File '{}' deleted successfully.".format(filename))
                except FileNotFoundError:
                    print("File '{}' not found.".format(filename))

        def move_file(self):
            src = filedialog.askopenfilename(title="Select File to Move")
            dest = filedialog.askdirectory(title="Select Destination Directory")
            if src and dest:
                try:
                    shutil.move(src, dest)
                    print("File '{}' moved to '{}'.".format(src, dest))
                except FileNotFoundError:
                    print("File '{}' not found.".format(src))

    if __name__ == "__main__":
        root = tk.Tk()
        app = FileManagerApp(root)
        root.mainloop()


# lucky game
def Luck_game():
    import random
    import tkinter as tk
    from emoji import emojize

    class LuckyGame:
        def __init__(self, master):
            self.master = master
            self.master.title("Luck game")
            self.master.geometry("400x300")

            self.points = 100
            self.bet = 0

            self.canvas = Canvas(master, width=300, height=150)
            self.canvas.pack()

            self.label_points = tk.Label(master, text=f"Points: {self.points}")
            self.label_points.pack()

            self.entry_bet = tk.Entry(master)
            self.entry_bet.pack()

            self.button_spin = Button(master, text="Spin", command=self.spin)
            self.button_spin.pack()

            self.label_result = tk.Label(master, text="")
            self.label_result.pack()

        def spin(self):
            try:
                self.bet = int(self.entry_bet.get())
            except ValueError:
                self.label_result.config(text="Type here a number to play!")
                return

            if self.bet > self.points:
                self.label_result.config(text="You dont have enough point to play!")
            else:
                self.points -= self.bet
                self.label_result.config(text="Spinning...")

                emojis = [emojize(":pear:"), emojize(":banana:"), emojize(":grapes:")]

                # Random sorrendbe helyezzük az emojikat
                random.shuffle(emojis)

                # Canvas törlése
                self.canvas.delete("all")

                # Pörgetés animáció
                for _ in range(20):
                    random.shuffle(emojis)
                    self.canvas.create_text(150, 75, text=emojis[0], font=("Arial", 24))
                    self.master.update()
                    self.master.after(50)
                    self.canvas.delete("all")

                # Végső eredmény megjelenítése
                self.canvas.create_text(150, 75, text=f"{emojis[0]} {emojis[1]} {emojis[2]}", font=("Arial", 24))

                if emojis[0] == emojis[1] == emojis[2]:
                    self.points += self.bet * 2
                    self.label_result.config(text=f"You won, we are double the points! Points: {self.points}")
                elif emojis[0] == emojis[1] or emojis[0] == emojis[2] or emojis[1] == emojis[2]:
                    self.points += self.bet
                    self.label_result.config(text=f"Two some fruit! Double: {self.points}")
                elif emojis.count(emojis[0]) == 3 and emojis[0] == emojize(":pear:"):
                    self.points += self.bet * 5
                    self.label_result.config(
                        text=f"You win some extra! congrats: {self.points}")
                else:
                    self.label_result.config(text=f"Sadly you didnt got anything Points: {self.points}")

                self.label_points.config(text=f"Points: {self.points}")

    root = tk.Tk()
    game = LuckyGame(root)
    root.mainloop()


# python code editor
def codeeditor():
    import PySimpleGUI as sg
    import code

    # Create a window layout with a text box for input, a button for execution, and a text box for output
    layout = [
        [sg.Text("Enter your Python code here:")],
        [sg.Multiline(size=(80, 20), key="-INPUT-")],
        [sg.Button("Run", bind_return_key=True)],
        [sg.Text("Output:")],
        [sg.Output(size=(80, 20), key="-OUTPUT-")]
    ]

    # Create a window object with the layout
    window = sg.Window("Python Editor", layout)

    # Create an interactive interpreter object with the global namespace
    interpreter = code.InteractiveInterpreter(globals())

    # Loop until the window is closed
    while True:
        # Read the window events and values
        event, values = window.read()
        # If the event is None, then the window is closed
        if event == sg.WINDOW_CLOSED:
            break
        # If the event is Run, then execute the input code
        elif event == "Run":
            # Get the input code from the values dictionary
            code = values["-INPUT-"]
            # Execute the code using the interpreter object
            interpreter.runsource(code)
            # Clear the input text box
            window["-INPUT-"].update("")

    # Close the window
    window.close()


# solar system
def solar_paint():
    import pygame
    import math

    pygame.init()

    WIDTH, HEIGHT = 800, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Planet Simulation")

    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (100, 149, 237)
    RED = (188, 39, 50)
    DARK_GREY = (80, 78, 81)

    FONT = pygame.font.SysFont("comicsans", 16)

    class Planet:
        AU = 149.6e6 * 1000
        G = 6.67428e-11
        SCALE = 250 / AU  # 1AU = 100 pixels
        TIMESTEP = 3600 * 24  # 1 day

        def __init__(self, x, y, radius, color, mass):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.mass = mass

            self.orbit = []
            self.sun = False
            self.distance_to_sun = 0

            self.x_vel = 0
            self.y_vel = 0

        def draw(self, win):
            x = self.x * self.SCALE + WIDTH / 2
            y = self.y * self.SCALE + HEIGHT / 2

            if len(self.orbit) > 2:
                updated_points = []
                for point in self.orbit:
                    x, y = point
                    x = x * self.SCALE + WIDTH / 2
                    y = y * self.SCALE + HEIGHT / 2
                    updated_points.append((x, y))

                pygame.draw.lines(win, self.color, False, updated_points, 2)

            pygame.draw.circle(win, self.color, (x, y), self.radius)

            if not self.sun:
                distance_text = FONT.render(f"{round(self.distance_to_sun / 1000, 1)}km", 1, WHITE)
                win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

        def attraction(self, other):
            other_x, other_y = other.x, other.y
            distance_x = other_x - self.x
            distance_y = other_y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            if other.sun:
                self.distance_to_sun = distance

            force = self.G * self.mass * other.mass / distance ** 2
            theta = math.atan2(distance_y, distance_x)
            force_x = math.cos(theta) * force
            force_y = math.sin(theta) * force
            return force_x, force_y

        def update_position(self, planets):
            total_fx = total_fy = 0
            for planet in planets:
                if self == planet:
                    continue

                fx, fy = self.attraction(planet)
                total_fx += fx
                total_fy += fy

            self.x_vel += total_fx / self.mass * self.TIMESTEP
            self.y_vel += total_fy / self.mass * self.TIMESTEP

            self.x += self.x_vel * self.TIMESTEP
            self.y += self.y_vel * self.TIMESTEP
            self.orbit.append((self.x, self.y))

    def main():
        run = True
        clock = pygame.time.Clock()

        sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
        sun.sun = True

        earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)
        earth.y_vel = 29.783 * 1000

        mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23)
        mars.y_vel = 24.077 * 1000

        mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10 ** 23)
        mercury.y_vel = -47.4 * 1000

        venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24)
        venus.y_vel = -35.02 * 1000

        planets = [sun, earth, mars, mercury, venus]

        while run:
            clock.tick(60)
            WIN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for planet in planets:
                planet.update_position(planets)
                planet.draw(WIN)

            pygame.display.update()

        pygame.quit()

    main()

# hand volume control
def hand_volume():
    import cv2
    import mediapipe as mp
    import pyautogui

    x1 = y1 = x2 = y2 = 0
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        frame_height, frame_width, success = img.shape
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        outpt = mp_hands.process(rgb_img)
        hand = outpt.multi_hand_landmarks
        if hand:
            for hands in hand:
                drawing_utils.draw_landmarks(img, hands)
                landmarks = hands.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=img, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                        x1 = x
                        y1 = y
                    if id == 4:
                        cv2.circle(img=img, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                        x2 = x
                        y2 = y
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
            cv2.line(img, (x1, y1), (x2, y2), (128, 0, 128), 5)
            if dist > 50:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

        cv2.imshow("Image", img)
        key = cv2.waitKey(10)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

# text to speech
def text_to_speech():
    import tkinter as tk
    from gtts import gTTS
    import os

    def lejatszas():
        szoveg = bevitel.get()
        nyelv = 'hu' if nyelv_valaszto.get() == 0 else 'en'
        tts = gTTS(text=szoveg, lang=nyelv, slow=False)
        tts.save("hang.mp3")
        os.system("start hang.mp3")

    def kivalasztott_nyelv(nyelv):
        nyelv_valaszto.set(nyelv)

    # Tkinter ablak létrehozása
    ablak = tk.Tk()
    ablak.title("Text to Speech")

    # Szövegbeviteli mező
    bevitel = tk.Entry(ablak, width=50)
    bevitel.pack(pady=10)

    # Nyelv választó gombok
    nyelv_valaszto = tk.IntVar()
    magyar_gomb = tk.Button(ablak, text="Hungary", command=lambda: kivalasztott_nyelv(0))
    angol_gomb = tk.Button(ablak, text="English", command=lambda: kivalasztott_nyelv(1))

    magyar_gomb.pack()
    angol_gomb.pack()

    # Lejátszás gomb
    gomb = tk.Button(ablak, text="Play", command=lejatszas)
    gomb.pack(pady=10)

    # Ablak futtatása
    ablak.mainloop()


# Olasz hangok
def italy_translate():
    import tkinter as tk
    from tkinter import messagebox
    from gtts import gTTS
    import os

    italian_to_hungarian = {
        "Hi": "ciao",
        "Good morning": "buongiorno",
        "Good evening": "buonasera",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "How are you?": "Come stai?",
        "Whats your name?": "Come ti chiami?",
        "Where are you?": "Dove sei?",
        "Where did you born?": "Di dove sei?",
        "I love you": "Ti amo",
        "Mom": "Madre",
        "Dad": "Padre",
        "Sister": "sorella",
        "Brother": "fratello",
        "How old are you?": "Quanti anni hai?",
        "Im 10 years old": "Ho dieci anni",
        # ... (you can edit it)
    }

    class ItalianLanguageApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Italy translator")

            self.label = tk.Label(root, text="Select a word:", font=("Helvetica", 16))
            self.label.pack(pady=20)

            self.word_choice = tk.StringVar(root)
            self.word_choice.set(list(italian_to_hungarian.keys())[0])
            self.word_dropdown = tk.OptionMenu(root, self.word_choice, *italian_to_hungarian.keys())
            self.word_dropdown.pack()

            self.translate_button = tk.Button(root, text="Translate", command=self.translate)
            self.translate_button.pack(pady=10)

        def translate(self):
            italian_word = self.word_choice.get()
            italian_translation = italian_to_hungarian.get(italian_word, "No translate.")

            if italian_translation != "No translate.":
                try:
                    tts = gTTS(text=italian_translation, lang="it")
                    tts.save("translation.mp3")
                    os.system("start translation.mp3")
                except Exception as e:
                    print("Error playing audio:", e)
            else:
                messagebox.showinfo("Translate", "None of them selected.")

    if __name__ == "__main__":
        app = tk.Tk()
        ItalianLanguageApp(app)
        app.mainloop()

# Számoló gép
def Calculator():
    import tkinter as tk
    import ast

    LARGE_FONT_STYLE = ("Arial", 40, "bold")
    SMALL_FONT_STYLE = ("Arial", 16)
    DIGITS_FONT_STYLE = ("Arial", 24, "bold")
    DEFAULT_FONT_STYLE = ("Arial", 20)

    OFF_WHITE = "#F8FAFF"
    WHITE = "#FFFFFF"
    LIGHT_BLUE = "#CCEDFF"
    LIGHT_GRAY = "#F5F5F5"
    LABEL_COLOR = "#25265E"

    class Calculator:
        def __init__(self):
            self.window = tk.Tk()
            self.window.geometry("375x667")
            self.window.resizable(0, 0)
            self.window.title("Calculator")

            self.total_expression = ""
            self.current_expression = ""
            self.display_frame = self.create_display_frame()

            self.total_label, self.label = self.create_display_labels()

            self.digits = {
                7: (1, 1), 8: (1, 2), 9: (1, 3),
                4: (2, 1), 5: (2, 2), 6: (2, 3),
                1: (3, 1), 2: (3, 2), 3: (3, 3),
                0: (4, 2), '.': (4, 1)
            }
            self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
            self.buttons_frame = self.create_buttons_frame()

            self.buttons_frame.rowconfigure(0, weight=1)
            for x in range(1, 5):
                self.buttons_frame.rowconfigure(x, weight=1)
                self.buttons_frame.columnconfigure(x, weight=1)
            self.create_digit_buttons()
            self.create_operator_buttons()
            self.create_special_buttons()
            self.bind_keys()

        def bind_keys(self):
            self.window.bind("<Return>", lambda event: self.evaluate())
            for key in self.digits:
                self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

            for key in self.operations:
                self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

        def create_special_buttons(self):
            self.create_clear_button()
            self.create_equals_button()
            self.create_square_button()
            self.create_sqrt_button()

        def create_display_labels(self):
            total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                                   fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
            total_label.pack(expand=True, fill='both')

            label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                             fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
            label.pack(expand=True, fill='both')

            return total_label, label

        def create_display_frame(self):
            frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
            frame.pack(expand=True, fill="both")
            return frame

        def add_to_expression(self, value):
            self.current_expression += str(value)
            self.update_label()

        def create_digit_buttons(self):
            for digit, grid_value in self.digits.items():
                button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                                   font=DIGITS_FONT_STYLE,
                                   borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
                button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

        def append_operator(self, operator):
            self.current_expression += operator
            self.total_expression += self.current_expression
            self.current_expression = ""
            self.update_total_label()
            self.update_label()

        def create_operator_buttons(self):
            i = 0
            for operator, symbol in self.operations.items():
                button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,
                                   font=DEFAULT_FONT_STYLE,
                                   borderwidth=0, command=lambda x=operator: self.append_operator(x))
                button.grid(row=i, column=4, sticky=tk.NSEW)
                i += 1

        def clear(self):
            self.current_expression = ""
            self.total_expression = ""
            self.update_label()
            self.update_total_label()

        def create_clear_button(self):
            button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=self.clear)
            button.grid(row=0, column=1, sticky=tk.NSEW)

        def square(self):
            self.current_expression = str(eval(f"{self.current_expression}**2"))
            self.update_label()

        def create_square_button(self):
            button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=self.square)
            button.grid(row=0, column=2, sticky=tk.NSEW)

        def sqrt(self):
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
            self.update_label()

        def create_sqrt_button(self):
            button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=self.sqrt)
            button.grid(row=0, column=3, sticky=tk.NSEW)

        def evaluate(self):
            self.total_expression += self.current_expression
            self.update_total_label()
            try:
                parsed_expression = ast.parse(self.total_expression, mode='eval')
                result = eval(compile(parsed_expression, filename='<string>', mode='eval'))
                if result == float('inf') or result == float('-inf'):
                    raise ZeroDivisionError
                self.current_expression = str(result)
                self.total_expression = ""
            except (SyntaxError, ZeroDivisionError) as e:
                self.current_expression = f"Error: {str(e)}"
            finally:
                self.update_label()

        def create_equals_button(self):
            button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=self.evaluate)
            button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

        def create_buttons_frame(self):
            frame = tk.Frame(self.window)
            frame.pack(expand=True, fill="both")
            return frame

        def update_total_label(self):
            expression = self.total_expression
            for operator, symbol in self.operations.items():
                expression = expression.replace(operator, f' {symbol} ')
            self.total_label.config(text=expression)

        def update_label(self):
            self.label.config(text=self.current_expression[:11])

        def run(self):
            self.window.mainloop()

    if __name__ == "__main__":
        calc = Calculator()
        calc.run()


# Data infos saver
def data_info_savers():
    import tkinter as tk
    import sqlite3
    import tkinter.ttk as ttk
    import tkinter.messagebox as tkMessageBox

    # DEVELOPED BY Mark Arvin
    root = tk.Tk()
    root.title("Contact List")
    width = 700
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    root.config(bg="#6666ff")

    # ============================VARIABLES===================================
    FIRSTNAME = tk.StringVar()
    LASTNAME = tk.StringVar()
    GENDER = tk.StringVar()
    AGE = tk.StringVar()
    ADDRESS = tk.StringVar()
    CONTACT = tk.StringVar()

    # ============================METHODS=====================================

    def Database():
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT)")
        cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def SubmitData():
        if FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
            result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
            conn = sqlite3.connect("pythontut.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO `member` (firstname, lastname, gender, age, address, contact) VALUES(?, ?, ?, ?, ?, ?)", (
                str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()),
                str(CONTACT.get())))
            conn.commit()
            cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            FIRSTNAME.set("")
            LASTNAME.set("")
            GENDER.set("")
            AGE.set("")
            ADDRESS.set("")
            CONTACT.set("")

    def UpdateData():
        if GENDER.get() == "":
            result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
            conn = sqlite3.connect("pythontut.db")
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE `member` SET `firstname` = ?, `lastname` = ?, `gender` =?, `age` = ?,  `address` = ?, `contact` = ? WHERE `mem_id` = ?",
                (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()), str(ADDRESS.get()),
                 str(CONTACT.get()), int(mem_id)))
            conn.commit()
            cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            FIRSTNAME.set("")
            LASTNAME.set("")
            GENDER.set("")
            AGE.set("")
            ADDRESS.set("")
            CONTACT.set("")

    def OnSelected(event):
        global mem_id, UpdateWindow
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        mem_id = selecteditem[0]
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")
        FIRSTNAME.set(selecteditem[1])
        LASTNAME.set(selecteditem[2])
        AGE.set(selecteditem[4])
        ADDRESS.set(selecteditem[5])
        CONTACT.set(selecteditem[6])
        UpdateWindow = tk.Toplevel()
        UpdateWindow.title("Contact List")
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width / 2) + 450) - (width / 2)
        y = ((screen_height / 2) + 20) - (height / 2)
        UpdateWindow.resizable(0, 0)
        UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        if 'NewWindow' in globals():
            NewWindow.destroy()

        # ===================FRAMES==============================
        FormTitle = tk.Frame(UpdateWindow)
        FormTitle.pack(side=tk.TOP)
        ContactForm = tk.Frame(UpdateWindow)
        ContactForm.pack(side=tk.TOP, pady=10)
        RadioGroup = tk.Frame(ContactForm)
        Male = tk.Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('arial', 14)).pack(side=tk.LEFT)
        Female = tk.Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('arial', 14)).pack(
            side=tk.LEFT)

        # ===================LABELS==============================
        lbl_title = tk.Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="orange", width=300)
        lbl_title.pack(fill=tk.X)
        lbl_firstname = tk.Label(ContactForm, text="Firstname", font=('arial', 14), bd=5)
        lbl_firstname.grid(row=0, sticky=tk.W)
        lbl_lastname = tk.Label(ContactForm, text="Lastname", font=('arial', 14), bd=5)
        lbl_lastname.grid(row=1, sticky=tk.W)
        lbl_gender = tk.Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
        lbl_gender.grid(row=2, sticky=tk.W)
        lbl_age = tk.Label(ContactForm, text="Age", font=('arial', 14), bd=5)
        lbl_age.grid(row=3, sticky=tk.W)
        lbl_address = tk.Label(ContactForm, text="Address", font=('arial', 14), bd=5)
        lbl_address.grid(row=4, sticky=tk.W)
        lbl_contact = tk.Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
        lbl_contact.grid(row=5, sticky=tk.W)

        # ===================ENTRY===============================
        firstname = tk.Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
        firstname.grid(row=0, column=1)
        lastname = tk.Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
        lastname.grid(row=1, column=1)
        RadioGroup.grid(row=2, column=1)
        age = tk.Entry(ContactForm, textvariable=AGE, font=('arial', 14))
        age.grid(row=3, column=1)
        address = tk.Entry(ContactForm, textvariable=ADDRESS, font=('arial', 14))
        address.grid(row=4, column=1)
        contact = tk.Entry(ContactForm, textvariable=CONTACT, font=('arial', 14))
        contact.grid(row=5, column=1)

        # ==================BUTTONS==============================
        btn_updatecon = Button(ContactForm, text="Update", width=50, command=UpdateData)
        btn_updatecon.grid(row=6, columnspan=2, pady=10)

    # fn1353p
    def DeleteData():
        if not tree.selection():
            result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
        else:
            result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                conn = sqlite3.connect("pythontut.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
                conn.commit()
                cursor.close()
                conn.close()

    def AddNewWindow():
        global NewWindow
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")
        NewWindow = tk.Toplevel()
        NewWindow.title("Contact List")
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width / 2) - 455) - (width / 2)
        y = ((screen_height / 2) + 20) - (height / 2)
        NewWindow.resizable(0, 0)
        NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        if 'UpdateWindow' in globals():
            UpdateWindow.destroy()

        # ===================FRAMES==============================
        FormTitle = tk.Frame(NewWindow)
        FormTitle.pack(side=tk.TOP)
        ContactForm = tk.Frame(NewWindow)
        ContactForm.pack(side=tk.TOP, pady=10)
        RadioGroup = tk.Frame(ContactForm)
        Male = tk.Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('arial', 14)).pack(side=tk.LEFT)
        Female = tk.Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('arial', 14)).pack(
            side=tk.LEFT)

        # ===================LABELS==============================
        lbl_title = tk.Label(FormTitle, text="Adding New Contacts", font=('arial', 16), bg="#66ff66", width=300)
        lbl_title.pack(fill=tk.X)
        lbl_firstname = tk.Label(ContactForm, text="Firstname", font=('arial', 14), bd=5)
        lbl_firstname.grid(row=0, sticky=tk.W)
        lbl_lastname = tk.Label(ContactForm, text="Lastname", font=('arial', 14), bd=5)
        lbl_lastname.grid(row=1, sticky=tk.W)
        lbl_gender = tk.Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
        lbl_gender.grid(row=2, sticky=tk.W)
        lbl_age = tk.Label(ContactForm, text="Age", font=('arial', 14), bd=5)
        lbl_age.grid(row=3, sticky=tk.W)
        lbl_address = tk.Label(ContactForm, text="Address", font=('arial', 14), bd=5)
        lbl_address.grid(row=4, sticky=tk.W)
        lbl_contact = tk.Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
        lbl_contact.grid(row=5, sticky=tk.W)

        # ===================ENTRY===============================
        firstname = tk.Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
        firstname.grid(row=0, column=1)
        lastname = tk.Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
        lastname.grid(row=1, column=1)
        RadioGroup.grid(row=2, column=1)
        age = tk.Entry(ContactForm, textvariable=AGE, font=('arial', 14))
        age.grid(row=3, column=1)
        address = tk.Entry(ContactForm, textvariable=ADDRESS, font=('arial', 14))
        address.grid(row=4, column=1)
        contact = tk.Entry(ContactForm, textvariable=CONTACT, font=('arial', 14))
        contact.grid(row=5, column=1)

        # ==================BUTTONS==============================
        btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData)
        btn_addcon.grid(row=6, columnspan=2, pady=10)

    # ============================FRAMES======================================
    Top = tk.Frame(root, width=500, bd=1, relief=tk.SOLID)
    Top.pack(side=tk.TOP)
    Mid = tk.Frame(root, width=500, bg="#6666ff")
    Mid.pack(side=tk.TOP)
    MidLeft = tk.Frame(Mid, width=100)
    MidLeft.pack(side=tk.LEFT, pady=10)
    MidLeftPadding = tk.Frame(Mid, width=370, bg="#6666ff")
    MidLeftPadding.pack(side=tk.LEFT)
    MidRight = tk.Frame(Mid, width=100)
    MidRight.pack(side=tk.RIGHT, pady=10)
    TableMargin = tk.Frame(root, width=500)
    TableMargin.pack(side=tk.TOP)
    # ============================LABELS======================================
    lbl_title = tk.Label(Top, text="Contact Management System", font=('arial', 16), width=500)
    lbl_title.pack(fill=tk.X)

    # ============================ENTRY=======================================

    # ============================BUTTONS=====================================
    btn_add = Button(MidLeft, text="+ ADD NEW", bg="#66ff66", command=AddNewWindow)
    btn_add.pack()
    btn_delete = Button(MidRight, text="DELETE", bg="red", command=DeleteData)
    btn_delete.pack(side=tk.RIGHT)

    # ============================TABLES======================================
    scrollbarx = tk.Scrollbar(TableMargin, orient=tk.HORIZONTAL)
    scrollbary = tk.Scrollbar(TableMargin, orient=tk.VERTICAL)
    tree = ttk.Treeview(TableMargin,
                        columns=("MemberID", "Firstname", "Lastname", "Gender", "Age", "Address", "Contact"),
                        height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
    tree.heading('MemberID', text="MemberID", anchor=tk.W)
    tree.heading('Firstname', text="Firstname", anchor=tk.W)
    tree.heading('Lastname', text="Lastname", anchor=tk.W)
    tree.heading('Gender', text="Gender", anchor=tk.W)
    tree.heading('Age', text="Age", anchor=tk.W)
    tree.heading('Address', text="Address", anchor=tk.W)
    tree.heading('Contact', text="Contact", anchor=tk.W)
    tree.column('#0', stretch=tk.NO, minwidth=0, width=0)
    tree.column('#1', stretch=tk.NO, minwidth=0, width=0)
    tree.column('#2', stretch=tk.NO, minwidth=0, width=80)
    tree.column('#3', stretch=tk.NO, minwidth=0, width=120)
    tree.column('#4', stretch=tk.NO, minwidth=0, width=90)
    tree.column('#5', stretch=tk.NO, minwidth=0, width=80)
    tree.column('#6', stretch=tk.NO, minwidth=0, width=120)
    tree.column('#7', stretch=tk.NO, minwidth=0, width=120)
    tree.pack()
    tree.bind('<Double-Button-1>', OnSelected)

    # ============================INITIALIZATION==============================
    if __name__ == '__main__':
        Database()
        root.mainloop()


# Flappy Bird játék
def flappy_bird():
    pygame.init()

    game_width = 400
    game_height = 300

    game_display = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Flappy Bird')

    clock = pygame.time.Clock()

    bird_size = 20
    bird_x = game_width / 4
    bird_y = game_height / 2

    gravity = 0.5
    jump = -10

    def game_loop():
        game_over = False
        y_speed = 0
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        y_speed = jump

            bird_y += y_speed
            y_speed += gravity

            if bird_y > game_height - bird_size:
                bird_y = game_height - bird_size
                y_speed = 0

            game_display.fill((255, 255, 255))
            pygame.draw.rect(game_display, (255, 0, 0), [bird_x, bird_y, bird_size, bird_size])
            pygame.display.update()

            clock.tick(30)

        pygame.quit()
        quit()

    game_loop()

# Timer alkalmazás
def timer_app():
    def start_timer():
        time_seconds = int(entry.get())
        countdown(time_seconds * 60)

    def countdown(seconds):
        while seconds:
            mins, secs = divmod(seconds, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            label.config(text=time_format)
            ablak.update()
            time.sleep(1)
            seconds -= 1
        label.config(text="Time's up!")

    ablak = tk.Tk()
    ablak.title("Timer App")

    label = tk.Label(ablak, text="", font=("Helvetica", 48))
    label.pack(pady=20)

    entry = tk.Entry(ablak, font=("Helvetica", 24))
    entry.pack(pady=10)

    start_button = tk.Button(ablak, text="Start Timer", command=start_timer)
    start_button.pack(pady=10)

    ablak.mainloop()

# Háttérszín változtató alkalmazás
def background_color_changer():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    def change_color():
        selected_color = color_var.get()
        ablak.configure(bg=selected_color)

    ablak = tk.Tk()
    ablak.title("Background Color Changer")

    color_var = tk.StringVar()
    color_var.set(colors[0])

    color_menu = tk.OptionMenu(ablak, color_var, *colors)
    color_menu.pack(pady=20)

    change_button = tk.Button(ablak, text="Change Color", command=change_color)
    change_button.pack(pady=10)

    ablak.mainloop()

# Betűtípus és szín változtató alkalmazás
def font_color_changer():
    fonts = ["Arial", "Times New Roman", "Courier New"]
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    def change_style():
        selected_font = font_var.get()
        selected_color = color_var.get()
        label.config(font=(selected_font, 20), fg=selected_color)

    ablak = tk.Tk()
    ablak.title("Font & Color Changer")

    font_var = tk.StringVar()
    font_var.set(fonts[0])

    color_var = tk.StringVar()
    color_var.set(colors[0])

    font_menu = tk.OptionMenu(ablak, font_var, *fonts)
    font_menu.pack(pady=10)

    color_menu = tk.OptionMenu(ablak, color_var, *colors)
    color_menu.pack(pady=10)

    change_button = tk.Button(ablak, text="Change Style", command=change_style)
    change_button.pack(pady=10)

    label = tk.Label(ablak, text="Hello, Tkinter!", font=("Arial", 20), fg="black")
    label.pack(pady=20)

    ablak.mainloop()

# Tetszőleges alkalmazás
def custom_app():
    messagebox.showinfo("Custom App", "This is a custom app of your choice!")

# Íme a telefonos alkalmazások kibővített változata:
def main():
    ablak = tk.Tk()
    ablak.title("📱 Emulált telefon alkalmazások 📱")

    snake_gomb = tk.Button(ablak, text="Snake.io", command=snake_io)
    snake_gomb.pack()

    camera_gomb = tk.Button(ablak, text="Camera App", command=camera_app)
    camera_gomb.pack()

    base64_gomb = tk.Button(ablak, text="Base64 Encoder App", command=base64_encoder)
    base64_gomb.pack()

    paint_gomb = tk.Button(ablak, text="Paint App", command=lambda:paint_app())
    paint_gomb.pack()

    file_manager_gomb = tk.Button(ablak, text="File Manager", command=lambda:file_managar())
    file_manager_gomb.pack()

    flappy_bird_gomb = tk.Button(ablak, text="Flappy Bird", command=flappy_bird)
    flappy_bird_gomb.pack()

    timer_gomb = tk.Button(ablak, text="Timer App", command=timer_app)
    timer_gomb.pack()

    bg_color_gomb = tk.Button(ablak, text="Background Color Changer", command=background_color_changer)
    bg_color_gomb.pack()

    font_color_gomb = tk.Button(ablak, text="Font & Color Changer", command=font_color_changer)
    font_color_gomb.pack()

    custom_app_gomb = tk.Button(ablak, text="Custom App", command=custom_app)
    custom_app_gomb.pack()

    ablak.mainloop()

def snake_io():
    pygame.init()

    game_width = 400
    game_height = 300

    game_display = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Snake.io')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font = pygame.font.SysFont(None, 25)

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(game_display, (0, 255, 0), [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font.render(msg, True, color)
        game_display.blit(mesg, [game_width / 6, game_height / 3])

    def game_loop():
        game_over = False
        game_close = False

        x1 = game_width / 2
        y1 = game_height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        foodx = round(np.random.randint(0, game_width - snake_block) / 10.0) * 10.0
        foody = round(np.random.randint(0, game_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                game_display.fill((255, 255, 255))
                message("You Lost! Press Q-Quit or C-Play Again", (255, 0, 0))
                our_snake(snake_block, snake_list)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= game_width or x1 < 0 or y1 >= game_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            game_display.fill((255, 255, 255))
            pygame.draw.rect(game_display, (255, 0, 0), [foodx, foody, snake_block, snake_block])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(snake_block, snake_list)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(np.random.randint(0, game_width - snake_block) / 10.0) * 10.0
                foody = round(np.random.randint(0, game_height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    game_loop()

# Kamera alkalmazás
def camera_app():
    import cv2

    def simple_camera():
        # Open the default camera (camera index 0)
        cap = cv2.VideoCapture(0)

        # Check if the camera is opened successfully
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # If the frame is read correctly, ret is True
            if not ret:
                print("Error: Couldn't read frame.")
                break

            # Display the resulting frame
            cv2.imshow('Simple Camera', frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()

    if __name__ == "__main__":
        simple_camera()


# Base64 Encoder App
def base64_encoder():
    ablak = tk.Tk()
    ablak.title("Base64 Encoder")

    def kodolas():
        szoveg = beviteli_mezo.get()
        kodolt_szoveg = base64.b64encode(szoveg.encode("utf-8")).decode("utf-8")
        kodolt_eredmeny.config(text="The base64 code: " + kodolt_szoveg)
        ablak.clipboard_clear()
        ablak.clipboard_append(kodolt_szoveg)
        ablak.update()

    beviteli_mezo = tk.Entry(ablak, width=40)
    beviteli_mezo.pack(pady=10)

    kodolo_gomb = tk.Button(ablak, text="Code & Copy", command=kodolas)
    kodolo_gomb.pack()

    kodolt_eredmeny = tk.Label(ablak, text="")
    kodolt_eredmeny.pack(pady=10)

    ablak.mainloop()

# Paint App
def paint_app():
    import tkinter as tk
    from tkinter import colorchooser, ttk

    class main:
        def __init__(self, master):
            self.master = master
            self.color_fg = 'Black'
            self.color_bg = 'white'
            self.old_x = None
            self.old_y = None
            self.pen_width = 5
            self.drawWidgets()
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)

        def paint(self, e):
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.pen_width, fill=self.color_fg,
                                   capstyle='round', smooth=True)
            self.old_x = e.x
            self.old_y = e.y

        def reset(self, e):
            self.old_x = None
            self.old_y = None

        def changedW(self, width):
            self.pen_width = width

        def clearcanvas(self):
            self.c.delete(tk.ALL)

        def change_fg(self):
            self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

        def change_bg(self):
            self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
            self.c['bg'] = self.color_bg

        def drawWidgets(self):
            self.controls = tk.Frame(self.master, padx=5, pady=5)
            textpw = tk.Label(self.controls, text='Pen Width', font='Georgia 16')
            textpw.grid(row=0, column=0)
            self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.changedW, orient='vertical')
            self.slider.set(self.pen_width)
            self.slider.grid(row=0, column=1)
            self.controls.pack(side="left")
            self.c = tk.Canvas(self.master, width=500, height=400, bg=self.color_bg)
            self.c.pack(fill=tk.BOTH, expand=True)

            menu = tk.Menu(self.master)
            self.master.config(menu=menu)
            optionmenu = tk.Menu(menu)
            menu.add_cascade(label='Menu', menu=optionmenu)
            optionmenu.add_command(label='Brush Color', command=self.change_fg)
            optionmenu.add_command(label='Background Color', command=self.change_bg)
            optionmenu.add_command(label='Clear Canvas', command=self.clearcanvas)
            optionmenu.add_command(label='Exit', command=self.master.destroy)

    win = tk.Tk()
    win.title("Paint App")
    main(win)
    win.mainloop()


def main():
    ablak = tk.Tk()
    ablak.iconbitmap('C:\\Users\\alizb\\Downloads\\favicon (2).ico')
    backro = PhotoImage(file='C:\\Users\\alizb\\Downloads\\R.png')

    my_label = tk.Label(ablak, image=backro)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    ablak.title("📱 Samsung (Hu) 📱")


    tic_tacbutton = tk.Button(ablak, text="Tic-Tac-Toe", bg="lightgreen", fg="white", command=lambda:tic_tac_tou())
    tic_tacbutton.place(x=30, y=230)

    fire_buttonwork = tk.Button(ablak, text=" 🧨Fire works🎇 ", bg="orange", fg="green", font="10", command=lambda:fireworks())
    fire_buttonwork.place(x=280, y=210)

    magic_button = tk.Button(ablak, text="Magic ball game", bg="purple", font=30, command=lambda:magic_game())
    magic_button.place(x=40, y=260)

    guessing_button = tk.Button(ablak, text="Guessing game", bg="yellow", fg="green", command=lambda:guessing_game())
    guessing_button.place(x=300, y=250)

    timer_button = tk.Button(ablak, text="Timer", bg="black", fg="blue", command=lambda:Timer())
    timer_button.place(x=40, y=300)

    translatorbuton = tk.Button(ablak, text="TRANSLATOR (REAL)", bg="black", fg="white", command=lambda:translator_app())
    translatorbuton.place(x=320, y=40)

    bank_button = tk.Button(ablak, text="Bank app", bg="red", command=lambda:bank_app())
    bank_button.place(x=80, y=120)

    todo_button = tk.Button(ablak, text="Todo app", bg="green", fg="dark green", command=lambda:todo_app())
    todo_button.place(x=110, y=150)

    weather_button = tk.Button(ablak, text="Weather", bg="yellow", fg="green", command=lambda:weather_app())
    weather_button.place(x=50, y=80)

    begginer_button = tk.Button(ablak, text="Begginer infos", fg="lime", bg="black", command=lambda:beginner_infotk())
    begginer_button.place(x=110, y=10)

    Cube_3Button = tk.Button(ablak, text="3D cube", bg="blue", fg="yellow", command=lambda:Cube_3dcoll())
    Cube_3Button.place(x=100, y=80)

    memory_button = tk.Button(ablak, text="Memory game", bg="brown", fg="orange", command=lambda:memor_game1())
    memory_button.place(x=100, y=50)

    celander_button = tk.Button(ablak, text="celander", bg="blue", fg="yellow", command=lambda:celendar1())
    celander_button.place(x=50, y=10)

    excel_button = tk.Button(ablak, text="Excel", fg="orange", bg="black", command=lambda:excel_python())
    excel_button.pack()

    noot_button = tk.Button(ablak, text="Nootebook", fg="blue", bg="cyan", command=lambda:nootebook())
    noot_button.pack()

    spider_kawaiibuton = tk.Button(ablak, text="Kawaii spiderman", fg="red", bg="dark blue", command=lambda:spiderman_kawaii())
    spider_kawaiibuton.pack()

    file_button = tk.Button(ablak, text="File manager", bg="green", fg="blue", command=lambda:file_managar())
    file_button.pack()

    spiderman_button = tk.Button(ablak, text="spider man art", bg="red", fg="dark blue", command=lambda:spider_man_art())
    spiderman_button.pack()

    clock_button = tk.Button(ablak, text="clock", bg="cyan", fg="dark blue", command=lambda:clock())
    clock_button.pack()

    white_button = tk.Button(ablak, text="White animation 🤍", bg="black", fg="white", command=lambda:white_text())
    white_button.pack()

    heart_button = tk.Button(ablak, text="heart animation 😍", bg="black", fg="red", command=lambda:heart_animation())
    heart_button.pack()

    mp3_button = tk.Button(ablak, text="mp3 player", bg="lime", command=lambda:mp3_player())
    mp3_button.pack()

    coordinate_button = tk.Button(ablak, text="coordinates", bg="yellow", command=lambda:coordinatep())
    coordinate_button.pack()

    data_button = tk.Button(ablak, text="data info saver", bg="blue", command=lambda:data_info_savers())
    data_button.pack()

    luck_button = tk.Button(ablak, text="Luck game", bg="yellow", command=lambda:Luck_game())
    luck_button.pack()

    code_buttonn = tk.Button(ablak, text="code python", bg="brown", command=lambda:codeeditor())
    code_buttonn.pack()

    solar_button = tk.Button(ablak, text="Solar system", bg="cyan", command=lambda:solar_paint())
    solar_button.pack()

    hand_button = tk.Button(ablak, text="Hand volume control", bg="yellow", command=lambda:hand_volume())
    hand_button.pack()

    speech_button = tk.Button(ablak, text="Text to speech", bg="green", command=lambda:text_to_speech())
    speech_button.pack()

    snake_gomb = tk.Button(ablak, text="Snake.io",bg="red", command=snake_io)
    snake_gomb.pack()

    camera_gomb = tk.Button(ablak, text="Camera App",bg="cyan", command=camera_app)
    camera_gomb.pack()

    base64_gomb = tk.Button(ablak, text="Base64 coder App",bg="pink", command=base64_encoder)
    base64_gomb.pack()

    paint_gomb = tk.Button(ablak, text="Paint App",bg="green", command=lambda:paint_app())
    paint_gomb.pack()

    data_saver_button = tk.Button(ablak, text="data saver",bg="orange", command=lambda:data_info_savers())
    data_saver_button.pack()

    color_settings = tk.Button(ablak, text="color settings",bg="yellow", command=lambda:font_color_changer())
    color_settings.pack()

    bg_setting = tk.Button(ablak, text = "Bg settings",bg="yellow", command=lambda:background_color_changer())
    bg_setting.pack()

    calculator = tk.Button(ablak, text = "Calculator", bg="brown", command=lambda: Calculator().run())
    calculator.pack()

    italy_button = tk.Button(ablak, text= "Italy translator", bg="yellow", command=lambda:italy_translate())
    italy_button.pack()

    ablak.geometry("500x700")

    ablak.mainloop()

if __name__ == "__main__":
    main()
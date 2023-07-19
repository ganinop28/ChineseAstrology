import tkinter as tk
def chinese_zodiac(year):
    zodiac_animals = ['Rat', 'Ox', 'Tiger', 'Cat', 'Dragon', 'Snake', 'Horse', 'Sheep','Monkey', 'Rooster', 'Dog', 'Pig', ]
    start_year = 1600  # The first year of the Chinese zodiac cycle
    offset = (year - start_year) % 12
    zodiac_year = zodiac_animals[offset]
    return zodiac_year

def refresh_answer(event=None):
    input_year = int(entry.get())
    zodiac_year = chinese_zodiac(input_year)
    answer_label.config(text=f"The Chinese zodiac year for {input_year} is the Year of the {zodiac_year}.")

# Create the main window
window = tk.Tk()
window.title("Chinese Zodiac Finder")

# Create the input label and entry field
input_label = tk.Label(window, text="Enter a year:")
input_label.pack()

entry = tk.Entry(window)
entry.pack()

# Bind the Enter key to the refresh function
entry.bind("<Return>", refresh_answer)

# Create the refresh button
refresh_button = tk.Button(window, text="Refresh", command=refresh_answer)
refresh_button.pack()

# Create the answer label
answer_label = tk.Label(window, text="The Chinese zodiac year will be displayed here.")
answer_label.pack()

# Start the application main loop
window.mainloop()
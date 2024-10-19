import tkinter as tk
from tkinter import messagebox


def calculate_bmi(weight, height, unit_system):
    """Calculate BMI based on weight and height using either metric or imperial units."""
    if unit_system == 'Metric': 
        bmi = weight / (height ** 2)
    else:  
        bmi = (weight / (height ** 2)) * 703
    return round(bmi, 2)


def calculate_protein_intake(weight, gender):
    """Calculate daily protein intake recommendation based on weight and gender."""
    if gender.lower() == 'male':
        protein_intake = weight * 1.2  
    else:
        protein_intake = weight * 1.0  
    return round(protein_intake, 2)


def calculate_calorie_intake(weight, height, age, gender, activity_level, unit_system):
    """Calculate daily calorie intake recommendation based on age, gender, and activity level."""
    if unit_system == 'Imperial':  
        weight = weight * 0.453592  
        height = height * 2.54 / 100  

    
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)

    if activity_level == 'Sedentary':
        calorie_needs = bmr * 1.2
    elif activity_level == 'Lightly Active':
        calorie_needs = bmr * 1.375
    elif activity_level == 'Moderately Active':
        calorie_needs = bmr * 1.55
    elif activity_level == 'Very Active':
        calorie_needs = bmr * 1.725
    else:  
        calorie_needs = bmr * 1.9

    return round(calorie_needs, 2)


def give_suggestions(age, gender):
    """Provide health suggestions based on age and gender."""
    if age < 18:
        return "Focus on balanced nutrition and regular physical activity."
    elif 18 <= age < 35:
        if gender.lower() == 'male':
            return "Focus on building muscle mass and cardiovascular health."
        else:
            return "Maintain a healthy body composition and hormonal balance."
    elif 35 <= age < 50:
        if gender.lower() == 'male':
            return "Maintain muscle mass and ensure adequate protein intake."
        else:
            return "Strength training and adequate calcium intake are essential."
    else:
        if gender.lower() == 'male':
            return "Focus on joint health, regular physical activity, and heart health."
        else:
            return "Bone health, joint flexibility, and nutrient-rich diet are key."


def show_results():
    try:
        age = int(entry_age.get())
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        gender = gender_var.get()
        activity_level = activity_var.get()
        unit_system = unit_var.get()

        
        bmi = calculate_bmi(weight, height, unit_system)
        protein_intake = calculate_protein_intake(weight, gender)
        calorie_intake = calculate_calorie_intake(weight, height, age, gender, activity_level, unit_system)
        suggestions = give_suggestions(age, gender)

        
        result_message = f"BMI: {bmi}\n"
        result_message += f"Recommended daily protein intake: {protein_intake} grams\n"
        result_message += f"Recommended daily calorie intake: {calorie_intake} calories\n"
        result_message += f"Health Suggestions: {suggestions}"
        messagebox.showinfo("Personal Healthcare Results", result_message)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for age, weight, and height.")

# Create the GUI window
window = tk.Tk()
window.title("Personal Healthcare Calculator")

# Labels and entries for user input
tk.Label(window, text="Age (years)").grid(row=0, column=0, padx=10, pady=5)
entry_age = tk.Entry(window)
entry_age.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Weight").grid(row=1, column=0, padx=10, pady=5)
entry_weight = tk.Entry(window)
entry_weight.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Height").grid(row=2, column=0, padx=10, pady=5)
entry_height = tk.Entry(window)
entry_height.grid(row=2, column=1, padx=10, pady=5)

# Unit system selection
tk.Label(window, text="Unit System").grid(row=3, column=0, padx=10, pady=5)
unit_var = tk.StringVar()
unit_var.set("Metric")  # Default value
tk.Radiobutton(window, text="Metric (kg, m)", variable=unit_var, value="Metric").grid(row=3, column=1, padx=10, pady=5)
tk.Radiobutton(window, text="Imperial (lbs, inches)", variable=unit_var, value="Imperial").grid(row=3, column=2, padx=10, pady=5)

# Gender selection
tk.Label(window, text="Gender").grid(row=4, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_var.set("Male")  # Default value
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").grid(row=4, column=1, padx=10, pady=5)
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").grid(row=4, column=2, padx=10, pady=5)

# Activity level selection
tk.Label(window, text="Activity Level").grid(row=5, column=0, padx=10, pady=5)
activity_var = tk.StringVar()
activity_var.set("Sedentary")  # Default value
activity_levels = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"]
activity_menu = tk.OptionMenu(window, activity_var, *activity_levels)
activity_menu.grid(row=5, column=1, padx=10, pady=5)

# Button to calculate and show results
tk.Button(window, text="Calculate", command=show_results).grid(row=6, column=1, padx=10, pady=20)

# Start the GUI event loop
window.mainloop()

def calculate_bmi(weight, height, unit='metric'):
    """
    Calculate BMI using either metric or imperial units.
    
    Parameters:
    - weight: Weight of the user (kg for metric, lb for imperial)
    - height: Height of the user (m for metric, inches for imperial)
    - unit: 'metric' for metric system, 'imperial' for imperial system
    
    Returns:
    - BMI value
    """
    if unit == 'metric':
        # BMI calculation for metric units
        bmi = weight / (height ** 2)
    elif unit == 'imperial':
        # BMI calculation for imperial units
        bmi = (weight / (height ** 2)) * 703
    else:
        raise ValueError("Invalid unit. Choose either 'metric' or 'imperial'.")
    
    return bmi

def bmi_status(bmi):
    """
    Determine the health status based on BMI.
    
    Parameters:
    - bmi: Calculated BMI value
    
    Returns:
    - A string indicating the BMI category
    """
    if bmi < 18.5:
        return "Underweight \nTip: Increase calorie intake with nutrient-dense foods like nuts, while doing strength training exercises like weightlifting or bodyweight workouts to build muscle and support healthy weight gain."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight \nGreat! Please maintain your healthy lifestyle as it should be."
    elif 25 <= bmi < 29.9:
        return "Overweight \nTip: Focus on a balanced diet rich in fruits, vegetables, lean proteins, and whole grains, with regular moderate physical activities like walking, swimming, or cycling to improve fitness."
    else:
        return "Obesity \nTip: Make a complete lifestyle shift with a portion-controlled, rich in nutrients diet, performing regular physical activity such as walking, swimming, or cycling, strength training, and stress-reduction methods like yoga or mindfulness."

def main():
    print("Welcome to the BMI Calculator!")
    unit = input("Would you like to use metric or imperial units? (metric/imperial): ").strip().lower()
    
    if unit == 'metric':
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
    elif unit == 'imperial':
        weight = float(input("Enter your weight in pounds (lb): "))
        height = float(input("Enter your height in inches (in): "))
    else:
        print("Invalid unit choice. Exiting program.")
        return
    
    # Calculate BMI
    bmi_value = calculate_bmi(weight, height, unit)
    
    # Get BMI status
    status = bmi_status(bmi_value)
    
    # Output result
    print(f"\nYour BMI is: {bmi_value:.2f}")
    print(f"Health status: {status}")

if __name__ == "__main__":
    main()

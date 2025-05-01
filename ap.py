# Fitness Guide App

# Store user data in a dictionary
user_profile = {}

def create_user_profile():
    user_profile["name"] = input("Enter your name: ")
    user_profile["age"] = int(input("Enter your age: "))
    user_profile["weight"] = float(input("Enter your weight (kg): "))
    user_profile["height"] = float(input("Enter your height (cm): "))
    user_profile["goal"] = input("Enter your fitness goal (e.g., weight loss, muscle gain): ")

    print("\nUser profile created successfully!")

def get_workout_plan(goal):
    workout_plans = {
        "weight loss": ["Jumping Jacks", "Running", "Cycling"],
        "muscle gain": ["Push-ups", "Squats", "Deadlifts"],
        "flexibility": ["Yoga", "Stretching", "Pilates"]
    }

    print(f"\nYour workout plan for {goal}:")
    if goal in workout_plans:
        for exercise in workout_plans[goal]:
            print(f"- {exercise}")
    else:
        print("Sorry, we don't have a plan for that goal.")

def track_meal():
    meals = {}
    while True:
        meal_name = input("\nEnter meal name (or 'done' to finish): ")
        if meal_name.lower() == "done":
            break
        calories = int(input(f"Enter calories for {meal_name}: "))
        meals[meal_name] = calories

    print("\nYour meals for the day:")
    total_calories = 0
    for meal, calories in meals.items():
        print(f"{meal}: {calories} calories")
        total_calories += calories
    print(f"Total calories: {total_calories}")

def track_progress():
    progress = []
    while True:
        weight_input = input("\nEnter your current weight (kg) or 'done' to finish: ")
        if weight_input.lower() == 'done':
            break
        try:
            weight = float(weight_input)
            progress.append(weight)
        except ValueError:
            print("Please enter a valid weight.")
            continue

    print("\nYour weight progress over time:")
    for i, weight in enumerate(progress, start=1):
        print(f"Day {i}: {weight} kg")

def main():
    while True:
        print("\n--- Fitness Guide App ---")
        print("1. Create User Profile")
        print("2. Get Workout Plan")
        print("3. Track Meals")
        print("4. Track Progress")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_user_profile()
        elif choice == "2":
            goal = input("Enter your fitness goal (weight loss, muscle gain, flexibility): ")
            get_workout_plan(goal)
        elif choice == "3":
            track_meal()
        elif choice == "4":
            track_progress()
        elif choice == "5":
            print("Exiting the app...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

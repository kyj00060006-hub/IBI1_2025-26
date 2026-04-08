class food_item:
    def __init__(self,name,calories,protein,carbohydrates,fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
    def __str__(self):
        return f"{self.name}:{self.calories}kcal,{self.protein}g protein,{self.carbohydrates}g carbs,{self.fat}g fat"

def track_nutrition(food_items_list):
    total_calories=0
    total_protein=0.0
    total_carbohydrates=0.0
    total_fat=0.0

    for item in food_items_list:
        total_calories+=item.calories
        total_protein+=item.protein
        total_carbohydrates+=item.carbohydrates
        total_fat+=item.fat

    print("\n--Nutrition Data Tracker--")
    print("Total consumption over 24 hours:")
    print(f"Total calories:{total_calories:.2f} kcal")
    print(f"Total protein:{total_protein:.2f} g")
    print(f"Total carbohydrates:{total_carbohydrates:.2f} g")
    print(f"Total fat:{total_fat:.2f} g")

    if total_calories>2500:
        print("Warning: Total calories exceeds 2,500 kcal!")
    if total_fat > 90:
        print("Warning: Total fat exceeds 90 g!")

# Example usage (name,calories,protein,carbohydrates,fat)
apple=food_item("Apple",60,0.3,15,0.5)
chicken_breast=food_item("Chicken Breast",165,31,0,3.6)
rice=food_item("Rice",205,4.3,45,0.4)
chocolate_bar=food_item("Chocolate Bar",230,2.5,25,12)
pizza=food_item("Pizza(slice)",300,12,35,10)
butter=food_item("Butter(2tbsp)",200,0.2,0,22)

consumed_food_today=[apple,chicken_breast,rice,chocolate_bar,pizza,butter,pizza,chocolate_bar]
track_nutrition(consumed_food_today)
# Develop a Diet Recommendation Expert System.

def diet_recommendation(age, bmi, condition):
    rules = []

    if bmi < 18.5:
        rules.append("Underweight: Include high-calorie foods like nuts, avocados, and whole grains.")
    elif 18.5 <= bmi < 25:
        rules.append("Normal BMI: Maintain a balanced diet with vegetables, fruits, proteins, and grains.")
    elif 25 <= bmi < 30:
        rules.append("Overweight: Reduce sugar and fat intake. Increase fiber and lean proteins.")
    else:
        rules.append("Obese: Consult a dietitian. Limit processed foods and increase physical activity.")

    if condition == "diabetes":
        rules.append("Diabetes: Avoid sugary foods. Prefer low-GI foods like legumes, oats, and leafy greens.")
    elif condition == "hypertension":
        rules.append("Hypertension: Reduce sodium intake. Prefer potassium-rich foods like bananas and spinach.")
    elif condition == "anemia":
        rules.append("Anemia: Increase iron-rich foods like spinach, red meat, and fortified cereals.")

    if age < 18:
        rules.append("Youth: Ensure adequate calcium and vitamin D for bone growth.")
    elif age >= 60:
        rules.append("Senior: Increase calcium, vitamin B12, and reduce saturated fats.")

    return rules

age = 45
bmi = 27.5
condition = "diabetes"

print(f"Diet Recommendations for Age={age}, BMI={bmi}, Condition={condition}:")
for recommendation in diet_recommendation(age, bmi, condition):
    print(" -", recommendation)

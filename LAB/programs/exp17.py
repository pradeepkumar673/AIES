# Develop a Medical Expert System.

disease_rules = {
    'Flu': ['fever', 'cough', 'body_ache', 'fatigue'],
    'Cold': ['runny_nose', 'sneezing', 'sore_throat', 'cough'],
    'COVID-19': ['fever', 'cough', 'loss_of_taste', 'shortness_of_breath'],
    'Malaria': ['fever', 'chills', 'sweating', 'headache'],
    'Typhoid': ['fever', 'abdominal_pain', 'weakness', 'loss_of_appetite'],
    'Dengue': ['fever', 'rash', 'joint_pain', 'bleeding'],
}

def diagnose(symptoms):
    results = []
    for disease, disease_symptoms in disease_rules.items():
        matched = set(symptoms) & set(disease_symptoms)
        score = len(matched) / len(disease_symptoms)
        if score >= 0.5:
            results.append((disease, round(score * 100, 2), list(matched)))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

patient_symptoms = ['fever', 'cough', 'fatigue', 'body_ache']

print("Medical Expert System - Diagnosis")
print("Patient Symptoms:", patient_symptoms)
print("\nPossible Diagnoses:")
diagnoses = diagnose(patient_symptoms)
if diagnoses:
    for disease, confidence, matched in diagnoses:
        print(f"  {disease}: {confidence}% match (Matched: {matched})")
else:
    print("  No matching disease found.")

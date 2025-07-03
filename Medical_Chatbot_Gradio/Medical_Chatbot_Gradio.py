import os
from openai import AzureOpenAI
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version=os.getenv("AZURE_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT")
)
deployment_name = os.getenv("DEPLOYMENT_NAME")

doctors = [
    {"name": "Dr. Mohamed Abdelsalam", "specialty": "Internal Medicine", "available": "Sunday and Tuesday"},
    {"name": "Dr. Sara Abdelalim", "specialty": "Dermatology", "available": "Saturday and Monday"},
    {"name": "Dr. Karim Samir", "specialty": "Orthopedics", "available": "Wednesday and Thursday"},
    {"name": "Dr. Fatma El-Sayed", "specialty": "Pediatrics", "available": "Daily except Friday"},
]

# Format doctors list
def recommend_doctors(diagnosis):
    diagnosis = diagnosis.lower()  # keyword matching
    recommendations = []

    if "bone" in diagnosis or "orthopedic" in diagnosis:
        recommendations.append(doctors[2])  
    elif "skin" in diagnosis or "dermatology" in diagnosis:
        recommendations.append(doctors[1]) 
    elif "stomach" in diagnosis or "cramp" in diagnosis or "abdomen" in diagnosis:
        recommendations.append(doctors[0]) 
    elif "child" in diagnosis or "infant" in diagnosis or "baby" in diagnosis:
        recommendations.append(doctors[3])
    else:
        recommendations = doctors  # Suggest all if unclear

    return "\n".join(
        [f"{doc['name']} ({doc['specialty']}) - Available: {doc['available']}" for doc in recommendations]
    )

def medical_bot(user_input):
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are an intelligent medical assistant that helps patients with basic preliminary diagnoses only. You do not offer treatment."},
                {"role": "user", "content": user_input},
            ],
            temperature=0,
            max_tokens=200
        )
        diagnosis = response.choices[0].message.content

        doctors_suggestion = recommend_doctors(diagnosis)
        return f" Preliminary Diagnosis:\n{diagnosis}\n\n Suggested Doctors:\n{doctors_suggestion}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

iface = gr.Interface(
    fn=medical_bot,
    inputs=gr.Textbox(lines=5, placeholder="Describe your medical condition..."),
    outputs="text",
    title="Smart Medical Assistant",
    description="Describe your health condition and get a preliminary diagnosis along with a suitable doctor suggestion."
)


if __name__ == "__main__":
    iface.launch()

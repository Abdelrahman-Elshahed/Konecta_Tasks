import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import chainlit as cl

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

# Recommendation logic
def recommend_doctors(diagnosis):
    diagnosis = diagnosis.lower()
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
        recommendations = doctors

    return "\n".join(
        [f"{doc['name']} ({doc['specialty']}) - Available: {doc['available']}" for doc in recommendations]
    )

# Chainlit handler for incoming messages
@cl.on_message
async def main(message: cl.Message):
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are an intelligent medical assistant that helps patients with basic preliminary diagnoses only. You do not offer treatment."},
                {"role": "user", "content": message.content},
            ],
            temperature=0,
            max_tokens=200
        )

        diagnosis = response.choices[0].message.content
        doctors_suggestion = recommend_doctors(diagnosis)

        await cl.Message(
            content=f"**Preliminary Diagnosis:**\n{diagnosis}\n\n**Suggested Doctors:**\n{doctors_suggestion}"
        ).send()

    except Exception as e:
        await cl.Message(content=f"An error occurred: {str(e)}").send()

import openai
import os

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Use existing file ID
file_id = "file-8vyXgNedfbtsGhsMZWijZu"
print(f"Using existing file ID: {file_id}")

# Start fine-tuning
fine_tune_response = openai.fine_tuning.jobs.create(
    training_file=file_id,
    model="gpt-3.5-turbo",
    hyperparameters={
        "n_epochs": 2
    }
)
print(f"Fine-tuning job started: {fine_tune_response}")
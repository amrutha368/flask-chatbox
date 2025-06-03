from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Function to generate chatbot responses
def get_chat_response(user_input):
    # Encode user input and add end-of-string token
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    
    # Generate a response from the model
    bot_output = model.generate(new_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    
    # Decode the model output to readable text
    response = tokenizer.decode(bot_output[:, new_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    return response

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Function to generate text using GPT-2
def generate_content(prompt, max_length=100, num_return_sequences=1):
    # Encode the input prompt
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text using GPT-2
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,  # Enables more randomness in the output
        temperature=0.7,  # Controls the creativity
        top_p=0.9,  # Nucleus sampling (focuses on more likely words)
        top_k=50  # Limits sampling to the top-k most likely words
    )

    # Decode the generated text
    generated_texts = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

    return generated_texts

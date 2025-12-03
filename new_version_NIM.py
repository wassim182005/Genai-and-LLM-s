import requests # For making HTTP requests

def generate_response(prompt): # Function to generate response from NVIDIA's LLM API
    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions" # NVIDIA LLM API endpoint 
    stream = False # Set to True if you want to receive the response in chunks (streaming)
    
    headers = { # HTTP headers for the request
        "Authorization": "Bearer  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", # Your NVIDIA API key
        "Accept": "text/event-stream" if stream else "application/json" # Accept header based on streaming preference
    }
    
    payload = { # Payload for the request
        "model": "meta/llama-4-maverick-17b-128e-instruct", # Model to use
        "messages": [{"role": "user", "content": prompt}],  # Your prompt here
        "max_tokens": 512, # Maximum tokens in the response
        "temperature": 0.7, # Controls randomness in the output
        "top_p": 0.9, # Controls diversity via nucleus sampling
        "frequency_penalty": 0.00, # Penalizes new tokens based on their existing frequency
        "presence_penalty": 0.00, # Penalizes new tokens based on whether they appear in the text so far
        "stream": stream
    }
    
    response = requests.post(invoke_url, headers=headers, json=payload) # Make the POST request to the API
    
    if response.status_code == 200: # Check if the request was successful
        if stream: # If streaming is enabled
            for line in response.iter_lines(): # Iterate over each line in the response
                if line: # If the line is not empty
                    print(line.decode("utf-8")) # Print the line (decoded from bytes to string)
        else: # If streaming is not enabled
            result = response.json() # Parse the JSON response  
            # Extract and return the AI's response
            return result["choices"][0]["message"]["content"] # Return the generated content
    else:
        return f"Error: {response.status_code} - {response.text}" # Return error message if request failed

# Get input from user
user_prompt = input("Enter your prompt: ") # Prompt for the AI model

# Generate and display response
print("\n" + "="*50) # chba7 text
print("Generating response...") # message 
print("="*50 + "\n") # chba7 text

response_text = generate_response(user_prompt) # Generate response from the AI model
print(response_text) # Print the generated response

#additional explenation
   
#  API = A menu at a restaurant (list of services you can order)

# Endpoint = The exact web address where you send your request to get AI responses from NVIDIA.

# NVIDIA LLM API Endpoint = The exact "phone number" to reach NVIDIA's AI kitchen

# Stream OFF = Get the whole answer at once (like receiving a complete email)

# Stream ON = Get the answer word by word (like watching someone type live)

# Headers are just the extra information that tells the server HOW to handle your request, WHO you are, and WHAT you expect back.

# remarque :
 
# No stream? → "Accept": "application/json"

# Yes stream? → "Accept": "text/event-stream"

# Payload is just the JSON "note" you're sending to NVIDIA that says:

# "Here's my question" -> "Here's how I want you to answer it" -> "Here are the rules for your response"



# Without payload: You're just calling NVIDIA and saying "Hello!"

# With payload: You're calling NVIDIA and saying "Hello! Please have AI model X answer this question with these settings..."

# Parsing = Navigating through these folders ( nvidia packet ) to find your file.

# extra : 

# requests.get(url)      # Get information
# requests.post(url)     # Send information  
# requests.put(url)      # Update information
# requests.delete(url)   # Delete information

# A database is an organized collection of structured data stored electronically, designed for efficient retrieval, management, and updating of information.
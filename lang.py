import os # For environment variable management
from langchain_nvidia_ai_endpoints import ChatNVIDIA # Import NVIDIA LLM integration

# DIRECTLY SET YOUR NVIDIA API KEY HERE
NVIDIA_API_KEY = "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"  # api key for llama 4 from nvidia

# Initialize NVIDIA LLM
llm = ChatNVIDIA(  # creating an instance of ChatNVIDIA class, which is LangChain's wrapper for interacting with NVIDIA's AI models. This object will handle all API calls to NVIDIA.
    model="meta/llama-4-maverick-17b-128e-instruct", # Specify the model to use
    temperature=0.9, # Set the creativity level of the responses
    api_key=NVIDIA_API_KEY,  # Use the key directly
    base_url="https://integrate.api.nvidia.com/v1" # The API endpoint URL where requests are sent
)

try: # Test the LLM with a sample prompt
    response = llm.invoke("Suggest me a skill that is in demand?") # Invoke the model with a prompt
    print(response.content) # Accesses the actual text answer from the AI response
except Exception as e: # Handle any errors that occur during the API call
    print(f"Error: {e}") # printi wch 7abit
    
    
   # llm.invoke(...): Calls the AI model with your question
   
   # response =: Stores the AI's answer in a variable called response
    
   # extar  :
   
   # Explanation: Controls creativity vs consistency:

   # 0.0: Very deterministic, same input → same output
   
   # 0.5: Balanced creativity

   # 0.9: High creativity, more varied responses

   #1.0+: Maximum randomness (can get nonsensical)  
   
   # resume :  langchain A framework that orchestrates chains of LLM calls with context persistence, tool integration, and retrieval from custom data sources.
   
   #    LangChain facilitates tasks and handles I/O for different LLMs by:

   # Standardizing how you interact with any LLM (OpenAI, Anthropic, NVIDIA, local models)

   # Managing the flow between LLMs, tools, memory, and data sources

   # Abstracting the complexity so you focus on what the AI should do, not how to connect it
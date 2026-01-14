# src/inference.py
import torch
from unsloth import FastLanguageModel

# --- CONFIGURATION ---
# 1. Match the Base Model used in your paper (DeepSeek) or the one in your code (Llama-3)
# based on your paper, it should be DeepSeek-R1-Distill-Qwen-7B
BASE_MODEL_NAME = "unsloth/DeepSeek-R1-Distill-Qwen-7B" 
ADAPTER_PATH = "https://huggingface.co/ptaninja/TRM-Ace-Adapter" # Path to your 'trm_ace_adapter' folder
MAX_SEQ_LENGTH = 2048

def load_agent():
    """
    Loads the TRM-Ace Agent: Base Model + Your Custom LoRA Adapter
    """
    print(f"[*] Loading Base Model: {BASE_MODEL_NAME}...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = BASE_MODEL_NAME,
        max_seq_length = MAX_SEQ_LENGTH,
        dtype = None,
        load_in_4bit = True,
    )

    print(f"[*] Injecting TRM-Ace Adapters from {ADAPTER_PATH}...")
    model.load_adapter(ADAPTER_PATH)
    
    # Enable native 2x faster inference
    FastLanguageModel.for_inference(model)
    
    return model, tokenizer

def generate_thought(model, tokenizer, instruction, context=""):
    """
    Executes the 'Generator' role: Takes an instruction and produces a reasoned response.
    """
    # The Prompt Template from your training code
    alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
"""
    
    inputs = tokenizer(
        [alpaca_prompt.format(instruction, context)], 
        return_tensors = "pt"
    ).to("cuda")

    outputs = model.generate(
        **inputs, 
        max_new_tokens = 512, # Allow room for "Chain of Thought" reasoning
        use_cache = True
    )
    
    # Decode and remove the prompt from the output
    response = tokenizer.batch_decode(outputs)[0]
    return response.split("### Response:")[-1].strip()

if __name__ == "__main__":
    # This block only runs if you execute 'python inference.py' directly
    agent_model, agent_tokenizer = load_agent()
    
    print("\n--- TRM-Ace Agent Active (Type 'exit' to quit) ---")
    while True:
        user_task = input("\n[?] Enter Task (e.g., 'Analyze this buffer overflow'): ")
        if user_task.lower() == 'exit': break
        
        user_context = input("[?] Enter Context (e.g., 'NX is disabled'): ")
        
        print("\n[!] Generator is Thinking...")
        result = generate_thought(agent_model, agent_tokenizer, user_task, user_context)
        
        print("\n--- AGENT RESPONSE ---")
        print(result)
        print("----------------------")

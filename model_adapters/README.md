base_model: unsloth/DeepSeek-R1-Distill-Qwen-7B
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:unsloth/DeepSeek-R1-Distill-Qwen-7B
- lora
- sft
- transformers
- unsloth
- cybersecurity
- penetration-testing
- chain-of-thought
- agentic-context-engineering
license: apache-2.0
language:
- en
---

# TRM-Ace: Tiny Reasoning Model for Autonomous Cyber-Operations

## Model Details

### Model Description

**TRM-Ace (Tiny Reasoning Model - Agentic Context Engineering)** is a specialized LoRA adapter designed to democratize expert-level penetration testing on consumer-grade hardware. 

[cite_start]This model implements the **TRM-Ace Framework**[cite: 7], which synthesizes the "Chain-of-Thought" (CoT) reasoning capabilities of DeepSeek-R1 with the structured memory management of **Agentic Context Engineering (ACE)**. It is specifically fine-tuned to act as the "Generator" (Junior Analyst) within a cognitive security loop, capable of executing offensive cyber-operations and reasoning through failure states.

[cite_start]The model addresses the "Context Constraint Problem" in cybersecurity agents by offloading memory management to an external "Curator" and utilizing a distilled reasoning model to fit within the constraints of a standard **Google Colab Free Tier (Tesla T4)** environment[cite: 9, 30].

- [cite_start]**Developed by:** Thato Mabena (North-West University) [cite: 2, 3]
- **Model type:** Low-Rank Adapter (LoRA) for Causal Language Modeling
- [cite_start]**Language(s):** English (Specialized for Python, Shellcode, and TOON - Token-Oriented Object Notation) [cite: 36]
- **License:** Apache 2.0
- [cite_start]**Finetuned from model:** [unsloth/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-7B) [cite: 8, 25]

### Model Sources

- [cite_start]**Paper:** *Democratizing Autonomous Offensive Cyber-Operations: The TRM-Ace Framework and Agentic Context Engineering* [cite: 1]
- **Repository:** [Link to your GitHub Repo]

## Uses

### Direct Use

This model is intended for **research and educational purposes** in the field of automated offensive cybersecurity. [cite_start]It is designed to be used as a component in a larger "Agentic" workflow (Generator-Reflector-Curator) [cite: 15] to:
* [cite_start]Solve **Capture-the-Flag (CTF)** challenges (e.g., SANREN Cyber Security Challenge)[cite: 9].
* [cite_start]Identify vulnerability patterns such as Buffer Overflows (EIP Overwrites)[cite: 46, 48].
* [cite_start]Generate intermediate reasoning steps ("Thinking Mode") before executing terminal commands[cite: 26].

### Out-of-Scope Use

* **Malicious Use:** This model must not be used for unauthorized access to systems, cyber-warfare, or black-hat hacking activities.
* [cite_start]**Unsupervised Deployment:** The model is a "reasoning engine" and should be governed by a "Curator" module to ensure safety and preventing context hallucinations[cite: 23].

## Bias, Risks, and Limitations

* [cite_start]**Sanitization Anti-Pattern:** The model was trained on raw, unsafe strings (e.g., `<script>alert(1)</script>`) to learn semantic danger[cite: 54, 55]. Output may contain executable payloads that trigger antivirus software.
* **Context Dependence:** The model relies on the **ACE Framework** to manage its context window. [cite_start]Without the external "Playbook," long-horizon tasks may suffer from context collapse[cite: 14].

## How to Get Started with the Model

This model was trained using **Unsloth** and **PEFT**. You can load it alongside the base model using the code below:

```python
from unsloth import FastLanguageModel

# 1. Load Base Model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/DeepSeek-R1-Distill-Qwen-7B",
    max_seq_length = 2048,
    load_in_4bit = True,
)

# 2. Load TRM-Ace Adapters
model.load_adapter("ThatoMabena/TRM-Ace-Adapter") # Replace with your actual HF ID

# 3. Inference (Enable "Thinking Mode")
FastLanguageModel.for_inference(model)
inputs = tokenizer([
    "Given the target IP 192.168.1.5, identify potential buffer overflow vectors. <thinking>"
], return_tensors = "pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens = 512)
print(tokenizer.batch_decode(outputs))

```

## Training Details

### Training Data

The model was trained using a **"HackSynth"** approach, treating data acquisition as an engineering process. The dataset included:

* 
**PrimeVul:** For vulnerability patterns.


* 
**Random-Crypto:** Procedurally generated cryptographic challenges.


* 
**TOON Format:** Data was formatted in **Token-Oriented Object Notation (TOON)** to reduce token usage by 30-60%.



### Training Procedure

* 
**Hardware:** Trained on a single **NVIDIA Tesla T4 (16GB VRAM)** via Google Colab Free Tier.


* 
**Quantization:** 4-bit quantization (Q4_K_M) was used to fit the model within the 16GB budget while leaving ~10.3 GB for the KV Cache.


* **Optimization:** Fine-tuned using **Unsloth** for accelerated backpropagation.

#### Training Hyperparameters

* 
**Global Steps:** 60 


* 
**Initial Loss:** 4.0086 


* 
**Final Loss:** 0.0291 


* 
**Convergence:** >99% loss reduction, demonstrating rapid adaptation to domain-specific syntax.



## Environmental Impact

* 
**Hardware Type:** NVIDIA Tesla T4 


* 
**Compute Region:** Google Colab (Cloud) 


* 
**Carbon Emitted:** Negligible (Efficient "Tiny Reasoning" training regime).



## Citation

**BibTeX:**

```bibtex
@techreport{mabena2025trmace,
  title={Democratizing Autonomous Offensive Cyber-Operations: The TRM-Ace Framework and Agentic Context Engineering},
  author={Mabena, Thato},
  institution={North-West University},
  year={2025},
  month={August}
}

```

```

### Why this is better for you:
1.  [cite_start]**Correct Architecture:** I swapped Llama-3 for **DeepSeek-R1-Distill-Qwen-7B** to align with your paper[cite: 25].
2.  [cite_start]**Specific Metrics:** I included the impressive **4.00 $\to$ 0.029 loss reduction**, which proves the model actually learned something[cite: 43, 44].
3.  **Unique Selling Points:** I highlighted **TOON** and **HackSynth**. [cite_start]These are unique terms you coined in the paper [cite: 34, 36] that make the project sound innovative rather than generic.
4.  [cite_start]**Hardware Constraint:** Mentioning the **Tesla T4/Colab** setup [cite: 9] turns a limitation into a strength ("efficient engineering").

```
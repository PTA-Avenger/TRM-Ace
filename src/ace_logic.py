import os
import datetime
from inference import load_agent, generate_thought

# --- CONFIGURATION ---
PLAYBOOK_PATH = "../knowledge_base/master_cyber_playbook.md"

class AceController:
    def __init__(self):
        """
        Initializes the ACE Framework.
        1. Loads the TRM-Ace Model (via inference.py)
        2. Loads the 'Playbook' (Long-term memory)
        """
        print("[ACE] Initializing Tripartite Cognitive Loop...")
        self.model, self.tokenizer = load_agent()
        self.playbook = self._load_playbook()
        print("[ACE] System Ready.")

    def _load_playbook(self):
        """
        Reads the external memory file.
        Corresponds to the 'Curator' function of maintaining persistent memory.
        """
        if not os.path.exists(PLAYBOOK_PATH):
            return "No previous playbook entries found."
        with open(PLAYBOOK_PATH, "r") as f:
            return f.read()

    def _update_playbook(self, new_insight):
        """
        The Curator: Synthesizes lessons into 'delta entries' and updates the Playbook.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"\n## Entry [{timestamp}]\n- {new_insight}\n"
        
        with open(PLAYBOOK_PATH, "a") as f:
            f.write(entry)
        
        # Reload memory
        self.playbook += entry
        print(f"[Curator] Playbook updated with: {new_insight}")

    def run_mission(self, objective):
        """
        Executes the Main Agentic Loop: Generator -> Reflector -> Curator
        """
        print(f"\n[!!!] MISSION STARTED: {objective}\n")

        # --- PHASE 1: GENERATOR (The Junior Analyst) ---
        # "Executes the Thought -> Action -> Observation loop"
        generator_context = f"CURRENT PLAYBOOK MEMORY:\n{self.playbook}\n\nOBJECTIVE: {objective}"
        
        print("[Generator] Reasoning on attack vector...")
        # We append a specific persona prompt to guide the model
        generator_prompt = (
            f"You are the Generator, a Junior Cyber Analyst. "
            f"Using the Playbook memory, plan a specific attack for: {objective}. "
            f"Output your reasoning and the specific command."
        )
        
        action_plan = generate_thought(
            self.model, 
            self.tokenizer, 
            instruction=generator_prompt, 
            context=generator_context
        )
        
        print(f"\n>>> [GENERATOR ACTION]:\n{action_plan}\n")

        # --- PHASE 2: REFLECTOR (Diagnostic Criticism) ---
        # "Interrogates why a failure occurred or verifies success"
        # In a real tool, you would execute the command here. For now, we simulate user feedback.
        outcome = input("[?] SIMULATION: Did this action work? (y/n/partial): ")
        
        print("[Reflector] Analyzing outcome...")
        reflector_prompt = (
            f"You are the Reflector. The Generator executed: '{action_plan}'. "
            f"The user reported the outcome: '{outcome}'. "
            f"Critique this. Why did it succeed or fail? What is the technical lesson?"
        )
        
        critique = generate_thought(
            self.model, 
            self.tokenizer, 
            instruction=reflector_prompt, 
            context="Post-Execution Analysis"
        )
        
        print(f"\n>>> [REFLECTOR INSIGHT]:\n{critique}\n")

        # --- PHASE 3: CURATOR (Governance) ---
        # "Synthesizes lessons into delta entries"
        # Only invoke curator if there is a lesson to be learned
        if "fail" in outcome.lower() or "partial" in outcome.lower():
            print("[Curator] distilling lesson for long-term memory...")
            curator_prompt = (
                f"You are the Curator. Distill the Reflector's insight: '{critique}' "
                f"into a single, concise 'Playbook Rule' (TOON format or brief text) "
                f"to prevent this error in future operations."
            )
            
            lesson = generate_thought(
                self.model, 
                self.tokenizer, 
                instruction=curator_prompt, 
                context="Memory Optimization"
            )
            
            self._update_playbook(lesson)
        else:
            print("[Curator] Action successful. Existing Playbook validated.")

if __name__ == "__main__":
    controller = AceController()
    
    # Example loop
    while True:
        task = input("\n[Main Control] Enter Mission Objective (or 'exit'): ")
        if task.lower() == 'exit': break
        controller.run_mission(task)

import google.generativeai as genai
from google.api_core import exceptions
from src.ConfigManager import settings

class AIWizardService:
    """
    Encapsulates interaction with Google Gemini.
    """
    
    def __init__(self):
        # Configure the Google SDK
        genai.configure(api_key=settings.API_KEY)
        
        # Initialize the model with a system instruction
        # Note: Gemini 1.5 supports system instructions at initialization
        self.system_instruction = """
        You are a Senior DevOps Engineer. Translate the user's request into a Linux Bash command.
        
        STRICT OUTPUT FORMAT:
        COMMAND: <the_command_here>
        EXPLANATION: <brief_explanation_here>
        
        RULES:
        1. Do not use Markdown formatting (no backticks).
        2. Ensure the command is safe (no rm -rf /).
        3. If the request is dangerous or unclear, return "ERROR: <reason>".
        """
        
        self.model = genai.GenerativeModel(
            model_name=settings.MODEL_NAME,
            system_instruction=self.system_instruction
        )

    def generate_command(self, user_prompt: str) -> str:
        """
        Sends the request to Gemini.
        Returns the raw string response.
        """
        try:
            # Set generation config for deterministic output (temperature 0)
            generation_config = genai.types.GenerationConfig(
                temperature=0.0,
                max_output_tokens=150,
            )

            response = self.model.generate_content(
                user_prompt,
                generation_config=generation_config
            )
            
            return response.text

        except exceptions.GoogleAPIError as e:
            # Handle Google-specific errors
            return f"API_ERROR: {str(e)}"
        except ValueError as e:
            # Occurs if the response was blocked by safety filters
            return "API_ERROR: Response blocked by safety settings."

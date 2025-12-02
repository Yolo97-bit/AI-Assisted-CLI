from typing import Dict, Optional
from src.Logger import logger

class CommandParser:
    """
    Pure business logic. 
    This class has NO dependency on OpenAI. It just processes text.
    This makes it very easy to write Unit Tests for.
    """

    @staticmethod
    def parse_response(raw_text: str) -> Optional[Dict[str, str]]:
        """
        Parses the AI's raw text into a structured dictionary.
        Expected format:
            COMMAND: ls -la
            EXPLANATION: Lists files
        """
        if "API_ERROR" in raw_text:
            logger.error(f"API Error received: {raw_text}")
            return None

        if "COMMAND:" not in raw_text or "EXPLANATION:" not in raw_text:
            logger.error("AI response did not match the expected format.")
            logger.error(f"Raw Output: {raw_text}")
            return None

        try:
            # Split by the known delimiter
            parts = raw_text.split("EXPLANATION:")
            
            command = parts[0].replace("COMMAND:", "").strip()
            explanation = parts[1].strip()

            return {
                "command": command,
                "explanation": explanation
            }
        except Exception as e:
            logger.error(f"Parsing Error: {e}")
            return None

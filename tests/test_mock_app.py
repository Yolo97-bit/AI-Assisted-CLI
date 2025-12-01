import sys
import unittest
from unittest.mock import patch, MagicMock

import os
# Set dummy API key to bypass ConfigManager check
os.environ["GOOGLE_API_KEY"] = "dummy_key"

# Ensure src is in path
sys.path.append(".")

from src.Main import main

class TestApp(unittest.TestCase):
    @patch('src.Main.AIWizardService')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_flow(self, mock_print, mock_input, MockAIWizardService):
        # Setup Mock AI Service
        mock_service_instance = MockAIWizardService.return_value
        mock_service_instance.generate_command.return_value = "COMMAND: echo 'Hello World'\nEXPLANATION: Prints hello world"

        # Setup Mock User Input
        # 1. Task description
        # 2. Confirm save (y)
        # 3. Exit
        mock_input.side_effect = ["print hello world", "y", "exit"]

        # Run Main
        try:
            main()
        except SystemExit:
            pass

        # Verify AI was called
        mock_service_instance.generate_command.assert_called_with("print hello world")

        # Verify Output
        # Check if "COMMAND: echo 'Hello World'" was printed (partially)
        found_command = False
        for call in mock_print.call_args_list:
            args, _ = call
            if args and "echo 'Hello World'" in str(args[0]):
                found_command = True
                break
        
        self.assertTrue(found_command, "The generated command was not printed to the console.")
        print("\n✅ Test Passed: Application logic verified with mocked AI service.")

if __name__ == '__main__':
    unittest.main()

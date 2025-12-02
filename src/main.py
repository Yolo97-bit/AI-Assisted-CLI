import sys
import os
from colorama import init, Fore, Style

# Import our modular classes
from src.AiServiceLayer import AIWizardService
from src.BusinessLogicParser import CommandParser
from src.Logger import logger

# Initialize colorama for colored terminal output
init(autoreset=True)

def save_script(command: str, explanation: str, filename="wizard_script.sh"):
    """Utility to save the command to a file."""
    try:
        with open(filename, "w") as f:
            f.write("#!/bin/bash\n")
            f.write(f"# Explanation: {explanation}\n")
            f.write(f"\n{command}\n")
        
        # Make executable (Linux/Mac only)
        if os.name != 'nt':
            os.chmod(filename, 0o755)
            
        print(f"\n{Fore.GREEN}✅ Saved to {filename}")
        print(f"{Fore.GREEN}👉 Run it with: ./wizard_script.sh")
        logger.info(f"Script saved to {filename}")
    except IOError as e:
        logger.error(f"File Write Error: {e}")
        print(f"{Fore.RED}❌ File Write Error: {e}")

def main():
    logger.info("Application started")
    print(f"{Fore.CYAN}{Style.BRIGHT}🧙‍♂️ Welcome to the Enterprise Linux Wizard")
    print(f"{Fore.CYAN}-------------------------------------------")

    # Initialize Service
    try:
        ai_service = AIWizardService()
    except Exception as e:
        logger.critical(f"Failed to initialize AI Service: {e}")
        print(f"{Fore.RED}Critical Error: Failed to initialize AI Service. Check logs for details.")
        sys.exit(1)

    while True:
        try:
            user_input = input(f"\n{Fore.YELLOW}📝 Describe your task (or 'exit'): {Style.RESET_ALL}")
            
            if user_input.lower() in ['exit', 'quit']:
                print(f"{Fore.CYAN}👋 Goodbye!")
                logger.info("Application shutdown requested by user")
                break

            print(f"{Style.DIM}🔮 Consulting the AI Model...", end="\r")

            # 1. Get Raw Data
            raw_response = ai_service.generate_command(user_input)

            # 2. Parse Data
            result = CommandParser.parse_response(raw_response)

            if result:
                print(" " * 30, end="\r") # Clear the "Thinking" line
                print(f"\n{Fore.BLUE}💻 COMMAND:     {Style.RESET_ALL}{result['command']}")
                print(f"{Fore.BLUE}📖 EXPLANATION: {Style.RESET_ALL}{result['explanation']}")

                # 3. User Confirmation
                confirm = input(f"\n{Fore.MAGENTA}💾 Save and Create Script? (y/n): {Style.RESET_ALL}")
                if confirm.lower() == 'y':
                    save_script(result['command'], result['explanation'])
            else:
                # Parser failed (error already logged in Parser)
                print(f"\n{Fore.RED}❌ Could not generate a valid command. Please try again.")

        except KeyboardInterrupt:
            print(f"\n{Fore.CYAN}👋 Goodbye!")
            logger.info("Application interrupted by user")
            break
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {e}")
            print(f"\n{Fore.RED}❌ An unexpected error occurred. Check logs.")

if __name__ == "__main__":
    main()

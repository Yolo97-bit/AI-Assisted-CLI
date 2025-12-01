# AI-Assisted CLI Wizard

An intelligent command-line interface tool that translates natural language requests into safe, executable Linux/Bash commands using Google's Gemini AI.

## Features

- **Natural Language Processing**: Translates plain English requests into shell commands.
- **Safety Mechanisms**: Prioritizes safe operations and avoids destructive commands.
- **Command Explanation**: Provides detailed explanations for every generated command.
- **Script Generation**: Allows saving commands as executable shell scripts.
- **Modular Architecture**: Clean separation of concerns between business logic, AI integration, and configuration.

## Prerequisites

- Python 3.8 or higher
- Google Cloud API Key for Gemini

## Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Yolo97-bit/ai-assisted-cli.git
    cd ai-assisted-cli
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**
    Create a `.env` file in the root directory with the following content:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    GEMINI_MODEL=gemini-2.5-flash-lite
    ```

## Usage

Run the application using the Python launcher (Windows) or standard python command:

```bash
# Windows
py -m src.Main

# Mac/Linux
python3 -m src.Main
```

### Example

```text
Welcome to the Enterprise Linux Wizard
-------------------------------------------

Describe your task (or 'exit'): list all files showing hidden ones
Consulting the AI Model...

COMMAND:     ls -la
EXPLANATION: Lists all files including hidden ones with detailed information.

Save and Create Script? (y/n): y

Saved to wizard_script.sh
Run it with: ./wizard_script.sh
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


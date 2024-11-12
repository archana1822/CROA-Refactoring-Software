# CRAO: Code Refactoring Analysis and Optimization Tool
[![License: GNU](https://img.shields.io/badge/License-GNU-green.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://www.python.org/)

CRAO (Code Refactoring Analysis and Optimization) is an open-source software tool designed to enhance software project quality through automated code restructuring and optimization. The tool analyzes source code snippets, identifies code smells, and performs automatic refactoring to improve code quality without altering external functionality.

## Features
- Automated code smell detection
- Code structure analysis and optimization
- Real-time code quality assessment
- Support for Python code snippets
- Interactive web interface using Streamlit
- Code complexity reduction
- Automated refactoring suggestions

## User Interface Demo

### Initial Interface
![WhatsApp Image 2024-11-12 at 13 06 17_9042dfb3](https://github.com/user-attachments/assets/33517c53-a7ba-4ea5-8b98-06cfead181ab)


The tool provides a clean, user-friendly interface where developers can input their Python code for analysis. The interface includes:
- A clear title and description
- A spacious code input area
- An "Analyze Code" button for triggering the analysis

### Code Analysis Example 1: Complex Function
![WhatsApp Image 2024-11-12 at 13 08 08_7d0fa265](https://github.com/user-attachments/assets/18786ac0-ed9a-48f5-81d7-bdf15cedd8c6)

In this example, the tool analyzes a function with multiple parameters and nested conditions:
- Identifies long parameter list (8 parameters)
- Suggests parameter reduction
- Provides an optimized version with improved structure
- Highlights potential code smells

### Code Analysis Example 2: Simple Functions
![WhatsApp Image 2024-11-12 at 13 10 37_a0884e6b](https://github.com/user-attachments/assets/4128d3fc-c987-490f-80c0-e8c0c240f194)

The tool can also analyze simpler code structures:
- Multiple small functions analyzed together
- Proper formatting and naming conventions checked
- Clear docstring presence verification
- No significant code smells detected in this case

## Installation

1. Clone the repository:
```bash
git clone https://github.com/archana1822/CROA-Refactoring-Software.git
cd CROA-Refactoring-Software
```
2. Code folder:
```bash
cd code
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the local address shown in the terminal (typically http://localhost:8501)

3. Enter your Python code in the text area and click "Analyze Code" to receive refactoring suggestions and optimizations.

## Example

Input code with code smell:
```python
def calculate_total(a, b, c, d, e, f, g, h):
    result = 0
    for i in range(len(a)):
        if a[i] > 0:
            if b[i] > 0:
                if c[i] > 0:
                    result += a[i] + b[i] + c[i]
    return result
```

Output after optimization:
```python
def calculate_total(a, b, c, *args):
    result = 0
    for i in range(len(a)):
        if all(x[i] > 0 for x in [a, b, c]):
            result += sum([a[i], b[i], c[i]])
    return result
```

## Architecture

CRAO follows a three-phase architecture:

1. **Source Code Analysis**: Parses input code into Abstract Syntax Tree (AST)
2. **Code Smell Detection**: Identifies code quality issues and their categories
3. **Refactoring Prediction**: Generates optimized code based on detected issues

## Requirements

- Python 3.7+
- streamlit
- ast
- astor

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.

## Authors

- Archana Patnaik - GIET University
- Neelamadhab Padhy - GIET University
- Lov Kumar - NIT Kurukshetra
- P Ankit Krishna - GIET University
- Rasmita Panigrahi - GIET University

## Citation

If you use CRAO in your research, please cite:

```bibtex
@article{patnaik2024crao,
  title={CRAO: An Open-Source Software for Code Refactoring Analysis and Optimization},
  author={Patnaik, Archana and Padhy, Neelamadhab and Kumar, Lov and Krishna, P Ankit and Panigrahi, Rasmita},
  year={2024}
}
```

## Support

For questions and support, please contact: archanapatnaik@giet.edu

## Links

- [GitHub Repository](https://github.com/archana1822/CROA-Refactoring-Software)
- [HuggingFace Space](https://huggingface.co/spaces/AnkitKrishna/Code-Refactoring-Analysis-and-Optimization-Tool)

## Acknowledgments

We thank the open-source community and all contributors who have helped in developing and improving CRAO.

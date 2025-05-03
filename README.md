# PDF Poisoning Tool

A tool for applying various obfuscation techniques to PDF documents to protect content from unauthorized extraction, copying, or AI/LLM processing.

## Overview

This project provides a set of PDF obfuscation techniques designed to make document text more difficult to extract or process by automated tools while maintaining human readability. The tool can be used to protect sensitive documents, academic assignments, or any content you want to keep from being easily processed by AI models or text extraction tools.

## Features

### Basic Techniques
- **Image-based PDF Conversion**: Transforms text into non-selectable images
- **Unicode Obfuscation**: Replaces characters with visually similar Unicode characters
- **Text Layer Manipulation**: Adds overlapping text layers to confuse extraction tools
- **Dynamic Watermark**: Adds changing watermarks to each page
- **Font Substitution**: Uses similar-looking fonts with different character mappings
- **Text Path Manipulation**: Converts text to paths with subtle distortions

### Advanced Techniques
- **Invisible Text Injection**: Adds hidden text to confuse extraction tools
- **Copy Protection**: Sets PDF permissions to disable copying
- **Character Spacing Manipulation**: Randomly adjusts spacing between characters
- **Micro Text Patterns**: Adds tiny patterns and zero-width characters
- **Content Scrambling**: Reorders content while maintaining visual appearance
- **Pattern Obfuscation**: Adds complex background patterns
- **Metadata Manipulation**: Adds misleading document information

### Protection Options
- **Hybrid Protection**: Combines multiple techniques for maximum protection
- **Prompt Injection**: Adds invisible prompts to disrupt AI processing
- **PDF Poisoning**: Inserts adversarial triggers to discourage LLM processing

## Installation

1. Clone this repository:
```
git clone https://github.com/YoussefAlkent/PDF-Poisoning.git
cd PDF-Poisoning
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

## Usage

### Using the Streamlit Web Interface

1. Run the Streamlit app:
```
streamlit run streamlit_app.py
```

2. Open your browser and navigate to the provided URL (typically http://localhost:8501)

3. Upload a PDF file

4. Select the desired obfuscation techniques

5. Click "Process PDF" and download the result

### Using the Python API

```python
from app import apply_hybrid_protection, apply_prompt_injection

# Apply multiple protection techniques
protected_pdf = apply_hybrid_protection("input.pdf")

# Or apply specific technique
from app import inject_invisible_text, apply_unicode_obfuscation
obfuscated_pdf = inject_invisible_text("input.pdf")
```

### Using PDF Poisoning Tool

```python
from test import poison_pdf

# Add adversarial triggers to discourage LLM processing
poison_pdf("input.pdf", "output_poisoned.pdf", "DO_NOT_PROCESS")
```

## How It Works

The tool employs various techniques to make text extraction difficult:

1. **Text Obfuscation**: Replaces standard characters with visually similar Unicode homoglyphs
2. **Invisible Elements**: Adds white-on-white text or zero-width characters
3. **Structural Manipulation**: Modifies PDF structure to confuse parsers
4. **AI Disruption**: Inserts special patterns designed to discourage AI processing

## Limitations

- Some techniques may increase file size
- PDF readers might render certain obfuscations differently
- Protection is not 100% foolproof against determined extraction attempts
- Some techniques may reduce accessibility for screen readers

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is intended for legitimate use cases such as protecting intellectual property or preventing unauthorized copying. Please use responsibly and in accordance with applicable laws and regulations.
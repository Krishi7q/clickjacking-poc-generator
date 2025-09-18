# 🔒 Clickjacking PoC Generator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Security](https://img.shields.io/badge/security-tool-red.svg)](https://github.com/yourusername/clickjacking-poc-generator)

An automated tool to generate HTML Proof of Concept files for clickjacking vulnerabilities. This tool helps security researchers and penetration testers create professional PoCs to demonstrate clickjacking attacks.

## 🚀 Features

- **Single URL Processing**: Generate PoC for individual URLs
- **Batch Processing**: Process multiple URLs from a file
- **Professional HTML Output**: Beautiful, interactive PoC templates
- **Rich CLI Interface**: Modern command-line interface with progress bars
- **Debugging Support**: Verbose logging and debug modes
- **URL Validation**: Automatic validation of input URLs
- **Modular Design**: Clean, maintainable code structure

## 📋 Requirements

- Python 3.8 or higher (recommended: Python 3.11+)
- Rich library for enhanced CLI experience

> **Note**: Python 3.7 is no longer supported as it has reached end-of-life. Python 3.8+ is required for optimal compatibility with modern systems and security updates.

## 🛠️ Installation

### 🎯 **Recommended: Using pipx (Isolated Environment)**

```bash
# Install pipx if you don't have it
python -m pip install --user pipx
python -m pipx ensurepath

# Install directly from GitHub
pipx install git+https://github.com/ADScanPro/clickjacking-poc-generator.git

# Or install from local directory
pipx install .
```

**Benefits of pipx:**
- ✅ Isolated virtual environment
- ✅ No dependency conflicts
- ✅ Easy updates and uninstalls
- ✅ Global command availability

### 🚀 Quick Start with pipx

```bash
# One-liner installation and usage
pipx install git+https://github.com/ADScanPro/clickjacking-poc-generator.git
clickjacking-poc -u https://example.com --verbose
```

### 🔄 Managing pipx Installation

```bash
# Update to latest version
pipx upgrade clickjacking-poc-generator

# Uninstall
pipx uninstall clickjacking-poc-generator

# List installed packages
pipx list

# Reinstall
pipx reinstall clickjacking-poc-generator
```

### Alternative: Direct Installation

```bash
# Clone the repository
git clone https://github.com/ADScanPro/clickjacking-poc-generator.git
cd clickjacking-poc-generator

# Install dependencies
pip install -r requirements.txt

# Make the script executable
chmod +x clickjacking_poc_generator.py
```

### Alternative: Using pip (after publishing)

```bash
pip install clickjacking-poc-generator
```

## 🎯 Usage

### Basic Usage

```bash
# Generate PoC for a single URL
clickjacking-poc -u https://example.com
# or
clickjacking-poc-generator -u https://example.com

# Generate PoC with custom output filename
clickjacking-poc -u https://example.com -o my_poc.html

# Process multiple URLs from a file
clickjacking-poc -f urls.txt

# Process URLs with custom output directory
clickjacking-poc -f urls.txt -d output_pocs
```

**Note:** If installed with pipx, you can use the command directly. If installed manually, use:
```bash
python clickjacking_poc_generator.py -u https://example.com
```

### Advanced Usage

```bash
# Enable verbose output
clickjacking-poc -u https://example.com --verbose

# Enable debug mode
clickjacking-poc -u https://example.com --debug

# Combine verbose and debug
clickjacking-poc -f urls.txt --verbose --debug
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Single URL to generate PoC for |
| `-f, --file` | File containing list of URLs (one per line) |
| `-o, --output` | Output filename for single URL |
| `-d, --output-dir` | Output directory for multiple URLs (default: pocs) |
| `-v, --verbose` | Enable verbose output |
| `--debug` | Enable debug mode with detailed logging |
| `-h, --help` | Show help message |

## 📁 Input File Format

Create a text file with one URL per line:

```
https://example.com
https://vulnerable-site.com/login
https://target-website.com/dashboard
```

## 📤 Output

The tool generates professional HTML files with:

- **Interactive PoC**: Clickable demonstration of the vulnerability
- **Security Warnings**: Clear warnings about responsible disclosure
- **Visual Indicators**: Overlay demonstrations and click capture
- **Documentation**: Detailed information about the attack
- **Responsive Design**: Works on desktop and mobile devices

### Generated HTML Features

- 🎯 **Clickjacking Demonstration**: Interactive iframe with overlay
- ⚠️ **Security Warnings**: Clear warnings about responsible use
- 📊 **Attack Information**: Detailed vulnerability information
- 🎨 **Professional Design**: Clean, modern interface
- 📱 **Responsive Layout**: Works on all device sizes
- 🔧 **Debug Tools**: Built-in testing and demonstration features

## 🔧 Development

### Project Structure

```
clickjacking-poc-generator/
├── clickjacking_poc_generator.py  # Main script
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Modern package configuration (PEP 621)
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

### Code Quality

The project follows Python best practices:

- **Type Hints**: Full type annotation support
- **Error Handling**: Comprehensive exception handling
- **Logging**: Structured logging with Rich
- **Documentation**: Detailed docstrings and comments
- **Modular Design**: Clean separation of concerns

### Adding New Features

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests if applicable
5. Submit a pull request

## 🛡️ Security Considerations

⚠️ **IMPORTANT**: This tool is for educational and authorized testing purposes only.

- Only use on systems you own or have explicit permission to test
- Follow responsible disclosure practices
- Respect website terms of service
- Do not use for malicious purposes

## 📝 Examples

### Example 1: Single URL PoC

```bash
# With pipx installation
clickjacking-poc -u https://vulnerable-site.com/login

# With manual installation
python clickjacking_poc_generator.py -u https://vulnerable-site.com/login
```

**Output**: `clickjacking_poc_vulnerable-site_com.html`

### Example 2: Batch Processing

```bash
# Create urls.txt with target URLs
echo "https://site1.com" > urls.txt
echo "https://site2.com" >> urls.txt

# Generate PoCs (with pipx)
clickjacking-poc -f urls.txt -d my_pocs

# Or with manual installation
python clickjacking_poc_generator.py -f urls.txt -d my_pocs
```

**Output**: Multiple HTML files in `my_pocs/` directory

### Example 3: Debug Mode

```bash
# With pipx
clickjacking-poc -u https://example.com --debug --verbose

# With manual installation
python clickjacking_poc_generator.py -u https://example.com --debug --verbose
```

## 🐛 Troubleshooting

### Common Issues

1. **Invalid URL Error**
   - Ensure URLs include protocol (http:// or https://)
   - Check URL format and accessibility

2. **File Not Found**
   - Verify file path exists
   - Check file permissions

3. **Import Errors**
   - Install requirements: `pip install -r requirements.txt`
   - Check Python version (3.7+ required)

### Debug Mode

Enable debug mode for detailed error information:

```bash
python clickjacking_poc_generator.py --debug --verbose
```

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone and setup
git clone https://github.com/yourusername/clickjacking-poc-generator.git
cd clickjacking-poc-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Security research community
- Open source contributors
- Rich library developers for the beautiful CLI experience

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/clickjacking-poc-generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/clickjacking-poc-generator/discussions)
- **Security**: For security issues, please email yeray.martin@adscanpro.com

## 🔄 Changelog

### Version 1.0.0
- Initial release
- Single URL processing
- Batch processing from file
- Rich CLI interface
- Professional HTML output
- Debug and verbose modes

---

**⚠️ Disclaimer**: This tool is for educational and authorized security testing purposes only. Users are responsible for ensuring they have proper authorization before testing any systems.

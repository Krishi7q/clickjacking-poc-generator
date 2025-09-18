#!/bin/bash
# Script to initialize Git repository for Clickjacking PoC Generator

echo "🚀 Initializing Git repository for Clickjacking PoC Generator..."

# Initialize git repository
git init

# Add all files
git add .

# Initial commit
git commit -m "Initial commit: Clickjacking PoC Generator MVP

- Add main script with CLI interface
- Add requirements.txt and pyproject.toml (PEP 621)
- Add comprehensive README.md
- Add .gitignore and LICENSE
- Add example URLs file
- Support single URL and batch processing
- Rich CLI interface with progress bars
- Professional HTML PoC templates
- Debug and verbose modes"

echo "✅ Git repository initialized successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Add remote origin: git remote add origin <your-repo-url>"
echo "3. Push to GitHub: git push -u origin main"
echo ""
echo "🔧 To test the tool:"
echo "python3 clickjacking_poc_generator.py -u https://example.com --verbose"
echo "python3 clickjacking_poc_generator.py -f example_urls.txt --verbose"

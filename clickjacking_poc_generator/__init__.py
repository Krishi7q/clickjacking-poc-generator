#!/usr/bin/env python3
"""
Clickjacking PoC Generator
Automated tool to generate HTML Proof of Concept files for clickjacking vulnerabilities.
"""

import argparse
import sys
import os
import re
from pathlib import Path
from typing import List, Optional
from urllib.parse import urlparse
import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.table import Table

# Configure logging
def setup_logging(debug: bool = False, verbose: bool = False) -> logging.Logger:
    """Setup logging configuration with rich handler."""
    level = logging.DEBUG if debug else (logging.INFO if verbose else logging.WARNING)
    
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )
    
    return logging.getLogger("clickjacking_poc")

logger = setup_logging()

class ClickjackingPoCGenerator:
    """Main class for generating clickjacking PoCs."""
    
    def __init__(self, debug: bool = False, verbose: bool = False):
        self.debug = debug
        self.verbose = verbose
        self.console = Console()
        self.logger = setup_logging(debug, verbose)
        
    def validate_url(self, url: str) -> bool:
        """Validate if the provided string is a valid URL."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception as e:
            if self.debug:
                self.logger.debug(f"URL validation error: {e}")
            return False
    
    def read_urls_from_file(self, file_path: str) -> List[str]:
        """Read URLs from a text file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip()]
            
            # Filter valid URLs
            valid_urls = [url for url in urls if self.validate_url(url)]
            
            if self.verbose:
                self.logger.info(f"Loaded {len(valid_urls)} valid URLs from {file_path}")
                if len(valid_urls) != len(urls):
                    self.logger.warning(f"Filtered out {len(urls) - len(valid_urls)} invalid URLs")
            
            return valid_urls
            
        except FileNotFoundError:
            self.logger.error(f"File not found: {file_path}")
            return []
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return []
    
    def generate_html_poc(self, target_url: str, output_file: Optional[str] = None) -> str:
        """Generate HTML PoC for clickjacking attack."""
        
        # Extract domain for naming
        domain = urlparse(target_url).netloc.replace('.', '_')
        
        if not output_file:
            output_file = f"clickjacking_poc_{domain}.html"
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickjacking PoC - {target_url}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 8px;
        }}
        
        .warning {{
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            color: #856404;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        
        .instructions {{
            background-color: #d1ecf1;
            border: 1px solid #bee5eb;
            color: #0c5460;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        
        .iframe-container {{
            position: relative;
            width: 100%;
            height: 600px;
            border: 2px solid #007bff;
            border-radius: 8px;
            overflow: hidden;
            margin: 20px 0;
        }}
        
        .overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 123, 255, 0.1);
            z-index: 10;
            pointer-events: none;
        }}
        
        .target-iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
        
        .info-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        
        .info-table th, .info-table td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        
        .info-table th {{
            background-color: #f8f9fa;
            font-weight: bold;
        }}
        
        .btn {{
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 5px;
        }}
        
        .btn:hover {{
            background-color: #0056b3;
        }}
        
        .btn-danger {{
            background-color: #dc3545;
        }}
        
        .btn-danger:hover {{
            background-color: #c82333;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔒 Clickjacking Vulnerability PoC</h1>
            <p>Proof of Concept for Clickjacking Attack</p>
        </div>
        
        <div class="warning">
            <strong>⚠️ WARNING:</strong> This is a security testing tool. Only use on systems you own or have explicit permission to test.
        </div>
        
        <div class="instructions">
            <h3>📋 Instructions:</h3>
            <ol>
                <li>This page demonstrates a clickjacking vulnerability</li>
                <li>The target website is loaded in an iframe below</li>
                <li>An invisible overlay covers the iframe to capture clicks</li>
                <li>Click anywhere on the iframe area to see the attack in action</li>
                <li>This PoC shows how an attacker could trick users into clicking unintended elements</li>
            </ol>
        </div>
        
        <div class="iframe-container">
            <div class="overlay" onclick="handleClick(event)"></div>
            <iframe 
                class="target-iframe" 
                src="{target_url}"
                sandbox="allow-scripts allow-same-origin allow-forms allow-popups"
                loading="lazy">
            </iframe>
        </div>
        
        <table class="info-table">
            <tr>
                <th>Target URL</th>
                <td>{target_url}</td>
            </tr>
            <tr>
                <th>Attack Type</th>
                <td>Clickjacking (UI Redressing)</td>
            </tr>
            <tr>
                <th>Generated</th>
                <td id="timestamp"></td>
            </tr>
        </table>
        
        <div style="text-align: center; margin-top: 20px;">
            <button class="btn" onclick="toggleOverlay()">Toggle Overlay Visibility</button>
            <button class="btn btn-danger" onclick="showAlert()">Test Click Capture</button>
        </div>
    </div>
    
    <script>
        function handleClick(event) {{
            event.preventDefault();
            alert('🚨 Clickjacking Attack Detected!\\n\\nA malicious site could capture this click and redirect it to perform unintended actions on the target website.');
        }}
        
        function toggleOverlay() {{
            const overlay = document.querySelector('.overlay');
            overlay.style.display = overlay.style.display === 'none' ? 'block' : 'none';
        }}
        
        function showAlert() {{
            alert('This demonstrates how an attacker could capture user clicks and perform actions on behalf of the user without their knowledge.');
        }}
        
        // Set timestamp
        document.getElementById('timestamp').textContent = new Date().toLocaleString();
        
        // Log for debugging
        console.log('Clickjacking PoC loaded for:', '{target_url}');
    </script>
</body>
</html>"""
        
        return html_content
    
    def save_poc(self, html_content: str, output_file: str) -> bool:
        """Save the HTML PoC to a file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            if self.verbose:
                self.logger.info(f"PoC saved to: {output_file}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving PoC to {output_file}: {e}")
            return False
    
    def generate_pocs(self, urls: List[str], output_dir: str = "pocs") -> List[str]:
        """Generate PoCs for a list of URLs."""
        
        # Create output directory
        Path(output_dir).mkdir(exist_ok=True)
        
        generated_files = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            
            task = progress.add_task("Generating PoCs...", total=len(urls))
            
            for i, url in enumerate(urls):
                try:
                    # Generate domain-based filename
                    domain = urlparse(url).netloc.replace('.', '_')
                    output_file = os.path.join(output_dir, f"clickjacking_poc_{domain}_{i+1}.html")
                    
                    # Generate HTML content
                    html_content = self.generate_html_poc(url, output_file)
                    
                    # Save file
                    if self.save_poc(html_content, output_file):
                        generated_files.append(output_file)
                        if self.verbose:
                            self.logger.info(f"Generated PoC for: {url}")
                    
                    progress.update(task, advance=1)
                    
                except Exception as e:
                    self.logger.error(f"Error generating PoC for {url}: {e}")
                    progress.update(task, advance=1)
                    continue
        
        return generated_files

def main():
    """Main function to handle CLI arguments and execute the tool."""
    parser = argparse.ArgumentParser(
        description="Clickjacking PoC Generator - Automated tool to generate HTML Proof of Concept files for clickjacking vulnerabilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -u https://example.com
  %(prog)s -f urls.txt
  %(prog)s -u https://example.com -o custom_poc.html
  %(prog)s -f urls.txt -d output_pocs --verbose --debug
        """
    )
    
    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-u', '--url', 
                           help='Single URL to generate PoC for')
    input_group.add_argument('-f', '--file', 
                           help='File containing list of URLs (one per line)')
    
    # Output options
    parser.add_argument('-o', '--output', 
                       help='Output filename for single URL (default: auto-generated)')
    parser.add_argument('-d', '--output-dir', 
                       default='pocs',
                       help='Output directory for multiple URLs (default: pocs)')
    
    # Debug and verbose options
    parser.add_argument('--verbose', '-v', 
                       action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--debug', 
                       action='store_true',
                       help='Enable debug mode with detailed logging')
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = ClickjackingPoCGenerator(debug=args.debug, verbose=args.verbose)
    console = Console()
    
    # Display header
    console.print(Panel.fit(
        "[bold blue]Clickjacking PoC Generator[/bold blue]\n"
        "Automated tool for generating HTML Proof of Concept files",
        border_style="blue"
    ))
    
    try:
        urls = []
        
        # Handle single URL
        if args.url:
            if not generator.validate_url(args.url):
                console.print(f"[red]Error: Invalid URL format: {args.url}[/red]")
                sys.exit(1)
            urls = [args.url]
            
            # Generate single PoC
            html_content = generator.generate_html_poc(args.url, args.output)
            output_file = args.output or f"clickjacking_poc_{urlparse(args.url).netloc.replace('.', '_')}.html"
            
            if generator.save_poc(html_content, output_file):
                console.print(f"[green]✓ PoC generated successfully: {output_file}[/green]")
            else:
                console.print("[red]✗ Failed to generate PoC[/red]")
                sys.exit(1)
        
        # Handle file with URLs
        elif args.file:
            urls = generator.read_urls_from_file(args.file)
            
            if not urls:
                console.print("[red]✗ No valid URLs found in file[/red]")
                sys.exit(1)
            
            # Generate multiple PoCs
            generated_files = generator.generate_pocs(urls, args.output_dir)
            
            if generated_files:
                console.print(f"[green]✓ Generated {len(generated_files)} PoC files in '{args.output_dir}' directory[/green]")
                
                # Display summary table
                table = Table(title="Generated PoC Files")
                table.add_column("File", style="cyan")
                table.add_column("URL", style="magenta")
                
                for i, file_path in enumerate(generated_files):
                    table.add_row(file_path, urls[i] if i < len(urls) else "N/A")
                
                console.print(table)
            else:
                console.print("[red]✗ Failed to generate any PoCs[/red]")
                sys.exit(1)
    
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        if args.debug:
            console.print_exception()
        sys.exit(1)

if __name__ == "__main__":
    main()

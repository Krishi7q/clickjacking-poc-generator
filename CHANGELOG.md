# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of Clickjacking PoC Generator
- Support for single URL and batch processing
- Rich CLI interface with progress bars
- Professional HTML PoC templates
- Debug and verbose modes
- Modern pyproject.toml configuration (PEP 621)
- Comprehensive documentation
- CI/CD pipeline with GitHub Actions
- Pre-commit hooks configuration
- Security scanning with Bandit and Safety

### Changed
- Migrated from setup.py to pyproject.toml for modern Python packaging

### Security
- Added security warnings in generated PoCs
- Implemented responsible disclosure guidelines
- Added input validation and URL sanitization

## [1.0.0] - 2025-01-18

### Added
- Initial MVP release
- Core functionality for generating clickjacking PoCs
- CLI interface with argument parsing
- HTML template generation
- URL validation
- Batch processing from file
- Rich console output
- Debug and verbose logging
- Professional documentation
- MIT License
- Git repository structure
- CI/CD pipeline
- Pre-commit hooks
- Security scanning

### Technical Details
- Python 3.7+ support
- Rich library for enhanced CLI experience
- Modern packaging with pyproject.toml
- Comprehensive error handling
- Type hints throughout codebase
- Modular design with clean separation of concerns

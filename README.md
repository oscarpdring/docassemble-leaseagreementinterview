# Lease Agreement Generator
A DocAssemble interview that generates customizable lease agreements with optional riders.

## Features
- Dynamic rent schedule calculation (annual increase or custom)
- Conditional document generation
- Number-to-words conversion
- Multiple guarantor support
- Automatic date and financial calculations

## Required Dependencies
- num2words
- docassemble.base.util

## Documents Generated
1. Base Lease Agreement (required)
2. Good Guy Guarantee (required)
3. Optional Documents:
  - 111 NCP Lease
  - Food & Beverage Use
  - Broker Agreement

## Input Fields
- Lease terms and dates
- Entity information
- Financial details
- Property specifics
- Broker details (if applicable)
- Special conditions

## Usage
1. Fill out interview questions
2. Review generated documents
3. If approved, download documents
4. If changes needed, select "No" to restart

## File Structure
- Main interview file
- Document templates (.docx)
- Helper functions for formatting and calculations

## Version
1.0

## License
[Your License Here]
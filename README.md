# PenTest Command Center

A comprehensive penetration testing toolkit with AI assistance for security professionals.

## Features

PenTest Command Center combines powerful tools and AI assistance for effective penetration testing:

- **Document Analysis:** Extract intelligence from documentation and scope details
- **OSINT:** Gather intelligence using Harvester and Shodan
- **Network Scanning:** Discover and map network topology
- **Vulnerability Scanning:** Identify security flaws with Nuclei
- **Exploitation:** Utilize Metasploit and other exploit tools
- **Password Cracking:** Integrated tools (Hashcat, John the Ripper, Hydra)
- **Persistence:** Establish and manage persistent access
- **Web Shells:** Generate and manage web shells in multiple languages
- **System Backdoors:** Implement various backdoor mechanisms
- **Terminal:** Direct command execution
- **Target Management:** Organize and track assessment targets
- **Team Management:** Manage team members, assign roles, and track activity
- **AI Assistant:** Get guidance and automate various tasks
- **LLM Pen Testing:** Test and evaluate AI systems for vulnerabilities
- **Reporting:** Generate comprehensive security reports

## Installation

### Prerequisites

- Python 3.8+
- Nmap
- Metasploit Framework (optional, for exploit capabilities)
- Hashcat (optional, for password cracking)
- John the Ripper (optional, for password cracking)
- Hydra (optional, for brute force attacks)
- Nuclei (optional, for vulnerability scanning)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pentest-command-center.git
   cd pentest-command-center
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the settings in `pentest_command_center/config/settings.py`

5. Run the application:
   ```bash
   python pentest_command_center/app.py
   ```

If you encounter the error "Cannot find empty port", you can specify an alternative port:
```bash
GRADIO_SERVER_PORT=7861 python pentest_command_center/app.py
```

## Usage Guide

### Document Analysis
Upload reconnaissance documents to extract intelligence. Supported formats include PDFs, images, and text files.

### OSINT
Use TheHarvester for email/domain harvesting and Shodan for discovering internet-facing assets.

### Network Scanning
Run various scan types:
- **Ping:** Fast host discovery
- **Quick:** Basic port scanning
- **Full:** Comprehensive service enumeration
- **Vuln:** Basic vulnerability detection

### Vulnerability Scanning
Use Nuclei templates to identify security flaws across your attack surface.

### Exploitation
Search and execute Metasploit modules against vulnerable targets.

### Password Cracking
- **Hashcat:** Powerful GPU-accelerated password recovery
- **John the Ripper:** Versatile password cracking
- **Hydra:** Network service brute forcing

### Web Shells
Generate web shells in multiple languages (PHP, ASP, ASPX, JSP, etc.) with various capabilities.

### Team Management
Coordinate your penetration testing team:
- **Add Members:** Create profiles with role, skills, and access level information
- **Edit Members:** Update member details and permissions as needed
- **Remove Members:** Safely remove team members when they leave projects
- **View Activity:** Track and monitor team activities with detailed logs
- **Manage Skills:** Track team capabilities with skill tagging system
- **Access Controls:** Set appropriate permissions with granular access levels

### AI Assistant
Get guidance on:
- Tool selection and usage
- Vulnerability analysis
- Exploitation techniques
- Report generation

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```
   OSError: Cannot find empty port in range: 7860-7860
   ```
   Solution: Specify an alternative port:
   ```bash
   GRADIO_SERVER_PORT=7861 python pentest_command_center/app.py
   ```

2. **Missing Dependencies**
   If you encounter errors about missing components or modules, ensure all requirements are installed:
   ```bash
   pip install -r requirements.txt
   ```

3. **Gradio Component Errors**
   The application requires Gradio 3.35.0+. If you encounter errors with components like:
   ```
   AttributeError: module 'gradio' has no attribute 'Box'
   ```
   Update Gradio:
   ```bash
   pip install --upgrade gradio
   ```

4. **System Monitor Errors**
   If you see errors related to the system monitor, ensure the DATA_DIR path in settings.py exists and is writable.

## Development

### Adding New Features

The application follows a modular design:
- Core modules in `/pentest_command_center/modules/`
- UI components in `/pentest_command_center/app.py`
- Utilities in `/pentest_command_center/utils/`
- AI capabilities in `/pentest_command_center/ai/`

When adding features:
1. Implement core functionality in appropriate module files
2. Add UI components in app.py using Gradio components
3. Connect UI to backend functionality using event handlers
4. Document additions in comments and this README

## Security Note

This tool is intended for authorized security testing only. Always ensure you have explicit permission before testing any systems, and adhere to responsible disclosure principles.

## License

[MIT License](LICENSE) 
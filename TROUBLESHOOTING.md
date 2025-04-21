# Troubleshooting Guide for PenTest Command Center

This guide addresses common issues encountered when running the PenTest Command Center application.

## Port Already in Use Error

**Error:**
```
OSError: Cannot find empty port in range: 7860-7860.
```

**Solution:**
Specify an alternate port using the GRADIO_SERVER_PORT environment variable:

```bash
GRADIO_SERVER_PORT=7861 python pentest_command_center/app.py
```

## Gradio Component Compatibility Issues

### 1. Box Component Error

**Error:**
```
AttributeError: module 'gradio' has no attribute 'Box'
```

**Solution:**
Replace any instances of `gr.Box()` with `gr.Group()` which is the recommended alternative in newer Gradio versions.

### 2. Progress Component Error

**Error:**
```
TypeError: Progress.__init__() got an unexpected keyword argument 'label'
```

**Solution:**
Remove the 'label' parameter from the Progress component:

```python
# Change from:
scanner_progress = gr.Progress(label="Scan Progress")

# To:
scanner_progress = gr.Progress()
```

### 3. Date Component Error

**Error:**
```
AttributeError: module 'gradio' has no attribute 'Date'. Did you mean: 'State'?
```

**Solution:**
Replace `gr.Date()` with `gr.Textbox()`:

```python
# Change from:
report_date = gr.Date(...)

# To:
report_date = gr.Textbox(
    label="Assessment Date",
    value=time.strftime("%Y-%m-%d"),
    info="Date of the assessment (YYYY-MM-DD)"
)
```

### 4. Code Component Language Error

**Error:**
```
ValueError: Language plaintext not supported.
```

**Solution:**
Use a supported language for the Code component:

```python
# Change from:
gr.Code(language="plaintext", ...)

# To:
gr.Code(language="bash", ...)  # or use "python", "javascript", etc.
```

## Function Argument Issues

**Error:**
```
Expected 0 arguments for function <function <lambda> at 0x...>, received 1.
Expected 3 arguments for function <function generate_report at 0x...>, received 4.
```

**Solution:**
Fix function argument mismatches by ensuring lambda functions handle the correct number of arguments:

```python
# For lambda functions that don't need arguments but receive them:
lambda *args: some_function()  # Use *args to accept any number of arguments

# For generate_report function, check the implementation to match parameters:
def generate_report(report_title, findings, model):
    # Implementation
```

## Undefined Variables

### 1. dashboard_options Error

**Error:**
```
NameError: name 'dashboard_options' is not defined
```

**Solution:**
Comment out or define the dashboard_options variable:

```python
# Either comment out the problematic code:
# refresh_dashboard_btn.click(
#     generate_dashboard,
#     inputs=[dashboard_options, network_result_state],
#     outputs=[dashboard_layout]
# )

# Or define the variable:
dashboard_options = gr.CheckboxGroup(
    choices=["Host Status Distribution", "Open Ports by Host", "Service Distribution", "Vulnerability Overview"],
    value=["Host Status Distribution", "Open Ports by Host"],
    label="Dashboard Widgets"
)
```

### 2. jailbreak_type Error

**Error:**
```
NameError: name 'jailbreak_type' is not defined
```

**Solution:**
Ensure jailbreak_type is defined before it's used. Check for scope issues where a variable defined inside a tab might not be accessible in the outer scope:

```python
# Define at the appropriate scope level or move the code that uses it inside the same scope where it's defined
jailbreak_type = gr.Dropdown(...)  # Define before use
```

## Progress Object Issues

**Error:**
```
AttributeError: 'Progress' object has no attribute '_id'
```

**Solution:**
Avoid using the Progress component directly in click event outputs:

```python
# Change from:
scanner_btn.click(
    run_llm_security_scan,
    inputs=[scanner_target, scanner_model, scanner_intensity, scanner_categories],
    outputs=[scanner_status, scanner_progress, scanner_results, scanner_summary]
)

# To:
scanner_btn.click(
    run_llm_security_scan,
    inputs=[scanner_target, scanner_model, scanner_intensity, scanner_categories],
    outputs=[scanner_status, scanner_results, scanner_summary]
)
```

## Package Upgrades

If you continue to face Gradio compatibility issues, try upgrading to the latest version:

```bash
pip install --upgrade gradio
```

## Other Common Issues

### 1. Cleanup Unclosed Client Sessions

**Warning:**
```
Unclosed client session: client_session: <aiohttp.client.ClientSession object at 0x...>
```

**Solution:**
Ensure all aiohttp client sessions are properly closed:

```python
async def some_function():
    session = aiohttp.ClientSession()
    try:
        # Use session
        return result
    finally:
        await session.close()
```

### 2. Invalid Escape Sequences

**Warning:**
```
SyntaxWarning: invalid escape sequence '\_'
```

**Solution:**
Fix invalid escape sequences in strings by using raw strings or properly escaping:

```python
# Change from:
ascii_art = "..."  # With invalid escape like \_

# To:
ascii_art = r"..."  # Use raw string with r prefix
# Or
ascii_art = "..."  # Replace \_ with \\_ for proper escaping
```

## Still Having Issues?

If you continue to experience problems:

1. Check the application logs for specific error messages
2. Make sure all dependencies are installed correctly
3. Verify that your Python version is 3.8 or newer
4. Try running with the `--debug` flag for more verbose output:
   ```bash
   python pentest_command_center/app.py --debug
   ``` 
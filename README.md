
# **Perl Syntax Checker**

## **Description**
This Python script checks the syntax of Perl files within a specified directory and its subdirectories. It uses the `perl -c` command to verify the syntax of each `.pl` or `.plx` file. The results are saved in an HTML report.

---

## **How It Works**
1. The script uses the `subprocess` module to run `perl -c` on each file with `.pl` or `.plx` extensions.
2. It generates an HTML report (`output.html`) containing:
   - A list of files checked.
   - Whether the syntax is valid or contains errors.
   - Detailed error messages, if any.
3. The script also removes all `__pycache__` directories after processing to keep the workspace clean, with specific handling based on the operating system.

---

## **Setting Up the Environment**

### **Ensure Perl is Installed**
- Verify that Perl is installed on your system by running:
  ```bash
  perl -v
  ```
- If Perl is not installed, download and install it from [Perl's official website](https://www.perl.org/get.html).

---

## **Usage**

### **Run the Script**
1. Ensure Python and Perl are installed on your system.
2. Place the script in the directory you wish to analyze.
3. Execute the script using Python:
   ```bash
   python script_name.py
   ```

### **Output**
The script generates an `output.html` file in the same directory, containing:
- Results for each `.pl` or `.plx` file checked.
- Syntax errors, if any, with detailed messages.

---

## **Removing __pycache__ Directories**

### **Linux**
The script uses the `find` command to locate and remove all `__pycache__` directories recursively:
```bash
find . -type d -name "__pycache__" | xargs rm -rf
```

### **Windows**
On Windows, the script uses PowerShell to find and remove `__pycache__` directories:
```powershell
Get-ChildItem -Path . -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
```

---

## **Requirements**
- Python 3.x
- Perl installed on your system

**Password Compiler**

<div align="center">

**An Advanced Python CLI Tool for high-fidelity Wordlist Generation**

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)](https://github.com/alfanoandrea/Password-Compiler)

</div>

- **Author:** `alfanowski`
- **Language:** Python
- **License:** See `LICENSE`

**Project Overview**

- **Description:** Password Compiler is a small, user-friendly Python utility that generates candidate password dictionaries derived from a person's name, surname and birth date. It is useful for security professionals who need to create targeted wordlists for password auditing, pentesting, or forensic recovery workflows. The tool is intentionally simple and run locally — no external account or personal data is sent unless you use the update feature (which downloads the latest script from the repository URL).

**Features**
- **Interactive input:** guided prompts for name, surname and birth date (DDMMYYYY).
- **Multiple output sizes:** three preconfigured output sizes (small, big, huge) to control dictionary size and runtime.
- **Local dictionary files:** generated wordlists are saved under the `dictionaries/` folder.
- **Self-update:** optional update command fetches the latest script from the configured upstream URL.

**Dependencies**
- **Required packages:** `requests`, `tqdm` (install via `pip`).
- **Note:** The standard library modules `itertools`, `os`, `re`, and `time` are also used.

Install the Python dependencies with:

```powershell
pip install -r requirements.txt
```

If you prefer to install only what you need:

```powershell
pip install requests tqdm
```

**Quickstart (Windows / PowerShell)**

1. Open a terminal in the project directory (where `PasswordCompiler.py` resides).
2. Ensure dependencies are installed (see above).
3. Run the script:

```powershell
python PasswordCompiler.py
```

4. Follow the on-screen menu:
- Select `Generate` to create a dictionary file.
- Select `Update` to check for and download the latest script from the configured upstream `scriptURL`.
- Select `Exit` to quit.

**Usage Details**
- When you choose `Generate`, the program will prompt for:
  - `Name` and `Surname` (alphabetic characters only).
  - `Birth date` in `DDMMYYYY` format.
  - A filename for the generated dictionary (saved as `dictionaries/<name>.txt`).
  - The output size: `Small` (≈ 15k+ passwords), `Big` (≈ 600k+), or `Huge` (≈ 25M+). The tool builds permutations of name/surname variations, date fragments and common separators/special characters.
- Generated files are written to the `dictionaries/` folder. If the folder does not exist, the script will create it.

**Security & Privacy**
- The tool runs locally and operates on data you enter interactively.
- Do not generate wordlists containing real users' sensitive information without proper authorization.
- The `Update` feature downloads the latest script from `scriptURL` — use this only on trusted networks.

**Examples**

Example session (illustrative):

```powershell
python PasswordCompiler.py
# choose: 1 Generate
# enter name: john
# enter surname: doe
# enter birth date: 01011990
# choose file name: john_doe
# choose size: Small
# output: dictionaries/john_doe.txt
```

**Development Notes**
- Main script: `PasswordCompiler.py`.
- Output directory: `dictionaries/`.
- Upstream script URL is stored in the `scriptURL` variable inside the script.
- Example dependencies are listed in `requirements.txt`.

**Troubleshooting**
- If you see a message about missing modules, run `pip install -r requirements.txt`.
- On Windows, run the script with the `python` command that points to a Python 3 interpreter.
- If the progress bar stalls during generation for very large sizes, consider selecting a smaller size or running on a machine with more memory/CPU.

**Contributing**
- Feel free to open issues or pull requests on the repository. Typical improvements:
  - More efficient generation algorithms (streaming, generators) for huge lists.
  - Additional input patterns and configurable templates.
  - Improved CLI flags for non-interactive/batch usage.

**Contact & Author**
- `alfanowski` — for questions, issues or contributions, open an issue on the repository or create a pull request.

**License**
- See the `LICENSE` file in this repository for full license terms.

Thank you for using Password Compiler — use responsibly.


<div align="center">

**Made with ❤️ by alfanowski**

</div>
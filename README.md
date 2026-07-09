# Python Code Optimizer 🚀

[![Visual Studio Marketplace Installs](https://img.shields.io/visual-studio-marketplace/i/AtharvaRamawat.auto-code-optimizer?color=blue&label=Installs&logo=visual-studio-code)](https://marketplace.visualstudio.com/items?itemName=AtharvaRamawat.auto-code-optimizer)
[![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/AtharvaRamawat.auto-code-optimizer?color=success&label=Version)](https://marketplace.visualstudio.com/items?itemName=AtharvaRamawat.auto-code-optimizer)

**Python Code Optimizer** is an intelligent Visual Studio Code extension that seamlessly refactors, cleans, and optimizes your Python code directly within your editor. 

Powered by a fine-tuned, cloud-hosted Large Language Model (LLM) deployed via Hugging Face and backed by Abstract Syntax Tree (AST) analysis, this tool acts as an AI pair programmer dedicated strictly to code quality and performance.

---

## ✨ Features

* **🧠 Smart Refactoring:** Automatically converts verbose and inefficient code (e.g., standard `for` loops) into modern, Pythonic data structures (e.g., list or dictionary comprehensions).
* **🧹 Syntax & Style Fixes:** Cleans up redundant conditional logic (e.g., converting `if x == True:` to `if x:`) and nudges code toward PEP 8 best practices.
* **⚡ Performance Boosts:** Identifies and resolves common execution bottlenecks, such as memory-heavy string concatenation inside loops, replacing them with optimized methods like `.join()`.
* **🛡️ Structural Awareness:** Uses AST alongside AI inference to ensure the structural integrity of your code remains intact during transformations.

---

## 📦 Installation

You can install this extension directly from the VS Code Marketplace.

**Method 1: VS Code Marketplace**
1. Navigate to the [Python Code Optimizer Extension Page](https://marketplace.visualstudio.com/items?itemName=AtharvaRamawat.auto-code-optimizer).
2. Click **Install**.

**Method 2: Command Palette**
1. Open VS Code.
2. Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (macOS) to open the Quick Open dialog.
3. Type the following command and press Enter:
   ```bash
   ext install AtharvaRamawat.auto-code-optimizer

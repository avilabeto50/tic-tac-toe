# Fallback: Running Locally (No Codespaces)

Use these instructions **only if GitHub Codespaces isn't working** for you.
You'll need to install Python and clone the repo to your own computer.

---

## Step 1 — Install Python

### On Windows

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click **"Download Python 3.x.x"** (the big yellow button).
3. Run the installer. **Important:** on the first screen, check the box that says **"Add Python to PATH"** before clicking Install Now.
4. Once installed, open **Command Prompt**:
   - Press `Win + R`, type `cmd`, and hit Enter.
5. Verify Python is installed by running:
   ```
   python --version
   ```
   You should see something like `Python 3.12.0`.

### On Mac

1. Open **Terminal** (press `Cmd + Space`, type "Terminal", hit Enter).
2. Check if Python 3 is already installed:
   ```
   python3 --version
   ```
   If you see a version number, skip the next step.
3. If not installed, go to [https://www.python.org/downloads/](https://www.python.org/downloads/), download the Mac installer, and follow the instructions.
4. Verify:
   ```
   python3 --version
   ```

---

## Step 2 — Clone Your Fork

First, make sure you have already **forked** the repo on GitHub (click the Fork button on the assignment page). Then:

### On Windows (Command Prompt)

```
git clone https://github.com/YOUR-USERNAME/tic-tac-toe.git
cd tic-tac-toe
```

### On Mac (Terminal)

```
git clone https://github.com/YOUR-USERNAME/tic-tac-toe.git
cd tic-tac-toe
```

> Replace `YOUR-USERNAME` with your actual GitHub username.

> **Don't have git?**
> - **Windows:** Download it from [https://git-scm.com/download/win](https://git-scm.com/download/win) and install with default settings. Then re-open Command Prompt.
> - **Mac:** Run `git --version` in Terminal — if not installed, macOS will prompt you to install it automatically.

---

## Step 3 — Run the Starter Code

### On Windows

```
python play.py
```

### On Mac

```
python3 play.py
```

You should see the board printed after each move, ending with a result.

---

## Step 4 — Edit `strategy.py`

Open `strategy.py` in any text editor (Notepad, TextEdit, VS Code, etc.).
Replace the starter logic inside `choose_move` with your own strategy.
Save the file, then run `play.py` again to test it.

---

## Step 5 — Save and Submit

Once you're happy with your strategy, push your changes back to GitHub:

### On Windows

```
git add strategy.py
git commit -m "My tic-tac-toe strategy"
git push
```

### On Mac

```
git add strategy.py
git commit -m "My tic-tac-toe strategy"
git push
```

Then go to your fork on GitHub and confirm that `strategy.py` shows your changes.
Paste your fork's URL into the assignment submission form:

```
https://github.com/YOUR-USERNAME/tic-tac-toe
```

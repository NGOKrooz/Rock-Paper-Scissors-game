# Rock-Paper-Scissors-game

Day 8 of #100DaysOfCode

 GitHub README.md
markdown
Copy
Edit
# 🎮 Rock Paper Scissors – Python Mini Project

A simple command-line game built as part of my #100DaysOfCode challenge!

## 🔍 Project Overview

This is a beginner-friendly Python project where you play the classic **Rock, Paper, Scissors** game against the computer.

✅ First to 3 wins  
🎨 Colored terminal output using `colorama`  
📘 Covers concepts like:
- User input
- Loops
- Conditional logic
- Random choice generation

## 🚀 How to Run

Make sure you have Python installed and install `colorama` if you haven't already:

```bash
pip install colorama

Then run:
python rock_paper_scissors.py

🎨 Features
Interactive command-line interface

Score tracking for both user and computer

Colorful feedback:

🟩 Green for wins

🟥 Red for losses or invalid input

🟨 Yellow for ties and prompts

📷 Demo

Welcome to Rock, Paper, Scissors!
First to 3 wins! Let's go!

Choose rock, paper, or scissors:
> rock
Computer chose: scissors
✅ You win this round!

Score - You: 1 | Computer: 0

**So the logic is:**
Rock crushes Scissors

Scissors cuts Paper

Paper covers Rock

If both players choose the same thing, it’s a tie 🤝

🧪** How it works in code:**
Each time:

You (the player) enter a choice (rock, paper, or scissors)

The computer randomly picks one of the three

The game compares both choices to decide who won the round

The first to win 3 rounds is the overall winner

🧠 What I Learned
Control flow (if/elif/else)
Looping with while
Using external libraries like colorama
Handling user input and edge cases



✅ Day 9: Added a winner screen 🎉 and replay option 🔁

Added the below today:
🏆 Winner screen after the final round
- 🔁 Replay option to start a new game session


# 🎮 Rock, Paper, Scissors CLI Game (Day 10 & 11)

## 📌 Objective
Polish the command-line interface (CLI) of the Rock, Paper, Scissors game to be **more interactive, intuitive, and visually engaging**.

---

## ✨ Features Added

### ✅ Core Enhancements
- **Stylish CLI Output:** Integrated `colorama` for colorful terminal messages.
- **User Personalization:** Added player name input with title casing.
- **Robust Input Handling:** Accepts and cleans up all uppercase/lowercase inputs and extra whitespace.
- **Game Stats Tracker:**
  - Total rounds
  - Wins
  - Losses
  - Ties
  - Win rate percentage

### 🎨 UI & UX Upgrades
- **Round Countdown:** Adds suspense with a 3-2-1 countdown before each round.
- **Visuals with Emojis & ASCII Art:** 
  - Rock 🪨  
  - Paper 📄  
  - Scissors ✂️  
- **Game Flow Clarity:** Display round numbers, stylish separators, and game over messages.

### 🧼 Code Refactor
- Modularized with reusable functions:
  - `get_player_choice()`
  - `countdown()`
  - `display_ascii()`
  - `print_separator()`

---

## 🧠 Lessons Learned
- How to refactor repetitive logic into clean functions
- CLI game design and player experience principles
- How to use colors and visuals to make CLI apps engaging
- Calculating real-time stats (win rate) in a loop
- Bonus: ASCII art rendering in Python 🐍

---

## 🔁 How to Play
1. Run the script.
2. Input your name.
3. Choose between Rock, Paper, or Scissors each round.
4. First to 3 wins the crown 👑
5. Stats are displayed at the end. Play again if you like!

---

## 🛠 Tech Used
- Python 3
- `colorama` library

---

## 📸 Sneak Peek

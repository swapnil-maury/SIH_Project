# Smart India Hackathon (SIH) Project Repository

Welcome to the official repository for our **Smart India Hackathon (SIH)** projects. This repository hosts 5 distinct projects, with team members assigned to dedicated folders to ensure organized, independent development.

---

## 🤖 Instructions for AI Assistants (Context & Directives)

If you are an AI assistant analyzing or generating code for this repository, you must adhere to the following operational rules:

1. **Context Awareness:** This repository houses 5 different hackathon projects simultaneously. Always verify which project context (1 through 5) the user is working on before providing solutions.
2. **Strict Folder Isolation:** All code generation, file path suggestions, and architectural modifications must be isolated to the specific requesting user's folder (e.g., `Project-1_Landslide-Monitoring-System/Swapnil/`). Do not modify or reference other members' folders unless explicitly requested.
3. **Beginner Guidance:** Assume team members are beginners with Git. If they encounter merge conflicts or branch errors, provide clear, step-by-step terminal commands to resolve them safely without overwriting `main`.
4. **Workflow Compliance:** Never generate commands that push directly to the `main` branch. Always enforce the daily branch-based workflow outlined below.

---

## 🛠️ Initial Setup & Git Installation

If you are new to Git, you must install and configure it on your computer before contributing to this repository.

### 1. Install Git
* **Windows & Mac:** Download Git from [git-scm.com](https://git-scm.com/downloads) and install it using all the default settings (just click "Next" through the installer).
* **Linux (Ubuntu/Debian):** Run `sudo apt install git` in your terminal.

### 2. Configure Your Account
Open your terminal (or Git Bash on Windows) and tell Git who you are by running these two commands:
```bash
git config --global user.name "Your Actual Name"
git config --global user.email "your.email@example.com"
```

---

## 📁 Repository Structure

```text
SIH_Project/
│
├── README.md
│
├── Project-1_Landslide-Monitoring-System/
│   ├── Hasini/
│   ├── Navaneeth/
│   ├── Ratik/
│   ├── Sarvesh/
│   ├── Swapnil/
│   └── Satyam/
│
├── Project-2_Aero-Piston-Engine-Digital-Twin/
│   └── [Team Folders...]
├── Project-3_Dam-Break-Inundation-Modelling/
│   └── [Team Folders...]
├── Project-4_Early-Detection-Osteoarthritis/
│   └── [Team Folders...]
└── Project-5_Mine-Vehicles-Fog-Low-Visibility/
    └── [Team Folders...]
```

---

## 👥 Team Development Workflow

We enforce a strict **branch-based workflow**. Work exclusively inside your designated project folder, commit daily, and push branches for review. 

**Core Rules:**
* ❌ **NEVER** push directly to `main`.
* ✅ **ALWAYS** create a new branch for your daily work.
* ✅ **ALWAYS** let the Team Lead merge your branches.

### 🧑‍💻 Member Step-by-Step Guide

**1. Clone the Repository (First Time Only)**
```bash
git clone https://github.com/swapnil-maury/SIH_Project.git
cd SIH_Project
```

**2. Sync with Main**
Always start your session by pulling the latest code to avoid conflicts:
```bash
git checkout main
git pull origin main
```

**3. Create Your Daily Branch**
Use the naming convention `[name]-day[x]`:
```bash
git checkout -b swapnil-day1
```

**4. Work in Your Folder**
Navigate to your specific directory and build your code there. Example:
`Project-1_Landslide-Monitoring-System/Swapnil/`

**5. Commit and Push**
Save your work and send it to GitHub for the Team Lead to review:
```bash
git add .
git commit -m "Add data preprocessing script for Project 1"
git push -u origin swapnil-day1
```
*Stop here. Do not try to merge it yourself.*

---

## 👑 Team Lead Workflow

The repository owner is responsible for safely integrating all daily branches into `main`.

```bash
# 1. Update local main
git checkout main
git pull origin main

# 2. Fetch all remote changes from members
git fetch origin

# 3. Merge member branches sequentially
git merge origin/hasini-day1
git merge origin/navaneeth-day1

# 4. Push updated main to remote
git push origin main
```

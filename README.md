# Smart India Hackathon (SIH) Project Repository

Welcome to the official repository for our **Smart India Hackathon (SIH)** projects. This repository houses 5 distinct projects, with 5 team members assigned to each project. Every member has a dedicated folder to organize and develop their work independently.

---

## 📁 Repository Structure

```text
SIH_Project/
│
├── README.md
├── .gitignore
├── .editorconfig
│
├── Project-1_Landslide-Monitoring-System/
│   ├── Member-1/
│   ├── Member-2/
│   ├── Member-3/
│   ├── Member-4/
│   └── Member-5/
│
├── Project-2_Aero-Piston-Engine-Digital-Twin/
│   ├── Member-1/
│   ├── Member-2/
│   ├── Member-3/
│   ├── Member-4/
│   └── Member-5/
│
├── Project-3_Dam-Break-Inundation-Modelling/
│   ├── Member-1/
│   ├── Member-2/
│   ├── Member-3/
│   ├── Member-4/
│   └── Member-5/
│
├── Project-4_Early-Detection-Osteoarthritis/
│   ├── Member-1/
│   ├── Member-2/
│   ├── Member-3/
│   ├── Member-4/
│   └── Member-5/
│
└── Project-5_Mine-Vehicles-Fog-Low-Visibility/
    ├── Member-1/
    ├── Member-2/
    ├── Member-3/
    ├── Member-4/
    └── Member-5/
```

---

## 🚀 SIH Projects Overview

### Project 1 — Landslide Monitoring System
* **Problem Statement:** Development of a system for monitoring landslide-prone areas and detecting potential landslide events using available datasets, sensors, environmental data, and/or AI/ML techniques.
* **Team:** Member 1 | Member 2 | Member 3 | Member 4 | Member 5

### Project 2 — AI-Enabled Real-Time Digital Twin System for Aero Piston Engines
* **Problem Statement:** AI-Enabled Real-Time Digital Twin System for Health Monitoring, Fault Prediction and Mission Reliability Enhancement of Aero Piston Engines used in MALE UAVs.
* **Team:** Member 1 | Member 2 | Member 3 | Member 4 | Member 5

### Project 3 — Dam Break Inundation Modelling
* **Problem Statement:** Dam Break Inundation Modelling Using Hydrodynamic Modelling of any River. Involves hydrodynamic modelling and simulation of flood inundation resulting from a potential dam-break event.
* **Team:** Member 1 | Member 2 | Member 3 | Member 4 | Member 5

### Project 4 — Early Detection System for Osteoarthritis
* **Problem Statement:** Early Detection System for Osteoarthritis. The dataset provided with the problem statement will be used for development, experimentation, and model evaluation.
* **Team:** Member 1 | Member 2 | Member 3 | Member 4 | Member 5

### Project 5 — Mine Vehicles in Fog and Low-Visibility Conditions
* **Problem Statement:** Mine Vehicles in Fog and Low-Visibility Conditions. The dataset provided with the problem statement will be used for development and experimentation.
* **Team:** Member 1 | Member 2 | Member 3 | Member 4 | Member 5

---

## 👥 Team Development Workflow

The repository follows a strict **branch-based workflow**. Members work inside their assigned project and folder, commit daily, and push branches to GitHub for review and integration by the team lead.

### 🛡️ Recommended Branch Rules
* ❌ **Never** work or push directly to `main`.
* ✅ Always create a new branch for each day's work.
* ✅ Push your branch after completing your daily tasks.
* ✅ The team lead reviews and merges all branches into `main`.

---

## 🧑‍💻 Member Step-by-Step Guide

### 1. Clone the Repository *(Run once)*
```bash
git clone https://github.com/swapnil-maury/SIH_Project.git
cd SIH_Project
```

### 2. Start the Day by Updating `main`
Before writing any code, ensure you have the latest updates:
```bash
git checkout main
git pull origin main
```

### 3. Create a New Daily Branch
Name your branch following the convention `member<number>-day<X>` (e.g., `member1-day1`):
```bash
git checkout -b member1-day1
```

### 4. Work Exclusively Inside Your Assigned Folder
If you are Member 1 working on Project 1, all your code and notes go inside:
```text
Project-1_Landslide-Monitoring-System/Member-1/
```
You can structure your folder as needed:
```text
Member-1/
├── README.md
├── src/
├── models/
├── scripts/
├── data/
└── requirements.txt
```
> **Note:** Do not modify another member's folder unless agreed upon by the team.

### 5. Check Changes and Status
```bash
git status
git diff
```

### 6. Commit Your Changes
Use concise and meaningful commit messages:
```bash
git add .
git commit -m "Add dataset preprocessing pipeline"
```

### 7. Push Your Branch
```bash
git push -u origin member1-day1
```

### 8. Do NOT Merge Your Branch
Stop here! Do not merge your branch into `main`. The team lead will collect, review, and merge everyone's work.

---

## 👑 Team Lead Workflow

The repository owner/team lead is responsible for reviewing and merging daily member branches into the `main` branch.

```bash
# Fetch all remote branches
git fetch origin

# Switch to main and pull latest changes
git checkout main
git pull origin main

# Merge each member's branch sequentially
git merge origin/member1-day1
git merge origin/member2-day1
git merge origin/member3-day1
git merge origin/member4-day1
git merge origin/member5-day1

# Push the updated main branch
git push origin main
```

---

## 🔄 Daily Workflow Lifecycle

```text
               MAIN
                 │
         git pull origin main
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
     Member 1  Member 2  Member 3
      Branch    Branch    Branch
        │        │        │
        ▼        ▼        ▼
       Work     Work     Work
        │        │        │
        ▼        ▼        ▼
      Commit   Commit   Commit
        │        │        │
        ▼        ▼        ▼
       Push     Push     Push
        └────────┼────────┘
                 │
                 ▼
             TEAM LEAD
                 │
                 ▼
        Review & Merge into `main`
                 │
                 ▼
            Push `main`
```

---

## 🎯 Golden Rule
```text
PULL MAIN → CREATE NEW BRANCH → WORK IN YOUR FOLDER → COMMIT → PUSH → TEAM LEAD MERGES
```

---

## 📌 Repository Information
* **Repository Name:** `SIH_Project`
* **Repository URL:** [https://github.com/swapnil-maury/SIH_Project](https://github.com/swapnil-maury/SIH_Project)
* **Default Branch:** `main`

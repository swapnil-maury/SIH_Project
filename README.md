SIH_Project

Repository for our Smart India Hackathon (SIH) projects.

This repository contains 5 SIH projects. Each project has 5 team members, and every member has their own folder to work in.

The repository owner/team lead will be responsible for merging all members' work into main.

📁 Repository Structure
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
🚀 SIH Projects
Project 1 — Landslide Monitoring System

Development of a system for monitoring landslide-prone areas and detecting
potential landslide events using available datasets, sensors, environmental
data, and/or AI/ML techniques.

Team
Member 1
Member 2
Member 3
Member 4
Member 5
Project 2 — AI-Enabled Real-Time Digital Twin System for Aero Piston Engines
Problem Statement

AI-Enabled Real-Time Digital Twin System for Health Monitoring, Fault Prediction and Mission Reliability Enhancement of Aero Piston Engines used in MALE UAVs.

Team
Member 1
Member 2
Member 3
Member 4
Member 5
Project 3 — Dam Break Inundation Modelling
Problem Statement

Dam Break Inundation Modelling Using Hydrodynamic Modelling of any River.

The project will involve hydrodynamic modelling and simulation of flood
inundation resulting from a potential dam-break event.

Team
Member 1
Member 2
Member 3
Member 4
Member 5
Project 4 — Early Detection System for Osteoarthritis
Problem Statement

Early Detection System for Osteoarthritis.

The dataset provided with the problem statement will be used for development,
experimentation, and model evaluation.

Team
Member 1
Member 2
Member 3
Member 4
Member 5
Project 5 — Mine Vehicles in Fog and Low-Visibility Conditions
Problem Statement

Mine Vehicles in Fog and Low-Visibility Conditions.

The dataset provided with the problem statement will be used for development
and experimentation.

Team
Member 1
Member 2
Member 3
Member 4
Member 5
👥 Team Development Workflow

The repository uses a branch-based workflow.

Each member has a dedicated folder inside their assigned project.

Important Rules
Never work directly on main.
Each member should work inside their assigned folder.
Create a new branch every day.
Push your branch to GitHub after completing your work.
Do not merge your own branch into main.
The repository owner/team lead will merge everyone's work.
Before starting work on a new day, pull the latest main.
Do not overwrite another member's work.
Use meaningful commit messages.
If you need to modify another member's folder, discuss it with them first.
🧑‍💻 Member Workflow

Every member should follow the steps below.

1. Clone the Repository

Run this only once on your computer:

git clone https://github.com/swapnil-maury/SIH_Project.git

Then enter the repository:

cd SIH_Project
2. Start the Day by Updating main

Before starting your work:

git checkout main
git pull origin main

This ensures that you have the latest work merged by the team lead.

3. Create a New Branch

Create a new branch for each day.

For example, Member 1 on Day 1:

git checkout -b member1-day1

Member 1 on Day 2:

git checkout main
git pull origin main
git checkout -b member1-day2

Examples of branch names:

member1-day1
member1-day2
member1-day3

member2-day1
member2-day2

member3-day1
member3-day2

member4-day1
member4-day2

member5-day1
member5-day2
4. Work Only Inside Your Folder

For example, if you are Member 1 working on Project 1:

Project-1_Landslide-Monitoring-System/
└── Member-1/

Your work should go inside:

Project-1_Landslide-Monitoring-System/Member-1/

You can organize your folder however you want:

Member-1/
├── README.md
├── src/
├── models/
├── scripts/
├── data/
└── requirements.txt

Do not modify another member's folder unless the team has agreed to it.

5. Check Your Changes

Before committing:

git status

To inspect the actual changes:

git diff
6. Commit Your Changes

Add your changes:

git add .

Commit them:

git commit -m "Add initial landslide preprocessing"

Use meaningful commit messages.

Examples:

Add dataset preprocessing
Add CNN model
Add initial model training
Fix preprocessing pipeline
Add API endpoint
Add frontend dashboard
Update documentation
Fix model inference
7. Push Your Branch

Push your branch to GitHub:

git push -u origin member1-day1

Replace member1-day1 with your actual branch name.

For example:

git push -u origin member3-day1
8. Do NOT Merge Your Branch

After pushing your branch, your work is done for the day.

Do not merge your branch into main.

The repository owner/team lead will collect and merge everyone's work.

Member
   │
   ▼
Create branch
   │
   ▼
Write code
   │
   ▼
Commit
   │
   ▼
Push branch
   │
   ▼
STOP
   │
   ▼
Team Lead merges
👑 Team Lead Workflow

The repository owner/team lead will merge the members' branches.

Suppose five members have completed their work:

member1-day1
member2-day1
member3-day1
member4-day1
member5-day1

The team lead can fetch all branches:

git fetch origin

Then merge them one by one into main.

First:

git checkout main
git pull origin main

Then:

git merge origin/member1-day1

Then:

git merge origin/member2-day1

Then:

git merge origin/member3-day1

Then:

git merge origin/member4-day1

Then:

git merge origin/member5-day1

If everything is correct:

git push origin main
🔄 Daily Team Workflow

The complete workflow is:

                    MAIN
                     │
                     │
              git pull origin main
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
    Member 1      Member 2     Member 3
      branch        branch       branch
        │            │            │
        ▼            ▼            ▼
      Work         Work          Work
        │            │            │
        ▼            ▼            ▼
      Commit       Commit        Commit
        │            │            │
        ▼            ▼            ▼
      Push         Push          Push
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
                TEAM LEAD
                     │
                     ▼
             Review all branches
                     │
                     ▼
             Merge into `main`
                     │
                     ▼
                Push `main`
                     │
                     ▼
              NEXT DAY STARTS
                     │
                     ▼
             git pull origin main
                     │
                     ▼
             Create new branch
📅 Example — Day 1
Member 1
git checkout main
git pull origin main
git checkout -b member1-day1

Member 1 works inside:

Project-X/Member-1/

Then:

git add .
git commit -m "Add initial implementation"
git push -u origin member1-day1
Member 2
git checkout main
git pull origin main
git checkout -b member2-day1

Work:

Project-X/Member-2/

Then:

git add .
git commit -m "Add data preprocessing"
git push -u origin member2-day1
Member 3
git checkout main
git pull origin main
git checkout -b member3-day1

Work:

Project-X/Member-3/

Then:

git add .
git commit -m "Add model implementation"
git push -u origin member3-day1
📅 Day 2

After the team lead has merged everyone's Day 1 work:

Every member starts with:

git checkout main
git pull origin main

Then creates a new branch.

For Member 1:

git checkout -b member1-day2

For Member 2:

git checkout -b member2-day2

For Member 3:

git checkout -b member3-day2

And so on.

🔀 Pull Requests
Members do NOT need to merge their own branches.

The main workflow is:

Member Branch
     │
     ▼
Push to GitHub
     │
     ▼
Team Lead reviews
     │
     ▼
Team Lead merges
     │
     ▼
main

If the team lead wants to use Pull Requests instead of manually merging
branches, members can create a Pull Request:

member1-day1 → main

The team lead then reviews and merges it.

Do not create unnecessary extra branches or merge the same work twice.

🛡️ Recommended main Branch Rule

The main branch should be treated as the stable/shared branch.

Recommended policy:

❌ Members should not directly push to main.

✅ Members create their own branch.

✅ Members push their branch.

✅ Team lead reviews the work.

✅ Team lead merges the work into main.
👤 Adding Team Members to GitHub

Repository:

https://github.com/swapnil-maury/SIH_Project

The repository owner can add members through:

GitHub
   ↓
SIH_Project
   ↓
Settings
   ↓
Collaborators
   ↓
Add people

Search using the person's:

GitHub username
GitHub email address

Send the invitation.

The member must accept the GitHub invitation before they can work with
the repository.

🔑 What a Collaborator Can Do

After being added with appropriate repository access, a member can:

Clone repository
      ↓
Create branch
      ↓
Modify their files
      ↓
Commit
      ↓
Push branch
      ↓
Wait for team lead

The member should not modify main directly.

🆘 If Someone Gets an Error

If you get:

Permission denied

or:

403

check that:

You accepted the GitHub repository invitation.
You are logged into the correct GitHub account.
Your Git remote points to the correct repository.

Check the remote:

git remote -v

It should show:

https://github.com/swapnil-maury/SIH_Project.git
🔍 Useful Git Commands
Check current branch
git branch
Switch to main
git checkout main
Pull latest main
git pull origin main
Create a new branch
git checkout -b branch-name
Check status
git status
View changes
git diff
Add files
git add .
Commit
git commit -m "Your message"
Push new branch
git push -u origin branch-name
Push existing branch
git push
Fetch all remote branches
git fetch origin
Switch to another branch
git checkout branch-name
⚠️ Important: Before Starting Work Every Day

Always run:

git checkout main
git pull origin main

Then create your new daily branch:

git checkout -b YOUR-NAME-dayX

For example:

git checkout main
git pull origin main
git checkout -b swapnil-day1
🎯 Golden Rule
PULL
  ↓
CREATE NEW BRANCH
  ↓
WORK IN YOUR FOLDER
  ↓
COMMIT
  ↓
PUSH
  ↓
TEAM LEAD MERGES
  ↓
NEXT DAY
  ↓
PULL MAIN
  ↓
CREATE NEW BRANCH
  ↓
REPEAT

Never work directly on main.

Never merge your own branch into main.

The team lead is responsible for merging everyone's completed work.

📌 Repository Information

Repository Name:

SIH_Project

Repository URL:

https://github.com/swapnil-maury/SIH_Project

Default Branch:

main

Projects:

1. Landslide Monitoring System
2. AI-Enabled Real-Time Digital Twin System for Health Monitoring,
   Fault Prediction and Mission Reliability Enhancement of Aero Piston
   Engines used in MALE UAVs
3. Dam Break Inundation Modelling Using Hydrodynamic Modelling of any River
4. Early Detection System for Osteoarthritis
5. Mine Vehicles in Fog and Low-Visibility Conditions
🏆 Development Philosophy

Each member works independently in their assigned folder while the team lead
maintains the main branch.

This keeps the project organized, makes it easier to track individual work,
and reduces the possibility of one member accidentally breaking another
member's code.
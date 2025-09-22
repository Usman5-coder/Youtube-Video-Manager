# 🎥 YouTube Video Manager (SQLite + Python)

A simple command-line application to **manage a list of YouTube videos** using **SQLite** as the database.  
You can add, view, update, and delete videos directly from the terminal.

---

## 🚀 Features
- 📋 **List all videos** stored in the database.
- ➕ **Add new videos** with name and time.
- ✏️ **Update existing videos** by ID.
- ❌ **Delete videos** by ID.
- 💾 Persistent storage using SQLite (`youtube_videos.db`).

---

## 📂 Project Structure
.
├── youtube_manager.py # Main Python script
├── youtube_videos.db # SQLite database (auto-created)
└── README.md # Documentation

yaml
Copy code

---

## ⚙️ Requirements
- Python **3.x**
- SQLite (comes pre-installed with Python)

---

## ▶️ How to Run
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the script:

   ```
   python youtube_manager.py
   ```
📖 Usage Guide
When you run the program, you’ll see a menu:
```
1. List Videos
2. Add Videos
3. Update Videos
4. Delete Videos
5. Exit
```
1️⃣ List Videos
Shows all stored videos:

```
(1, "My First Video", "10:05")
(2, "Python Tutorial", "25:30")
```
2️⃣ Add Video
You’ll be prompted to enter:
Video Name
Video Time

```
Example:
Enter the video Name: Python Crash Course
Enter the video Time: 12:45
```
3️⃣ Update Video
You’ll be prompted to enter:
Video ID
New Name
New Time

4️⃣ Delete Video
Enter the ID of the video you want to delete.

5️⃣ Exit
Closes the program.

🗄 Database Schema
```
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
);
```

📌 Notes
The database file youtube_videos.db is automatically created on first run.

All changes are saved automatically.

The app runs fully in the terminal/command prompt.

📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it.


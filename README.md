# 🌟 File Organizer – Python Automation Project

A powerful and clean Python automation tool that **automatically organizes files** inside any folder by sorting them into categories like **Images**, **Videos**, **Documents**, **Audio**, **Code**, and **Others**.

This project highlights **automation, Python scripting, CLI design, and real-world problem solving** — perfect for showcasing in resumes or GitHub portfolios.

---

## 🚀 Features

✨ Automatically detects file types  
📁 Creates folders for each category  
📦 Moves files into their correct organized folders  
🧪 **Dry-Run Mode** – shows what will happen without making changes  
🔍 **Verbose Mode** – prints every action step-by-step  
⚡ Clean Python scripting with good structure  

---

## 🛠️ Technologies Used

- **Python 3**
- `os`
- `shutil`
- `pathlib`
- `argparse`

---

## 📦 How to Use

### 1️⃣ Dry Run (simulate the action, no changes)

```bash
python file_organizer.py "path/to/your/folder" --dry-run --verbose
```

### 2️⃣ Run for Real (organize your files)

```bash
python file_organizer.py "path/to/your/folder" --verbose
```

---

## 📁 Example Output

### 📌 Before Running
```
Downloads/
├── photo.png
├── movie.mp4
├── notes.pdf
├── music.mp3
├── script.py
```

### 📌 After Running
```
Downloads/
├── Images/photo.png
├── Videos/movie.mp4
├── Documents/notes.pdf
├── Audio/music.mp3
├── Code/script.py
```

---

## 📂 Folder Categories

| 🗂️ Category | 🏷️ Extensions |
|------------|------------------------------|
| Images     | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp |
| Videos     | .mp4, .mkv, .avi, .mov, .flv |
| Documents  | .pdf, .doc, .docx, .ppt, .pptx, .xlsx |
| Audio      | .mp3, .wav, .aac, .ogg |
| Code       | .py, .c, .cpp, .html, .css, .js |
| Others     | Anything else |

---

## 👨‍💻 Author

**Prithveeraj Shewale**  
Python | C | C++ | HTML | DSA | AI Beginner  
📍 Pune, Maharashtra  

---

## ⭐ Why This Project Is Resume-Worthy

- Shows **real-world automation skills**  
- Demonstrates **file handling** and **directory management**  
- Uses **professional CLI arguments**  
- Has **dry-run + verbose** modes — seen in real utilities  
- Solves an actual daily problem (messy downloads folder!)  
- Strong project for **fresher-level interviews & GitHub portfolio**  

---

## 🌈 If This Helped You  
⭐ Star the repository  
📌 Add it to your portfolio  
🔥 Show it in interviews confidently  

---

Made with ❤️ by Prithveeraj Shewale

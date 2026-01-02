# Create a GIF using Python 🐍

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

This project creates an **animated GIF** from multiple images using Python and the `imageio` library.  
It’s beginner-friendly and demonstrates **file handling, image processing, and GIF creation**.

---

## 📂 Project Structure
```
create-gif-using-python/
├── create_gif.py         # Your  Python code
├── images/               # Folder containing images and GIF
│   ├── hippocorn1.png
│   ├── hippocorn2.png
│   ├── hippocorn3.png
│   ├── hippocorn4.png
│   └── hippocorn.gif     # Output GIF (optional)
├── README.md
├── requirements.txt
└── .gitignore
```
---

## 💻 Requirements

- Python 3.x  
- `imageio` library

Install the required library using:

```bash
pip install -r requirements.txt
The requirements.txt makes it easy for anyone to install dependencies.
```
---

## ⚡ How to Run

-Place all images you want to include in the GIF in the same folder as create_gif.py.

-Open terminal in this folder.

-Run the script:

   python create_gif.py

-The GIF will be created in the same folder (default name: hippocorn.gif).

---

## 🔧 Customization

-Change or add images in the list:

  filenames =    ['hippocorn1.png','hippocorn2.png','hippocorn3.png','hippocorn4.png']

-Adjust GIF speed:

   create_gif(filenames, output_name='hippocorn.gif', duration=500, loop=0)

-duration → time per frame in milliseconds

-loop → number of loops (0 = infinite)

---

## 🖼️ Example Output


---

## 📌 Tips

-Keep images small for faster processing

-Use .gitignore to avoid pushing unnecessary files

-Add requirements.txt for easy setup

---

## 📚 Learnings

-How to handle files in Python

-Using imageio for image processing and GIF creation

-Structuring a project for GitHub

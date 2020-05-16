Minimal PyQt5 Showcase
======================

This is a minimalistic demonstration of PyQt5 for simple cross-platform Python GUIs.

![Win10](https://i.imgur.com/hmuGfAZ.png)
![Xming](https://i.imgur.com/tp2pm71.png)

---

| Prerequisite | Description |
|--------------|-------------|
| PyQt5        | `pip install -r requirements.txt`
| Qt Creator   | (optional) to edit the UI

---

| File               | Description |
|--------------------|-------------|
| `main.py`          | Program to run
| `mainwindow.ui`    | UI file, edited with _Qt Creator_
| `Makefile`         | Defines make-targets, ie. run `make` from command-line
| `README.md`        | This file   |
| `requirements.txt` | _PyPi_ (Pip) prerequisites
| `ui_mainwindow.py` | Generated from `mainwindow.ui`

---

| _Make_ target | Description |
|---------------|-------------|
| `all`         | Generate .py-files from .ui-files
| `window`      | Generate everything and open main window

---

[YouTube inspiration](https://youtu.be/TyR5OBdYzSs)

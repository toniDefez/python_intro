# Python Introduction Guide

A curated set of Jupyter notebooks and exercises that introduce the fundamentals of Python programming. Use this repository as a rapid study path or a refresher on the language, its standard library, and the data science ecosystem.

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Getting Started](#getting-started)
4. [Suggested Learning Path](#suggested-learning-path)
5. [Python Quick Reference](#python-quick-reference)
6. [Recommended Resources](#recommended-resources)

## Overview

The material is organised as a progression of notebooks that cover core Python concepts, common programming patterns, and introductory data science tools. Each topic combines explanations with hands-on code examples that you can execute and modify interactively.

Key learning outcomes include:

- Understanding Python syntax, data types, and control flow.
- Writing reusable functions and working with modules.
- Applying object-oriented and functional programming techniques.
- Exploring data using NumPy, pandas, and Matplotlib.
- Practising through incremental exercises that reinforce each concept.

## Repository Structure

| Path | Description |
| --- | --- |
| `README.md` | Quick start instructions and learning roadmap (this file). |
| `requirements.txt` | Dependencies used throughout the notebooks (Jupyter, NumPy, pandas, Matplotlib, etc.). |
| `docs/quick_reference.md` | One-page Python syntax cheat sheet to accompany the notebooks. |
| `*.ipynb` | Standalone notebooks that introduce language fundamentals, OOP, functional programming, collections, and data libraries. |
| `exercise/` | Practice notebooks organised by difficulty to consolidate the concepts from the main lessons. |

> Tip: Open the notebooks in the suggested order below to get a smooth introduction. Feel free to jump around once you are comfortable with the basics.

## Getting Started

1. **Install Python 3.10+** (3.11 recommended).
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install the dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. **Launch JupyterLab or the classic notebook interface:**
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```
5. **Open the notebooks** listed below and run the cells sequentially. Use `Shift + Enter` to execute a cell.

If you are new to virtual environments, review the [official documentation](https://docs.python.org/3/library/venv.html) for platform-specific details.

## Suggested Learning Path

1. **Python Foundations**
   - `functions.ipynb`: syntax, indentation rules, variables, basic I/O.
   - `comprension_colecciones.ipynb`: lists, tuples, dictionaries, sets, and comprehensions.
   - `access_modifications.ipynb`: working with data structures and manipulating their contents.

2. **Control Flow and Functional Patterns**
   - `functional_programming.ipynb`: lambda functions, map/filter/reduce, iterators.
   - `lamba.ipynb`: focused practice with anonymous functions and functional techniques.

3. **Object-Oriented Programming**
   - `objects.ipynb`: classes, instances, encapsulation.
   - `herencia.ipynb`: inheritance, method overriding, polymorphism.
   - `access_modifications.ipynb`: access modifiers, properties, and dataclasses.

4. **Applied Python**
   - `numpy.ipynb`: array operations and numerical computing.
   - `pandas.ipynb`: tabular data manipulation and analysis.
   - `matplotlib.ipynb`: data visualisation fundamentals.

5. **Practice**
   - Work through the notebooks in the `exercise/` directory. They align with the lessons above and provide progressively challenging problems.
   - Revisit earlier notebooks if you need to reinforce a concept before moving forward.

As you progress, take notes or adapt the examples into scripts to cement your understanding.

## Python Quick Reference

When you need a concise reminder of syntax and idioms, consult [`docs/quick_reference.md`](docs/quick_reference.md). It covers:

- Common commands for running Python and managing virtual environments.
- Core language features (strings, numbers, collections, control flow, functions).
- Object-oriented programming patterns and error handling.
- File I/O, testing strategies, and key data science libraries.

Keep the cheat sheet open alongside the notebooks for quick lookups.

## Recommended Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/) articles for deeper dives into specific topics.
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) for practical automation projects.
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) to write idiomatic code.
- [pandas Documentation](https://pandas.pydata.org/docs/) and [NumPy Documentation](https://numpy.org/doc/) for data-focused workflows.

Happy coding! Use this repository as your rapid Python refresher or starting point, and expand it with your own notebooks as you learn.

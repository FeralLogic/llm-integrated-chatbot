# Apartment Chatbot using Ollama and Mistral Model

This project demonstrates a simple chatbot application built with Python using Ollama and Mistral language model and Python's Tkinter module for a GUI.

<img width="507" height="337" alt="Chatbot" src="https://github.com/user-attachments/assets/cfd022d2-0999-4c58-9244-e217bef3a664" />


## Purpose

The main objective is to explore how Large Language Models (LLMs) can be integrated into a practical application, such as a chatbot for answering questions about an apartment community. It also serves as a learning exercise in:
- Using Ollama’s LLM API
- Creating a chatbot interface
- Designing a basic GUI with Tkinter

> **Note**: The apartment community and all associated information are completely fictitious. This chatbot is for demonstration and learning purposes only and should not be used in a real-world rental or property management setting.

## Features

- Text-based chatbot powered by Mistral via Ollama
- Simple, scrollable GUI built with Tkinter
- Customizable system prompt and context
- Low-temperature setting (`0.2`) for consistent responses

## Future Improvements
- Provide more detailed and structured context to the model 
- Add support for RAG (Retrieval-Augmented Generation) for real-time knowledge integration

## Configuration

Configuration is loaded via `config.ini`:

```ini
[ollama]
host = http://localhost:11434
url = http://localhost:11434
model = mistral

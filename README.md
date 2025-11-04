# Human vs AI — 2048 (Rule-Based Agent)

This project implements a Human vs AI version of the 2048 game.

- Left board: Human plays
- Right board: AI plays automatically using rule-based logic
- Built with Python & Pygame

##  AI Logic
The AI tries each possible move and selects the best one based on:

- Number of empty tiles
- Higher score after move
- Larger tile priority

This is a **Rule-Based AI system** (no machine learning).

## Files
main.py → Game window & loop  
game_logic.py → 2048 mechanics  
ai_agent.py → AI decision rules  

##  How to Run
```bash
pip install pygame
python main.py

# story_generator.py
# Copyright (c) 2025 made with love by @uncannystranger
#
# Main script for the Story Generator project.

import json
import random
from datetime import datetime
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
SAVED_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'saved_stories')

os.makedirs(SAVED_DIR, exist_ok=True)

def load_list(filename):
    with open(os.path.join(DATA_DIR, filename), 'r') as f:
        return json.load(f)

def generate_story():
    characters = load_list('characters.json')
    settings = load_list('settings.json')
    conflicts = load_list('conflicts.json')
    twists = load_list('twists.json')
    story = (
        f"{random.choice(characters)} {random.choice(settings)}, "
        f"{random.choice(conflicts)}, {random.choice(twists)}."
    )
    return story

def save_story(story):
    filename = f"story_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    path = os.path.join(SAVED_DIR, filename)
    with open(path, 'w') as f:
        f.write(story)
    print(f"Story saved as {path}")

def main():
    story = generate_story()
    print("\n\033[1;36mYour Story:\033[0m\n")
    print(f"\033[1;33m{story}\033[0m")
    save = input("\nSave this story? (y/n): ").strip().lower()
    if save == 'y':
        save_story(story)

if __name__ == "__main__":
    main()

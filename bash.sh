#!/bin/bash

# Define the list of folder names
folders=(
  "Beginner Strings"
  "Cascade"
  "The Book Club"
  "Notes Sphere"
  "T2 Simple Sign on"
  "SMart File Library"
  "Back to the Future"
  "Ciphered Intel Ft. Roman Reigns"
  "Cryptic Colors"
  "Malware Mystery"
  "Secret Transmission"
  "Substituted Transmission"
  "Uncharted"
  "ML CTF Challenge"
  "Feedback"
  "sssh!! The nuke code"
  "Hidden go"
  "Wishlist"
  "Echoes of Encryption"
  "The Last"
)

# Loop through the list of folder names
for folder in "${folders[@]}"; do
  # Create a solution.md file inside the directory
  echo "Solution for $folder" > "$folder/solution.md"
done


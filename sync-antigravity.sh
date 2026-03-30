#!/bin/bash

# Configuration
SOURCE_DIR="/home/david/.agents/skills"
TARGET_DIR="/home/david/.gemini/antigravity/skills"

echo "Sincronizando skills de $SOURCE_DIR hacia $TARGET_DIR..."

# Ensure target exists
mkdir -p "$TARGET_DIR"

# Loop through each skill in .agents/skills
for skill_path in "$SOURCE_DIR"/*; do
    if [ -d "$skill_path" ]; then
        skill_name=$(basename "$skill_path")
        
        # Skip internal/special skills if needed
        if [[ "$skill_name" == "sdd-"* ]] || [[ "$skill_name" == "_shared" ]]; then
            continue
        fi
        
        # Check if already exists in target
        if [ -e "$TARGET_DIR/$skill_name" ]; then
            # If it already exists, remove it (whether it was a link or directory)
            # to replace it with a fresh copy
            echo "↺ Actualizando $skill_name (copia fresca)"
            rm -rf "$TARGET_DIR/$skill_name"
        else
            echo "+ Copiando $skill_name"
        fi
        
        # Copy the directory instead of symlinking
        cp -r "$skill_path" "$TARGET_DIR/"
    fi
done

echo "Sincronización terminada."

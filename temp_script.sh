#!/bin/bash
OUTPUT_FILE="all_files_contents.txt"
EXCLUDE_DIRS=("__pycache__" ".git" ".env" ".flaskenv")
EXCLUDE_FILES=(".gitignore" "lms.drawio" "README.md" "$OUTPUT_FILE")
> "$OUTPUT_FILE"
process_files() {
    local folder="$1"
    for file in "$folder"/*; do
        if [[ -d "$file" ]]; then
            dir_name=$(basename "$file")
            if [[ " ${EXCLUDE_DIRS[@]} " =~ " $dir_name " ]]; then
                continue
            fi
            process_files "$file"
        elif [[ -f "$file" ]]; then
            file_name=$(basename "$file")
            if [[ " ${EXCLUDE_FILES[@]} " =~ " $file_name " ]]; then
                continue
            fi
            echo -e "\n==== $file ====" >> "$OUTPUT_FILE"
            cat "$file" >> "$OUTPUT_FILE"
        fi
    done
}
process_files "."
echo "All relevant files and contents have been saved to $OUTPUT_FILE"

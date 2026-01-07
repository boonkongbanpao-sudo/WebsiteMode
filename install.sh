#!/bin/bash

clear
echo ">>> Installing WebsiteMode..."
sleep 0.5

# install python ถ้ายังไม่มี
pkg install -y python >/dev/null 2>&1

# ตั้งโหมดถาวร
echo "enabled" > "$HOME/.websitemode"

# ใส่ prompt ครั้งเดียว
if ! grep -q "WEBSITEMODE_PROMPT" "$HOME/.bashrc"; then
cat << 'EOF' >> "$HOME/.bashrc"

# ===== WEBSITEMODE_PROMPT =====
if [ -f "$HOME/.websitemode" ]; then
    RED="\[\033[1;91m\]"
    BLINK="\[\033[5m\]"
    RESET="\[\033[0m\]"
    PS1="${BLINK}${RED}┃・>》 ${RESET}"
fi
EOF
fi

echo ">>> Applying theme..."
sleep 0.5

# แสดงหน้าโหลด + banner ครั้งแรก
python start.py

echo
echo ">>> Done."
echo ">>> Close & re-open Termux"
sleep 1

#!/bin/bash

clear
echo ">>> Installing WebsiteMode..."

# install python ถ้ายังไม่มี
pkg install -y python >/dev/null 2>&1

# สร้างโหมดถาวร
echo "enabled" > $HOME/.websitemode

# กันรันซ้ำใน bashrc
if ! grep -q "WEBSITEMODE_PROMPT" $HOME/.bashrc; then
cat << 'EOF' >> $HOME/.bashrc

# ===== WEBSITEMODE_PROMPT =====
if [ -f "$HOME/.websitemode" ]; then
    RED="\[\033[1;91m\]"
    BLINK="\[\033[5m\]"
    RESET="\[\033[0m\]"
    PS1="${BLINK}${RED}┃・>》 ${RESET}"
fi
EOF
fi

# รันหน้าโหลด + banner ครั้งแรก
python start.py

echo
echo ">>> Install complete"
echo ">>> Restart Termux to apply"
sleep 1

# รีหน้าอัตโนมัติ
exec bash

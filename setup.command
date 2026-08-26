#!/bin/bash
# ดับเบิลคลิกไฟล์นี้บนเครื่องใหม่ = ติดตั้ง + เปิด auto-push พร้อมใช้เลย
set -e
DIR="$HOME/Documents/CodingTemplate/code-templates"

git config --global user.name "CBPonnapothJ"
git config --global user.email "ponnapoth.j@cubiccreative.org"
git config --global credential.helper osxkeychain

if [ -d "$DIR/.git" ]; then
  echo "มี repo อยู่แล้ว -> pull ล่าสุด"
  cd "$DIR" && git pull
else
  echo "clone repo..."
  mkdir -p "$HOME/Documents/CodingTemplate"
  git clone https://github.com/CBPonnapothJ/code-templates.git "$DIR"
  cd "$DIR"
fi

echo ""
echo "=============================================="
echo " พร้อมใช้! เปิดโฟลเดอร์นี้ใน PyCharm:"
echo " $DIR"
echo " กำลังเปิด auto-push (ปิด = Ctrl-C)"
echo "=============================================="
echo ""
exec ./autopush.sh

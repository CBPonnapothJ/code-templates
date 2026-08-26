# code-templates

โค้ด 3 ไฟล์ (`file1.py`, `file2.py`, `file3.py`) ที่หน้าเว็บ Coding Template ดึงไปแสดง
ผ่าน GitHub raw. แก้ไฟล์ + push → เว็บอัพเดตเองภายใน ~1 นาที.

## ตั้งค่าเครื่องใหม่ (ทำครั้งเดียว)

1. เช็ค git (mac มีอยู่แล้ว ถ้าไม่มีจะเด้งให้ติดตั้ง):
   ```bash
   git --version
   ```

2. ตั้งชื่อ + เปิด keychain จำ token (ครั้งเดียวต่อเครื่อง):
   ```bash
   git config --global user.name "CBPonnapothJ"
   git config --global user.email "ponnapoth.j@cubiccreative.org"
   git config --global credential.helper osxkeychain
   ```

3. Clone:
   ```bash
   git clone https://github.com/CBPonnapothJ/code-templates.git ~/Documents/CodingTemplate/code-templates
   ```

## ใช้งาน

1. เปิดโฟลเดอร์ `~/Documents/CodingTemplate/code-templates` ใน PyCharm
2. เปิด auto-push ค้างไว้ 1 terminal:
   ```bash
   ~/Documents/CodingTemplate/code-templates/autopush.sh
   ```
   ครั้งแรกจะถาม Username = `CBPonnapothJ`, Password = **token** (สร้างที่
   github.com/settings/tokens → classic → ติ๊ก `repo`). keychain จำให้ ครั้งต่อไปไม่ถามอีก.
3. แก้ `.py` ใน PyCharm → save → auto commit+push ภายใน 5 วิ → เว็บเห็น ~1 นาที

ปิด auto-push = Ctrl-C ใน terminal นั้น.

## ถ้าไม่อยาก auto (push เอง)
```bash
git commit -am "update" && git push
```

## เริ่มงานแต่ละครั้ง (กันชนกับที่เครื่องอื่น push ไว้)
```bash
git pull
```

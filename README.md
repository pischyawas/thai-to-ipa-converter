# thai-to-ipa-converter
แปลง TH TO IPA phoneme
📌 แปลงข้อความภาษาไทยเป็นสัทอักษรสากล (IPA Phoneme)
💡 ใช้ Epitran + Panphon ในการแปลงอักษรไทยเป็น IPA

📥 วิธีติดตั้ง
ต้องมี Python 3.7 ขึ้นไป และติดตั้งไลบรารีที่จำเป็นก่อน

bash
Copy
Edit
pip install pandas epitran panphon openpyxl
🛠️ วิธีใช้งาน
เตรียมไฟล์ Excel (.xlsx)

ต้องมี คอลัมน์ "คำศัพท์" (เก็บคำภาษาไทยที่ต้องการแปลง)
ดาวน์โหลดไฟล์ Epitran.py จาก Repo นี้

แก้ไข file_path = "ชื่อไฟล์.xlsx" ตามชื่อไฟล์ของพี่
รันสคริปต์

bash
Copy
Edit
python Epitran.py
🎉 ผลลัพธ์: ไฟล์ใหม่ ipaphoneme_ipa.xlsx ที่แปลงเป็น IPA แล้ว!

📂 รูปแบบ Input / Output
📌 ตัวอย่างไฟล์ Input (ipaphoneme.xlsx)

คำศัพท์
สวัสดี
ขอบคุณ
ไทย
📌 ตัวอย่างไฟล์ Output (ipaphoneme_ipa.xlsx)

คำศัพท์	IPA
สวัสดี	sà.wà.dīː
ขอบคุณ	kʰɔ̀ːp.kʰun
ไทย	tʰaj
⚠️ หมายเหตุ
ต้องติดตั้ง panphon และตรวจสอบว่า featuretable.csv อยู่ใน site-packages/panphon/data/
ถ้าเจอปัญหา UnicodeDecodeError ลองเปิดไฟล์ CSV และบันทึกใหม่เป็น UTF-8 (Notepad++ ใช้ได้)
รองรับเฉพาะภาษาไทยเท่านั้น (ใช้ Epitran โมเดล tha-Thai)
✨ ขอบคุณที่ใช้ Thai to IPA Converter! ✨
หากมีข้อเสนอแนะหรือปัญหา สามารถเปิด Issue หรือ Pull Request ได้เลย 💖🚀


Thai to IPA Converter
📌 แปลงข้อความภาษาไทยเป็นสัทอักษรสากล (IPA Phoneme)
💡 ใช้ Epitran + Panphon ในการแปลงอักษรไทยเป็น IPA
📥 วิธีติดตั้ง
ต้องมี Python 3.7 ขึ้นไป และติดตั้งไลบรารีที่จำเป็นก่อน

pip install pandas epitran panphon openpyxl

---------------------------------------------------------

🛠️ วิธีใช้งาน
เตรียมไฟล์ Excel (.xlsx)

ต้องมี คอลัมน์ "คำศัพท์" (เก็บคำภาษาไทยที่ต้องการแปลง)
ดาวน์โหลดไฟล์ Epitran.py จาก Repo นี้

แก้ไข file_path = "ชื่อไฟล์.xlsx" ตามชื่อไฟล์ของพี่
รันสคริปต์
python Epitran.py

-----------------------------------------------------------

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

----------------------------------------------------------
⚠️ ปัญหาที่พบบ่อย และแนวทางแก้ไข
1️⃣ ปัญหา: UnicodeDecodeError หรืออ่านไฟล์แล้วมีปัญหาเกี่ยวกับ Encoding
🔹 อาการ:

เจอ UnicodeDecodeError เวลาอ่านไฟล์ CSV
ผลลัพธ์แสดงสัญลักษณ์แปลกๆ หรืออ่านผิดพลาด
🔹 แนวทางแก้ไข:

ลองเปิดไฟล์ ipaphoneme.xlsx ใน Notepad++, VS Code หรือ Excel
บันทึกใหม่เป็น UTF-8 โดยเลือก "Save As" → Encoding: UTF-8
อัปเดตโค้ดให้อ่านเป็น UTF-8 (ใน Epitran.py ใช้ encoding="utf-8")

df = pd.read_excel(file_path, dtype=str)  # ป้องกัน NaN และอ่านเป็น string เสมอ

2️⃣ ปัญหา: FileNotFoundError: No such file or directory 'featuretable.csv'
🔹 อาการ:

ติดตั้ง panphon แล้ว แต่ยังหา featuretable.csv ไม่เจอ

**แนวทางแก้ไข**

1.ตรวจสอบว่าไฟล์อยู่ในโฟลเดอร์ site-packages/panphon/data/
dir %LOCALAPPDATA%\Programs\Python\Python310\Lib\site-packages\panphon\data\

2.ถ้าไม่มีไฟล์ ดาวน์โหลดไฟล์ featuretable.csv ให้ copy ไฟล์ ipa_all.csv เปลี่ยนชื่อ เป็น featuretable.cs


3️⃣ ปัญหา: AttributeError: 'float' object has no attribute 'lower'
🔹 อาการ:

มีค่า NaN หรือค่าที่ไม่ใช่ str อยู่ในคอลัมน์ "คำศัพท์"
🔹 แนวทางแก้ไข:

อัปเดตโค้ดให้แทน NaN ด้วยค่าว่าง ("") และแปลงทุกค่าเป็น str
df["คำศัพท์"] = df["คำศัพท์"].fillna("").astype(str)  # ป้องกัน NaN และอ่านเป็น string เสมอ

---------------------------------------------------------------------

✨ ขอบคุณที่ใช้ Thai to IPA Converter! ✨
หากมีข้อเสนอแนะหรือปัญหา สามารถเปิด Issue หรือ Pull Request ได้เลย 💖🚀

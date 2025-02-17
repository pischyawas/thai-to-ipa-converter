import pandas as pd
import epitran

# โหลดข้อมูลจาก Excel
file_path = "ipaphoneme.xlsx"  # ใช้ชื่อไฟล์ของพี่
df = pd.read_excel(file_path)

# ใช้ Epitran แปลงเป็น IPA
epi = epitran.Epitran("tha-Thai")

def convert_to_ipa(word):
    return epi.transliterate(str(word))  # แปลงทุกค่าเป็น str ก่อนแปลง IPA

# แปลงคำในคอลัมน์ 'คำศัพท์' เป็น IPA
df["คำศัพท์"] = df["คำศัพท์"].fillna("").astype(str)  # แปลง NaN เป็น string
df["IPA"] = df["คำศัพท์"].apply(convert_to_ipa)

# บันทึกไฟล์ใหม่
output_path = "ipaphoneme_ipa.xlsx"
df.to_excel(output_path, index=False)

print(f"บันทึกไฟล์ที่: {output_path}")

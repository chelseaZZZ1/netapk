[app]
# ชื่อแอปพลิเคชันและ Package
title = FF Netcutter
package.name = ffnetcutter
package.domain = org.test

# ซอร์สโค้ดหลัก
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# เวอร์ชันแอป
version = 0.1

# ไลบรารีที่ต้องใช้ (ปรับตามที่โปรเจกต์คุณใช้จริง)
requirements = python3,kivy

# -----------------------------------------------------------------------------
# Android configuration (จุดสำคัญมาก)
# -----------------------------------------------------------------------------

# บังคับยอมรับ SDK License อัตโนมัติ (ห้ามลืมเปิดเป็น True)
android.accept_sdk_license = True

# ตั้งค่า API และ Architecture
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Orientation
orientation = portrait

# 🇬🇧 **Explanation in English**

## 💻 Professional Calculator

### 📝 General Overview  
This project is a powerful graphical calculator developed using **PyQt5** and **QDarkStyle**. Its modern interface, readable fonts, calculation history, and full keyboard input support are among its key features.

---

### 🎯 Features  
- Dark UI with minimalist, modern design  
- Interactive buttons with hover and press effects  
- Full calculation history display  
- Keyboard input support (numbers, operations, delete, execute calculation)  
- Basic mathematical operations: addition, subtraction, multiplication, division, percentage, and sign inversion  
- Responsive layout with clear **Segoe UI** font  
- Visual styling using **QDarkStyle** for a professional look

---

### 🧠 Program Architecture  
The program utilizes the main class `Calculator`, which inherits from `QMainWindow` and includes the following components:  
- `QLineEdit` for input display  
- `QTextEdit` for logging calculation history  
- `QGridLayout` for structuring the buttons  
- Signal connections to methods managing input and operations  
- Keyboard event support via `keyPressEvent`

---

### 📦 Installation & Execution

#### Requirements  
```
pip install PyQt5 qdarkstyle
```

#### Run the program  
```
python calculator.py
```

---

### 🖼️ UI Overview  
The interface includes a result display box, a history area, and a button grid. Colors are configured with a dark theme to offer a polished and user-friendly experience.

---

### 📁 File Structure  
```
calculator.py         # Main calculator program file  
README.md             # Project description in English
```

---

### 📢 Contribution  
If you have suggestions to improve the project or would like to develop an advanced version (such as scientific functions or graphical features), I’d be thrilled to collaborate!


---


# **توضیحات به زبان فارسی**


## 💻 Professioneller Taschenrechner

### 📝 توضیح کلی  
این پروژه یک ماشین حساب گرافیکی قدرتمند است که با استفاده از **PyQt5** و **QDarkStyle** طراحی شده است. رابط کاربری مدرن، فونت‌های خوانا، تاریخچه محاسبات، و پشتیبانی کامل از تعامل با صفحه‌کلید از جمله ویژگی‌های کلیدی آن هستند.

---

### 🎯 ویژگی‌ها  
- رابط کاربری تاریک با طراحی مینیمال و مدرن  
- دکمه‌های تعاملی با افکت‌های هاور و فشرده شدن  
- نمایش تاریخچه کامل محاسبات  
- پشتیبانی از ورودی صفحه‌کلید (اعداد، عملیات، حذف، اجرای محاسبه)  
- انجام عملیات پایه ریاضی: جمع، تفریق، ضرب، تقسیم، درصد، و تغییر علامت عدد  
- طراحی واکنش‌گرا با فونت خوانا **Segoe UI**  
- استفاده از استایل گرافیکی **QDarkStyle** برای جلوه‌ای حرفه‌ای

---

### 🧠 معماری برنامه  
برنامه از کلاس اصلی `Calculator` استفاده می‌کند که از `QMainWindow` ارث‌بری دارد و شامل اجزای زیر است:  
- `QLineEdit` برای نمایش ورودی‌ها  
- `QTextEdit` برای ثبت تاریخچه محاسبات  
- `QGridLayout` برای ساختاردهی دکمه‌ها  
- اتصال سیگنال‌ها به متدهای کنترل ورودی و عملیات  
- پشتیبانی از رویدادهای صفحه‌کلید با استفاده از `keyPressEvent`

---

### 📦 نصب و اجرای برنامه

#### پیش‌نیازها  
```
pip install PyQt5 qdarkstyle
```

#### اجرای برنامه  
```
python calculator.py
```

---

### 🖼️ نمایی از رابط کاربری  
رابط برنامه شامل باکس نمایش نتیجه، ناحیه تاریخچه، و صفحه‌کلید دکمه‌هاست. رنگ‌ها با استایل تاریک تنظیم شده‌اند تا تجربه‌ای حرفه‌ای و چشم‌نواز ایجاد شود.

---

### 📁 ساختار فایل‌ها  
```
calculator.py         # فایل اصلی ماشین حساب  
README.md             # معرفی پروژه به زبان فارسی
```

---

### 📢 مشارکت  
اگر پیشنهادی برای بهبود پروژه دارید یا تمایل دارید نسخه‌ی پیشرفته‌تری (مثل محاسبات علمی یا نمودارها) طراحی کنیم، خوشحال می‌شم در ادامه با هم همکاری کنیم!

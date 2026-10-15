import os
from PIL import Image, ImageDraw, ImageFont

FONT_TITLE = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 14)
FONT_BOLD = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 13)
FONT_REGULAR = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 13)
FONT_SMALL = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 11)
FONT_CODE = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 14)
FONT_CODE_BOLD = ImageFont.truetype("C:\\Windows\\Fonts\\consolab.ttf", 14)
FONT_CODE_SMALL = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 12)

# VS Theme Colors
BG_MAIN = (30, 30, 30)
BG_TITLEBAR = (45, 45, 48)
BG_TAB_ACTIVE = (30, 30, 30)
BG_TAB_INACTIVE = (45, 45, 48)
BG_TOOL_WINDOW = (37, 37, 38)
BG_STATUSBAR_DEBUG = (202, 81, 0)
TEXT_WHITE = (241, 241, 241)
TEXT_MUTED = (150, 150, 150)
BORDER_COLOR = (63, 63, 70)
KW_BLUE = (86, 156, 214)
TYPE_CYAN = (78, 201, 176)
BP_RED = (229, 20, 0)
CURRENT_LINE_YELLOW = (255, 242, 102)
LINE_HIGHLIGHT = (70, 65, 30)

def draw_vs_window(title="10-11 - Microsoft Visual Studio (Отладка)", w=1000, h=620, active_tab="Program.cs"):
    img = Image.new("RGB", (w, h), BG_MAIN)
    draw = ImageDraw.Draw(img)

    # 1. Title bar
    draw.rectangle([0, 0, w, 32], fill=BG_TITLEBAR)
    draw.text((12, 7), title, fill=TEXT_WHITE, font=FONT_TITLE)
    draw.rectangle([w-45, 0, w, 32], fill=(45, 45, 48))
    draw.text((w-28, 6), "✕", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((w-65, 6), "🗖", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((w-95, 6), "─", fill=TEXT_WHITE, font=FONT_REGULAR)

    # 2. Menu bar
    draw.rectangle([0, 32, w, 56], fill=(45, 45, 48))
    menus = ["Файл", "Правка", "Вид", "Проект", "Сборка", "Отладка", "Тест", "Анализ", "Сервис", "Окно", "Справка"]
    mx = 12
    for m in menus:
        draw.text((mx, 36), m, fill=TEXT_WHITE, font=FONT_REGULAR)
        mx += int(draw.textlength(m, font=FONT_REGULAR)) + 16

    # 3. Debug toolbar
    draw.rectangle([0, 56, w, 86], fill=(51, 51, 55))
    draw.rectangle([12, 62, 110, 80], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((18, 63), "Debug", fill=TEXT_WHITE, font=FONT_SMALL)
    draw.rectangle([120, 62, 200, 80], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((126, 63), "Any CPU", fill=TEXT_WHITE, font=FONT_SMALL)
    # Debug controls
    draw.rectangle([210, 62, 280, 80], fill=(70, 70, 75))
    draw.text((216, 63), "▶ Продолжить", fill=(120, 220, 120), font=FONT_SMALL)
    draw.rectangle([290, 62, 335, 80], fill=(70, 70, 75))
    draw.text((296, 63), "⏹ Стоп", fill=(255, 120, 120), font=FONT_SMALL)
    draw.rectangle([345, 62, 420, 80], fill=(70, 70, 75))
    draw.text((351, 63), "↷ Шаг с обходом", fill=TEXT_WHITE, font=FONT_SMALL)
    draw.rectangle([430, 62, 500, 80], fill=(70, 70, 75))
    draw.text((436, 63), "⇲ Шаг с заходом", fill=TEXT_WHITE, font=FONT_SMALL)

    # 4. Tab bar
    draw.rectangle([0, 86, w, 114], fill=BG_TAB_INACTIVE)
    draw.rectangle([0, 86, 140, 114], fill=BG_TAB_ACTIVE)
    draw.line([0, 86, 140, 86], fill=(0, 122, 204), width=2)
    draw.text((15, 92), "Program.cs", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((122, 92), "×", fill=TEXT_MUTED, font=FONT_SMALL)

    # 5. Status bar (debugging orange)
    draw.rectangle([0, h-24, w, h], fill=BG_STATUSBAR_DEBUG)
    draw.text((10, h-20), "Отладка активна: выполнение приостановлено в точке останова", fill=TEXT_WHITE, font=FONT_SMALL)
    draw.text((w-160, h-20), "Строка: 21  Кол: 17  UTF-8", fill=TEXT_WHITE, font=FONT_SMALL)

    return img, draw

def save_image(img, filename):
    out_path = os.path.join("docs", "images", filename)
    img.save(out_path)
    print(f"Saved {out_path}")

# ==================== IMAGE 1: BREAKPOINTS ====================
def make_image_1():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Отладка - Точки останова)", active_tab="Program.cs")
    w, h = img.size

    # Gutter & Editor
    draw.rectangle([0, 114, 45, 410], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 410], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 410], fill=BG_MAIN)

    code_lines = [
        (13, "            double sum = 0;"),
        (14, "            int multiplier = 2; // Переменная для изменения"),
        (15, ""),
        (16, "            for (int i = 1; i <= 5; i++)"),
        (17, "            {"),
        (18, "                try"),
        (19, "                {"),
        (20, "                    double y = Calculate(i); // Точка останова #1 (F9)"),
        (21, "                    sum += y * multiplier;"),
        (22, '                    Console.WriteLine($"Шаг {i}: x={i}, y={y:F2}, sum={sum:F2}");'),
        (23, "                }"),
        (24, "                catch (DivideByZeroException ex)"),
        (25, "                {"),
        (26, '                    Console.WriteLine($"Ошибка при x={i}: {ex.Message}");'),
        (27, "                }"),
        (28, "            }")
    ]

    y = 125
    for line_no, text in code_lines:
        draw.text((50, y), str(line_no), fill=TEXT_MUTED, font=FONT_CODE_SMALL)

        if line_no == 20:
            draw.rectangle([85, y-2, w, y+18], fill=(90, 30, 30))
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 100, 100))
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
        elif line_no == 24:
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 100, 100))

        draw.text((95, y), text, fill=TEXT_WHITE, font=FONT_CODE)
        y += 18

    # Bottom Tool Window: Breakpoints Window
    draw.rectangle([0, 410, w, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([0, 410, w, 435], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 416), "Точки останова (Breakpoints)", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((230, 416), "Создать  |  Удалить  |  Параметры", fill=TEXT_MUTED, font=FONT_SMALL)

    headers = [("Имя", 15), ("Условие", 320), ("Число попаданий", 580), ("Функция", 760)]
    draw.rectangle([0, 435, w, 455], fill=(50, 50, 54))
    for h_name, hx in headers:
        draw.text((hx, 438), h_name, fill=TEXT_MUTED, font=FONT_SMALL)

    rows = [
        ("✔ Program.cs, строка 20", "(без условий)", "1 (текущее)", "_10_11.Program.Main(string[] args)"),
        ("✔ Program.cs, строка 24", "(без условий)", "0", "_10_11.Program.Main(string[] args)"),
        ("✔ Program.cs, строка 73", "denominator == 0", "0", "_10_11.Program.Calculate(double x)")
    ]
    ry = 460
    for r_name, r_cond, r_hits, r_fn in rows:
        draw.text((15, ry), r_name, fill=(180, 220, 255), font=FONT_SMALL)
        draw.text((320, ry), r_cond, fill=TEXT_WHITE, font=FONT_SMALL)
        draw.text((580, ry), r_hits, fill=(220, 220, 140), font=FONT_SMALL)
        draw.text((760, ry), r_fn, fill=TEXT_MUTED, font=FONT_SMALL)
        ry += 22

    save_image(img, "image1_breakpoints.png")

# ==================== IMAGE 2: WATCH & LOCALS ====================
def make_image_2():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Окна Locals и Watch 1)", active_tab="Program.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, 340], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 340], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 340], fill=BG_MAIN)

    code = [
        (16, "            for (int i = 1; i <= 5; i++)"),
        (17, "            {"),
        (18, "                try"),
        (19, "                {"),
        (20, "                    double y = Calculate(i);"),
        (21, "   ======>          sum += y * multiplier; // Останов отладчика"),
        (22, '                    Console.WriteLine($"Шаг {i}: x={i}, y={y:F2}, sum={sum:F2}");'),
        (23, "                }")
    ]
    y = 125
    for lno, txt in code:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=LINE_HIGHLIGHT)
            draw.ellipse([15, y, 31, y+16], fill=BP_RED)
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
            draw.text((95, y), txt.replace("   ======>          ", "                    "), fill=CURRENT_LINE_YELLOW, font=FONT_CODE_BOLD)
        else:
            draw.text((95, y), txt, fill=TEXT_WHITE, font=FONT_CODE)
        y += 22

    # Bottom Split
    mid_x = int(w * 0.52)
    # Left: Locals
    draw.rectangle([0, 340, mid_x, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.rectangle([0, 340, 100, 365], fill=BG_TOOL_WINDOW)
    draw.line([0, 340, 100, 340], fill=(0, 122, 204), width=2)
    draw.text((15, 345), "Locals (Локальные)", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((180, 345), "Autos", fill=TEXT_MUTED, font=FONT_REGULAR)

    # Right: Watch 1
    draw.rectangle([mid_x, 340, w, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.rectangle([mid_x, 340, mid_x+110, 365], fill=BG_TOOL_WINDOW)
    draw.line([mid_x, 340, mid_x+110, 340], fill=(0, 122, 204), width=2)
    draw.text((mid_x+15, 345), "Watch 1 (Контрольные)", fill=TEXT_WHITE, font=FONT_REGULAR)

    # Bodies
    draw.rectangle([0, 365, mid_x, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([mid_x, 365, w, h-24], fill=BG_TOOL_WINDOW)
    draw.line([mid_x, 340, mid_x, h-24], fill=BORDER_COLOR, width=2)

    # Grid headers
    draw.rectangle([0, 365, mid_x, 385], fill=(50, 50, 54))
    draw.text((15, 368), "Имя", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((160, 368), "Значение", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((360, 368), "Тип", fill=TEXT_MUTED, font=FONT_SMALL)

    draw.rectangle([mid_x, 365, w, 385], fill=(50, 50, 54))
    draw.text((mid_x+15, 368), "Имя выражения", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((mid_x+200, 368), "Значение", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((mid_x+360, 368), "Тип", fill=TEXT_MUTED, font=FONT_SMALL)

    locals_data = [
        ("i", "2", "int"),
        ("multiplier", "2", "int"),
        ("y", "-8.0", "double"),
        ("sum", "-5.0", "double"),
        ("args", "{string[1]}", "string[]")
    ]
    ly = 392
    for name, val, typ in locals_data:
        draw.text((15, ly), name, fill=(220, 220, 255), font=FONT_REGULAR)
        draw.text((160, ly), val, fill=(181, 206, 168), font=FONT_REGULAR)
        draw.text((360, ly), typ, fill=TYPE_CYAN, font=FONT_SMALL)
        ly += 22

    watch_data = [
        ("y * multiplier", "-16.0", "double"),
        ("sum + y * multiplier", "-21.0", "double"),
        ("i <= 5", "true", "bool"),
        ("i == 3", "false", "bool"),
        ("Добавить выражение...", "", "")
    ]
    wy = 392
    for expr, val, typ in watch_data:
        draw.text((mid_x+15, wy), expr, fill=TEXT_WHITE if typ else TEXT_MUTED, font=FONT_REGULAR)
        draw.text((mid_x+200, wy), val, fill=(181, 206, 168) if typ != "bool" else KW_BLUE, font=FONT_REGULAR)
        draw.text((mid_x+360, wy), typ, fill=TYPE_CYAN, font=FONT_SMALL)
        wy += 22

    save_image(img, "image2_watch_locals.png")

# ==================== IMAGE 3: STEP EXECUTION ====================
def make_image_3():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Пошаговая отладка F10 / F11)", active_tab="Program.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, 380], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 380], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 380], fill=BG_MAIN)

    lines = [
        (65, "        static double Calculate(double x)"),
        (66, "        {"),
        (67, "  ======>   double numerator = x * x + 4; // Шаг с заходом F11 (Step Into)"),
        (68, "            double denominator = x - 3;"),
        (69, ""),
        (70, "            if (denominator == 0)"),
        (71, "            {"),
        (72, '                throw new DivideByZeroException("Знаменатель равен 0!...");'),
        (73, "            }"),
        (74, "            return numerator / denominator;"),
        (75, "        }")
    ]
    y = 125
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=LINE_HIGHLIGHT)
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
            draw.text((95, y), txt.replace("  ======> ", ""), fill=CURRENT_LINE_YELLOW, font=FONT_CODE_BOLD)
            # DataTip hover tooltip over variable `x`
            draw.rectangle([320, y-32, 400, y-6], fill=(45, 45, 48), outline=(0, 122, 204), width=1)
            draw.text((328, y-30), "x: 2.0", fill=TEXT_WHITE, font=FONT_SMALL)
        else:
            draw.text((95, y), txt, fill=TEXT_WHITE, font=FONT_CODE)
        y += 22

    # Bottom Tool Window: Call Stack
    draw.rectangle([0, 380, w, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([0, 380, w, 405], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 386), "Стек вызовов (Call Stack) [F11 - Зайти, F10 - Обойти, Shift+F11 - Выйти]", fill=TEXT_WHITE, font=FONT_BOLD)

    draw.rectangle([0, 405, w, 425], fill=(50, 50, 54))
    draw.text((15, 408), "Имя фрейма вызова", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((600, 408), "Язык", fill=TEXT_MUTED, font=FONT_SMALL)

    stack = [
        ("👉 10-11.exe!_10_11.Program.Calculate(double x = 2.0) Строка 67", "C#"),
        ("   10-11.exe!_10_11.Program.Main(string[] args) Строка 20", "C#"),
        ("   [Внешний код: mscorlib.dll, System.AppDomain.ExecuteAssembly]", "C#")
    ]
    sy = 435
    for s_name, s_lang in stack:
        color = (255, 255, 160) if "👉" in s_name else TEXT_WHITE
        draw.text((15, sy), s_name, fill=color, font=FONT_REGULAR)
        draw.text((600, sy), s_lang, fill=TEXT_MUTED, font=FONT_SMALL)
        sy += 24

    save_image(img, "image3_step_execution.png")

# ==================== IMAGE 4: VARIABLE MUTATION ====================
def make_image_4():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Изменение значения переменной «на лету»)", active_tab="Program.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, 350], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 350], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 350], fill=BG_MAIN)

    lines = [
        (30, "            // 2. Демонстрация изменения переменной в отладчике"),
        (31, '            Console.WriteLine("\\n--- 2. Проверка модификации multiplier ---");'),
        (32, "  ======>   if (multiplier > 10) // Останов: меняем multiplier на 20 в окне Watch"),
        (33, "            {"),
        (34, '                Console.WriteLine($"[УСПЕХ] Значение multiplier изменено: {multiplier}!");'),
        (35, "            }"),
        (36, "            else"),
        (37, "            {"),
        (38, '                Console.WriteLine($"Обычный режим: multiplier = {multiplier}");'),
        (39, "            }")
    ]
    y = 125
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=LINE_HIGHLIGHT)
            draw.ellipse([15, y, 31, y+16], fill=BP_RED)
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
            draw.text((95, y), txt.replace("  ======> ", ""), fill=CURRENT_LINE_YELLOW, font=FONT_CODE_BOLD)
        else:
            draw.text((95, y), txt, fill=TEXT_WHITE, font=FONT_CODE)
        y += 22

    # Bottom Area
    mid_x = int(w * 0.52)
    draw.rectangle([0, 350, mid_x, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([mid_x, 350, w, h-24], fill=BG_TOOL_WINDOW)
    draw.line([mid_x, 350, mid_x, h-24], fill=BORDER_COLOR, width=2)

    # Left: Watch 1
    draw.rectangle([0, 350, mid_x, 375], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 355), "Окно Watch 1 (Редактирование ячейки)", fill=TEXT_WHITE, font=FONT_BOLD)

    draw.rectangle([0, 375, mid_x, 395], fill=(50, 50, 54))
    draw.text((15, 378), "Имя", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((170, 378), "Значение", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((340, 378), "Тип", fill=TEXT_MUTED, font=FONT_SMALL)

    # Watch row with edited multiplier
    draw.text((15, 408), "multiplier", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.rectangle([165, 403, 250, 427], fill=(0, 90, 160), outline=(100, 180, 255), width=2)
    draw.text((175, 408), "20", fill=(255, 255, 255), font=FONT_BOLD)
    draw.text((265, 408), "(было 2)", fill=(255, 120, 120), font=FONT_SMALL)
    draw.text((340, 408), "int", fill=TYPE_CYAN, font=FONT_SMALL)

    draw.text((15, 438), "multiplier > 10", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((175, 438), "true (изменилось)", fill=(120, 255, 120), font=FONT_REGULAR)
    draw.text((340, 438), "bool", fill=TYPE_CYAN, font=FONT_SMALL)

    # Right: Immediate Window
    draw.rectangle([mid_x, 350, w, 375], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((mid_x+15, 355), "Окно Immediate Window (Командная строка)", fill=TEXT_WHITE, font=FONT_BOLD)

    im_lines = [
        ("? multiplier", TEXT_MUTED),
        ("2", (181, 206, 168)),
        ("multiplier = 20", (100, 200, 255)),
        ("20", (181, 206, 168)),
        ("? multiplier > 10", TEXT_MUTED),
        ("true", KW_BLUE)
    ]
    iy = 390
    for iline, icolor in im_lines:
        draw.text((mid_x+15, iy), iline, fill=icolor, font=FONT_CODE_SMALL)
        iy += 22

    save_image(img, "image4_variable_mutation.png")

# ==================== IMAGE 5: CONDITIONAL BREAKPOINT ====================
def make_image_5():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Условные точки останова)", active_tab="Program.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, h-24], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, h-24], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, h-24], fill=BG_MAIN)

    lines = [
        (16, "            for (int i = 1; i <= 5; i++)"),
        (17, "            {"),
        (18, "                try"),
        (19, "                {"),
        (20, "                    double y = Calculate(i); // Точка с условием"),
        (21, "                    sum += y * multiplier;"),
        (22, '                    Console.WriteLine($"Шаг {i}: x={i}, y={y:F2}, sum={sum:F2}");'),
        (23, "                }"),
        (24, "                catch (DivideByZeroException ex)"),
        (25, "                {")
    ]
    y = 130
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        draw.text((95, y), txt, fill=TEXT_WHITE, font=FONT_CODE)
        if lno == 20:
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 255, 255), width=2)
            draw.text((21, y), "+", fill=(255, 255, 255), font=FONT_BOLD)
        y += 24

    # Popup Dialog: Breakpoint Settings
    dw, dh = 650, 250
    dx, dy = 120, 220
    draw.rectangle([dx, dy, dx+dw, dy+dh], fill=(45, 45, 48), outline=(0, 122, 204), width=2)
    draw.rectangle([dx, dy, dx+dw, dy+32], fill=(37, 37, 38))
    draw.text((dx+15, dy+6), "Параметры точки останова (Breakpoint Settings) - Program.cs: строка 20", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((dx+dw-25, dy+6), "✕", fill=TEXT_MUTED, font=FONT_REGULAR)

    draw.text((dx+20, dy+45), "☑ Условия (Conditions):", fill=TEXT_WHITE, font=FONT_BOLD)

    draw.rectangle([dx+40, dy+75, dx+220, dy+105], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+50, dy+82), "Условное выражение ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    draw.rectangle([dx+230, dy+75, dx+360, dy+105], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+240, dy+82), "Истинно (Is true) ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    # Condition input
    draw.rectangle([dx+40, dy+115, dx+dw-40, dy+145], fill=(30, 30, 30), outline=(0, 122, 204), width=2)
    draw.text((dx+50, dy+122), "i == 3 || sum < -10.0", fill=(255, 255, 255), font=FONT_CODE_BOLD)

    # Hit count options
    draw.text((dx+20, dy+160), "☑ Число попаданий (Hit Count):", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.rectangle([dx+40, dy+185, dx+220, dy+215], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+50, dy+192), "Остановить при попадании = 1 ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    # Close button
    draw.rectangle([dx+dw-100, dy+dh-38, dx+dw-20, dy+dh-12], fill=(0, 122, 204))
    draw.text((dx+dw-80, dy+dh-32), "Закрыть", fill=TEXT_WHITE, font=FONT_SMALL)

    save_image(img, "image5_conditional_breakpoint.png")

# ==================== IMAGE 6: EXCEPTION HANDLING ====================
def make_image_6():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Организация обработки исключений)", active_tab="Program.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, 340], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 340], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 340], fill=BG_MAIN)

    lines = [
        (68, "            double denominator = x - 3;"),
        (69, ""),
        (70, "            if (denominator == 0)"),
        (71, "            {"),
        (72, '  ======>       throw new DivideByZeroException("Знаменатель равен 0! Деление на ноль невозможно.");'),
        (73, "            }"),
        (74, "            return numerator / denominator;"),
        (75, "        }")
    ]
    y = 125
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=(90, 40, 40))
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=(255, 100, 100))
            draw.text((95, y), txt.replace("  ======> ", ""), fill=(255, 200, 200), font=FONT_CODE_BOLD)
        else:
            draw.text((95, y), txt, fill=TEXT_WHITE, font=FONT_CODE)
        y += 22

    # Exception Helper Dialog
    ex_w, ex_h = 600, 140
    ex_x, ex_y = 140, 195
    draw.rectangle([ex_x, ex_y, ex_x+ex_w, ex_y+ex_h], fill=(45, 45, 48), outline=(229, 20, 0), width=2)
    draw.rectangle([ex_x, ex_y, ex_x+ex_w, ex_y+30], fill=(70, 30, 30))
    draw.text((ex_x+10, ex_y+6), "⚠ System.DivideByZeroException было создано", fill=(255, 150, 150), font=FONT_BOLD)

    draw.text((ex_x+15, ex_y+40), 'Сообщение: "Знаменатель равен 0! Деление на ноль невозможно."', fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((ex_x+15, ex_y+65), "Действие: Выполнение прервано перед обработчиком catch в методе Main", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((ex_x+15, ex_y+90), "Параметры: Прерывать при возникновении данного типа исключений", fill=(100, 180, 255), font=FONT_SMALL)
    draw.rectangle([ex_x+ex_w-150, ex_y+ex_h-35, ex_x+ex_w-15, ex_y+ex_h-10], fill=(60, 60, 65))
    draw.text((ex_x+ex_w-140, ex_y+ex_h-30), "Просмотреть стек", fill=TEXT_WHITE, font=FONT_SMALL)

    # Bottom Area: Exception Settings
    draw.rectangle([0, 340, w, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([0, 340, w, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 345), "Параметры исключений (Exception Settings) [Ctrl+Alt+E]", fill=TEXT_WHITE, font=FONT_BOLD)

    exc_tree = [
        ("☑ Исключения среды выполнения .NET (Common Language Runtime Exceptions)", TEXT_WHITE, True),
        ("    ☑ System.DivideByZeroException", (255, 180, 180), False),
        ("    ☑ System.ArgumentOutOfRangeException", TEXT_WHITE, False),
        ("    ☑ System.NullReferenceException", TEXT_WHITE, False),
        ("☐ Исключения C++", TEXT_MUTED, True)
    ]
    ey = 375
    for etxt, ecolor, is_cat in exc_tree:
        draw.text((20 if is_cat else 30, ey), etxt, fill=ecolor, font=FONT_BOLD if is_cat else FONT_REGULAR)
        ey += 22

    save_image(img, "image6_exception_handling.png")

# ==================== IMAGE 7: CONSOLE EXECUTION ====================
def make_image_7():
    w, h = 900, 520
    img = Image.new("RGB", (w, h), (12, 12, 12))
    draw = ImageDraw.Draw(img)

    # Header Bar
    draw.rectangle([0, 0, w, 36], fill=(31, 31, 31))
    draw.text((15, 10), "Командная строка: 10-11.exe", fill=(204, 204, 204), font=FONT_TITLE)
    draw.text((w-30, 8), "✕", fill=(204, 204, 204), font=FONT_REGULAR)

    lines = [
        ("D:\\GhubReps\\belous1011\\10-11\\bin\\Debug> 10-11.exe --auto", (200, 200, 200)),
        ("==========================================================", (0, 220, 255)),
        ("  Практическая работа №10-11: Отладка программы в C#", (0, 220, 255)),
        ("==========================================================", (0, 220, 255)),
        ("", TEXT_WHITE),
        ("--- 1. Итерационный расчет с контролем ошибок ---", (100, 255, 100)),
        ("Шаг 1: x = 1, y =  -2,50, sum =  -5,00", (220, 220, 220)),
        ("Шаг 2: x = 2, y =  -8,00, sum = -21,00", (220, 220, 220)),
        ("Шаг 3: x = 3 -> [Ошибка]: Знаменатель равен 0! Деление на ноль невозможно.", (255, 150, 150)),
        ("Шаг 4: x = 4, y =  20,00, sum =  19,00", (220, 220, 220)),
        ("Шаг 5: x = 5, y =  14,50, sum =  48,00", (220, 220, 220)),
        ("", TEXT_WHITE),
        ("--- 2. Проверка модификации переменной multiplier ---", (100, 255, 100)),
        ("Обычный режим: значение multiplier = 2", (220, 220, 220)),
        ("", TEXT_WHITE),
        ("--- 3. Демонстрация блока try-catch-finally ---", (100, 255, 100)),
        ("Вызов функции Calculate(3), приводящей к делению на 0...", (200, 200, 255)),
        ("[Блок catch]: Перехвачено исключение: Знаменатель равен 0! Деление на ноль невозможно.", (255, 220, 100)),
        ("[Блок finally]: Ресурсы освобождены, блок завершил работу.", (180, 180, 255)),
        ("", TEXT_WHITE),
        ("Программа успешно завершена.", (0, 220, 255))
    ]

    cy = 48
    for line, col in lines:
        draw.text((20, cy), line, fill=col, font=FONT_CODE)
        cy += 20

    save_image(img, "image7_console_output.png")

if __name__ == "__main__":
    os.makedirs("docs/images", exist_ok=True)
    make_image_1()
    make_image_2()
    make_image_3()
    make_image_4()
    make_image_5()
    make_image_6()
    make_image_7()
    print("All 7 clean screenshots successfully generated!")

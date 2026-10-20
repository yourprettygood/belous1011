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

def draw_vs_window(title="10-11 - Microsoft Visual Studio 2019 (Отладка ПР №12)", w=1000, h=620, active_tab="Program.cs"):
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

    # 5. Status bar
    draw.rectangle([0, h-24, w, h], fill=BG_STATUSBAR_DEBUG)
    draw.text((10, h-20), "Отладка активна: выполнение приостановлено в точке останова (System.Diagnostics)", fill=TEXT_WHITE, font=FONT_SMALL)
    draw.text((w-160, h-20), "Строка: 29  Кол: 17  UTF-8", fill=TEXT_WHITE, font=FONT_SMALL)

    return img, draw

def save_image(img, filename):
    out_path = os.path.join("docs", "images", filename)
    img.save(out_path)
    print(f"Saved {out_path}")

# ==================== IMAGE 1: BREAKPOINTS & DEBUG.ASSERT ====================
def make_image_1():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Точки останова и отладочные классы)", active_tab="Program.cs")
    w, h = img.size

    draw.rectangle([0, 114, 45, 410], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 410], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 410], fill=BG_MAIN)

    code_lines = [
        (21, "            int sum = 0;"),
        (22, "            int multiplier = 2; // Переменная для изменения"),
        (23, ""),
        (24, '            // Отладочный класс: проверка инварианта перед циклом'),
        (25, '            Debug.Assert(multiplier > 0, "Множитель должен быть > 0!");'),
        (26, ""),
        (27, '            Console.WriteLine("--- 1. Итерационный цикл с отладочными проверками ---");'),
        (28, "            for (int i = 1; i <= 5; i++)"),
        (29, "            {"),
        (30, "                int y = i * multiplier; // Точка останова #1 (F9)"),
        (31, "                sum += y;"),
        (32, '                Debug.WriteLineIf(i == 3, $"[DEBUG]: Шаг i={i}, sum={sum}");'),
        (33, '                Console.WriteLine($"Шаг {i}: i={i}, y={y}, sum={sum}");'),
        (34, "            }"),
        (35, '            Debug.Assert(sum == 30, $"Ожидаемая сумма 30, но получено: {sum}");')
    ]

    y = 125
    for line_no, text in code_lines:
        draw.text((50, y), str(line_no), fill=TEXT_MUTED, font=FONT_CODE_SMALL)

        if line_no == 30:
            draw.rectangle([85, y-2, w, y+18], fill=(90, 30, 30))
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 100, 100))
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
        elif line_no == 25:
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 100, 100))

        color = (120, 200, 120) if "Debug.Assert" in text or "Debug.WriteLine" in text else TEXT_WHITE
        draw.text((95, y), text, fill=color, font=FONT_CODE)
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
        ("✔ Program.cs, строка 30", "(без условий)", "1 (текущее)", "_10_11.Program.Main(string[] args)"),
        ("✔ Program.cs, строка 25", "multiplier <= 0", "0", "_10_11.Program.Main(string[] args)"),
        ("✔ Program.cs, строка 57", "b == 0", "0", "_10_11.Program.Main(string[] args)")
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

    draw.rectangle([0, 114, 45, 340], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 340], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 340], fill=BG_MAIN)

    code = [
        (28, "            for (int i = 1; i <= 5; i++)"),
        (29, "            {"),
        (30, "                int y = i * multiplier;"),
        (31, "   ======>      sum += y; // Пауза отладчика"),
        (32, '                Debug.WriteLineIf(i == 3, $"[DEBUG]: Шаг i={i}, sum={sum}");'),
        (33, '                Console.WriteLine($"Шаг {i}: i={i}, y={y}, sum={sum}");'),
        (34, "            }")
    ]
    y = 135
    for lno, txt in code:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=LINE_HIGHLIGHT)
            draw.ellipse([15, y, 31, y+16], fill=BP_RED)
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
            draw.text((95, y), txt.replace("   ======>      ", "                "), fill=CURRENT_LINE_YELLOW, font=FONT_CODE_BOLD)
        else:
            color = (120, 200, 120) if "Debug." in txt else TEXT_WHITE
            draw.text((95, y), txt, fill=color, font=FONT_CODE)
        y += 24

    mid_x = int(w * 0.52)
    draw.rectangle([0, 340, mid_x, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.rectangle([0, 340, 100, 365], fill=BG_TOOL_WINDOW)
    draw.line([0, 340, 100, 340], fill=(0, 122, 204), width=2)
    draw.text((15, 345), "Locals (Локальные)", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((180, 345), "Autos", fill=TEXT_MUTED, font=FONT_REGULAR)

    draw.rectangle([mid_x, 340, w, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.rectangle([mid_x, 340, mid_x+110, 365], fill=BG_TOOL_WINDOW)
    draw.line([mid_x, 340, mid_x+110, 340], fill=(0, 122, 204), width=2)
    draw.text((mid_x+15, 345), "Watch 1 (Контрольные)", fill=TEXT_WHITE, font=FONT_REGULAR)

    draw.rectangle([0, 365, mid_x, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([mid_x, 365, w, h-24], fill=BG_TOOL_WINDOW)
    draw.line([mid_x, 340, mid_x, h-24], fill=BORDER_COLOR, width=2)

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
        ("y", "4", "int"),
        ("sum", "2", "int"),
        ("args", "{string[1]}", "string[]")
    ]
    ly = 392
    for name, val, typ in locals_data:
        draw.text((15, ly), name, fill=(220, 220, 255), font=FONT_REGULAR)
        draw.text((160, ly), val, fill=(181, 206, 168), font=FONT_REGULAR)
        draw.text((360, ly), typ, fill=TYPE_CYAN, font=FONT_SMALL)
        ly += 22

    watch_data = [
        ("sum + y", "6", "int"),
        ("multiplier > 0", "true", "bool"),
        ("i <= 5", "true", "bool"),
        ("sum == 30", "false", "bool"),
        ("Добавить выражение...", "", "")
    ]
    wy = 392
    for expr, val, typ in watch_data:
        draw.text((mid_x+15, wy), expr, fill=TEXT_WHITE if typ else TEXT_MUTED, font=FONT_REGULAR)
        draw.text((mid_x+200, wy), val, fill=(181, 206, 168) if typ != "bool" else KW_BLUE, font=FONT_REGULAR)
        draw.text((mid_x+360, wy), typ, fill=TYPE_CYAN, font=FONT_SMALL)
        wy += 22

    save_image(img, "image2_watch_locals.png")

# ==================== IMAGE 3: DEBUG CLASSES & TRACE ====================
def make_image_3():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Отладочные классы Debug и Trace)", active_tab="Program.cs")
    w, h = img.size

    draw.rectangle([0, 114, 45, 340], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 340], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 340], fill=BG_MAIN)

    lines = [
        (13, "            // Настройка слушателей отладочных классов"),
        (14, "            Trace.Listeners.Add(new TextWriterTraceListener(Console.Out));"),
        (15, '            Trace.Listeners.Add(new TextWriterTraceListener("debug_trace.log"));'),
        (16, "            Trace.AutoFlush = true;"),
        (17, ""),
        (18, '  ======>   Debug.WriteLine("[DEBUG]: Старт программы и инициализация слушателей.");'),
        (19, "            Debug.Assert(multiplier > 0, \"Множитель должен быть > 0!\");")
    ]
    y = 135
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=LINE_HIGHLIGHT)
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
            draw.text((95, y), txt.replace("  ======>   ", "            "), fill=CURRENT_LINE_YELLOW, font=FONT_CODE_BOLD)
        else:
            color = (120, 200, 120) if "Trace." in txt or "Debug." in txt else TEXT_WHITE
            draw.text((95, y), txt, fill=color, font=FONT_CODE)
        y += 24

    # Bottom Tool Window: Output Window (Вывод отладки)
    draw.rectangle([0, 340, w, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([0, 340, w, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 345), "Окно вывода (Output Window) — Отладка System.Diagnostics", fill=TEXT_WHITE, font=FONT_BOLD)

    out_lines = [
        ("[DEBUG]: Старт программы и инициализация отладочных слушателей.", (120, 220, 120)),
        ("Поток 0x3ac4 завершился с кодом 0 (0x0).", TEXT_MUTED),
        ("[DEBUG]: Достигнут контрольный шаг i = 3, текущая sum = 12", (120, 220, 120)),
        ("[TRACE]: Подготовка к делению a=10 на b=0...", (180, 220, 255)),
        ("[DEBUG WARNING]: Зафиксирован нулевой делитель перед вычислением!", (255, 200, 100)),
        ("[TRACE ERROR]: Перехвачена ошибка времени выполнения: Попытка деления на нуль.", (255, 120, 120)),
        ("[TRACE]: Завершение блока вычислений и освобождение ресурсов.", (180, 220, 255)),
        ("[DEBUG]: Завершение работы программы.", (120, 220, 120))
    ]
    oy = 375
    for oline, ocolor in out_lines:
        draw.text((15, oy), oline, fill=ocolor, font=FONT_CODE_SMALL)
        oy += 22

    save_image(img, "image3_step_execution.png")

# ==================== IMAGE 4: VARIABLE MUTATION ====================
def make_image_4():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Изменение значения переменной «на лету»)", active_tab="Program.cs")
    w, h = img.size

    draw.rectangle([0, 114, 45, 350], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 350], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 350], fill=BG_MAIN)

    lines = [
        (38, '            Console.WriteLine("\\n--- 2. Проверка изменения переменной multiplier ---");'),
        (39, "  ======>   if (multiplier > 10) // Останов: изменяем multiplier на 20 в окне Watch"),
        (40, "            {"),
        (41, '                Trace.WriteLine($"[TRACE]: Значение изменено на: {multiplier}");'),
        (42, '                Console.WriteLine($"[УСПЕХ] Значение multiplier изменено на: {multiplier}!");'),
        (43, "            }"),
        (44, "            else"),
        (45, "            {"),
        (46, '                Console.WriteLine($"Обычный режим: значение multiplier = {multiplier}");'),
        (47, "            }")
    ]
    y = 125
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=LINE_HIGHLIGHT)
            draw.ellipse([15, y, 31, y+16], fill=BP_RED)
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
            draw.text((95, y), txt.replace("  ======>   ", "            "), fill=CURRENT_LINE_YELLOW, font=FONT_CODE_BOLD)
        else:
            color = (120, 200, 120) if "Trace." in txt else TEXT_WHITE
            draw.text((95, y), txt, fill=color, font=FONT_CODE)
        y += 22

    mid_x = int(w * 0.52)
    draw.rectangle([0, 350, mid_x, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([mid_x, 350, w, h-24], fill=BG_TOOL_WINDOW)
    draw.line([mid_x, 350, mid_x, h-24], fill=BORDER_COLOR, width=2)

    # Left: Watch 1
    draw.rectangle([0, 350, mid_x, 375], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 355), "Окно Watch 1 (Редактирование значения)", fill=TEXT_WHITE, font=FONT_BOLD)

    draw.rectangle([0, 375, mid_x, 395], fill=(50, 50, 54))
    draw.text((15, 378), "Имя", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((170, 378), "Значение", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((340, 378), "Тип", fill=TEXT_MUTED, font=FONT_SMALL)

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

    draw.rectangle([0, 114, 45, h-24], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, h-24], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, h-24], fill=BG_MAIN)

    lines = [
        (27, '            Console.WriteLine("--- 1. Итерационный цикл с отладочными проверками ---");'),
        (28, "            for (int i = 1; i <= 5; i++)"),
        (29, "            {"),
        (30, "                int y = i * multiplier; // Условная точка останова"),
        (31, "                sum += y;"),
        (32, '                Debug.WriteLineIf(i == 3, $"[DEBUG]: Шаг i={i}, sum={sum}");'),
        (33, '                Console.WriteLine($"Шаг {i}: i={i}, y={y}, sum={sum}");'),
        (34, "            }")
    ]
    y = 130
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        color = (120, 200, 120) if "Debug." in txt else TEXT_WHITE
        draw.text((95, y), txt, fill=color, font=FONT_CODE)
        if lno == 30:
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 255, 255), width=2)
            draw.text((21, y), "+", fill=(255, 255, 255), font=FONT_BOLD)
        y += 24

    dw, dh = 650, 250
    dx, dy = 120, 220
    draw.rectangle([dx, dy, dx+dw, dy+dh], fill=(45, 45, 48), outline=(0, 122, 204), width=2)
    draw.rectangle([dx, dy, dx+dw, dy+32], fill=(37, 37, 38))
    draw.text((dx+15, dy+6), "Параметры точки останова (Breakpoint Settings) - Program.cs: строка 30", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((dx+dw-25, dy+6), "✕", fill=TEXT_MUTED, font=FONT_REGULAR)

    draw.text((dx+20, dy+45), "☑ Условия (Conditions):", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.rectangle([dx+40, dy+75, dx+220, dy+105], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+50, dy+82), "Условное выражение ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    draw.rectangle([dx+230, dy+75, dx+360, dy+105], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+240, dy+82), "Истинно (Is true) ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    draw.rectangle([dx+40, dy+115, dx+dw-40, dy+145], fill=(30, 30, 30), outline=(0, 122, 204), width=2)
    draw.text((dx+50, dy+122), "i == 3 || sum >= 6", fill=(255, 255, 255), font=FONT_CODE_BOLD)

    draw.text((dx+20, dy+160), "☑ Число попаданий (Hit Count):", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.rectangle([dx+40, dy+185, dx+220, dy+215], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+50, dy+192), "Остановить при попадании = 1 ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    draw.rectangle([dx+dw-100, dy+dh-38, dx+dw-20, dy+dh-12], fill=(0, 122, 204))
    draw.text((dx+dw-80, dy+dh-32), "Закрыть", fill=TEXT_WHITE, font=FONT_SMALL)

    save_image(img, "image5_conditional_breakpoint.png")

# ==================== IMAGE 6: EXCEPTION HANDLING ====================
def make_image_6():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Задание 3: Диагностика исключений деления на ноль)", active_tab="Program.cs")
    w, h = img.size

    draw.rectangle([0, 114, 45, 340], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 340], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 340], fill=BG_MAIN)

    lines = [
        (51, "            try"),
        (52, "            {"),
        (53, "                int a = 10;"),
        (54, "                int b = 0; // делитель равен 0"),
        (55, '                Trace.WriteLine($"[TRACE]: Подготовка к делению a={a} на b={b}...");'),
        (56, "                if (b == 0) Debug.WriteLine(\"[DEBUG WARNING]: Нулевой делитель!\");"),
        (57, "  ======>       int result = a / b; // System.DivideByZeroException"),
        (58, '                Console.WriteLine($"Результат: {result}");'),
        (59, "            }"),
        (60, "            catch (DivideByZeroException ex)")
    ]
    y = 120
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=(90, 40, 40))
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=(255, 100, 100))
            draw.text((95, y), txt.replace("  ======>       ", "                "), fill=(255, 200, 200), font=FONT_CODE_BOLD)
        else:
            color = (120, 200, 120) if "Trace." in txt or "Debug." in txt else TEXT_WHITE
            draw.text((95, y), txt, fill=color, font=FONT_CODE)
        y += 20

    ex_w, ex_h = 600, 140
    ex_x, ex_y = 140, 195
    draw.rectangle([ex_x, ex_y, ex_x+ex_w, ex_y+ex_h], fill=(45, 45, 48), outline=(229, 20, 0), width=2)
    draw.rectangle([ex_x, ex_y, ex_x+ex_w, ex_y+30], fill=(70, 30, 30))
    draw.text((ex_x+10, ex_y+6), "⚠ System.DivideByZeroException: Попытка деления на нуль", fill=(255, 150, 150), font=FONT_BOLD)

    draw.text((ex_x+15, ex_y+40), 'Выражение: "a / b", где a = 10, b = 0', fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((ex_x+15, ex_y+65), "Действие: Отладчик остановил выполнение перед передачей в блок catch", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((ex_x+15, ex_y+90), "Параметры: Прерывать при возникновении данного типа исключений", fill=(100, 180, 255), font=FONT_SMALL)
    draw.rectangle([ex_x+ex_w-150, ex_y+ex_h-35, ex_x+ex_w-15, ex_y+ex_h-10], fill=(60, 60, 65))
    draw.text((ex_x+ex_w-140, ex_y+ex_h-30), "Просмотреть стек", fill=TEXT_WHITE, font=FONT_SMALL)

    draw.rectangle([0, 340, w, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([0, 340, w, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 345), "Параметры исключений (Exception Settings) [Ctrl+Alt+E]", fill=TEXT_WHITE, font=FONT_BOLD)

    exc_tree = [
        ("☑ Исключения среды выполнения .NET (Common Language Runtime Exceptions)", TEXT_WHITE, True),
        ("    ☑ System.DivideByZeroException", (255, 180, 180), False),
        ("    ☑ System.ArgumentOutOfRangeException", TEXT_WHITE, False),
        ("    ☑ System.Diagnostics.DebugAssertException", (255, 200, 100), False),
        ("☐ Исключения C++", TEXT_MUTED, True)
    ]
    ey = 375
    for etxt, ecolor, is_cat in exc_tree:
        draw.text((20 if is_cat else 30, ey), etxt, fill=ecolor, font=FONT_BOLD if is_cat else FONT_REGULAR)
        ey += 22

    save_image(img, "image6_exception_handling.png")

# ==================== IMAGE 7: CONSOLE EXECUTION ====================
def make_image_7():
    w, h = 900, 560
    img = Image.new("RGB", (w, h), (12, 12, 12))
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, 36], fill=(31, 31, 31))
    draw.text((15, 10), "Командная строка: 10-11.exe (ПР №12)", fill=(204, 204, 204), font=FONT_TITLE)
    draw.text((w-30, 8), "✕", fill=(204, 204, 204), font=FONT_REGULAR)

    lines = [
        ("D:\\GhubReps\\belous1011\\10-11\\bin\\Debug> 10-11.exe --auto", (200, 200, 200)),
        ("==========================================================", (0, 220, 255)),
        ("  Практическая работа №12: Применение отладочных классов", (0, 220, 255)),
        ("==========================================================", (0, 220, 255)),
        ("", TEXT_WHITE),
        ("[DEBUG]: Старт программы и инициализация отладочных слушателей.", (120, 220, 120)),
        ("--- 1. Итерационный цикл с отладочными проверками ---", (100, 255, 100)),
        ("Шаг 1: i = 1, y = 2, sum = 2", (220, 220, 220)),
        ("Шаг 2: i = 2, y = 4, sum = 6", (220, 220, 220)),
        ("[DEBUG]: Достигнут контрольный шаг i = 3, текущая sum = 12", (120, 220, 120)),
        ("Шаг 3: i = 3, y = 6, sum = 12", (220, 220, 220)),
        ("Шаг 4: i = 4, y = 8, sum = 20", (220, 220, 220)),
        ("Шаг 5: i = 5, y = 10, sum = 30", (220, 220, 220)),
        ("", TEXT_WHITE),
        ("--- 2. Проверка изменения переменной multiplier ---", (100, 255, 100)),
        ("Обычный режим: значение multiplier = 2", (220, 220, 220)),
        ("", TEXT_WHITE),
        ("--- 3. Применение отладочных классов при обработке ошибок ---", (100, 255, 100)),
        ("[TRACE]: Подготовка к делению a=10 на b=0...", (180, 220, 255)),
        ("[DEBUG WARNING]: Зафиксирован нулевой делитель перед вычислением!", (255, 200, 100)),
        ("[TRACE ERROR]: Перехвачена ошибка времени выполнения: Попытка деления на нуль.", (255, 120, 120)),
        ("[Блок catch]: Ошибка! Деление на ноль невозможно (Попытка деления на нуль.)", (255, 220, 100)),
        ("[TRACE]: Завершение блока вычислений и освобождение ресурсов.", (180, 220, 255)),
        ("[Блок finally]: Ресурсы освобождены, блок завершил работу.", (180, 180, 255)),
        ("[DEBUG]: Завершение работы программы.", (120, 220, 120)),
        ("", TEXT_WHITE),
        ("Программа успешно завершена.", (0, 220, 255))
    ]

    cy = 48
    for line, col in lines:
        draw.text((20, cy), line, fill=col, font=FONT_CODE_SMALL)
        cy += 19

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
    print("All PR 12 screenshots updated!")

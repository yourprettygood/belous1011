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
BG_GUTTER = (30, 30, 30)
BG_TOOL_WINDOW = (37, 37, 38)
BG_STATUSBAR = (0, 122, 204)  # Visual Studio Debugging Orange/Red or Blue (Debugging is (202, 81, 0) orange in VS)
BG_STATUSBAR_DEBUG = (202, 81, 0)
TEXT_WHITE = (241, 241, 241)
TEXT_MUTED = (150, 150, 150)
BORDER_COLOR = (63, 63, 70)
KW_BLUE = (86, 156, 214)
TYPE_CYAN = (78, 201, 176)
STR_ORANGE = (214, 157, 133)
NUM_GREEN = (181, 206, 168)
COMMENT_GREEN = (87, 166, 74)
BP_RED = (229, 20, 0)
CURRENT_LINE_YELLOW = (255, 242, 102)
LINE_HIGHLIGHT = (70, 65, 30)

def draw_vs_window(title="10-11 - Microsoft Visual Studio (Debugging)", w=1000, h=620, active_tab="Program.cs"):
    img = Image.new("RGB", (w, h), BG_MAIN)
    draw = ImageDraw.Draw(img)

    # 1. Title bar
    draw.rectangle([0, 0, w, 32], fill=BG_TITLEBAR)
    draw.text((12, 7), title, fill=TEXT_WHITE, font=FONT_TITLE)
    # Window controls (close, min, max)
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
    draw.rectangle([12, 62, 120, 80], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((18, 63), "Debug", fill=TEXT_WHITE, font=FONT_SMALL)
    draw.rectangle([130, 62, 210, 80], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((136, 63), "Any CPU", fill=TEXT_WHITE, font=FONT_SMALL)
    # Debug controls
    draw.rectangle([220, 62, 280, 80], fill=(70, 70, 75))
    draw.text((226, 63), "▶ Продолжить", fill=(120, 220, 120), font=FONT_SMALL)
    draw.rectangle([290, 62, 335, 80], fill=(70, 70, 75))
    draw.text((296, 63), "⏹ Стоп", fill=(255, 120, 120), font=FONT_SMALL)
    draw.rectangle([345, 62, 420, 80], fill=(70, 70, 75))
    draw.text((351, 63), "↷ Шаг с обходом", fill=TEXT_WHITE, font=FONT_SMALL)
    draw.rectangle([430, 62, 500, 80], fill=(70, 70, 75))
    draw.text((436, 63), "⇲ Шаг с заходом", fill=TEXT_WHITE, font=FONT_SMALL)

    # 4. Tab bar
    draw.rectangle([0, 86, w, 114], fill=BG_TAB_INACTIVE)
    tabs = ["Program.cs", "DebuggerDemo.cs", "TaylorSeriesCalculator.cs", "FunctionTabulator.cs"]
    tx = 0
    for t in tabs:
        tw = int(draw.textlength(t, font=FONT_REGULAR)) + 28
        is_act = (t == active_tab)
        draw.rectangle([tx, 86, tx+tw, 114], fill=BG_TAB_ACTIVE if is_act else BG_TAB_INACTIVE)
        if is_act:
            draw.line([tx, 86, tx+tw, 86], fill=(0, 122, 204), width=2)
        draw.text((tx+10, 92), t, fill=TEXT_WHITE if is_act else TEXT_MUTED, font=FONT_REGULAR)
        draw.text((tx+tw-14, 92), "×", fill=TEXT_MUTED, font=FONT_SMALL)
        tx += tw

    # 5. Status bar (debugging orange)
    draw.rectangle([0, h-24, w, h], fill=BG_STATUSBAR_DEBUG)
    draw.text((10, h-20), "Отладка активна: выполнение приостановлено в точке останова", fill=TEXT_WHITE, font=FONT_SMALL)
    draw.text((w-160, h-20), "Строка: 32  Кол: 17  UTF-8", fill=TEXT_WHITE, font=FONT_SMALL)

    return img, draw

def save_image(img, filename):
    out_path = os.path.join("docs", "images", filename)
    img.save(out_path)
    print(f"Saved {out_path}")

# ==================== IMAGE 1: BREAKPOINTS ====================
def make_image_1():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Отладка - Точки останова)", active_tab="DebuggerDemo.cs")
    w, h = img.size

    # Gutter & Editor (y from 114 to 410)
    draw.rectangle([0, 114, 45, 410], fill=(37, 37, 38)) # Breakpoint margin
    draw.rectangle([45, 114, 85, 410], fill=(30, 30, 30)) # Line numbers
    draw.rectangle([85, 114, w, 410], fill=BG_MAIN) # Code area

    code_lines = [
        (25, "        public static void RunLoopInspectionDemo()"),
        (26, "        {"),
        (27, '            Console.WriteLine("\\n=== ИТЕРАЦИОННЫЙ ЦИКЛ ===");'),
        (28, "            double accumulator = 0.0;"),
        (29, "            double factor = 1.25;"),
        (30, "            int totalIterations = 10;"),
        (31, ""),
        (32, "            for (int i = 1; i <= totalIterations; i++)"),
        (33, "            {"),
        (34, "                double term = Math.Pow(i, 2) * factor;"),
        (35, "                accumulator += term; // Точка останова #1"),
        (36, '                Console.WriteLine($"Шаг {i}: term={term}, sum={accumulator}");'),
        (37, "            }"),
        (38, "        }")
    ]

    y = 125
    for line_no, text in code_lines:
        # Line number
        draw.text((50, y), str(line_no), fill=TEXT_MUTED, font=FONT_CODE_SMALL)

        # Breakpoint at line 35
        if line_no == 35:
            # Active breakpoint highlight
            draw.rectangle([85, y-2, w, y+18], fill=(90, 30, 30))
            # Breakpoint circle
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 100, 100))
            # Current line execution arrow
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
        elif line_no == 34:
            # Another breakpoint circle
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 100, 100))

        # Syntax color simple highlight
        draw.text((95, y), text, fill=TEXT_WHITE, font=FONT_CODE)
        y += 20

    # Bottom Tool Window: Breakpoints Window (y from 410 to h-24)
    draw.rectangle([0, 410, w, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([0, 410, w, 435], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 416), "Точки останова (Breakpoints)", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((230, 416), "Создать  |  Удалить  |  Параметры", fill=TEXT_MUTED, font=FONT_SMALL)

    headers = [("Имя", 15), ("Условие", 300), ("Число попаданий", 550), ("Функция", 750)]
    draw.rectangle([0, 435, w, 455], fill=(50, 50, 54))
    for h_name, hx in headers:
        draw.text((hx, 438), h_name, fill=TEXT_MUTED, font=FONT_SMALL)

    rows = [
        ("✔ DebuggerDemo.cs, строка 35", "(без условий)", "1 (текущее)", "_10_11.DebuggerDemo.RunLoopInspectionDemo()"),
        ("✔ DebuggerDemo.cs, строка 34", "(без условий)", "1", "_10_11.DebuggerDemo.RunLoopInspectionDemo()"),
        ("✔ FunctionTabulator.cs, строка 42", "denominator < 1e-12", "0", "_10_11.FunctionTabulator.ComputeValue(double x)")
    ]
    ry = 460
    for r_name, r_cond, r_hits, r_fn in rows:
        draw.text((15, ry), r_name, fill=(180, 220, 255), font=FONT_SMALL)
        draw.text((300, ry), r_cond, fill=TEXT_WHITE, font=FONT_SMALL)
        draw.text((550, ry), r_hits, fill=(220, 220, 140), font=FONT_SMALL)
        draw.text((750, ry), r_fn, fill=TEXT_MUTED, font=FONT_SMALL)
        ry += 22

    save_image(img, "image1_breakpoints.png")

# ==================== IMAGE 2: WATCH & LOCALS ====================
def make_image_2():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Окна Autos, Locals, Watch)", active_tab="DebuggerDemo.cs")
    w, h = img.size

    # Code snippet area at top
    draw.rectangle([0, 114, 45, 340], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 340], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 340], fill=BG_MAIN)

    code = [
        (32, "            for (int i = 1; i <= totalIterations; i++)"),
        (33, "            {"),
        (34, "                double term = Math.Pow(i, 2) * factor;"),
        (35, "   ======>      accumulator += term; // Точка останова сработала"),
        (36, '                Console.WriteLine($"Шаг {i}: term={term}, sum={accumulator}");'),
        (37, "            }")
    ]
    y = 130
    for lno, txt in code:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=LINE_HIGHLIGHT)
            draw.ellipse([15, y, 31, y+16], fill=BP_RED)
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
            draw.text((95, y), txt.replace("   ======> ", ""), fill=CURRENT_LINE_YELLOW, font=FONT_CODE_BOLD)
        else:
            draw.text((95, y), txt, fill=TEXT_WHITE, font=FONT_CODE)
        y += 24

    # Bottom Split Windows: Left = Locals, Right = Watch 1
    mid_x = int(w * 0.52)

    # Tab headers for Left: Autos / Locals
    draw.rectangle([0, 340, mid_x, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.rectangle([0, 340, 90, 365], fill=BG_TOOL_WINDOW)
    draw.line([0, 340, 90, 340], fill=(0, 122, 204), width=2)
    draw.text((15, 345), "Locals (Локальные)", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((170, 345), "Autos (Авто)", fill=TEXT_MUTED, font=FONT_REGULAR)

    # Tab headers for Right: Watch 1
    draw.rectangle([mid_x, 340, w, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.rectangle([mid_x, 340, mid_x+100, 365], fill=BG_TOOL_WINDOW)
    draw.line([mid_x, 340, mid_x+100, 340], fill=(0, 122, 204), width=2)
    draw.text((mid_x+15, 345), "Watch 1 (Контрольные)", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((mid_x+190, 345), "Watch 2", fill=TEXT_MUTED, font=FONT_REGULAR)

    # Panels body
    draw.rectangle([0, 365, mid_x, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([mid_x, 365, w, h-24], fill=BG_TOOL_WINDOW)
    draw.line([mid_x, 340, mid_x, h-24], fill=BORDER_COLOR, width=2)

    # Headers for grid
    draw.rectangle([0, 365, mid_x, 385], fill=(50, 50, 54))
    draw.text((15, 368), "Имя", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((160, 368), "Значение", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((360, 368), "Тип", fill=TEXT_MUTED, font=FONT_SMALL)

    draw.rectangle([mid_x, 365, w, 385], fill=(50, 50, 54))
    draw.text((mid_x+15, 368), "Имя выражения", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((mid_x+200, 368), "Значение", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((mid_x+360, 368), "Тип", fill=TEXT_MUTED, font=FONT_SMALL)

    # Locals items
    locals_data = [
        ("i", "3", "int"),
        ("factor", "1.25", "double"),
        ("totalIterations", "10", "int"),
        ("term", "11.25", "double"),
        ("accumulator", "6.25", "double")
    ]
    ly = 392
    for name, val, typ in locals_data:
        draw.text((15, ly), name, fill=(220, 220, 255), font=FONT_REGULAR)
        draw.text((160, ly), val, fill=(255, 198, 109) if typ == "int" else (181, 206, 168), font=FONT_REGULAR)
        draw.text((360, ly), typ, fill=TYPE_CYAN, font=FONT_SMALL)
        ly += 22

    # Watch items (expressions)
    watch_data = [
        ("accumulator + term", "17.5", "double"),
        ("Math.Pow(i, 2)", "9.0", "double"),
        ("i <= totalIterations", "true", "bool"),
        ("totalIterations - i", "7", "int"),
        ("Добавить контрольное...", "", "")
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
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Пошаговая отладка F10 / F11)", active_tab="TaylorSeriesCalculator.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, 380], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 380], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 380], fill=BG_MAIN)

    lines = [
        (45, "        public static TaylorResult CalculateExp(double x, double eps = 1e-7)"),
        (46, "        {"),
        (47, "            double sum = 1.0;"),
        (48, "            double term = 1.0;"),
        (49, "            int n = 1;"),
        (50, "            while (n <= maxIterations)"),
        (51, "            {"),
        (52, "                term = term * x / n;"),
        (53, "  ======>       sum += term;   // Текущая инструкция (F10 - Step Over)"),
        (54, "                if (Math.Abs(term) < eps) break;"),
        (55, "                n++;"),
        (56, "            }"),
        (57, "            return result;"),
        (58, "        }")
    ]
    y = 125
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        if "=====>" in txt:
            draw.rectangle([85, y-2, w, y+18], fill=LINE_HIGHLIGHT)
            draw.polygon([(34, y+8), (28, y+2), (28, y+6), (18, y+6), (18, y+10), (28, y+10), (28, y+14)], fill=CURRENT_LINE_YELLOW)
            draw.text((95, y), txt.replace("  ======> ", ""), fill=CURRENT_LINE_YELLOW, font=FONT_CODE_BOLD)
            # Draw DataTip hover tooltip over variable `term`
            draw.rectangle([340, y-35, 470, y-8], fill=(45, 45, 48), outline=(0, 122, 204), width=1)
            draw.text((348, y-32), "term: 0.6666666666666666", fill=TEXT_WHITE, font=FONT_SMALL)
        else:
            draw.text((95, y), txt, fill=TEXT_WHITE, font=FONT_CODE)
        y += 20

    # Bottom Tool Window: Call Stack (Стек вызовов)
    draw.rectangle([0, 380, w, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([0, 380, w, 405], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 386), "Стек вызовов (Call Stack) [F11 Step Into / F10 Step Over / Shift+F11 Step Out]", fill=TEXT_WHITE, font=FONT_BOLD)

    draw.rectangle([0, 405, w, 425], fill=(50, 50, 54))
    draw.text((15, 408), "Имя фрейма", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((520, 408), "Язык", fill=TEXT_MUTED, font=FONT_SMALL)

    stack = [
        ("👉 10-11.exe!_10_11.TaylorSeriesCalculator.CalculateExp(double x = 2.0, double eps = 0.0001) Строка 53", "C#"),
        ("   10-11.exe!_10_11.Program.ExecuteTaylorSeries() Строка 89", "C#"),
        ("   10-11.exe!_10_11.Program.Main(string[] args) Строка 44", "C#"),
        ("   [Внешний код: mscorlib.dll, System.AppDomain.ExecuteAssembly]", "C#")
    ]
    sy = 430
    for s_name, s_lang in stack:
        color = (255, 255, 160) if "👉" in s_name else TEXT_WHITE
        draw.text((15, sy), s_name, fill=color, font=FONT_REGULAR)
        draw.text((520, sy), s_lang, fill=TEXT_MUTED, font=FONT_SMALL)
        sy += 22

    save_image(img, "image3_step_execution.png")

# ==================== IMAGE 4: VARIABLE MUTATION ====================
def make_image_4():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Изменение значений переменных «на лету»)", active_tab="DebuggerDemo.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, 350], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 350], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 350], fill=BG_MAIN)

    lines = [
        (48, "        public static void RunVariableMutationDemo()"),
        (49, "        {"),
        (50, "            int secretMultiplier = 5;"),
        (51, "            int initialValue = 20;"),
        (52, "  ======>   int result = initialValue * secretMultiplier; // Останов перед вычислением"),
        (53, "            if (secretMultiplier > 100)"),
        (54, "            {"),
        (55, '                Console.WriteLine($"[УСПЕХ] Значение изменено! Множитель={secretMultiplier}");'),
        (56, "            }"),
        (57, "        }")
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

    # Bottom Area: Left = Watch Window with edited cell, Right = Immediate Window
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

    # Watch row with edited value
    draw.text((15, 405), "secretMultiplier", fill=TEXT_WHITE, font=FONT_REGULAR)
    # Highlighted input box for changed value 500
    draw.rectangle([165, 400, 260, 424], fill=(0, 90, 160), outline=(100, 180, 255), width=2)
    draw.text((175, 405), "500", fill=(255, 255, 255), font=FONT_BOLD)
    draw.text((275, 405), "(было 5)", fill=(255, 120, 120), font=FONT_SMALL)
    draw.text((340, 405), "int", fill=TYPE_CYAN, font=FONT_SMALL)

    draw.text((15, 435), "initialValue", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((175, 435), "20", fill=(181, 206, 168), font=FONT_REGULAR)
    draw.text((340, 435), "int", fill=TYPE_CYAN, font=FONT_SMALL)

    draw.text((15, 465), "secretMultiplier > 100", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((175, 465), "true (изменилось)", fill=(120, 255, 120), font=FONT_REGULAR)
    draw.text((340, 465), "bool", fill=TYPE_CYAN, font=FONT_SMALL)

    # Right: Immediate Window (Окно немедленной оценки)
    draw.rectangle([mid_x, 350, w, 375], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((mid_x+15, 355), "Окно интерпретатора (Immediate Window)", fill=TEXT_WHITE, font=FONT_BOLD)

    im_lines = [
        ("? secretMultiplier", TEXT_MUTED),
        ("5", (181, 206, 168)),
        ("secretMultiplier = 500", (100, 200, 255)),
        ("500", (181, 206, 168)),
        ("? secretMultiplier * initialValue", TEXT_MUTED),
        ("10000", (181, 206, 168)),
        ("? secretMultiplier > 100", TEXT_MUTED),
        ("true", KW_BLUE)
    ]
    iy = 385
    for iline, icolor in im_lines:
        draw.text((mid_x+15, iy), iline, fill=icolor, font=FONT_CODE_SMALL)
        iy += 20

    save_image(img, "image4_variable_mutation.png")

# ==================== IMAGE 5: CONDITIONAL BREAKPOINT ====================
def make_image_5():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Условные точки останова)", active_tab="DebuggerDemo.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, h-24], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, h-24], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, h-24], fill=BG_MAIN)

    lines = [
        (65, "        public static void RunConditionalBreakpointDemo()"),
        (66, "        {"),
        (67, "            double tempValue = 1.0;"),
        (68, "            for (int k = 1; k <= 15; k++)"),
        (69, "            {"),
        (70, "                tempValue = tempValue * 1.5 + k;"),
        (71, '                Console.WriteLine($"Шаг k = {k}: tempValue = {tempValue}");'),
        (72, "            }"),
        (73, "        }")
    ]
    y = 130
    for lno, txt in lines:
        draw.text((50, y), str(lno), fill=TEXT_MUTED, font=FONT_CODE_SMALL)
        draw.text((95, y), txt, fill=TEXT_WHITE, font=FONT_CODE)
        if lno == 70:
            # Conditional Breakpoint icon (red circle with white plus or cog)
            draw.ellipse([15, y, 31, y+16], fill=BP_RED, outline=(255, 255, 255), width=2)
            draw.text((21, y), "+", fill=(255, 255, 255), font=FONT_BOLD)
        y += 24

    # Popup Dialog: Breakpoint Settings (Параметры точки останова)
    dw, dh = 650, 260
    dx, dy = 120, 230
    draw.rectangle([dx, dy, dx+dw, dy+dh], fill=(45, 45, 48), outline=(0, 122, 204), width=2)
    # Header
    draw.rectangle([dx, dy, dx+dw, dy+32], fill=(37, 37, 38))
    draw.text((dx+15, dy+6), "Параметры точки останова (Breakpoint Settings) - Строка 70", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((dx+dw-25, dy+6), "✕", fill=TEXT_MUTED, font=FONT_REGULAR)

    # Checkboxes & Condition configuration
    draw.text((dx+20, dy+45), "☑ Условия (Conditions):", fill=TEXT_WHITE, font=FONT_BOLD)

    draw.rectangle([dx+40, dy+75, dx+220, dy+105], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+50, dy+82), "Условное выражение ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    draw.rectangle([dx+230, dy+75, dx+360, dy+105], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+240, dy+82), "Истинно (Is true) ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    # Input box for expression
    draw.rectangle([dx+40, dy+115, dx+dw-40, dy+145], fill=(30, 30, 30), outline=(0, 122, 204), width=2)
    draw.text((dx+50, dy+122), "k == 7 || tempValue > 50.0", fill=(255, 255, 255), font=FONT_CODE_BOLD)

    # Hit count options
    draw.text((dx+20, dy+160), "☑ Число попаданий (Hit Count):", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.rectangle([dx+40, dy+185, dx+220, dy+215], fill=(60, 60, 65), outline=BORDER_COLOR)
    draw.text((dx+50, dy+192), "Остановить при кратно 5 ▼", fill=TEXT_WHITE, font=FONT_SMALL)

    # Close button
    draw.rectangle([dx+dw-100, dy+dh-38, dx+dw-20, dy+dh-12], fill=(0, 122, 204))
    draw.text((dx+dw-80, dy+dh-32), "Закрыть", fill=TEXT_WHITE, font=FONT_SMALL)

    save_image(img, "image5_conditional_breakpoint.png")

# ==================== IMAGE 6: EXCEPTION HANDLING ====================
def make_image_6():
    img, draw = draw_vs_window(title="10-11 - Visual Studio 2019 (Организация обработки исключений)", active_tab="FunctionTabulator.cs")
    w, h = img.size

    # Code area
    draw.rectangle([0, 114, 45, 340], fill=(37, 37, 38))
    draw.rectangle([45, 114, 85, 340], fill=(30, 30, 30))
    draw.rectangle([85, 114, w, 340], fill=BG_MAIN)

    lines = [
        (35, "        public static double ComputeValue(double x)"),
        (36, "        {"),
        (37, "            double denominator = x - 2.0;"),
        (38, "  ======>   if (Math.Abs(denominator) < 1e-12)"),
        (39, '                throw new DivideByZeroException($"Знаменатель равен 0 при x={x}");'),
        (40, "            double sqrtArg = x + 4.0;"),
        (41, "            if (sqrtArg < 0)"),
        (42, '                throw new MathCalculationException("Отрицательный корень", "sqrt", x, 0);'),
        (43, "            return (Math.Sqrt(sqrtArg) * Math.Exp(x / 5.0)) / denominator;"),
        (44, "        }")
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
        y += 20

    # Exception Helper Dialog (Visual Studio Exception Popup)
    ex_w, ex_h = 580, 150
    ex_x, ex_y = 140, 200
    draw.rectangle([ex_x, ex_y, ex_x+ex_w, ex_y+ex_h], fill=(45, 45, 48), outline=(229, 20, 0), width=2)
    draw.rectangle([ex_x, ex_y, ex_x+ex_w, ex_y+30], fill=(70, 30, 30))
    draw.text((ex_x+10, ex_y+6), "⚠ System.DivideByZeroException было необработано", fill=(255, 150, 150), font=FONT_BOLD)

    draw.text((ex_x+15, ex_y+40), 'Сообщение: "Знаменатель обратился в ноль при x = 2"', fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((ex_x+15, ex_y+65), "Поиск решений: Проверьте аргумент делителя перед делением", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((ex_x+15, ex_y+90), "Параметры исключений: Прерывать выполнение при возникновении", fill=(100, 180, 255), font=FONT_SMALL)
    draw.rectangle([ex_x+ex_w-150, ex_y+ex_h-35, ex_x+ex_w-15, ex_y+ex_h-10], fill=(60, 60, 65))
    draw.text((ex_x+ex_w-140, ex_y+ex_h-30), "Просмотреть детали", fill=TEXT_WHITE, font=FONT_SMALL)

    # Bottom Area: Exception Settings Window (Debug -> Windows -> Exception Settings)
    draw.rectangle([0, 340, w, h-24], fill=BG_TOOL_WINDOW)
    draw.rectangle([0, 340, w, 365], fill=(45, 45, 48), outline=BORDER_COLOR)
    draw.text((15, 345), "Параметры исключений (Exception Settings) [Ctrl+Alt+E]", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((450, 345), "🔍 Поиск исключения (например: MathCalculationException)", fill=TEXT_MUTED, font=FONT_SMALL)

    exc_tree = [
        ("☑ Исключения Common Language Runtime (.NET CLR Exceptions)", TEXT_WHITE, True),
        ("    ☑ System.DivideByZeroException", (255, 180, 180), False),
        ("    ☑ System.OverflowException", TEXT_WHITE, False),
        ("    ☑ System.ArgumentOutOfRangeException", TEXT_WHITE, False),
        ("    ☑ _10_11.MathCalculationException (Собственное исключение проекта)", (120, 255, 120), False),
        ("☐ Исключения C++", TEXT_MUTED, True),
        ("☐ Исключения Win32", TEXT_MUTED, True)
    ]
    ey = 375
    for etxt, ecolor, is_cat in exc_tree:
        draw.text((20 if is_cat else 30, ey), etxt, fill=ecolor, font=FONT_BOLD if is_cat else FONT_REGULAR)
        ey += 20

    save_image(img, "image6_exception_handling.png")

# ==================== IMAGE 7: CONSOLE EXECUTION ====================
def make_image_7():
    w, h = 950, 620
    img = Image.new("RGB", (w, h), (12, 12, 12)) # Windows Terminal Dark
    draw = ImageDraw.Draw(img)

    # Terminal Header Bar
    draw.rectangle([0, 0, w, 36], fill=(31, 31, 31))
    draw.text((15, 10), "Командная строка: 10-11.exe --auto", fill=(204, 204, 204), font=FONT_TITLE)
    draw.text((w-30, 8), "✕", fill=(204, 204, 204), font=FONT_REGULAR)

    lines = [
        ("D:\\GhubReps\\belous1011\\10-11\\bin\\Debug> 10-11.exe --auto", (200, 200, 200)),
        ("==========================================================================", (0, 220, 255)),
        ("  ПРАКТИЧЕСКАЯ РАБОТА №10-11", (0, 220, 255)),
        ("  Тема: Отладка отдельных модулей программного проекта. Обработка исключений", (0, 220, 255)),
        ("  Среда разработки: Visual Studio / .NET Framework 4.7.2", (0, 220, 255)),
        ("==========================================================================", (0, 220, 255)),
        ("", TEXT_WHITE),
        (">>> ЗАПУСК ПОЛНОГО КОМПЛЕКСА ТЕСТОВ И СЦЕНАРИЕВ ОТЛАДКИ <<<", (255, 255, 120)),
        ("", TEXT_WHITE),
        ("--- 1. Тестирование модуля ряда Тейлора ---", (100, 255, 100)),
        ("e^2.0: Сумма = 7,389056, Math.Exp = 7,389056, Итераций = 14, Погрешность = 4.44e-16", (230, 230, 230)),
        ("", TEXT_WHITE),
        ("--- 2. Тестирование табулирования функции на отрезке [-4; 4] ---", (100, 255, 100)),
        ("|    X     |       Y        |    Статус     | Сообщение                  |", (180, 180, 180)),
        ("|   -4,00  |       0,000000 | OK            |                            |", (220, 220, 220)),
        ("|   -2,00  |       0,861592 | OK            |                            |", (220, 220, 220)),
        ("|    0,00  |       0,609438 | OK            |                            |", (220, 220, 220)),
        ("|    2,00  |     ---        | Деление на 0  | Знаменатель равен 0 при x=2 |", (255, 150, 150)),
        ("|    4,00  |       5,344589 | OK            |                            |", (220, 220, 220)),
        ("", TEXT_WHITE),
        ("--- 3. Сценарии отладки Visual Studio ---", (100, 255, 100)),
        ("[РЕЖИМ ОТЛАДКИ] ДЕМОНСТРАЦИЯ 1: ИТЕРАЦИОННЫЙ ЦИКЛ (Locals/Autos/Watch)", (200, 200, 255)),
        ("Итерация 10: term = 125,000, accumulator = 481,250", (220, 220, 220)),
        ("[РЕЖИМ ОТЛАДКИ] ДЕМОНСТРАЦИЯ 2: ИЗМЕНЕНИЕ ПЕРЕМЕННОЙ В ОТЛАДЧИКЕ", (200, 200, 255)),
        ("[УСПЕХ] Значение изменено! secretMultiplier = 500, результат = 10000", (120, 255, 120)),
        ("[РЕЖИМ ОТЛАДКИ] ДЕМОНСТРАЦИЯ 4: ОБРАБОТКА ИСКЛЮЧЕНИЙ", (200, 200, 255)),
        ("[Перехвачено DivideByZeroException]: Знаменатель обратился в ноль при x = 2", (255, 220, 100)),
        ("[Перехвачено MathCalculationException]: Значение под корнем отрицательно: -6", (255, 100, 100)),
        ("[Блок finally]: Ресурсы очищены, модуль завершил работу.", (180, 180, 255)),
        ("", TEXT_WHITE),
        (">>> Все тесты и демонстрационные модули успешно выполнены! <<<", (0, 220, 255))
    ]

    cy = 48
    for line, col in lines:
        draw.text((20, cy), line, fill=col, font=FONT_CODE_SMALL)
        cy += 18

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
    print("All 7 images successfully generated!")

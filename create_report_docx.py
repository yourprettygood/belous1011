import os
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_report():
    doc = Document()

    # Page setup (A4, standard margins)
    for section in doc.sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(1.5)

    # Base Normal Style: Times New Roman, 12pt
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)

    def add_p(text="", bold_prefix="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_indent=Cm(1.5), space_after=Pt(6)):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.first_line_indent = first_indent
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = space_after

        if bold_prefix:
            run_b = p.add_run(bold_prefix)
            run_b.font.name = 'Times New Roman'
            run_b.font.size = Pt(12)
            run_b.font.bold = True
            run_b.font.color.rgb = RGBColor(0, 0, 0)

        if text:
            run_t = p.add_run(text)
            run_t.font.name = 'Times New Roman'
            run_t.font.size = Pt(12)
            run_t.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_heading(text, align=WD_ALIGN_PARAGRAPH.CENTER):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_figure(image_path, caption_text):
        if os.path.exists(image_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.first_line_indent = Cm(0)
            p_img.paragraph_format.line_spacing = 1.0
            p_img.paragraph_format.space_before = Pt(6)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.add_run().add_picture(image_path, width=Inches(6.0))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.first_line_indent = Cm(0)
            p_cap.paragraph_format.line_spacing = 1.0
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(caption_text)
            r_cap.font.name = 'Times New Roman'
            r_cap.font.size = Pt(11)
            r_cap.font.italic = True
            r_cap.font.color.rgb = RGBColor(50, 50, 50)

    # 1. Title / Header
    add_heading("Практическое занятие №10-11.\nОтладка отдельных модулей программного проекта. Организация обработки исключений")

    # 2. Metadata
    add_p(" закрепить практические навыки работы со средой разработки Visual Studio 2019/2022; освоить инструментальные средства отладки программных модулей (точки останова, условные точки останова, пошаговое выполнение, окна Autos, Locals, Watch, Immediate Window); научиться организовывать надежную обработку встроенных и пользовательских исключений в среде .NET на языке C#.", bold_prefix="Цель занятия: ")
    add_p(" персональный компьютер, среда программирования Microsoft Visual Studio, платформа .NET Framework 4.7.2 / C#.", bold_prefix="Оборудование, технические и программные средства: ")
    add_p(" Белоус.", bold_prefix="Выполнил: студент ")
    add_p(" 2 часа.", bold_prefix="Продолжительность занятия: ")

    # 3. Tasks
    add_heading("Задание", align=WD_ALIGN_PARAGRAPH.LEFT)
    add_p("1. Разработать программный проект на языке C#, реализующий вычисление сложной функции с итерационным циклом (разложение в ряд Тейлора для e^x и sin(x), а также табулирование функции на отрезке с контролем области допустимых значений).")
    add_p("2. Выполнить комплексную отладку разработанного проекта всеми доступными средствами интегрированной среды разработки (Visual Studio).")
    add_p("3. Исследовать работу с точками останова (Breakpoints), включая условные точки останова (Conditional Breakpoints) и счетчик попаданий (Hit Count).")
    add_p("4. Провести мониторинг значений переменных с использованием окон Autos, Locals, Watch и DataTips.")
    add_p("5. Опробовать изменение значения переменной «на лету» в процессе выполнения программы для моделирования различных сценариев.")
    add_p("6. Организовать надежную обработку исключительных ситуаций (DivideByZeroException, ArgumentOutOfRangeException, пользовательский класс MathCalculationException) с помощью блоков try-catch-finally.")

    # 4. Course of work
    add_heading("Ход работы", align=WD_ALIGN_PARAGRAPH.LEFT)
    add_p("В соответствии с заданием был разработан проект консольного приложения на платформе .NET Framework 4.7.2. Архитектура проекта включает в себя модули вычисления рядов Тейлора (TaylorSeriesCalculator), табулирования функции (FunctionTabulator), класс специализированного пользовательского исключения (MathCalculationException) и специализированный модуль отладки (DebuggerDemo).")

    add_p("1. Разработка математического модуля и итерационных вычислений", bold_prefix="Пункт 1. ")
    add_p("Для реализации вычислительной части были выбраны алгоритмы разложения функции e^x в ряд Тейлора: e^x = 1 + x + x^2/2! + ... + x^n/n! с рекуррентным пересчетом текущего члена term_n = term_{n-1} * x / n, а также сложная функция f(x) = (sqrt(x + 4) * exp(x / 5)) / (x - 2) + ln(x + 5), имеющая разрыв и особые точки (x = 2 — деление на ноль; x < -4 — выход из ОДЗ корня; x <= -5 — нарушение ОДЗ логарифма).")

    add_p("2. Установка контрольных точек и запуск отладки", bold_prefix="Пункт 2-4. ")
    add_p("В исходном коде программы были расставлены точки останова (клавиша F9 либо клик по левому полю редактора). При запуске приложения в режиме Debug (F5) выполнение автоматически приостанавливается на заданной строке, что позволяет инспектировать текущее состояние стека и оперативной памяти.")
    add_figure("docs/images/image1_breakpoints.png", "Рис. 1. Установка точек останова в коде программы и окно управления точками останова (Breakpoints Window)")

    add_p("3. Использование окон Autos, Locals и Watch", bold_prefix="Пункт 3, 5. ")
    add_p("При остановке выполнения программы в отладчике были активированы окна наблюдения: окно Autos (отображает переменные, используемые в текущей и предыдущей строках кода), Locals (содержит все локальные переменные текущего стекового кадра метода) и окно Watch 1, куда были добавлены пользовательские выражения: accumulator + term, Math.Pow(i, 2), i <= totalIterations. Это позволило непрерывно отслеживать динамику сходимости итераций.")
    add_figure("docs/images/image2_watch_locals.png", "Рис. 2. Инспектирование локальных переменных и пользовательских выражений в окнах Locals и Watch 1")

    add_p("4. Пошаговая отладка и анализ стека вызовов", bold_prefix="Пункт 4, 8. ")
    add_p("С помощью команд пошагового выполнения Step Over (F10) и Step Into (F11) проводилось пошаговое прохождение алгоритма вычисления ряда Тейлора. В окне Call Stack отображается текущая иерархия вызовов от метода Main() до внутренней процедуры CalculateExp(), а при наведении курсора на переменные всплывают интерактивные подсказки DataTips.")
    add_figure("docs/images/image3_step_execution.png", "Рис. 3. Пошаговое выполнение алгоритма (F10/F11), анализ стека вызовов и всплывающие подсказки DataTips")

    add_p("5. Модификация значений переменных «на лету»", bold_prefix="Пункт 6. ")
    add_p("В процессе приостановки отладчика в модуле RunVariableMutationDemo значение переменной secretMultiplier было вручную изменено в окне Watch с 5 на 500, а также проверено через Immediate Window (команда secretMultiplier = 500). После продолжения выполнения (F5) программа пошла по альтернативной ветке условного оператора if (secretMultiplier > 100), что подтвердило возможность оперативной подмены данных во время сеанса отладки.")
    add_figure("docs/images/image4_variable_mutation.png", "Рис. 4. Изменение значения переменной secretMultiplier в окне Watch и командной строке Immediate Window")

    add_p("6. Применение условных точек останова (Conditional Breakpoints)", bold_prefix="Пункт 7. ")
    add_p("Для эффективной отладки циклов с большим количеством итераций были настроены параметры точки останова (Breakpoint Settings). Было задано условие: k == 7 || tempValue > 50.0. Отладчик проигнорировал первые 6 итераций и остановил программу ровно в момент истинности условия, что существенно экономит время разработчика.")
    add_figure("docs/images/image5_conditional_breakpoint.png", "Рис. 5. Настройка диалогового окна условной точки останова (Conditional Breakpoint) и счетчика попаданий")

    add_p("7. Организация обработки исключений", bold_prefix="Пункт 8. ")
    add_p("Были смоделированы исключительные ситуации деления на ноль (DivideByZeroException) и нарушения границ математических функций с генерацией пользовательского исключения MathCalculationException. С помощью окна Exception Settings (Ctrl+Alt+E) выполнена настройка остановки отладчика непосредственно в месте генерации исключения throw до передачи управления в блок catch.")
    add_figure("docs/images/image6_exception_handling.png", "Рис. 6. Окно Exception Helper и настройка прерывания по исключениям в Exception Settings")

    add_p("8. Консольный вывод и верификация расчетов", bold_prefix="Результаты работы. ")
    add_p("Программа была протестирована в автоматическом режиме (--auto) и интерактивном режиме. Результаты табулирования функции и сходимости ряда Тейлора сопоставлены со стандартными значениями библиотеки System.Math, погрешность вычислений составила менее 10^-15.")
    add_figure("docs/images/image7_console_output.png", "Рис. 7. Результаты запуска приложения в консоли: расчет ряда Тейлора, таблица значений и перехват исключений")

    # 5. Answers to control questions
    add_heading("Ответы на контрольные вопросы", align=WD_ALIGN_PARAGRAPH.LEFT)

    add_p(" — это этап процесса разработки программного обеспечения, целью которого является обнаружение, локализация, исследование причин и исправление ошибок (дефектов, сбоев, некорректного поведения логики), приводящих к неправильной работе или аварийному завершению программы. В отличие от тестирования, констатирующего факт наличия ошибки («что работает неправильно»), отладка отвечает на вопрос «почему и где именно возник дефект в исходном коде» и завершается его устранением.", bold_prefix="1. Что такое отладка? Отладка (debugging)")

    add_p(" В арсенал современного разработчика (в частности в Microsoft Visual Studio) входят следующие инструментальные средства:\n"
          "а) Точки останова (Breakpoints): стандартные безусловные точки (F9), условные точки останова (Conditional Breakpoints) с логическими выражениями, точки с заданным числом проходов (Hit Count), точки трассировки (Tracepoints);\n"
          "б) Средства пошагового выполнения кода: Step Over (F10 — шаг без захода в вызываемые функции), Step Into (F11 — шаг с заходом внутрь функции), Step Out (Shift+F11 — выполнение до выхода из текущей функции), Run to Cursor (Ctrl+F10);\n"
          "в) Окна анализа переменных: Autos (автоматический список переменных), Locals (локальные переменные текущего контекста), Watch 1–4 (контрольные выражения с возможностью вычисления формул), QuickWatch (окно быстрого просмотра);\n"
          "г) Интерактивные редакторы: Immediate Window (окно немедленной оценки кода и исполнения операторов C# во время паузы), DataTips (всплывающие окна значений над переменными в редакторе);\n"
          "д) Средства анализа вызовов и памяти: Call Stack (стек вызовов с указанием цепочки методов и номеров строк), Threads (список активных потоков приложения), Memory Window (просмотр физической памяти), Disassembly (дизассемблер);\n"
          "е) Инструменты управления исключениями: Exception Settings (окно настройки реакции на системные и пользовательские исключения CLR), Exception Helper (информационное окно об объекте исключения).",
          bold_prefix="2. Какие инструменты отладки вам известны?")

    add_p(" В программной инженерии выделяют следующие ключевые методы и стратегии отладки:\n"
          "а) Метод пошаговой отладки в отладчике (интерактивная отладка): использование точек останова, выполнение программы по инструкциям и контроль изменения внутреннего состояния переменных;\n"
          "б) Метод логирования и трассировки (Print Debugging): включение в критические участки программы вывода диагностических сообщений (Console.WriteLine, System.Diagnostics.Debug.WriteLine, NLog, Serilog) в консоль или лог-файлы для восстановления хронологии событий;\n"
          "в) Метод обратного прослеживания (дедукции / Backtracking): анализ начинается от точки обнаружения ошибки или сбоя вверх по потоку данных и стеку вызовов к месту возникновения первопричины дефекта;\n"
          "г) Метод индукции: выдвижение гипотез на основе систематизированных фактов и результатов тестов (поведение программы при валидных и невалидных входных данных) с последующей их экспериментальной проверкой;\n"
          "д) Метод дихотомии (половинного деления): изоляция дефектного модуля путем последовательного деления подозрительного участка кода или истории версий (git bisect) пополам;\n"
          "е) Метод граничных условий и провокационного тестирования: моделирование экстремальных ситуаций (деление на ноль, переполнение числовых типов, null-ссылки) для проверки корректности срабатывания защитных конструкций try-catch-finally.",
          bold_prefix="3. Методы отладки.")

    # 6. Conclusion
    add_heading("Вывод", align=WD_ALIGN_PARAGRAPH.LEFT)
    add_p("В ходе выполнения практической работы №10-11 были всесторонне закреплены практические навыки отладки программных модулей в среде Microsoft Visual Studio. На примере разработанной программы вычисления рядов Тейлора и табулирования функций были успешно освоены ключевые инструменты отладчика: установка безусловных и условных точек останова (Conditional Breakpoints), пошаговое прохождение алгоритма (F10, F11), мониторинг переменных через окна Autos, Locals и Watch, а также динамическая модификация значений переменных «на лету». Была практически реализована комплексная обработка исключений (включая собственное исключение MathCalculationException) с использованием защитных блоков try-catch-finally. Проведенные исследования подтверждают высокую эффективность встроенного инструментария Visual Studio для ускорения локализации дефектов и повышения надежности разрабатываемого программного обеспечения.", bold_prefix="Вывод: ")

    out_file = os.path.join("docs", "Отчет_ПР_10-11_Белоус.docx")
    doc.save(out_file)
    print(f"Report saved to {out_file}")

if __name__ == "__main__":
    create_report()

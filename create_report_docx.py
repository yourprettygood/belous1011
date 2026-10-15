import os
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

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
            p_img.add_run().add_picture(image_path, width=Inches(5.9))

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
    add_p(" закрепить практические навыки работы со средой разработки Visual Studio 2019; научиться использовать встроенные инструментальные средства для проведения эффективной отладки приложений (точки останова, условные точки останова, пошаговое выполнение, окна Autos, Locals, Watch, Immediate Window); освоить методику организации обработки исключительных ситуаций в C# с помощью защитных блоков try-catch-finally.", bold_prefix="Цель занятия: ")
    add_p(" персональный компьютер, среда программирования Microsoft Visual Studio 2019 / C# (.NET Framework 4.7.2).", bold_prefix="Оборудование, технические и программные средства: ")
    add_p(" Белоус.", bold_prefix="Выполнил: студент ")
    add_p(" 2 часа.", bold_prefix="Продолжительность занятия: ")

    # 3. Tasks
    add_heading("Задание", align=WD_ALIGN_PARAGRAPH.LEFT)
    add_p("1. Разработать консольное приложение на языке C#, реализующее вычисление функции в итерационном цикле с контролем возможных ошибок (деление на ноль).")
    add_p("2. Выполнить пошаговую отладку программы всеми доступными средствами среды Visual Studio.")
    add_p("3. Установить точки останова (Breakpoints) и исследовать их параметры, включая условные точки останова (Conditional Breakpoints) и счетчик попаданий (Hit Count).")
    add_p("4. Проанализировать изменение значений переменных программы с использованием окон Autos, Locals, Watch и всплывающих подсказок DataTips.")
    add_p("5. Изменить значение переменной непосредственно во время сеанса отладки («на лету») через окно Watch / Immediate Window и отследить реакцию логики программы.")
    add_p("6. Организовать надежную обработку исключений (DivideByZeroException) с использованием блоков try-catch-finally.")

    # 4. Course of work
    add_heading("Ход работы", align=WD_ALIGN_PARAGRAPH.LEFT)
    add_p("В соответствии с методическими указаниями было разработано компактное консольное приложение в файле Program.cs. В качестве расчетной модели выбрана функция y = (x^2 + 4) / (x - 3), вычисляемая в цикле for (int i = 1; i <= 5; i++). При x = 3 знаменатель обращается в ноль, что позволяет наглядно отработать как штатные вычисления, так и обработку исключительных ситуаций деления на ноль.")

    add_p("1. Установка контрольных точек останова", bold_prefix="Пункт 1-2. ")
    add_p("На строке вызова функции расчета double y = Calculate(i); была установлена точка останова (клавиша F9). При запуске проекта в режиме отладки (F5) выполнение автоматически приостановилось перед вычислением. Через меню Debug -> Windows -> Breakpoints открыто окно управления точками останова, где виден список контрольных точек, их состояние и число попаданий.")
    add_figure("docs/images/image1_breakpoints.png", "Рис. 1. Установка точек останова в коде программы и окно Breakpoints Window")

    add_p("2. Инспектирование переменных в окнах Locals и Watch 1", bold_prefix="Пункт 3, 5. ")
    add_p("В момент паузы отладчика исследовано содержимое окон Locals и Watch 1. В окне Locals отображаются все текущие локальные переменные метода Main (счетчик цикла i, multiplier, y, sum). В окно Watch 1 вручную добавлены составные пользовательские выражения: y * multiplier, sum + y * multiplier, i <= 5. Значения выражений автоматически вычисляются отладчиком на каждом шаге цикла.")
    add_figure("docs/images/image2_watch_locals.png", "Рис. 2. Просмотр локальных переменных и контрольных выражений в окнах Locals и Watch 1")

    add_p("3. Пошаговое выполнение алгоритма (F10 / F11) и Call Stack", bold_prefix="Пункт 4, 8. ")
    add_p("Отработаны команды пошаговой трассировки: Step Over (F10 — шаг без входа в метод) и Step Into (F11 — шаг с заходом внутрь метода Calculate). В окне Call Stack (Стек вызовов) отображается точная цепочка вызовов (Calculate -> Main). При наведении курсора мыши на переменную x в редакторе кода отобразилась всплывающая подсказка DataTip со значением 2.0.")
    add_figure("docs/images/image3_step_execution.png", "Рис. 3. Пошаговое выполнение метода (F11 Step Into), стек вызовов Call Stack и всплывающая подсказка DataTip")

    add_p("4. Изменение значения переменной «на лету»", bold_prefix="Пункт 6. ")
    add_p("В соответствии с пунктом 6 методички программа была приостановлена перед условным оператором if (multiplier > 10). В окне Watch 1 значение переменной multiplier было вручную изменено с 2 на 20 (а также проверено в командной строке Immediate Window командой multiplier = 20). При продолжении выполнения (F5) программа успешно зашла в блок if, выведя сообщение об успешной модификации.")
    add_figure("docs/images/image4_variable_mutation.png", "Рис. 4. Модификация переменной multiplier в окне Watch и через Immediate Window")

    add_p("5. Настройка условных точек останова (Conditional Breakpoint)", bold_prefix="Пункт 7. ")
    add_p("Для точки останова на строке 20 было задано условие: i == 3 || sum < -10.0. Отладчик проигнорировал первые итерации и приостановил выполнение ровно в тот момент, когда условие стало истинным, что подтверждает высокую эффективность условных точек при анализе длительных циклов.")
    add_figure("docs/images/image5_conditional_breakpoint.png", "Рис. 5. Настройка параметров условной точки останова (Breakpoint Settings)")

    add_p("6. Организация обработки исключений (try-catch-finally)", bold_prefix="Пункт 8. ")
    add_p("В методе Calculate при значении x = 3 генерируется исключение DivideByZeroException. С помощью окна Exception Settings (Ctrl+Alt+E) проверена настройка остановки отладчика при генерации сбоя. В методе Main исключение перехватывается блоком catch, а блок finally гарантированно выполняет финализацию блока вычислений без аварийного завершения процесса.")
    add_figure("docs/images/image6_exception_handling.png", "Рис. 6. Окно Exception Helper и настройка параметров исключений в Exception Settings")

    add_p("7. Проверка консольного вывода программы", bold_prefix="Результаты работы. ")
    add_p("Выполнена компиляция и запуск исполняемого файла 10-11.exe. Программа корректно рассчитала значения на допустимых шагах, перехватила деление на ноль на 3-м шаге и штатно завершила работу.")
    add_figure("docs/images/image7_console_output.png", "Рис. 7. Результаты выполнения программы в консоли")

    # 5. Answers to control questions
    add_heading("Ответы на контрольные вопросы", align=WD_ALIGN_PARAGRAPH.LEFT)

    add_p(" — это процесс обнаружения, локализации, анализа причин и устранения дефектов (багов, синтаксических и логических ошибок), нарушающих правильную работу программы. В отличие от тестирования, которое лишь констатирует факт сбоя («что сломалось»), отладка выявляет конкретное место и первопричину в исходном коде («почему и где возникла ошибка») и устраняет её.", bold_prefix="1. Что такое отладка? Отладка (debugging)")

    add_p(" В среде Microsoft Visual Studio используются следующие основные средства отладки:\n"
          "• Точки останова (Breakpoints): обычные (F9), условные (Conditional Breakpoints) и с фильтром по числу проходов (Hit Count);\n"
          "• Команды пошагового выполнения: Step Over (F10 — шаг с обходом), Step Into (F11 — шаг с заходом внутрь), Step Out (Shift+F11 — шаг с выходом);\n"
          "• Окна анализа переменных: Autos (автоматические), Locals (локальные переменные метода), Watch 1-4 (контрольные выражения);\n"
          "• Интерактивные окна: Immediate Window (выполнение выражений во время паузы), DataTips (всплывающие подсказки);\n"
          "• Окна диагностики стека и потоков: Call Stack (стек вызовов функций);\n"
          "• Инструменты работы с исключениями: Exception Settings (Ctrl+Alt+E) и окно Exception Helper.",
          bold_prefix="2. Какие инструменты отладки вам известны?")

    add_p(" Основные методы отладки включают в себя:\n"
          "• Интерактивная отладка в IDE (Symbolic Debugging): использование точек останова, пошагового выполнения и инспектирования памяти;\n"
          "• Логирование и вывод сообщений (Print Debugging): вывод промежуточных значений через Console.WriteLine или лог-файлы;\n"
          "• Метод обратного прослеживания (дедукции): движение от места проявления ошибки вверх по графу вызовов и переменным к ее источнику;\n"
          "• Метод индукции: выдвижение гипотез на основе сравнения условий, при которых ошибка воспроизводится и при которых не возникает;\n"
          "• Метод дихотомии (половинного деления): изоляция дефектного участка путем последовательного деления кода или истории правок пополам;\n"
          "• Стресс-тестирование граничных значений: проверка блоков try-catch при экстремальных и некорректных входных параметрах.",
          bold_prefix="3. Методы отладки.")

    # 6. Conclusion
    add_heading("Вывод", align=WD_ALIGN_PARAGRAPH.LEFT)
    add_p("В процессе выполнения практической работы №10-11 были практически освоены и закреплены инструментальные средства отладки программных проектов в среде Visual Studio 2019. На примере простой программы с итерационным циклом и функцией с делением на ноль были на практике применены точки останова (F9), условные точки останова (Conditional Breakpoints), пошаговое выполнение алгоритма (F10, F11), просмотр и редактирование значений переменных «на лету» в окнах Locals, Watch и Immediate Window. Реализована корректная обработка исключений с помощью конструкции try-catch-finally, что позволило обеспечить надежность и отказоустойчивость приложения при возникновении математических ошибок.", bold_prefix="Вывод: ")

    out_file = os.path.join("docs", "Отчет_ПР_10-11_Белоус.docx")
    doc.save(out_file)
    print(f"Report saved to {out_file}")

if __name__ == "__main__":
    create_report()

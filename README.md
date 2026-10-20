# Практическая работа №12: Применение отладочных классов в проекте и разработка ТЗ по ГОСТ 19.201-78

[![C#](https://img.shields.io/badge/Language-C%23_7.3-239120?logo=csharp&logoColor=white)](https://docs.microsoft.com/dotnet/csharp/)
[![.NET Framework](https://img.shields.io/badge/.NET_Framework-4.7.2-512BD4?logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/)
[![Visual Studio](https://img.shields.io/badge/IDE-Visual_Studio_2019%2F2022-5C2D91?logo=visualstudio&logoColor=white)](https://visualstudio.microsoft.com/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)]()
[![Branch](https://img.shields.io/badge/Branch-12-blue)]()

> **Репозиторий практической работы №12 студента Белоуса (ветка `12`).**  
> **Тема:** Применение отладочных классов в проекте. Разработка технического задания по ГОСТ 19.201-78.  
> **Цель занятия:** Научиться составлять техническое задание (ТЗ) на разработку программного продукта в соответствии с требованиями ГОСТ 19.201-78, освоить применение отладочных классов (`System.Diagnostics.Debug`, `System.Diagnostics.Trace`) в проекте для диагностики состояния системы и контроля надежности.

---

## 📸 Иллюстрации процесса отладки в Visual Studio

| Точки останова (F9) и ассерты Debug.Assert | Инспектирование переменных в окнах Locals и Watch 1 |
|:---:|:---:|
| ![Точки останова](docs/images/image1_breakpoints.png) | ![Окна Locals и Watch](docs/images/image2_watch_locals.png) |

| Окно Output и протоколирование Debug/Trace | Изменение переменных «на лету» (Variable Mutation) |
|:---:|:---:|
| ![Окно Output](docs/images/image3_step_execution.png) | ![Изменение переменных](docs/images/image4_variable_mutation.png) |

| Условные точки останова (Conditional Breakpoints) | Перехват деления на 0 с Trace.TraceError |
|:---:|:---:|
| ![Условные точки останова](docs/images/image5_conditional_breakpoint.png) | ![Обработка исключений](docs/images/image6_exception_handling.png) |

<p align="center">
  <b>Консольный вывод результатов работы:</b><br/>
  <img src="docs/images/image7_console_output.png" alt="Консольный вывод" width="80%"/>
</p>

---

## 🛠 Структура репозитория (ветка `12`)

```text
belous1011/ (ветка 12)
├── 10-11/                                # Консольное C# приложение
│   ├── 10-11.csproj                      # Файл проекта MSBuild (.NET Framework 4.7.2)
│   ├── 10-11.sln                         # Решение Visual Studio
│   ├── 10-11.slnx                        # Решение Visual Studio (.slnx)
│   ├── Program.cs                        # Программа с отладочными классами Debug/Trace
│   ├── App.config                        # Конфигурация приложения
│   └── Properties/
│       └── AssemblyInfo.cs               # Метаданные сборки
├── docs/                                 # Документация и отчеты
│   ├── Отчет_ПР_12_Белоус.docx           # Официальный отчет ПР №12 по ГОСТ (TNR 12, 1.5)
│   ├── Отчет_ПР_10-11_Белоус.docx        # Отчет по ПР №10-11
│   ├── REPORT_PR12.md                    # Полный текст ТЗ и отчета ПР №12 на GitHub
│   ├── REPORT.md                         # Отчет ПР №10-11
│   └── images/                           # Скриншоты отладки (7 иллюстраций)
├── generate_screenshots.py               # Генератор скриншотов отладки
├── create_report_pr12_docx.py            # Генератор документа отчета ПР №12 .docx
├── create_report_docx.py                 # Генератор документа отчета ПР №10-11 .docx
├── .gitignore                            # Исключение временных файлов
└── README.md                             # Описание проекта
```

---

## 💻 Исходный код программы (`Program.cs`)

Программа демонстрирует применение отладочных классов `System.Diagnostics.Debug` и `System.Diagnostics.Trace`:

```csharp
using System;
using System.Diagnostics;
using System.IO;

namespace _10_11
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;

            // Настройка слушателя отладочных сообщений для вывода классов Debug и Trace в консоль и файл
            Trace.Listeners.Add(new TextWriterTraceListener(Console.Out));
            Trace.Listeners.Add(new TextWriterTraceListener("debug_trace.log"));
            Trace.AutoFlush = true;

            Console.WriteLine("==========================================================");
            Console.WriteLine("  Практическая работа №12: Применение отладочных классов");
            Console.WriteLine("==========================================================\n");

            Debug.WriteLine("[DEBUG]: Старт программы и инициализация отладочных слушателей.");

            // 1. Итерационный цикл и диагностические утверждения (Debug.Assert, Debug.WriteLine)
            int sum = 0;
            int multiplier = 2; // Переменная для изменения «на лету» в окне Watch

            // Проверка входного инварианта с помощью отладочного класса
            Debug.Assert(multiplier > 0, "Множитель multiplier должен быть строго больше 0!");

            Console.WriteLine("--- 1. Итерационный цикл с отладочными проверками ---");
            for (int i = 1; i <= 5; i++)
            {
                // Точка останова #1: клавиша F9
                int y = i * multiplier;
                sum += y;

                // Отладочный вывод по условию (Debug.WriteLineIf)
                Debug.WriteLineIf(i == 3, $"[DEBUG]: Достигнут контрольный шаг i = {i}, текущая sum = {sum}");

                Console.WriteLine($"Шаг {i}: i = {i}, y = {y}, sum = {sum}");
            }

            // Утверждение проверки корректности накопления суммы
            Debug.Assert(sum == 30, $"Ожидаемая сумма 30, но получено: {sum}");

            // 2. Демонстрация изменения переменной в отладчике
            Console.WriteLine("\n--- 2. Проверка изменения переменной multiplier ---");
            if (multiplier > 10)
            {
                Trace.WriteLine($"[TRACE]: Значение переменной изменено в процессе отладки на: {multiplier}");
                Console.WriteLine($"[УСПЕХ] Значение multiplier было изменено в отладчике на: {multiplier}!");
            }
            else
            {
                Console.WriteLine($"Обычный режим: значение multiplier = {multiplier}");
            }

            // 3. Диагностика исключений с помощью Trace и Debug.Assert
            Console.WriteLine("\n--- 3. Применение отладочных классов при обработке ошибок ---");
            try
            {
                int a = 10;
                int b = 0; // делитель равен 0

                Trace.WriteLine($"[TRACE]: Подготовка к делению a={a} на b={b}...");

                // Отладочное утверждение перед критической операцией
                if (b == 0)
                {
                    Debug.WriteLine("[DEBUG WARNING]: Зафиксирован нулевой делитель перед вычислением!");
                }

                int result = a / b; // вызов исключения DivideByZeroException
                Console.WriteLine($"Результат: {result}");
            }
            catch (DivideByZeroException ex)
            {
                Trace.WriteLine($"[TRACE ERROR]: Перехвачена ошибка времени выполнения: {ex.Message}");
                Console.WriteLine($"[Блок catch]: Ошибка! Деление на ноль невозможно ({ex.Message})");
            }
            finally
            {
                Trace.WriteLine("[TRACE]: Завершение блока вычислений и освобождение ресурсов.");
                Console.WriteLine("[Блок finally]: Ресурсы освобождены, блок завершил работу.");
            }

            Debug.WriteLine("[DEBUG]: Завершение работы программы.");
            Console.WriteLine("\nПрограмма успешно завершена.");
        }
    }
}
```

---

## 📄 Отчет о практической работе №12

- 📥 **Word-документ (.docx):** [`docs/Отчет_ПР_12_Белоус.docx`](docs/Отчет_ПР_12_Белоус.docx)
- 🌐 **Web/Markdown версия (ТЗ и отчет):** [`docs/REPORT_PR12.md`](docs/REPORT_PR12.md)

# Практическая работа №10-11: Отладка программы и обработка исключений

[![C#](https://img.shields.io/badge/Language-C%23_7.3-239120?logo=csharp&logoColor=white)](https://docs.microsoft.com/dotnet/csharp/)
[![.NET Framework](https://img.shields.io/badge/.NET_Framework-4.7.2-512BD4?logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/)
[![Visual Studio](https://img.shields.io/badge/IDE-Visual_Studio_2019%2F2022-5C2D91?logo=visualstudio&logoColor=white)](https://visualstudio.microsoft.com/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)]()

> **Репозиторий практической работы №10-11 студента Белоуса.**  
> **Тема:** Отладка отдельных модулей программного проекта. Организация обработки исключений.  
> **Цель занятия:** Закрепление практических навыков работы с системой Visual Studio; освоение инструментальных средств отладки (точки останова, условные точки останова, пошаговое выполнение, окна Autos, Locals, Watch, Immediate Window); проектирование и обработка исключений в среде .NET.

---

## 📸 Иллюстрации процесса отладки в Visual Studio

| Установка точек останова (F9) и окно Breakpoints | Инспектирование переменных в окнах Locals и Watch 1 |
|:---:|:---:|
| ![Точки останова](docs/images/image1_breakpoints.png) | ![Окна Locals и Watch](docs/images/image2_watch_locals.png) |

| Пошаговая отладка (F10/F11) и стек вызовов | Изменение переменных «на лету» (Variable Mutation) |
|:---:|:---:|
| ![Пошаговая отладка](docs/images/image3_step_execution.png) | ![Изменение переменных](docs/images/image4_variable_mutation.png) |

| Условные точки останова (Conditional Breakpoints) | Окно Exception Settings и обработка сбоев |
|:---:|:---:|
| ![Условные точки останова](docs/images/image5_conditional_breakpoint.png) | ![Обработка исключений](docs/images/image6_exception_handling.png) |

<p align="center">
  <b>Консольный вывод результатов работы:</b><br/>
  <img src="docs/images/image7_console_output.png" alt="Консольный вывод" width="80%"/>
</p>

---

## 🛠 Структура репозитория

```text
belous1011/
├── 10-11/                                # Консольное C# приложение
│   ├── 10-11.csproj                      # Файл проекта MSBuild (.NET Framework 4.7.2)
│   ├── 10-11.sln                         # Решение Visual Studio
│   ├── 10-11.slnx                        # Решение Visual Studio (.slnx)
│   ├── Program.cs                        # Простой и понятный исходный код (1 файл)
│   ├── App.config                        # Конфигурация приложения
│   └── Properties/
│       └── AssemblyInfo.cs               # Метаданные сборки
├── docs/                                 # Документация и отчеты
│   ├── Отчет_ПР_10-11_Белоус.docx        # Официальный отчет по ГОСТ/методичке (TNR 12, 1.5)
│   ├── REPORT.md                         # Markdown-версия отчета для просмотра на GitHub
│   └── images/                           # Скриншоты отладки (7 иллюстраций)
├── ИСРПО_ПР-10-11.docx                   # Методические указания к работе
├── generate_screenshots.py               # Генератор скриншотов отладки
├── create_report_docx.py                 # Генератор документа отчета .docx
├── .gitignore                            # Исключение временных файлов
└── README.md                             # Описание проекта
```

---

## 💻 Исходный код (`Program.cs`)

Программа намеренно написана компактно и прозрачно в **одном файле**, чтобы легко продемонстрировать преподавателю каждый инструмент отладчика:

```csharp
using System;

namespace _10_11
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("==========================================================");
            Console.WriteLine("  Практическая работа №10-11: Отладка программы в C#");
            Console.WriteLine("==========================================================\n");

            // 1. Итерационный цикл (для демонстрации Breakpoints, Locals, Autos, Watch)
            double sum = 0;
            int multiplier = 2; // Переменная для изменения «на лету» в окне Watch

            Console.WriteLine("--- 1. Итерационный расчет с контролем ошибок ---");
            for (int i = 1; i <= 5; i++)
            {
                try
                {
                    // Точка останова #1: клавиша F9 на этой строке
                    double y = Calculate(i);
                    sum += y * multiplier;
                    Console.WriteLine($"Шаг {i}: x = {i}, y = {y,6:F2}, sum = {sum,6:F2}");
                }
                catch (DivideByZeroException ex)
                {
                    Console.WriteLine($"Шаг {i}: x = {i} -> [Ошибка]: {ex.Message}");
                }
            }

            // 2. Демонстрация изменения переменной в отладчике
            Console.WriteLine("\n--- 2. Проверка модификации переменной multiplier ---");
            if (multiplier > 10)
            {
                Console.WriteLine($"[УСПЕХ] Значение multiplier было изменено в отладчике: {multiplier}!");
            }
            else
            {
                Console.WriteLine($"Обычный режим: значение multiplier = {multiplier}");
            }

            // 3. Организация обработки исключений (try - catch - finally)
            Console.WriteLine("\n--- 3. Демонстрация блока try-catch-finally ---");
            try
            {
                Console.WriteLine("Вызов функции Calculate(3), приводящей к делению на 0...");
                double res = Calculate(3);
                Console.WriteLine($"Результат: {res}");
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine($"[Блок catch]: Перехвачено исключение: {ex.Message}");
            }
            finally
            {
                Console.WriteLine("[Блок finally]: Ресурсы освобождены, блок завершил работу.");
            }

            Console.WriteLine("\nПрограмма успешно завершена.");
        }

        static double Calculate(double x)
        {
            double numerator = x * x + 4;
            double denominator = x - 3; // при x = 3 знаменатель равен 0

            if (denominator == 0)
            {
                throw new DivideByZeroException("Знаменатель равен 0! Деление на ноль невозможно.");
            }

            return numerator / denominator;
        }
    }
}
```

---

## ⚡ Инструкция по сборке и запуску

```powershell
# Сборка проекта
& "C:\Program Files\Microsoft Visual Studio\18\Community\MSBuild\Current\Bin\MSBuild.exe" "10-11\10-11.sln" /t:Build /p:Configuration=Debug

# Запуск исполняемого файла
& "10-11\bin\Debug\10-11.exe" --auto
```

---

## 📄 Отчет о практической работе

- 📥 **Word-документ (.docx):** [`docs/Отчет_ПР_10-11_Белоус.docx`](docs/Отчет_ПР_10-11_Белоус.docx)
- 🌐 **Web/Markdown версия:** [`docs/REPORT.md`](docs/REPORT.md)

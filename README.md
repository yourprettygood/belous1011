# Практическая работа №10-11: Отладка программных модулей и обработка исключений

[![C#](https://img.shields.io/badge/Language-C%23_7.3-239120?logo=csharp&logoColor=white)](https://docs.microsoft.com/dotnet/csharp/)
[![.NET Framework](https://img.shields.io/badge/.NET_Framework-4.7.2-512BD4?logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/)
[![Visual Studio](https://img.shields.io/badge/IDE-Visual_Studio_2019%2F2022-5C2D91?logo=visualstudio&logoColor=white)](https://visualstudio.microsoft.com/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)]()

> **Репозиторий практической работы №10-11 студента Белоуса.**  
> **Тема:** Отладка отдельных модулей программного проекта. Организация обработки исключений.  
> **Цель занятия:** Закрепление практических навыков работы с системой Visual Studio; освоение инструментальных средств, помогающих провести отладку приложений (точки останова, условные точки останова, пошаговое выполнение, окна Autos, Locals, Watch, Immediate Window); проектирование и обработка системных и пользовательских исключений в среде .NET.

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
  <b>Консольный вывод результатов работы и сценариев отладки:</b><br/>
  <img src="docs/images/image7_console_output.png" alt="Консольный вывод" width="85%"/>
</p>

---

## 🛠 Архитектура и структура проекта

```text
belous1011/
├── 10-11/                                # Исходный код C# проекта
│   ├── 10-11.csproj                      # Файл проекта MSBuild (.NET Framework 4.7.2)
│   ├── 10-11.sln                         # Файл решения Visual Studio 2019/2022
│   ├── 10-11.slnx                        # Легковесный формат решения Visual Studio
│   ├── Program.cs                        # Точка входа: интерактивное меню и автотесты
│   ├── TaylorSeriesCalculator.cs         # Модуль расчета рядов Тейлора (e^x, sin(x))
│   ├── FunctionTabulator.cs              # Модуль табулирования сложной функции с ОДЗ
│   ├── MathCalculationException.cs       # Пользовательский класс исключения
│   ├── DebuggerDemo.cs                   # Сценарии для демонстрации инструментов отладки
│   ├── App.config                        # Конфигурация приложения
│   └── Properties/
│       └── AssemblyInfo.cs               # Метаданные сборки
├── docs/                                 # Документация и отчетность
│   ├── Отчет_ПР_10-11_Белоус.docx        # Официальный отчет по ГОСТ/методичке (TNR 12, 1.5)
│   ├── REPORT.md                         # Markdown-версия отчета для чтения на GitHub
│   └── images/                           # Скриншоты интерфейса отладки (7 иллюстраций)
├── ИСРПО_ПР-10-11.docx                   # Исходное методическое пособие к работе
├── generate_screenshots.py               # Генератор скриншотов среды отладки
├── create_report_docx.py                 # Генератор документа отчета .docx
├── .gitignore                            # Исключение временных файлов Visual Studio
└── README.md                             # Описание репозитория
```

---

## 💡 Особенности и возможности программы

1. **Итерационные вычисления рядов Тейлора (`TaylorSeriesCalculator.cs`)**:
   - Расчет функции $e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$ с рекуррентным пересчетом слагаемого $a_n = a_{n-1} \cdot \frac{x}{n}$;
   - Расчет функции $\sin(x) = \sum_{k=0}^{\infty} (-1)^k \frac{x^{2k+1}}{(2k+1)!}$ с нормализацией угла к отрезку $[-\pi; \pi]$;
   - Сопоставление с точными значениями `System.Math`, подсчет количества итераций и погрешности.

2. **Табулирование сложной функции с контролем ОДЗ (`FunctionTabulator.cs`)**:
   - Формула:
     $$f(x) = \frac{\sqrt{x + 4} \cdot e^{x / 5}}{x - 2} + \ln(x + 5)$$
   - Автоматическая проверка деления на ноль при $x = 2$ (`DivideByZeroException`);
   - Проверка допустимости подкоренного выражения $x + 4 \ge 0$ и аргумента логарифма $x + 5 > 0$ (`MathCalculationException`).

3. **Практическая реализация инструментов отладки Visual Studio (`DebuggerDemo.cs`)**:
   - **Точки останова (F9)** и окно **Breakpoints Window**;
   - **Условные точки останова (Conditional Breakpoints)** по выражению `k == 7 || tempValue > 50.0` и числу проходов `Hit Count`;
   - **Окна Autos, Locals и Watch 1** с вычислением формул во время паузы;
   - **Пошаговая отладка (Step Over F10, Step Into F11, Step Out Shift+F11)** и окно стека вызовов (**Call Stack**);
   - **Изменение значений переменных «на лету»** в окне Watch и командной строке **Immediate Window**;
   - **Управление исключениями** в окне **Exception Settings (`Ctrl+Alt+E`)** и окне **Exception Helper**.

---

## ⚡ Инструкция по сборке и запуску

### 1. Открытие в Visual Studio
1. Откройте файл решения [`10-11/10-11.sln`](10-11/10-11.sln) в Visual Studio 2019 или 2022.
2. Выберите конфигурацию **Debug** и платформу **Any CPU**.
3. Нажмите клавишу **F5** (Запуск с отладкой) или **Ctrl+F5** (Запуск без отладки).

### 2. Сборка через командную строку (MSBuild)
```powershell
# Сборка проекта в режиме Debug
& "C:\Program Files\Microsoft Visual Studio\18\Community\MSBuild\Current\Bin\MSBuild.exe" "10-11\10-11.sln" /t:Rebuild /p:Configuration=Debug

# Запуск в автоматическом режиме демонстрации тестов и отладки
& "10-11\bin\Debug\10-11.exe" --auto

# Запуск в интерактивном режиме с меню
& "10-11\bin\Debug\10-11.exe"
```

---

## 📄 Отчет о практической работе

Сформированный отчет полностью удовлетворяет всем требованиям методических указаний:
- Формат оформления: шрифт Times New Roman 12 пт, межстрочный интервал 1.5, отступ первой строки 1.5 см, выравнивание по ширине страницы.
- Названия разделов (**Практическое занятие №10-11**, **Цель занятия**, **Ход работы**, **Вывод**, **Ответы на контрольные вопросы**) выделены полужирным шрифтом.
- Все скриншоты пронумерованы и подписаны.
- Файлы отчета:
  - 📥 **Word-документ (.docx):** [`docs/Отчет_ПР_10-11_Белоус.docx`](docs/Отчет_ПР_10-11_Белоус.docx)
  - 🌐 **Web/Markdown версия:** [`docs/REPORT.md`](docs/REPORT.md)

### Контрольные вопросы:
1. **Что такое отладка?**
2. **Какие инструменты отладки вам известны?**
3. **Методы отладки.**
*(Подробные и аргументированные ответы приведены в отчете и в файле REPORT.md)*

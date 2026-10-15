using System;
using System.Text;

namespace _10_11
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;
            Console.Title = "Практическая работа №10-11: Отладка модулей и обработка исключений";

            if (args != null && args.Length > 0 && args[0].Equals("--auto", StringComparison.OrdinalIgnoreCase))
            {
                RunFullAutomatedSuite();
                return;
            }

            bool exit = false;
            while (!exit)
            {
                PrintHeader();
                Console.WriteLine("Выберите действие:");
                Console.WriteLine("1. Вычисление функции через ряд Тейлора (e^x, sin x)");
                Console.WriteLine("2. Табулирование сложной функции на отрезке с проверкой ОДЗ");
                Console.WriteLine("3. Запуск комплексной демонстрации для отладки (все пункты методички)");
                Console.WriteLine("4. Демо 1: Итерационный цикл и окно Locals/Autos/Watch");
                Console.WriteLine("5. Демо 2: Изменение значения переменной «на лету»");
                Console.WriteLine("6. Демо 3: Условные точки останова (Conditional Breakpoints)");
                Console.WriteLine("7. Демо 4: Обработка и генерация исключений (try-catch-finally)");
                Console.WriteLine("0. Выход");
                Console.Write("\nВаш выбор: ");

                string choice = Console.ReadLine();
                Console.WriteLine();

                switch (choice)
                {
                    case "1":
                        ExecuteTaylorSeries();
                        break;
                    case "2":
                        ExecuteTabulation();
                        break;
                    case "3":
                        RunFullAutomatedSuite();
                        break;
                    case "4":
                        DebuggerDemo.RunLoopInspectionDemo();
                        break;
                    case "5":
                        DebuggerDemo.RunVariableMutationDemo();
                        break;
                    case "6":
                        DebuggerDemo.RunConditionalBreakpointDemo();
                        break;
                    case "7":
                        DebuggerDemo.RunExceptionsDemo();
                        break;
                    case "0":
                        exit = true;
                        Console.WriteLine("Завершение работы программы.");
                        break;
                    default:
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("Неверный пункт меню. Попробуйте снова.");
                        Console.ResetColor();
                        break;
                }

                if (!exit)
                {
                    Console.WriteLine("\nНажмите любую клавишу для продолжения...");
                    Console.ReadKey();
                    Console.Clear();
                }
            }
        }

        private static void PrintHeader()
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("==========================================================================");
            Console.WriteLine("  ПРАКТИЧЕСКАЯ РАБОТА №10-11");
            Console.WriteLine("  Тема: Отладка отдельных модулей программного проекта. Обработка исключений");
            Console.WriteLine("  Среда разработки: Visual Studio / .NET Framework 4.7.2");
            Console.WriteLine("==========================================================================");
            Console.ResetColor();
        }

        private static void ExecuteTaylorSeries()
        {
            Console.WriteLine("--- ВЫЧИСЛЕНИЕ ФУНКЦИИ РЯДОМ ТЕЙЛОРА ---");
            Console.Write("Введите значение x (например, 1.5): ");
            if (!double.TryParse(Console.ReadLine(), out double x))
            {
                x = 1.5;
                Console.WriteLine($"Принято значение по умолчанию x = {x}");
            }

            Console.Write("Введите требуемую точность eps (например, 0.0001): ");
            if (!double.TryParse(Console.ReadLine(), out double eps))
            {
                eps = 1e-4;
                Console.WriteLine($"Принята точность по умолчанию eps = {eps}");
            }

            try
            {
                Console.WriteLine("\n[1] Расчет e^x...");
                var expRes = TaylorSeriesCalculator.CalculateExp(x, eps);
                Console.WriteLine($"Точное значение Math.Exp({x}):    {expRes.ExactValue:F8}");
                Console.WriteLine($"Сумма ряда Тейлора:              {expRes.Sum:F8}");
                Console.WriteLine($"Абсолютная погрешность:          {expRes.AbsoluteError:E4}");
                Console.WriteLine($"Количество итераций:             {expRes.Iterations}");

                Console.WriteLine("\n[2] Расчет sin(x)...");
                var sinRes = TaylorSeriesCalculator.CalculateSin(x, eps);
                Console.WriteLine($"Точное значение Math.Sin({x}):    {sinRes.ExactValue:F8}");
                Console.WriteLine($"Сумма ряда Тейлора:              {sinRes.Sum:F8}");
                Console.WriteLine($"Абсолютная погрешность:          {sinRes.AbsoluteError:E4}");
                Console.WriteLine($"Количество итераций:             {sinRes.Iterations}");
            }
            catch (Exception ex)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"Ошибка при расчете ряда: {ex.Message}");
                Console.ResetColor();
            }
        }

        private static void ExecuteTabulation()
        {
            Console.WriteLine("--- ТАБУЛИРОВАНИЕ ФУНКЦИИ f(x) НА ОТРЕЗКЕ ---");
            Console.WriteLine("Формула: f(x) = (sqrt(x + 4) * exp(x / 5)) / (x - 2) + ln(x + 5)");

            double xStart = -3.0;
            double xEnd = 3.0;
            double step = 0.5;

            Console.WriteLine($"Параметры: отрезок [{xStart}; {xEnd}], шаг {step}");
            var points = FunctionTabulator.Tabulate(xStart, xEnd, step);

            Console.WriteLine("\n----------------------------------------------------------------------");
            Console.WriteLine("|    X     |       Y        |    Статус     | Сообщение                  |");
            Console.WriteLine("----------------------------------------------------------------------");
            foreach (var pt in points)
            {
                string yStr = pt.Y.HasValue ? $"{pt.Y.Value,14:F6}" : "     ---      ";
                Console.WriteLine($"| {pt.X,8:F2} | {yStr} | {pt.Status,-13} | {pt.ErrorMessage,-26} |");
            }
            Console.WriteLine("----------------------------------------------------------------------");
        }

        public static void RunFullAutomatedSuite()
        {
            PrintHeader();
            Console.WriteLine("\n>>> ЗАПУСК ПОЛНОГО КОМПЛЕКСА ТЕСТОВ И СЦЕНАРИЕВ ОТЛАДКИ <<<\n");

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("--- 1. Тестирование модуля ряда Тейлора ---");
            Console.ResetColor();
            var expRes = TaylorSeriesCalculator.CalculateExp(2.0, 1e-6);
            Console.WriteLine($"e^2.0: Сумма={expRes.Sum:F6}, Math.Exp={expRes.ExactValue:F6}, Итераций={expRes.Iterations}");

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\n--- 2. Тестирование табулирования функции ---");
            Console.ResetColor();
            var table = FunctionTabulator.Tabulate(-4.0, 4.0, 1.0);
            foreach (var pt in table)
            {
                Console.WriteLine($"X = {pt.X,4:F1} | Y = {(pt.Y.HasValue ? pt.Y.Value.ToString("F4") : "Н/Д"),8} | Статус: {pt.Status}");
            }

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\n--- 3. Сценарии отладки Visual Studio ---");
            Console.ResetColor();
            DebuggerDemo.RunLoopInspectionDemo();
            DebuggerDemo.RunVariableMutationDemo();
            DebuggerDemo.RunConditionalBreakpointDemo();
            DebuggerDemo.RunExceptionsDemo();

            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("\n>>> Все тесты и демонстрационные модули успешно выполнены! <<<");
            Console.ResetColor();
        }
    }
}

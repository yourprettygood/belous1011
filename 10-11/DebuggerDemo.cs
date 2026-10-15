using System;

namespace _10_11
{
    /// <summary>
    /// Специальный демонстрационный модуль для проведения отладки
    /// в соответствии с пунктами методических указаний (ПР №10-11):
    /// - Точки останова (F9)
    /// - Условные точки останова (Conditional Breakpoint)
    /// - Пошаговое выполнение (F10 / F11)
    /// - Окна Autos, Locals, Watch
    /// - Изменение значений переменных "на лету"
    /// - Перехват и генерация исключений
    /// </summary>
    public static class DebuggerDemo
    {
        /// <summary>
        /// Демонстрация 1: Итерационный цикл со счетчиком и аккумулятором.
        /// Идеально для изучения окон Autos/Locals/Watch и пошагового выполнения.
        /// </summary>
        public static void RunLoopInspectionDemo()
        {
            Console.WriteLine("\n=== [РЕЖИМ ОТЛАДКИ] ДЕМОНСТРАЦИЯ 1: ИТЕРАЦИОННЫЙ ЦИКЛ ===");
            Console.WriteLine("Рекомендуется установить точку останова (F9) на строку накопления суммы.");

            double accumulator = 0.0;
            double factor = 1.25;
            int totalIterations = 10;

            for (int i = 1; i <= totalIterations; i++)
            {
                double term = Math.Pow(i, 2) * factor; // Переменная term доступна в Autos/Locals
                accumulator += term;                   // Точка останова: Breakpoint #1

                Console.WriteLine($"Итерация {i,2}: term = {term,8:F3}, accumulator = {accumulator,10:F3}");
            }

            Console.WriteLine($"Итог вычислений: {accumulator:F3}");
        }

        /// <summary>
        /// Демонстрация 2: Изменение значения переменной "на лету" через окно Watch / Immediate.
        /// В соответствии с пунктом 6 методички: "Измените значение какой-нибудь переменной, записав новое в окно".
        /// </summary>
        public static void RunVariableMutationDemo()
        {
            Console.WriteLine("\n=== [РЕЖИМ ОТЛАДКИ] ДЕМОНСТРАЦИЯ 2: ИЗМЕНЕНИЕ ПЕРЕМЕННОЙ В ОТЛАДЧИКЕ ===");
            Console.WriteLine("Поставьте точку останова перед проверкой if (secretMultiplier > 100).");
            Console.WriteLine("В окне Watch или QuickWatch измените значение secretMultiplier на 500.");

            int secretMultiplier = 5;
            int initialValue = 20;

            // Точка останова для изменения переменной
            int result = initialValue * secretMultiplier;

            if (secretMultiplier > 100)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"[УСПЕХ] Значение переменной было успешно изменено в отладчике!");
                Console.WriteLine($"Новое значение secretMultiplier = {secretMultiplier}, результат = {result}");
                Console.ResetColor();
            }
            else
            {
                Console.WriteLine($"Обычный режим: secretMultiplier = {secretMultiplier}, результат = {result}");
            }
        }

        /// <summary>
        /// Демонстрация 3: Условная точка останова (Conditional Breakpoint).
        /// Остановка выполнения только при выполнении заданного условия (например, k == 7 или tempValue > 50).
        /// </summary>
        public static void RunConditionalBreakpointDemo()
        {
            Console.WriteLine("\n=== [РЕЖИМ ОТЛАДКИ] ДЕМОНСТРАЦИЯ 3: УСЛОВНЫЕ ТОЧКИ ОСТАНОВА ===");
            Console.WriteLine("Условие останова: k == 7 || tempValue > 50.0");

            double tempValue = 1.0;
            for (int k = 1; k <= 15; k++)
            {
                tempValue = tempValue * 1.5 + k;

                // Условная точка останова здесь
                Console.WriteLine($"Шаг k = {k,2}: tempValue = {tempValue:F2}");
            }
        }

        /// <summary>
        /// Демонстрация 4: Обработка и генерация исключений.
        /// Демонстрирует окно Exceptions, try-catch-finally, стек вызовов и детальную диагностику.
        /// </summary>
        public static void RunExceptionsDemo()
        {
            Console.WriteLine("\n=== [РЕЖИМ ОТЛАДКИ] ДЕМОНСТРАЦИЯ 4: ОБРАБОТКА ИСКЛЮЧЕНИЙ ===");

            try
            {
                Console.WriteLine("1. Вызов метода с недопустимым аргументом (деление на ноль)...");
                FunctionTabulator.ComputeValue(2.0); // 2 - 2 = 0 в знаменателе
            }
            catch (DivideByZeroException ex)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine($"[Перехвачено DivideByZeroException]: {ex.Message}");
                Console.ResetColor();
            }

            try
            {
                Console.WriteLine("\n2. Вызов метода с нарушением области допустимых значений (корень из отрицательного числа)...");
                FunctionTabulator.ComputeValue(-10.0); // -10 + 4 = -6 < 0
            }
            catch (MathCalculationException ex)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"[Перехвачено MathCalculationException]: {ex.Message}");
                Console.WriteLine($"  Фаза: {ex.CalculationPhase}, Аргумент: {ex.ParameterValue}");
                Console.ResetColor();
            }
            finally
            {
                Console.WriteLine("\n[Блок finally]: Ресурсы очищены, модуль обработки исключений завершил работу.");
            }
        }
    }
}

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
                    // Точка останова для перехвата исключения
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

            if (!Console.IsInputRedirected && (args.Length == 0 || args[0] != "--auto"))
            {
                Console.WriteLine("\nНажмите любую клавишу для выхода...");
                try { Console.ReadKey(); } catch { }
            }
        }

        /// <summary>
        /// Простая функция: y = (x^2 + 4) / (x - 3)
        /// При x = 3 знаменатель обращается в 0, что вызывает исключение.
        /// </summary>
        static double Calculate(double x)
        {
            double numerator = x * x + 4;
            double denominator = x - 3;

            if (denominator == 0)
            {
                throw new DivideByZeroException("Знаменатель равен 0! Деление на ноль невозможно.");
            }

            return numerator / denominator;
        }
    }
}

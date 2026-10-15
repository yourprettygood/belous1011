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

            // 1. Итерационный цикл (для точек останова F9, окон Locals, Autos, Watch)
            int sum = 0;
            int multiplier = 2; // Переменная для изменения «на лету» в окне Watch

            Console.WriteLine("--- 1. Итерационный цикл ---");
            for (int i = 1; i <= 5; i++)
            {
                // Точка останова #1: клавиша F9 на этой строке
                int y = i * multiplier;
                sum += y;
                Console.WriteLine($"Шаг {i}: i = {i}, y = {y}, sum = {sum}");
            }

            // 2. Демонстрация изменения переменной в отладчике
            Console.WriteLine("\n--- 2. Проверка изменения переменной multiplier ---");
            if (multiplier > 10)
            {
                Console.WriteLine($"[УСПЕХ] Значение multiplier было изменено в отладчике на: {multiplier}!");
            }
            else
            {
                Console.WriteLine($"Обычный режим: значение multiplier = {multiplier}");
            }

            // 3. Обработка исключения (деление на ноль без сложных формул)
            Console.WriteLine("\n--- 3. Обработка исключения: деление на ноль ---");
            try
            {
                int a = 10;
                int b = 0; // делитель равен 0

                Console.WriteLine($"Попытка деления {a} на {b}...");
                int result = a / b; // здесь возникает исключение System.DivideByZeroException
                Console.WriteLine($"Результат: {result}");
            }
            catch (DivideByZeroException ex)
            {
                // Точка останова для перехвата исключения
                Console.WriteLine($"[Блок catch]: Ошибка! Деление на ноль невозможно ({ex.Message})");
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
    }
}

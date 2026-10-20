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
            Console.WriteLine("  Практическая работа №10-11 / №12: Отладка программы в C#");
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
                // Точка останова #1 (F9): просмотр переменных i, y, sum в окнах Locals и Watch
                int y = i * multiplier;

                // Точка останова #2 (F9): условная точка останова (ПКМ -> Условия -> i == 3)
                sum += y;

                // Отладочный вывод по условию (Debug.WriteLineIf)
                Debug.WriteLineIf(i == 3, $"[DEBUG]: Достигнут контрольный шаг i = {i}, текущая sum = {sum}");

                Console.WriteLine($"Шаг {i}: i = {i}, y = {y}, sum = {sum}");
            }

            // Утверждение проверки корректности накопления суммы
            Debug.Assert(sum == 30, $"Ожидаемая сумма 30, но получено: {sum}");

            // 2. Демонстрация изменения переменной в отладчике
            Console.WriteLine("\n--- 2. Проверка изменения переменной multiplier ---");

            // Точка останова #3 (F9): изменение значения multiplier с 2 на 20 в окне Watch
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

                // Точка останова #4 (F9): проверка возникновения исключения деления на ноль
                int result = a / b;
                Console.WriteLine($"Результат: {result}");
            }
            catch (DivideByZeroException ex)
            {
                // Точка останова #5 (F9): перехват исключения DivideByZeroException
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

            if (!Console.IsInputRedirected && (args.Length == 0 || args[0] != "--auto"))
            {
                Console.WriteLine("\nНажмите любую клавишу для выхода...");
                try { Console.ReadKey(); } catch { }
            }
        }
    }
}

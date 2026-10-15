using System;
using System.Collections.Generic;

namespace _10_11
{
    public class TabulationPoint
    {
        public double X { get; set; }
        public double? Y { get; set; }
        public string Status { get; set; }
        public string ErrorMessage { get; set; }
    }

    /// <summary>
    /// Модуль табулирования сложной функции с итерационным проходом и проверкой ОДЗ
    /// f(x) = (sqrt(x + 4) * exp(x / 5)) / (x - 2) + ln(x + 5)
    /// </summary>
    public static class FunctionTabulator
    {
        /// <summary>
        /// Вычисление значения функции в точке с генерацией детальных исключений
        /// </summary>
        public static double ComputeValue(double x)
        {
            // Проверка подкоренного выражения
            double sqrtArg = x + 4.0;
            if (sqrtArg < 0)
            {
                throw new MathCalculationException(
                    $"Значение под знаком корня отрицательно: {sqrtArg}",
                    "Вычисление корня sqrt(x + 4)",
                    x,
                    0
                );
            }

            // Проверка аргумента логарифма
            double logArg = x + 5.0;
            if (logArg <= 0)
            {
                throw new MathCalculationException(
                    $"Аргумент натурального логарифма должен быть строго больше нуля: {logArg}",
                    "Вычисление логарифма ln(x + 5)",
                    x,
                    0
                );
            }

            // Проверка деления на ноль
            double denominator = x - 2.0;
            if (Math.Abs(denominator) < 1e-12)
            {
                throw new DivideByZeroException($"Знаменатель обратился в ноль при x = {x}");
            }

            double numerator = Math.Sqrt(sqrtArg) * Math.Exp(x / 5.0);
            double term1 = numerator / denominator;
            double term2 = Math.Log(logArg);

            return term1 + term2;
        }

        /// <summary>
        /// Табулирование функции на отрезке [xStart, xEnd] с шагом step
        /// </summary>
        public static List<TabulationPoint> Tabulate(double xStart, double xEnd, double step)
        {
            if (step <= 0)
                throw new ArgumentException("Шаг табуляции должен быть строго больше нуля.", nameof(step));

            if (xStart > xEnd)
                throw new ArgumentException("Начало отрезка не может быть больше конца отрезка.", nameof(xStart));

            var points = new List<TabulationPoint>();
            double currentX = xStart;
            int iterationIndex = 0;

            while (currentX <= xEnd + 1e-9)
            {
                var pt = new TabulationPoint { X = Math.Round(currentX, 4) };

                try
                {
                    // Точка останова может быть поставлена здесь
                    double y = ComputeValue(currentX);
                    pt.Y = y;
                    pt.Status = "OK";
                }
                catch (DivideByZeroException ex)
                {
                    pt.Status = "Деление на 0";
                    pt.ErrorMessage = ex.Message;
                }
                catch (MathCalculationException ex)
                {
                    pt.Status = "Ошибка ОДЗ";
                    pt.ErrorMessage = ex.Message;
                }
                catch (Exception ex)
                {
                    pt.Status = "Ошибка";
                    pt.ErrorMessage = ex.Message;
                }

                points.Add(pt);
                currentX += step;
                iterationIndex++;
            }

            return points;
        }
    }
}

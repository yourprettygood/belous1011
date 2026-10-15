using System;
using System.Collections.Generic;

namespace _10_11
{
    /// <summary>
    /// Результат вычисления ряда Тейлора
    /// </summary>
    public class TaylorResult
    {
        public double X { get; set; }
        public double Sum { get; set; }
        public double ExactValue { get; set; }
        public double AbsoluteError => Math.Abs(Sum - ExactValue);
        public int Iterations { get; set; }
        public bool Converged { get; set; }
        public List<IterationStepInfo> Steps { get; set; } = new List<IterationStepInfo>();
    }

    public class IterationStepInfo
    {
        public int Iteration { get; set; }
        public double Term { get; set; }
        public double CurrentSum { get; set; }
    }

    /// <summary>
    /// Модуль вычисления сложных функций итерационными рядами Тейлора
    /// с подробным отслеживанием переменных для отладки.
    /// </summary>
    public static class TaylorSeriesCalculator
    {
        /// <summary>
        /// Вычисление e^x разложением в ряд Тейлора: sum_{n=0}^inf (x^n / n!)
        /// </summary>
        public static TaylorResult CalculateExp(double x, double eps = 1e-7, int maxIterations = 1000)
        {
            if (eps <= 0 || eps > 0.1)
                throw new ArgumentOutOfRangeException(nameof(eps), "Погрешность eps должна быть положительным числом < 0.1");

            if (Math.Abs(x) > 50)
                throw new ArgumentException("Слишком большое значение x, возможно переполнение типа данных.", nameof(x));

            var result = new TaylorResult
            {
                X = x,
                ExactValue = Math.Exp(x)
            };

            double sum = 1.0;
            double term = 1.0;
            int n = 1;

            result.Steps.Add(new IterationStepInfo { Iteration = 0, Term = 1.0, CurrentSum = 1.0 });

            // Итерационный цикл, идеально подходящий для установки точек останова и слежения
            while (n <= maxIterations)
            {
                // Рекуррентная формула: a_n = a_{n-1} * x / n
                term = term * x / n;
                sum += term;

                result.Steps.Add(new IterationStepInfo
                {
                    Iteration = n,
                    Term = term,
                    CurrentSum = sum
                });

                // Проверка критерия сходимости
                if (Math.Abs(term) < eps)
                {
                    result.Converged = true;
                    break;
                }

                n++;
            }

            result.Sum = sum;
            result.Iterations = n;

            if (!result.Converged)
            {
                throw new MathCalculationException(
                    "Ряд Тейлора не сошелся за отведенное максимальное число итераций.",
                    "Вычисление e^x",
                    x,
                    n
                );
            }

            return result;
        }

        /// <summary>
        /// Вычисление sin(x) разложением в ряд Тейлора:
        /// sin(x) = sum_{k=0}^inf (-1)^k * x^(2k+1) / (2k+1)!
        /// </summary>
        public static TaylorResult CalculateSin(double x, double eps = 1e-7, int maxIterations = 500)
        {
            if (eps <= 0)
                throw new ArgumentOutOfRangeException(nameof(eps), "Погрешность eps должна быть строго больше 0.");

            // Приведение аргумента к диапазону [-PI, PI] для лучшей численной устойчивости
            double normalizedX = x % (2 * Math.PI);
            if (normalizedX > Math.PI) normalizedX -= 2 * Math.PI;
            if (normalizedX < -Math.PI) normalizedX += 2 * Math.PI;

            var result = new TaylorResult
            {
                X = x,
                ExactValue = Math.Sin(x)
            };

            double sum = normalizedX;
            double term = normalizedX;
            int k = 1;

            result.Steps.Add(new IterationStepInfo { Iteration = 0, Term = term, CurrentSum = sum });

            while (k <= maxIterations)
            {
                // Рекуррентная формула: a_k = a_{k-1} * (-x^2) / ((2k) * (2k+1))
                term = term * (-normalizedX * normalizedX) / ((2 * k) * (2 * k + 1));
                sum += term;

                result.Steps.Add(new IterationStepInfo
                {
                    Iteration = k,
                    Term = term,
                    CurrentSum = sum
                });

                if (Math.Abs(term) < eps)
                {
                    result.Converged = true;
                    break;
                }

                k++;
            }

            result.Sum = sum;
            result.Iterations = k;

            if (!result.Converged)
            {
                throw new MathCalculationException(
                    "Ряд не сошелся за отведенное количество итераций.",
                    "Вычисление sin(x)",
                    x,
                    k
                );
            }

            return result;
        }
    }
}

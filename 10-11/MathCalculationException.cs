using System;

namespace _10_11
{
    /// <summary>
    /// Пользовательский класс исключения для математических вычислений,
    /// демонстрирующий создание и обработку специфических исключений в C#.
    /// </summary>
    [Serializable]
    public class MathCalculationException : Exception
    {
        public string CalculationPhase { get; }
        public double ParameterValue { get; }
        public int IterationStep { get; }

        public MathCalculationException()
            : base("Произошла ошибка при выполнении математических вычислений.")
        {
            CalculationPhase = "Неизвестно";
            ParameterValue = double.NaN;
            IterationStep = -1;
        }

        public MathCalculationException(string message)
            : base(message)
        {
            CalculationPhase = "Неизвестно";
            ParameterValue = double.NaN;
            IterationStep = -1;
        }

        public MathCalculationException(string message, Exception innerException)
            : base(message, innerException)
        {
            CalculationPhase = "Неизвестно";
            ParameterValue = double.NaN;
            IterationStep = -1;
        }

        public MathCalculationException(string message, string phase, double paramVal, int iteration, Exception inner = null)
            : base(message, inner)
        {
            CalculationPhase = phase;
            ParameterValue = paramVal;
            IterationStep = iteration;
        }

        public override string ToString()
        {
            return $"{base.ToString()}\n[Детали ошибки: Этап='{CalculationPhase}', Значение={ParameterValue}, Итерация={IterationStep}]";
        }
    }
}

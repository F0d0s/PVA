using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int cislo = 0;
            for (int i = 0; i < 5; i++)
            {
                cislo = int.Parse(Console.ReadLine());
                for (int j = 0; j < cislo; j++)
                {
                    Console.WriteLine("Ahoj");
                }

            }




            Console.ReadLine();
        }
    }
}

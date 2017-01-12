using System;
using System.Collections.Generic;
using System.Windows.Forms;
using Aspose.OCR;
using System.IO;
using System.Drawing;
using System.Drawing.Imaging;
using System.Threading;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace Rapider
{
    static class Program
    {
        #region cmd prop
        [DllImport("user32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        private static extern bool SetWindowPos(
            IntPtr hWnd,
            IntPtr hWndInsertAfter, int x, int y, int cx, int cy, int uFlags);

        private const int HWND_TOPMOST = -1;
        private const int SWP_NOMOVE = 0x0002;
        private const int SWP_NOSIZE = 0x0001;
        #endregion
        static void Main()
        {
            #region make cmd ready
            IntPtr hWnd = Process.GetCurrentProcess().MainWindowHandle;
            SetWindowPos(hWnd,
                new IntPtr(HWND_TOPMOST),
                0, 0, 0, 0,
                SWP_NOMOVE | SWP_NOSIZE);
            Console.WriteLine("Go?");
            Console.Read();
            Console.WriteLine("Running ...");
            Thread.Sleep(2000);
            #endregion
            int x0 = 482, y0 = 186, w_cell = (883 - x0) / 7, h_cell = (760 - y0) / 10;
            var wl = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };

            #region taking Screenshot
            Rectangle bounds = Screen.GetBounds(Point.Empty);
            using (Bitmap bitmap = new Bitmap(bounds.Width, bounds.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap))
                {
                    g.CopyFromScreen(Point.Empty, Point.Empty, new Size(bounds.Width, bounds.Height));
                }
                bitmap.Save("w.tiff", ImageFormat.Tiff);
            }
            Console.WriteLine("Scrn Capture Done");
            #endregion

            #region OCR
            var ocr = new List<PositionModel>();
            for (int i = 0; i < 10; i++)
            {
                var engine = new OcrEngine();
                engine.Image = ImageStream.FromFile(Directory.GetCurrentDirectory() + "/w.tiff");
                for (int j = 0; j < 7; j++)
                {
                    IRecognitionBlock block = RecognitionBlock.CreateTextBlock(x0 + j * w_cell + 8, y0 + i * h_cell + 8, 35, 35);
                    block.Whitelist = wl;
                    engine.Config.ClearRecognitionBlocks();
                    engine.Config.AddRecognitionBlock(block);
                    engine.Config.DetectTextRegions = false;
                    engine.Config.RemoveNonText = true;
                    if (engine.Process())
                        try
                        {
                            var n = int.Parse(engine.Text.ToString());
                            ocr.Add(new PositionModel { i = i, j = j, n = n });
                            Console.WriteLine(string.Format("Find {0} : in {1},{2}", n, i, j));
                        }
                        catch
                        {
                            //ocr.Add(new PositionModel { i = i, j = j, n = 100 });
                        }
                }
            }
            Console.WriteLine("Ocr Done");
            #endregion

            ocr.Sort((xx, yx) => xx.n.CompareTo(yx.n));
            Console.WriteLine("Ocr Sort Done");
            #region Mouse Click
            var mouse = new MouseHandler();
            Console.WriteLine("Clicking begins...");
            int prev = 0;
            foreach (var item in ocr)
            {
                if (item.n > 70) continue;
                if (item.n == prev) continue;
                mouse.SetCursorPosition(x0 + item.j * w_cell + 5, y0 + item.i * h_cell + 5);
                mouse.DoMouseClick();
                Console.WriteLine(string.Format("{0}:click at {1},{2}", item.n ,item.i, item.j));
                prev = item.n;
                Thread.Sleep(100);
            }
            #endregion

            Console.Read();
        }
    }
}

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class WriteStudents
{
   public static void main(String [] args)
   {
    if(args.length == 0)
    {
        System.out.println("Please enter a file to read");
        System.exit(1);
    }
    try
    {
        Scanner in = new Scanner(new File(args[0]));
        int numStudents = in.nextInt();
        System.out.println(numStudents);
        Student [] group = new Student[numStudents]; // Your program should fill in this array from a file. The filename will be on the command line.
        PrintWriter out = new PrintWriter(new File(args[1]));
        for(int i = 0;i < numStudents; i++)
        {
            String name = in.next();
            int mark = in.nextInt() + 1;
            group[i] = new Student(name, mark);
        }
        for(i = 0;i < numStudents;i++)
        {
            out.println(group[i])
        }
        out.close();
    }
    catch(FileNotFoundException e)
    {
        System.out.println("The file does not exist");
    }
    finally
    {
    }
   }
}

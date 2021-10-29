import Report.Top5costTasks;
import Report.Top5employees;
import Report.Top5longTasks;

import java.io.FileNotFoundException;
import java.text.ParseException;

public class Main {
    public static void main(String[] args) throws FileNotFoundException, ParseException {
        if (args.length < 2) {
            System.err.println("Provide parameters: [action] [object]");
            System.exit(1);
        }
        switch (args[0]) {
            case "import":
                System.out.println("Importing file " + args[1]);
                switch (args[1]) {
                    case "positions.csv":
                        ImportData.importPositions(args[1]);
                        break;
                    case "employees.csv":
                        ImportData.importEmployees(args[1]);
                        break;
                    case "timesheet.csv":
                        ImportData.importTimesheet(args[1]);
                        break;
                }
                break;
            case "get":
                System.out.println("Timesheet for employee " + args[1]);
                printTimesheet(args[1]);
                break;
            case "remove":
                System.out.println("Removing timesheet with id " + args[1]);
                removeTimesheet(Integer.valueOf(args[1]));
                break;
            case "report":
                System.out.println("Report " + args[1]);
                switch (args[1]) {
                    case "top5longTasks":
                        Top5longTasks.report();
                        break;
                    case "top5costTasks":
                        Top5costTasks.report();
                        break;
                    case "top5employees":
                        Top5employees.report();
                        break;
                }
                break;
        }
    }

    public static void printTimesheet(String employeeName) {

    }

    public static void removeTimesheet(Integer timesheetId) {

    }
}

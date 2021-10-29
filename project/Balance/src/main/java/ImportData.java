import dao.PositionDao;

import java.io.File;
import java.io.FileNotFoundException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class ImportData {
    private static final String DATA_PATH = "data";
    private static final SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.ENGLISH);

    public static void importPositions(String filename) throws FileNotFoundException {
        PositionDao positionDao = new PositionDao();
        Scanner scanner = new Scanner(new File(DATA_PATH + File.separatorChar + filename));
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            Scanner s = new Scanner(line).useDelimiter(",");
            String name = s.next();
            Integer rate = s.nextInt();
            // TODO save position
            System.out.println(line);
        }
        scanner.close();
    }

    public static void importEmployees(String filename) throws FileNotFoundException {
    }

    public static void importTimesheet(String filename) throws FileNotFoundException, ParseException {
    }
}

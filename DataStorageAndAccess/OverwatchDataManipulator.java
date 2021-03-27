import datacollection.DataCollector;
import datacollection.overwatch.OverwatchDataCollector;
import datacleaner.DataCleaner;
import datacleaner.overwatch.OverwatchDataCleaner;
import org.json.*;
import java.io.*;
import java.lang.*;
import java.util.*;

/**
* Class to manipulate the overwatch data.
* <p>
* This class is responsible for reading, parsing, cleaning, and inserting the
* overwatch data obtained from the data collection portion of the project.
*/
public class OverwatchDataManipulator
{
  public static String battletag;
  public static String gameMode;

  public static void main(String[] args)
  {
    try
    {
      loadAppSettings();
      DataCollector dc = new OverwatchDataCollector(battletag, gameMode);
      getJsonString(dc);
    }
    catch (FileNotFoundException fileNotFound)
    {
      System.out.println("Couldn't find appsettings.json in the DataStorageAndAccess folder...");
    }
    catch (IOException inputOutput)
    {
      System.out.println("A necessary file does not have read access...");
    }
  }

  public static void getJsonString(DataCollector dc)
  {
    String str = dc.getJsonDataString();
    DataCleaner dataCleaner = new OverwatchDataCleaner(str);
    JSONObject obj = dataCleaner.cleanData();
  }

  /**
  * Loads the application settings.
  */
  public static void loadAppSettings() throws FileNotFoundException, IOException
  {
    File appSettings = new File("appsettings.json");
    FileReader fr = new FileReader(appSettings);
    BufferedReader reader = new BufferedReader(fr);
    StringBuffer sb = new StringBuffer();
    String str;
    while((str = reader.readLine())!= null){
       sb.append(str);
    }

    JSONObject settings = new JSONObject(sb.toString());
    battletag = settings.getString("Username");
    gameMode = settings.getString("GameMode");
  }
}

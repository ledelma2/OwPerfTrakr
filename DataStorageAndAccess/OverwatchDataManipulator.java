import datacollection.DataCollector;
import datacollection.overwatch.OverwatchDataCollector;
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
    catch (Exception e)
    {
      System.out.println("An error occured");
    }
  }

  public static void getJsonString(DataCollector dc)
  {
    System.out.println(dc.getJsonDataString());
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

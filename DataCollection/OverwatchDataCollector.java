package datacollection.overwatch;

import java.io.*;
import java.lang.*;
import java.util.*;
import datacollection.DataCollector;

/**
* Class to specifically collect data from the overwatch web scraper.
*/
public class OverwatchDataCollector implements DataCollector
{
  private List<String> args;

  private final String COMMAND = "python3";
  private final String FILE_NAME_AND_PATH = "DataCollection/web_scraper/overwatch_data_collector.py";

  /**
  * Creates a new instance of the OverwatchDataCollector class given a battletag
  * and gamemode parameter.
  *
  * @param battletag  battletag of the user whose stats are desired. Entered in
  * the format of "[name]#[id]"
  * @param gameMode   game mode for the stats desired. "qp" for quick play,
  * "comp" for competitive
  */
  public OverwatchDataCollector(String battletag, String gameMode)
  {
    args = new ArrayList<String>();
    args.add(COMMAND);
    args.add(this.getScriptDirectory());
    args.add(battletag);
    args.add(gameMode);
  }

  /**
  Gets overwatch json data in string representation.
  */
  public String getJsonDataString()
  {
    try
    {
      ProcessBuilder pb = new ProcessBuilder(args);
      pb.redirectErrorStream(true);
      Process process = pb.start();
      InputStreamReader inputStreamReader = new InputStreamReader(process.getInputStream());
      BufferedReader reader = new BufferedReader(inputStreamReader);
      StringBuffer sb = new StringBuffer();
      String str;
      while((str = reader.readLine())!= null){
         sb.append(str);
      }

      return sb.toString();
    }
    catch (IOException ioe)
    {
      System.out.println("Error occured while running python script");
      System.out.println(ioe.toString());
    }

    return "[{}]";
  }

  /**
  * Gets the overwatch_data_collector.py directory by parsing the current working one.
  */
  private String getScriptDirectory()
  {
    String workingDir;
    String scriptDir;
    String[] workingDirArr;
    workingDir = System.getProperty("user.dir");
    workingDirArr = workingDir.split("/");
    workingDirArr[workingDirArr.length - 1] = FILE_NAME_AND_PATH;
    scriptDir = String.join("/", workingDirArr);
    return scriptDir;
  }
}

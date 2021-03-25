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
  private final String FILE_NAME_AND_PATH = "./DataCollection/web_scraper/overwatch_data_collector.py";

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
    args.add(FILE_NAME_AND_PATH);
    args.add(battletag);
    args.add(gameMode);
  }

  public String getJsonDataString()
  {
    ProcessBuilder pb = new ProcessBuilder(args);
    System.out.println("command: " + pb.command());
    return "Hello";
  }
}

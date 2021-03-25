import datacollection.DataCollector;
import datacollection.util.OverwatchDataCollector;

/**
* Class to manipulate the overwatch data.
* <p>
* This class is responsible for reading, parsing, cleaning, and inserting the
* overwatch data obtained from the data collection portion of the project.
*/
public class OverwatchDataManipulator
{
  public static void main(String[] args)
  {
    DataCollector dc = new OverwatchDataCollector();
    getJsonString(dc);
  }

  public static void getJsonString(DataCollector dc)
  {
    System.out.println(dc.getJsonStringData());
  }
}

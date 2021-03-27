package datacleaner.overwatch;

import org.json.*;
import java.io.*;
import java.lang.*;
import java.util.*;
import datacleaner.DataCleaner;

/**
* Class to specifically clean data from the OverwatchDataCollector.
*/
public class OverwatchDataCleaner implements DataCleaner
{
  private String uncleanedData;
  private JSONArray transformedData;
  private JSONObject cleanedData;

  /**
  * Creates a new instance of the OverwatchDataCleaner class.
  *
  * @param  data  String of the data to be cleaned
  */
  public OverwatchDataCleaner(String data)
  {
    this.uncleanedData = data;
  }

  /**
  * Cleans the data.
  *
  * @return json object of the cleaned data.
  */
  public JSONObject cleanData()
  {
    transformUncleanedData();
    try
    {
      writeToFile(transformedData.toString());
    }
    catch(IOException ioe)
    {
      System.out.println("File error");
    }
    cleanTransformedData();
    return cleanedData;
  }

  private void writeToFile(String str) throws IOException
  {
    BufferedWriter writer = new BufferedWriter(new FileWriter("data.json"));
    writer.write(str);

    writer.close();
  }

  /**
  * Transforms the uncleaned string data into a json object representation.
  */
  private void transformUncleanedData()
  {
    System.out.println(uncleanedData);
    transformedData = new JSONArray(uncleanedData);
  }

  /**
  * Cleans the transformed data.
  */
  private void cleanTransformedData()
  {
    cleanedData = new JSONObject();
  }
}

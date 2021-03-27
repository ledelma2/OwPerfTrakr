package datacleaning.overwatch;

import org.json.*;
import datacleaning.DataCleaner;

/**
* Class to specifically clean data from the OverwatchDataCollector.
*/
public class OverwatchDataCleaner implements DataCleaner
{
  private String uncleanedData;
  private JSONObject transformedData;
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
    transformedData = transformOverwatchData(uncleanedData);
    cleanedData = cleanOverwatchData(transformedData);
    return cleanedData;
  }

  /**
  * Transforms the string data into a json object representation.
  */
  private JSONObject transformOverwatchData(String data)
  {
    return new JSONObject();
  }

  /**
  * Cleans the transformed data.
  *
  * @param  data  json object of the transformed data to be cleaned
  * @return       json object of the cleaned, transformed data
  */
  private JSONObject cleanTransformedData(JSONObject data)
  {
    return new JSONObject();
  }
}

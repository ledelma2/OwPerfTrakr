package datacleaning;

import org.json.*;

/**
* Interface for all data cleaner classes.
*/
public interface DataCleaner
{
  /**
  * Function to transform the string data to a json mapping.
  *
  * @param  data  string representation of the data to be transformed
  * @return       the json object representation of the data
  */
  JSONObject transformData(String data);

  /**
  * Function to clean the json object data.
  *
  * @param  data  json object representation of the data to be cleaned
  * @return       json object with the cleaned data.
  */
  JSONObject cleanData(JSONObject data);
}

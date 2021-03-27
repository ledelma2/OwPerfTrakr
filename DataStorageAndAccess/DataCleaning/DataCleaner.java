package datacleaning;

import org.json.*;

/**
* Interface for all data cleaner classes.
*/
public interface DataCleaner
{
  /**
  * Function to clean the json object data.
  *
  * @param  data  json object representation of the data to be cleaned
  * @return       json object with the cleaned data.
  */
  JSONObject cleanData(JSONObject data);
}

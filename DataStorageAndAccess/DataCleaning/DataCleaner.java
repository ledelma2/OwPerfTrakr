package datacleaner;

import org.json.*;

/**
* Interface for all data cleaner classes.
*/
public interface DataCleaner
{
  /**
  * Function to clean the json object data.
  *
  * @return json object with the cleaned data
  */
  JSONObject cleanData();
}

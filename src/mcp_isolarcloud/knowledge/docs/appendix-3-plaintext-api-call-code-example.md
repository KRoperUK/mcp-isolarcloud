# Appendix 3: Plaintext API Call Code Example

# **Appendix 3: Plaintext API Call Code Example**

```
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
public class UserTest{
    Public static void main(String[] args)
    {
        CloseableHttpClienthttpclient = HttpClients.createDefault();
        String url = "https://API domain name which is provided by iSolarCloud/xxx/xxx";
        HttpPosthttppost = new HttpPost(url);
        try
        {
            // Header
            httppost.addHeader("sys_code", "901");
            HashMap<String, Object>req = new HashMap<String, Object>();
            // Public parameter
            req.put("appkey", "authorized appkey"); 
req.put("token", "token returned by login API");  
            // Service
            req.put("service", "service name");
            req.put("parameter 1", "parameter value");
            String jsonStr = com.alibaba.fastjson.JSON.toJSONString(req);
            System.out.println("send json-<" + jsonStr.toString());
            StringEntitystrEntity = new StringEntity(jsonStr);
            strEntity.setContentType("application/json");
            httppost.setEntity(strEntity);
            CloseableHttpResponse response = httpclient.execute(httppost);
            try
            {
                HttpEntity entity = response.getEntity();
                InputStreaminputStream = entity.getContent();
                InputStreamReaderinputStreamReader = new InputStreamReader(
                        inputStream, "UTF-8");
                BufferedReader reader = new BufferedReader(inputStreamReader); 
                StringBuilder result = new StringBuilder();
                String s;
                while (((s = reader.readLine()) != null))
                {
                    result.append(s);
                }
                reader.close();
                System.out.println("receive json-<" + result.toString());
            }
            finally
            {
                response.close();
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                httpclient.close();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        }
    }
}
```

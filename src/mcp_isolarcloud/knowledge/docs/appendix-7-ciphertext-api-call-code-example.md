# Appendix 7: Ciphertext API Call Code Example

# **Appendix 7: API Encrypted Call Sample Code**

```
1. Header encapsulation
String publicKey = "xxxxx" ;// publicKey assigned by iSolarCloud
// publicEncrypt methods in Appendix 3
String x-random-secret-key = publicEncrypt("A123456zA123456z", publicKey) ;//x-random-secret-key could be different in different requests
String x-access-key = "i71w7tskmns5********i3b8zqncvay3" ;//accessKey assigned by iSolarCloud

2. Body encapsulation
// Use login API as an example，Besides request body parameter  in 2.1, api_key_param is also in need：
//nonce is a 32 bit random string of letters and numbers, it should be different in every call;
//timestamp is UNIX time stamp in milliseconds，if error code E913 is returned,
// Use GET method to call  https://API domain name which is provided by iSolarCloud/timestamp
String requestBody =
{
    "api_key_param": {
        "nonce": "cb360459bd624c6ab15308c4b6847856",
        "timestamp": "1616725497384"
    },
    "appkey": "***********",
    "login_type": "1",
    "user_account": "******",
    "user_password": "******"
};	
                                                                                                                              
3. Request call
CloseableHttpClient httpclient = HttpClients.createDefault();
String url = "https://API domain name which is provided by iSolarCloud/v1/userService/login";
HttpPost httppost = new HttpPost(url);
// Request header
httppost.addHeader("x-random-secret-key", x-random-secret-key);
httppost.addHeader("x-access-key", x-access-key);
...... //Set other request header
// Encryption methods in Appendix 4
String encryptedRequestBody = encrypt(requestBody, "A123456zA123456z") ; 
StringEntity strEntity = new StringEntity(encryptedRequestBody);
strEntity.setContentType("application/json");
httppost.setEntity(strEntity);
CloseableHttpResponse response = httpclient.execute(httppost);
HttpEntity entity = response.getEntity();
InputStream inputStream = entity.getContent();
InputStreamReader inputStreamReader = new InputStreamReader(inputStream, "UTF-8");
BufferedReader reader = new BufferedReader(inputStreamReader);
StringBuilder responseBody = new StringBuilder();
String s = null;
while (((s = reader.readLine()) != null))
{
    responseBody.append(s);
}
reader.close();
// Decryption methods in Appendix 5
String decryptedResponseBody = decrypt(responseBody, "A123456zA123456z") ;
```

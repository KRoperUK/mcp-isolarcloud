# Appendix 2: API Error Code Definitions

# **Appendix 2: API Error Code Definitions**

| **Error Code Name** | **Type** | **Error Code** |
| --- | --- | --- |
| success | Call successful | 1 |
| error | Internal service exception | -1 |
| er\_unknown\_exception | Unknown exception | 000 |
| er\_missing\_parameter:appkey | appkey cannot be empty | 001 |
| er\_missing\_parameter:token | token cannot be empty | 002 |
| er\_missing\_parameter:sys\_code | sys\_code cannot be empty | 003 |
| er\_invalid\_appkey | Invalid appkey | E00000 |
| er\_api\_service\_has\_expired | API service expired | E00001 |
| er\_parameter\_decrypt\_error | Parameter decryption exception | E00002 |
| er\_token\_login\_invalid | The token is invalid or has expired | E00003 |
| er\_month\_call\_api\_times\_upper\_limit | Max API calls reached | E998 |
| er\_hour\_call\_api\_times\_upper\_limit | Max API calls reached | E999 |
| er\_missing\_parameter | Required parameter missing | 009 |
| er\_parameter\_value\_invalid | Parameter value invalid | 010 |
| er\_sql\_exception | SQL exception | 011 |
| Unauthorized access | Access has not been authorized | E900 |
| Call too frequently | The call frequency is too high | E901 |
| Abnormal network environment | IP address change frequency is too high | E903 |
| Request is not encrypted | The request has not been encrypted | E902 |
| Missing parameter in request header: x-random-secret-key | The x-random-secret-key is missing from the request header | E904 |
| AES decryption exception | There was an issue with AES decryption | E905 |
| RSA decryption exception | There was an issue with RSA decryption | E906 |
| AES random secret key length must be 16 | The length of the AES random secret key must be 16 | E907 |
| Missing key parameter: api\_key\_param | The api\_key\_param is missing | E908 |
| Invalid parameter format: nonce [32-bit string of numbers and letters] | The parameter format is invalid: nonce [32-bit string of numbers and letters] | E909 |
| Repeated request | The request nonce must be regenerated for repeated requests | E910 |
| Missing parameter in request header: x-access-key | The x-access-key is missing from the request header | E911 |
| Illegal x-access-key | The x-access-key is invalid | E912 |
| Expired request | The request has expired, the time difference between the timestamp (UTC+0 UNIX) in the request and the server time is too high | E913 |
| Mismatched appkey and x-access-key | The appkey and access-key do not match | E914 |
| Login too frequently | Too many repeated login attempts | E916 |
| Permit Denied By White IP Address | The access request is rejected because the client IP address is not in the allowed IP whitelist. | E918 |
| Permit Denied By White List User | Access is denied as the current user account is not included in the user whitelist. | E919 |
| system not found | The target system corresponding to the request cannot be found or does not exist. | E994 |
| request body too large | The size of the request body exceeds the server's maximum allowed limit. | E995 |
| api not found | The requested API interface address does not exist or cannot be matched. | E996 |
| transform business response data occur error | An error occurred while parsing and converting the business response data returned by the interface. | E997 |

# Getting Started

# 1 Usage Specifications of API

APIs contained in this document support unencrypted call and encrypted call; encrypted call methods are presented in apendix 7.

## 1.1 Access Steps

Users can acquire powerstation information and device information with Sungrow Developer Portal Open API. In the first step。

users call **/eco/v1/auth** API to identify authentication with user account and password which are provided by iEnergycharge and acquire authorized token. Then, users can call other APIs witin token's term of validity (24 hours).

Note: Within the token's term of validity, its term of validity will be reset to 24 hours after every call. Therefore, there is no need for the users to acquire new token every time.

## 1.2 Error Code Definition

More details in [Appendix 2：API Error Code Definition](#/document/md?link_index=324)

## 1.3 Constraint Description

（1） User accounts, appkey and related information used in this document call APIs under the rules of

《Sungrow Developer Portal Open API-Authorization Instructions》and get corresponding response;

（2）Http requests are sent in POST mode

（3）Appkey with authorization is a must when users call platform service, parameter in request body is named appkey;

（4）Every API call need a token to verify identity, corresponding request body parameter is token，[**/eco/v1/auth** API is an exception]；

（5）parameters in request header：

| **Name** | **Type** | **Length** | **Description** | **Required?** |
| --- | --- | --- | --- | --- |
| Content-Type | String | 32 | Input：application/json;charset=UTF-8 | Yes |
| sys\_code | String | 11 | System code：third party call use 901 | Yes |
| x-access-key | String | 32 | Access\_key assigned by iSolarCloud | Yes |
| x-random-secret-key | String | 16 | It's secret key of this request and its plaintext length is 16 bit. It should be transmitted after RSA encryption.  Output parameters use this plaintext key to process AES decryption.  **This parameter is needed when API call is encrypted call.** [How to acquire](https://developer-api.isolarcloud.com/#/document/md?link_index=329) x-random-secret-key | No |

（6）Parameters in this table are needed in request body of all APIs. These parameters will not be listed in each API's definition.

| **Name** | **Type** | **Length** | **Description** | **Required?** |
| --- | --- | --- | --- | --- |
| appkey | String | 32 | Authorization code，required (APi assign appkey to client system)。 | Yes |
| token | String | 40 | Token (returned by API after success login) | Yes |
| lang | String | 6 | Language（default as chinese）：   - Simplified Chinese：\_zh\_CN - English：\_en\_US - Japanese：\_ja\_JP - Spanish：\_es\_ES - German：\_de\_DE - Brazilian Portuguese：\_pt\_BR - Portuguese：\_pt\_BR - French：\_fr\_FR - Italian：\_it\_IT - Korean：\_ko\_KR - Dutch：\_nl\_NL - Polish：\_pl\_PL - Vietnamese：\_vi\_VN - Traditional Chinese：\_zh\_TW | No |
| api\_key\_param | Map |  | Other public parameter | No |
| timestamp | String |  | Greenwich UNIX timestamp（millisecond） | No |
| nonce | String | 32 | 32 bit random string of numbers and letters | No |

（7）Parameters in this table are contained in response body of all APIs. These parameters will not be listed in each API's definition.

| **Name** | **Type** | **Length** | **Description** |
| --- | --- | --- | --- |
| req\_serial\_num | String | 32 | Request serial number |
| result\_code | String | 11 | Error code |
| result\_msg | String | 100 | Message |
| result\_data | Object |  | Result data：Supported data structure：String，Map，List , etc .  specific data format is decided by each API. Each API's output parameters are contained in result\_data. |

(8) API domain name: Please select the corresponding API domain name for each site of iSolarCloud when calling API interfaces:

- China: https://openapi.isolarcloud.com/
- International: https://openapi.isolarcloud.com.hk/
- Europe: https://openapi.isolarcloud.eu/
- Australia: https://openapi.isolarcloud.au/

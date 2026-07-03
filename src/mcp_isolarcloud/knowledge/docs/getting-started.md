# Getting Started

# Getting Started

The Developer Portal provides developers with an efficient and convenient way to build and integrate a wide range of functions and services.

All you need to do is choose the API endpoints that match your actual needs. This documentation will provide you with information about the API and how to integrate it.

## 1. API Usage Guide

The APIs outlined in this article support both plaintext and ciphertext calls. The method and instructions for ciphertext calls are explained in the appendix. For details on encryption and decryption methods, refer to [Appendix 7: Ciphertext API Call Code Example](#/document/md?link_index=219)

### 1.1 Call Steps

The caller can obtain the required plant and device information from Developer Portal. The caller first needs to obtain the authorization of the owner of the iSolarCloud plant.

and then get the token through the authorization code, and you can obtain the authorized plant and device information through the token.

### 1.2 Error Code Definitions

 Refer to **[Appendix 2: API Error Code Definitions](#/document/md?link_index=224)**

### 1.3 Constraint Description

 (1) All user accounts, appkeys, and other relevant information used in all endpoints in this article will be called and have relevant data obtained in strict accordance with the provisions of the Sungrow iSolarCloud Platform Endpoint Open API Authorization Instructions;

(2) All http requests are made in POST mode;

(3) To call all platform services, pass in an appkey authorized by the platform. The request body parameter name is: appkey;

(4) Each API call requires a access-token for identity verification. The request body parameter name is: Authorization, The format is:"Bearer " + access\_token；

(5) Relevant parameters in the request header are as follows:

| **Parameter name** | **Type** | **Length** | **Description** | **Required** |
| --- | --- | --- | --- | --- |
| Content-Type | String | 32 | Pass: application/json;charset=UTF-8 | Y |
| x-access-key | String | 32 | access\_key assigned by iSolarCloud | Y |
| x-random-secret-key | String | 16 | The key for this request has a plaintext length of 16 bits and can only be passed after RSA encryption. The output parameter uses a plaintext key for AES decryption. **[How to get an](#/document/md?link_index=219)** x-random-secret-key **when passing an encrypted request** | N |
| Authorization | String | 50 | Token，example：Bearer {access\_token} | 是 |

(6) Pass the following public parameters in the request body (these parameters will not be outlined individually in each endpoint definition).

| **Parameter name** | **Type** | **Length** | **Description** | **Required** |
| --- | --- | --- | --- | --- |
| appkey | String | 32 | Auth code, required (the appkey assigned by the endpoint to the client system) | Y |
| lang | String | 6 | Language (default is Simplified Chinese):   - Simplified Chinese: \_zh\_CN - English: \_en\_US - Japanese: \_ja\_JP - Spanish: \_es\_ES - German: \_de\_DE - Brazilian Portuguese:\_pt\_BR - Portuguese:\_pt\_BR - French: \_fr\_FR - Italian: \_it\_IT - Korean: \_ko\_KR - Dutch: \_nl\_NL - Polish: \_pl\_PL - Vietnamese:\_vi\_VN - Traditional Chinese: \_zh\_TW | N |
| api\_key\_param | Map |  | Other public parameter | No |
| timestamp | String |  | Greenwich UNIX timestamp（millisecond） | No |
| nonce | String | 32 | 32 bit random string of numbers and letters | No |

(7) The following public output parameters will not be outlined individually in each API definition.

| **Parameter name** | **Type** | **Length** | **Description** |
| --- | --- | --- | --- |
| req\_serial\_num | String | 32 | Request sequence number |
| result\_code | String | 11 | Error code |
| result\_msg | String | 100 | Prompt message |
| result\_data | Object |  | Returned data: Supported types: string, map and list.  For specific data types, refer to the corresponding API output parameter definition in this article.  The output data outlined in this article can be found under result\_data. |

(8) API domain name: Please select the corresponding API domain name for each site of iSolarCloud when calling API interfaces:

- China: https://gateway.isolarcloud.com/
- International: https://gateway.isolarcloud.com.hk/
- Europe: https://gateway.isolarcloud.eu/
- Australia: https://augateway.isolarcloud.com/

## 2. Appendix

- [Appendix 1: Device Type Dictionary Definitions](#/document/md?link_index=225)
- [Appendix 2: API Error Code Definitions](#/document/md?link_index=224)
- [Appendix 3: Plaintext API Call Code Example](#/document/md?link_index=223)
- [Appendix 4: RSA Encryption Code Example](#/document/md?link_index=222)
- [Appendix 5: AES Encryption Code Example](#/document/md?link_index=221)
- [Appendix 6: AES Decryption Code Example](#/document/md?link_index=220)
- [Appendix 7: Ciphertext API Call Code Example](#/document/md?link_index=219)
- [Appendix 8: API Call Help Instructions](#/document/md?link_index=229)
- [Appendix 9: Error Code Enumeration](#/document/md?link_index=230)
- [Appendix 10: Control Parameter Definitions](#/document/md?link_index=257)

## 3. Common Measuring Point Enumeration

- [Common inverter measuring points](#/document/md?link_index=245 "Common inverter measuring points")
- [Common plant measuring points](#/document/md?link_index=242 " Common plant measuring points")
- [Common combiner box measuring points](#/document/md?link_index=241 "Common combiner box measuring points")
- [Common environment monitoring device measuring points](#/document/md?link_index=243)
- [Common meter measuring points](#/document/md?link_index=240)
- [Common communications device measuring points](#/document/md?link_index=234)
- [Common energy storage inverter measuring points](#/document/md?link_index=236)
- [Common communications module measuring points](#/document/md?link_index=235)
- [Common battery measuring points](#/document/md?link_index=232)
- [Common EMS device measuring points](#/document/md?link_index=233)
- [Common LC device measuring points](#/document/md?link_index=246)
- [Common PCS device measuring points](#/document/md?link_index=244)
- [Common CMU device measuring points](#/document/md?link_index=237)
- [Common BSC device measuring points](#/document/md?link_index=239)
- [Common charging station measuring points](#/document/md?link_index=239)
- [Common Measuring Points of Micro-inverters](#/document/md?link_index=238)

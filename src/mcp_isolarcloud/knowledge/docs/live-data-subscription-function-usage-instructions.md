# Live Data Subscription Function Usage Instructions

# Live Data Subscription Function Usage Instructions

Under normal circumstances, the measurement point data of the inverter is reported every 5 minutes. In some scenarios, we may want the data reporting frequency to be faster.

The live data subscription function provides the ability to control the frequency at which the inverter reports measurement point data.

# 1. Prerequisites

  (1) Application for mqtt account and password

  (2) The inverter supports the live data subscription function

# 2. Account Application

The live data function requires you to submit an application. After that, we will allocate an mqtt username and password for you before you can invoke it.

## 2.1 Application Process

(1) Prepare application materials

- Please provide a detailed description of your requirements for specific functions in the open API project, including but not limited to the business scenarios where you plan to use these functions and the expected usage frequency.
- Please provide appkey or application name which you used to apply for API in the portal.

(2) Send application materials to the designated email

Please send your prepared application materials to developer-api@sungrowpower.com.

+ Please note "Open API Live Data Application - [Your Name/Enterprise Name]" in the email subject to help us quickly identify your application.

(3) Wait for review and feedback + We will review your application within 10 working days after receiving it. During the review process, if we need any additional information from you, we will contact you via the email you provided. + If your application is approved, we will send the allocated username and password to your application email.

## 2.2 Notes

(1) Please ensure that the application materials you provide are true, accurate, and complete. This will help us process your application quickly.

(2) Do not attempt to call the functions that require application permission before receiving the username and password allocated by us to avoid unnecessary errors.

(3) If you have any questions or encounter any problems during the application process, please contact us via email.

## 3. Usage Steps

### 3.1 Retrieve the Corresponding mqtt Information Based on the appkey

Call the interface `/openapi/platform/datasubscribe/getConfig` to obtain the mqtt account information. If you have already applied for and been allocated an mqtt account, this interface will return the relevant mqtt information, including: mqtt connection address, account, password, supported mqtt protocol types for this appkey, and mqtt public key. For interface details, please refer to the interface documentation: [Retrieve the corresponding mqtt information based on the appkey](#/document/api?link_index=353)

### **3.2**Enable Live Data Upload

Call the interface `/openapi/platform/datasubscribe/start` to send instructions to the inverter and enable the live data upload function. This interface will return the topic for each inverter's live data reporting. For interface details, please refer to the interface documentation: [Enable Live Data Upload](#/document/api?link_index=152)

### **3.3**Disable Live Data Upload

Call the interface `/openapi/platform/datasubscribe/stop` to send instructions to the inverter and disable live data upload. For interface details, please refer to the interface documentation: [Disable live data upload](#/document/api?link_index=153)

### **3.4**Obtain Live Data Reported by the Inverter

(1) Real-time consumption of live data

![](https://isc-file.oss-cn-hangzhou.aliyuncs.com/openapi/liveData/mqtt_consume.png)

Use an mqtt connection tool, such as MQTTX, to log in to your mqtt account, connect to the mqtt service, and subscribe to the topic returned by the interface in step 3.2. **When connecting via mqtt, the following information needs to be filled in:**

- Connection name: You can enter any characters.
- Client ID: It must be globally unique.
- Host: This includes the mqtt protocol type and the mqtt host, corresponding to the protocol type and host part of the mqtt\_url\_list field returned by the interface in step 3.1.
- Port: The port number of the mqtt service, corresponding to the port number part of the mqtt\_url\_list returned by the interface in step 3.1.
- Path: The mqtt access path, corresponding to the path part of the mqtt\_url\_list returned by the interface in step 3.1. Only required when the used mqtt protocol is ws or wss, and defaults to /mqtt.
- Username: The mqtt account, corresponding to the mqtt\_username field returned by the interface in step 3.1.
- Password: The mqtt password, corresponding to the mqtt\_password field returned by the interface in step 3.1.

![](https://isc-file.oss-cn-hangzhou.aliyuncs.com/openapi/liveData/mqtt_config.png)

```
Note:
- The original message consumed by mqtt is encrypted and can be decrypted using the RSA public key obtained in step 3.1. Use mqtt_rsa_public_key to decrypt the data.
- If real-time viewing of the data reported by the device is not required, this operation and step 3.1 can be skipped.
```

**Example code for decrypting using RSA public key：**

```
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.io.IOUtils;

import javax.crypto.Cipher;
import java.io.ByteArrayOutputStream;
import java.security.KeyFactory;
import java.security.interfaces.RSAPublicKey;
import java.security.spec.X509EncodedKeySpec;

/**
 * RSA Public key decryption
 **/
public static String publicDecrypt(String data, String publicKey){
    String result = null;
    try{
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        X509EncodedKeySpec x509KeySpec = new X509EncodedKeySpec(Base64.decodeBase64(publicKey));
        RSAPublicKey key = (RSAPublicKey) keyFactory.generatePublic(x509KeySpec);
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.DECRYPT_MODE, key);
        result = new String(rsaSplitCodec(cipher, Cipher.DECRYPT_MODE, Base64.decodeBase64(data), key.getModulus().bitLength()), "UTF-8");
    }catch(Exception e){
        //Deal Exception
    }
    return result;
}

private static byte[] rsaSplitCodec(Cipher cipher, int opmode, byte[] datas, int keySize){
    int maxBlock;
    if(opmode == Cipher.DECRYPT_MODE){
        maxBlock = keySize / 8;
    }else{
        maxBlock = keySize / 8 - 11;
    }
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    int offSet = 0;
    byte[] buff;
    int i = 0;
    byte[] resultDatas = null ;
    try{
        while(datas.length > offSet){
            if(datas.length-offSet > maxBlock){
                buff = cipher.doFinal(datas, offSet, maxBlock);
            }else{
                buff = cipher.doFinal(datas, offSet, datas.length-offSet);
            }
            out.write(buff, 0, buff.length);
            i++;
            offSet = i * maxBlock;
        }
        resultDatas = out.toByteArray();
    } catch(Exception e){
        //Deal Exception
    } finally {
        IOUtils.closeQuietly(out);
    }
    return resultDatas;
}
```

(2) Get History Data

- Call the interface `/openapi/platform/datasubscribe/getHisData` to query the historical data reported by the device. For interface details, please refer to the interface documentation: [Get History Data](#/document/api?link_index=354)

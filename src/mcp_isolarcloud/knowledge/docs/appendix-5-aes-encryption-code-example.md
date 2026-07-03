# Appendix 5: AES Encryption Code Example

# **Appendix 5: AES Encryption Code Example**

```
/**
*AES encryption rule：
*Encryption mode：ECB
*Padding method：pkcs5padding
*data block：128 bit
*Offset：no offset
*Output：hex
*Character set：utf8 encoding
**/
public String encrypt(String content, String password)  throws Exception {
    try {
        byte[] result = null;
        byte[] passwordBytes = getSecretKey(password) ;
        SecretKeySpec skeySpec = new SecretKeySpec(passwordBytes, "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, skeySpec);
        result = cipher.doFinal(content.getBytes("UTF-8"));
        return parseByte2HexStr(result) ;
    } catch (Exception e) {
        //Deal Exception
    }
}
                                                                                                                                        
public byte[] getSecretKey(String key) throws Exception{
    final byte paddingChar = '0';
    byte[] realKey = new byte[16];
    byte[] byteKey = key.getBytes("UTF-8");
    for (int i =0;i<realKey.length;i++){
        if (i<byteKey.length){
            realKey[i] = byteKey[i];
        }else{
            realKey[i] = paddingChar;
        }
    }
    return realKey;
}

public String parseByte2HexStr(byte buf[]) {
    StringBuffer sb = new StringBuffer();
    for (int i = 0; i < buf.length; i++) {
        String hex = Integer.toHexString(buf[i] & 0xFF);
        if (hex.length() == 1) {
            hex = '0' + hex;
        }
        sb.append(hex.toUpperCase());
    }
    return sb.toString();
}
```

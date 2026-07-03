# Appendix 6: AES Decryption Code Example

# **Appendix 6: AES Decryption Code Example**

```
/**
*Decryption mode：ECB
*Padding method：pkcs5padding
*Data block：128 bit
*Offset：no offset
*Output：hex
*Character set：utf8 encoding;
**/
                                                                                                                                        
public  String decrypt(String content, String password) throws Exception {                              
    try {
        byte[] original = null;
        byte[] decryptFrom = parseHexStr2Byte(content);
        byte[] passwordBytes = getSecretKey(password) ;
        SecretKeySpec skeySpec = new SecretKeySpec(passwordBytes, "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, skeySpec);
        original = cipher.doFinal(decryptFrom);
        return new String(original);
    } catch (Exception e) {
        //Deal Exception
    }
}

public byte[] parseHexStr2Byte(String hexStr) {
    if (hexStr.length() < 1) {
        return null;
    }
    byte[] result = new byte[hexStr.length() / 2];
    for (int i = 0; i < hexStr.length() / 2; i++) {
        int high = Integer.parseInt(hexStr.substring(i * 2, i * 2 + 1), 16);
        int low = Integer.parseInt(hexStr.substring(i * 2 + 1, i * 2 + 2),
                16);
        result[i] = (byte) (high * 16 + low);
    }
    return result;
}
```

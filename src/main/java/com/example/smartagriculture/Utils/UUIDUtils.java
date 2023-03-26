package com.example.smartagriculture.Utils;

import java.util.UUID;

// 界面上传图片时考虑到可能会有用户的图片名称一致，使用UUID来对图片名称进行重新生成
public class UUIDUtils {
    public static String getUUID(){
        return UUID.randomUUID().toString().replace("-", "");
    }
}
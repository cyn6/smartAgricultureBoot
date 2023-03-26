package com.example.smartagriculture.Controller;

import com.example.smartagriculture.Utils.UUIDUtils;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.io.IOException;

@RestController
public class UploadController {
    // 这里的ACCESS_PATH返回的是为前端配置的资源路径,也是python程序的图片路径
//    private static final String ACCESS_PATH = "http://10.184.17.72:9099/upload/"; //tomcat服务器也可以
    private static final String ACCESS_PATH = "http://10.184.17.72:8088/upload/"; //用nginx访问图片

    @RequestMapping(value = "/upload", method = RequestMethod.POST)
    public String upload(MultipartFile image, HttpServletRequest request) throws IOException {
        System.out.println("================上传图片================");
        System.out.println("image size: " + image.getSize());
        System.out.println("image type: " + image.getContentType());
        System.out.println("image name: " + image.getOriginalFilename());
        System.out.println(System.getProperty("user.dir"));
        // TODO: 这里修改上传图片路径相关
        // String path = request.getServletContext().getRealPath("/upload/");  // 临时文件夹
        String path = "/data/cyn/app/smartAgricultureBoot/upload/"; // 固定目录
        String newImageName = UUIDUtils.getUUID() + image.getOriginalFilename().substring(image.getOriginalFilename().lastIndexOf("."));
        System.out.println("image path: " + ACCESS_PATH + newImageName);
        saveImage(image, path, newImageName);
        return ACCESS_PATH + newImageName;
    }
    public void saveImage(MultipartFile image, String path, String newImageName) throws IOException {
        File dir = new File(path);
        if (!dir.exists()) {
            dir.mkdir();
        }
        File file = new File(path + newImageName);
        image.transferTo(file);
    }
}
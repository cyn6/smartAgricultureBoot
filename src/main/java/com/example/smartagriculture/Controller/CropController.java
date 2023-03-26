package com.example.smartagriculture.Controller;

import com.example.smartagriculture.Entity.Crop;
import com.example.smartagriculture.Service.CropService;
import com.example.smartagriculture.Utils.UUIDUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.io.IOException;

@RestController
public class CropController {
    @Autowired
    private CropService cropService;

    @RequestMapping(value = "/crop", method = RequestMethod.GET)
    public String detect(String imagePath, String detectType) {
        System.out.println("image path: " + imagePath);
        System.out.println("detect type: " + detectType);
        String result = cropService.detect(imagePath, detectType);
        return result;
    }

}

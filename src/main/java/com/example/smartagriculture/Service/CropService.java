package com.example.smartagriculture.Service;

import com.example.smartagriculture.Entity.Crop;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.util.ArrayList;

@Service
public class CropService {
    // TODO: 这里修改python相关参数
    public String pythonInterpreter = "/home/cyn/anaconda3/envs/PlantDiseases/bin/python";
    public String filePath = "/data/cyn/app/smartAgricultureBoot/plantAPI/main.py";
    public String detect(String imageUrl, String detectType) {
        Crop cropResult = new Crop();
        String result = "";
        String pythonScript = this.pythonInterpreter +" "+ this.filePath + " --type " + detectType + " --img_url " + imageUrl;
        try {
            Process process = Runtime.getRuntime().exec(pythonScript);
            InputStreamReader ir = new InputStreamReader(process.getInputStream());
            LineNumberReader input = new LineNumberReader(ir);
            result = input.readLine();
//            switch (detectType) {
//                case "disease":
//                    cropResult.setDisease(result);
//                    break;
//                case "insect":
//                    cropResult.setInsect(result);
//                    break;
//                case "nutrition":
//                    cropResult.setNutrition(result);
//                    break;
//                case "status":
//                    cropResult.setStatus(result);
//                    break;
//            }
            System.out.println(detectType + " result: " + result);
            input.close();
            ir.close();
            int re = process.waitFor();
            System.out.println("python script: \n" + pythonScript);
        } catch (IOException | InterruptedException e) {
            System.out.println("Error when running Python Script: " + e.getMessage());
        }
        return result;
    }
}

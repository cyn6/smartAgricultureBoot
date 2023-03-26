package com.example.smartagriculture.Config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        //其中image表示访问的前缀。"file:F:/img/"是文件真实的存储路径
        // TODO: 这里设置静态资源（上传的图片）映射路径
        // 用nginx就不用这个了
//        registry.addResourceHandler("/upload/**")
//                .addResourceLocations("file:/data/cyn/app/SmartAgriculture/smartagriculture/upload/");
    }
}

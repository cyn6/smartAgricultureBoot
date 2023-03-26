package com.example.smartagriculture.Config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

//标注这个类是一个配置类
@Configuration
//实现 WebMvcConfigurer 接口
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")  //设置允许跨域访问的路径
                .allowedOriginPatterns("*")  //设置允许跨域访问的源
                .allowedMethods("POST", "GET", "PUT", "OPTIONS", "DELETE")  //允许跨域请求的方法
                .maxAge(168000)  //预检间隔时间
                .allowedHeaders("*")  //允许头部设置
                .allowCredentials(true);  //是否发送 cookie
    }
}

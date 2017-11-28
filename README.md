# ApkPerforTools（天月平台）
android 性能测试工具

# 实现技术：
python + bottle + jquery + nginx

# 功能：
### 1，测试apk内存
### 2，测试apk cpu
### 3，测试apk流量
### 4，测试apk频率
### 5，截图并验证UI

# 测试流程：
上传apk（自动安装解析）——> 选择测试apk ——> 测试 ——> 测试结果图表

# 注：
### 1，目前还未添加队列功能
### 2，bottle默认为单进程服务器，故启了多个端口；需要与nginx配合使用，解决ajax请求跨域问题。
### 3，图表使用的是百度echarts

# Nginx配置方法说明：
 ##         location /api/meminfo {
 ##            proxy_pass   http://127.0.0.1:8082;
 ##         }
 
 ##         location /api/cpuinfo {
 ##              proxy_pass   http://127.0.0.1:8083; 

# 相关功能图

功能还在完善，腾讯优测是我的目标，谢谢关注^_^

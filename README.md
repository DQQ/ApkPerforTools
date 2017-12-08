### ApkPerforTools（天月平台）
android 性能测试工具

### 实现技术：
python + bottle + jquery + nginx

### 功能：
###### 1，测试apk内存
###### 2，测试apk cpu
###### 3，测试apk流量
###### 4，测试apk频率
###### 5，截图并验证UI

### 测试流程：
###### 上传apk（自动解析apk信息）——>任务列表（选择测试apk） ——> 测试（浅度或深度遍历应用，收集应用性能数据、按时间截图） ——> 测试结果集及数据图表详情

### 注：
###### 1，目前还未添加队列功能
###### 2，bottle默认为单进程服务器，故启了多个端口；需要与nginx配合使用，解决ajax请求跨域问题。
###### 3，图表使用的是百度echarts

### Nginx配置方法说明：
1，请求转发：
 ######         location /api/meminfo {
 ######            proxy_pass   http://127.0.0.1:8082;
 ######         }
 
 ######         location /api/cpuinfo {
 ######              proxy_pass   http://127.0.0.1:8083; 
 2，配置解决上传文件过大问题：
    在http{}段中加入 client_max_body_size 20m; 20m为允许最大上传的大小。
### 相关功能图
https://github.com/DQQ/ApkPerforTools/blob/master/result/IMG68.jpeg

功能还在完善，腾讯优测是我的目标，谢谢关注^_^

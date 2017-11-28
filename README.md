# ApkPerforTools
ApkPerforTools
android 性能测试工具

实现技术：
python + bottle + jquery + nginx

测试流程：
上传apk（自动安装解析）——> 选择测试apk ——> 测试 ——> 测试结果图表

注：
1，目前还未添加队列功能
2，bottle默认为单进程服务器，故启了多个端口；需要与nginx配合使用，解决ajax请求跨域问题。
3，图表使用的是百度echarts

Nginx配置方法说明：
 60         location /api/meminfo {
 61            #rewrite ^/api/meminfo/(.*)$ /$1 break;
 62            #include uwsgi_params;
 63            #uwsgi_pass 127.0.0.1:8082;
 64            proxy_pass   http://127.0.0.1:8082;
 65         }
 66 
 67         location /api/cpuinfo {
 68             # rewrite ^/api/cpuinfo/(.*)$ /$1 break;
 69              #include uwsgi_params;
 70              #uwsgi_pass 127.0.0.1:8082;
 71              proxy_pass   http://127.0.0.1:8083;
 72 


功能还在完善，腾讯优测是我的目标，谢谢关注^_^

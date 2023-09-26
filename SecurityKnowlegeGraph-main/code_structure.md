### 项目功能目录

* attack    根目录
  * attack		项目配置目录
  * webapp      项目主体目录
    * log_conf                日志上报
    * neo4j_conf            neo4j数据库交互
    * services                 视图逻辑
      * attack              attack管理
      * information   情报命中
      * log_query       情报查询
      * rule                 命中规则
      * threaten         威胁命中 
    * static                 静态文件
    * templates              html页面
        * base.html         
        * home.html
        * login.html
    * urls                   接口路由
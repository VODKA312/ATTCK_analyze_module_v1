### 白泽（WhitePondSecurityKG）

​ATT&CK知识图谱是一个通用的网络安全基础运营平台，命名为“白泽(平台英文名称为：White Pond Security Knowledage Graph, 简称WhitePondSecurityKG，缩写为WPSKG)”，计划满足日常网络安全综合分析、ATP监测、攻击溯源等场景需求，同时解决在大规模复杂环境场景下遇到的稳定性和性能问题，打造国内首个大型安全知识图谱。

      项目采用了Noe4J和Python Django结合架构，在知识抽取、数据聚合、标识建立、关系搭建、自然语言处理、模型预训练等技术，降低在分析过程的漏报与误报情况。目前集成了Red Team、kafka、netflow、log。

### 项目功能目录

* attack    根目录
  * attack		项目配置目录
  * webapp      项目主体目录
    * log_conf                日志上报
    * neo4j_conf            neo4j数据库交互
    * services                 视图逻辑
      * attack              attack管理
      * information           情报命中
      * log_query             情报查询
      * rule                 命中规则
      * threaten             威胁命中 
    * static                 静态文件
    * templates              html页面

### 环境要求

-  Linux or MacOS or Windows
-  安装 [neo4j-community](https://neo4j.com/download-center/#community)
- Python 3.9+ 

### 安装

##### 修改配置

编辑项目路径下的attack文件夹中setting.py配置文件，修改数据库配置为自己本地地址、用户名和密码：
``` Python
NEO4J_URL = "neo4j://localhost:7687"
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'cong18559116656.'
```
目前使用sqlite3数据库，具备原始数据，登录时默认用户名：admin， 密码：admin，若先使用mysql数据库，可修改setting.py中DATABASES配置项，并安装mysqlclient第三方扩展包。

##### 安装步骤：

```Bash
git clone 
cd attack
pip install -r requirements.txt
python manage.py runserver
```

完整步骤：首先克隆项目代码

```Bash
git clone 
```

创建虚拟环境并激活

注：这里的venv是你设置的虚拟环境名称。

```
python3 -m venv venv
. venv/bin/activate
```

接下来，安装依赖：

```Bash
cd attack
pip install -r requirements.txt
```
### 如何开启服务
```Bash
source venv/bin/activate
```

启动neo4j服务：
```Bash
sudo systemctl start neo4j
```
检查是否连接
```Bash
cypher-shell
```
username: neo4j
password: cong18559116656.

最后，启动服务器：

```Bash
python manage.py runserver
```

启动日志上报功能：

```Bash
cd attack/webapp/log_conf
python main.py
```

### 使用说明
#### 启动创建图谱功能
```Bash
python webapp/neo4j_conf/attack_manage/cretate_graph.py
```
#### neo4j网页版查询
http://localhost:7474 
#### 首页
首页： 数据的视图展示

#### ATT&CK管理
导入attack数据： att&ck管理 ——> 总览 ——> 批量导入(数据模板请参照[ATT&CK官网数据](http://attack.mitre.org/docs/enterprise-attack-v12.0/enterprise-attack-v12.0.xlsx)
。目前增加战术、技术、软件、缓解措施、战役、数据资源、组织的name和description的中文解释字段展示，需要下载模板后在末尾增加name_zh和description_zh两个字段，并在相应字段下填入内容，再进行导入即可。见如下示例：
![](/md_data/eg_template_import.png)

注意：导入数据时会删除neo4j中原有的数据，请谨慎操作！

数据编辑：attack相关的数据可在对应页新建，也可修改删除对应的单条数据，点击查看可查看到数据的其他详细信息（下同）。

关系管理：在attack管理下的关系管理页面可创建、修改、删除不同节点的关系。

#### 日志查询
在日志管理页面可根据条件查询想要的数据，可在单条日志处操作处置或忽略日志。

#### 命中规则
在命中规则管理页面可创建、删除规则及查询相应的规则。批量创建规则请选择批量导入（数据模板请参照项目webapp——>static——>data_template——>log2attckrule.xlsx）。

#### 威胁命中
在威胁命中管理页面查看命中数据，可通过条件查询得到相应的数据。

#### 情报命中
在情报命中管理页面查看命中数据，可通过条件查询得到相应的数据。

#### 导出
项目的table数据支持数据导出，可在不通页面导出需要的数据




# 省边界上的县查询方法

本文档说明如何使用 AreaCity-Query-Geometry 工具查询省边界上的县。

## 工具简介

AreaCity-Query-Geometry 是一个基于 JTS (Java Topology Suite) 库的地理边界查询工具，可以从省市区县乡镇边界数据中查找与任意点、线、面相交的矢量边界。

### 核心功能

- 查询一个坐标点对应的城市信息
- 查询一条路径经过的所有城市
- 查询一个矢量范围覆盖的所有城市
- 查询一个城市或下一级所有边界数据（WKT格式）
- 支持通过 HTTP API 服务进行查询调用
- 支持通过 Java 代码进行查询调用

## 查询省边界上的县的方法

### 方法一：通过 HTTP API 查询

对于以下省份：
- 内蒙古自治区
- 吉林省
- 湖北省
- 湖南省
- 广西壮族自治区
- 重庆市
- 四川省
- 贵州省
- 云南省
- 陕西省
- 甘肃省
- 青海省
- 宁夏回族自治区

可以通过以下步骤查询省边界上的县：

#### 步骤1：获取省边界WKT数据

```http
GET /queryGeometry?name=内蒙古自治区&deep=0
```

#### 步骤2：查询与省边界相交的县级行政区

```http
GET /queryGeometry?name=内蒙古自治区&deep=2
```

参数说明：
- `name`: 省份名称
- `deep`: 查询深度（0=省级，1=市级，2=县级，3=乡镇级）

### 方法二：通过 Java 代码查询

```java
import com.github.xiangyuecn.areacity.query.AreaCityQuery;

public class ProvinceBoundaryQuery {
    
    // 要查询的省份列表
    private static final String[] PROVINCES = {
        "内蒙古自治区",
        "吉林省",
        "湖北省",
        "湖南省",
        "广西壮族自治区",
        "重庆市",
        "四川省",
        "贵州省",
        "云南省",
        "陕西省",
        "甘肃省",
        "青海省",
        "宁夏回族自治区"
    };
    
    public static void main(String[] args) throws Exception {
        // 初始化查询器
        AreaCityQuery query = new AreaCityQuery();
        
        // 加载边界数据
        query.initFromFile("ok_geo.json");
        
        // 遍历每个省份，查询边界上的县
        for (String province : PROVINCES) {
            System.out.println("=== " + province + " 边界上的县 ===");
            
            // 获取省边界
            String provinceBoundary = query.getWKT(province);
            
            // 查询与省边界相交的所有县级行政区
            // 使用 QueryGeometry 方法，传入边界WKT和查询深度
            String[] counties = query.queryByGeometry(provinceBoundary, 2);
            
            for (String county : counties) {
                System.out.println(county);
            }
        }
    }
}
```

### 方法三：使用边界相交查询

更精确地查询位于省边界上的县，可以使用边界线相交查询：

```java
import org.locationtech.jts.geom.Geometry;
import org.locationtech.jts.io.WKTReader;

public class BorderCountyQuery {
    
    public static void queryBorderCounties(AreaCityQuery query, String provinceName) {
        // 获取省边界几何对象
        Geometry provinceGeometry = query.getGeometry(provinceName);
        
        // 获取省边界线（不是面积，而是边界线）
        Geometry provinceBoundary = provinceGeometry.getBoundary();
        
        // 查询所有与边界线相交的县级行政区
        // 这将只返回位于省边界上的县，而不是省内所有的县
        List<String> borderCounties = query.queryIntersects(provinceBoundary, 2);
        
        for (String county : borderCounties) {
            System.out.println(county);
        }
    }
}
```

## 数据源

边界数据来自 [AreaCity-JsSpider-StatsGov](https://github.com/xiangyuecn/AreaCity-JsSpider-StatsGov) 开源项目，该项目提供了中国省市区县乡镇完整的边界数据。

## 使用建议

1. **下载数据**: 首先从 AreaCity-JsSpider-StatsGov 下载 `ok_geo.json` 边界数据文件
2. **启动服务**: 运行 `start-server.bat`（Windows）或 `start-server.sh`（Linux/Mac）启动HTTP服务
3. **执行查询**: 使用 HTTP API 或 Java 代码进行查询

## 注意事项

- 内存占用低，性能优良（1秒可查1万个以上坐标）
- 源码简单，包括测试脚本共5个文件
- 支持 WKT 格式输出边界数据
- 可以自定义 geojson 边界数据文件

## 相关项目

- [AreaCity-JsSpider-StatsGov](https://github.com/xiangyuecn/AreaCity-JsSpider-StatsGov) - 省市区县乡镇边界数据
- [AreaCity-Query-Geometry](https://github.com/xiangyuecn/AreaCity-Query-Geometry) - 边界查询工具

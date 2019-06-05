> ## 代码结构说明

```c
test.py                     统计算法的主要逻辑
use_demo.py                 使用示例
```

> ## 使用说明

- ### test.py模块 deal函数说明

    ```python
    def deal(fileName, sizes):
      pass
  
    ```
    - 参数`fileName`: 数据集的路径文件路径
    - 参数`sizes`: 取样的数组，例如：[100, 200, 300, 400] => 表示分别对前100、前200、前300和前400个节点进行统计
    - 返回值: 包含对每个情况下，8种属性分别有多少个命中。返回结果的数据格式如下：
        ```json
        [
            {
                "information":21,
                "betweenness":24,
                "network":25,
                "degree":21,
                "lac":23,
                "subgragh":9,
                "closeness":17,
                "eigenvector":9,
                "size":100
            },
            {
                "information":49,
                "betweenness":53,
                "network":59,
                "degree":49,
                "lac":46,
                "subgragh":17,
                "closeness":36,
                "eigenvector":17,
                "size":200
            },
            {
                "information":77,
                "betweenness":83,
                "network":81,
                "degree":77,
                "lac":71,
                "subgragh":28,
                "closeness":53,
                "eigenvector":28,
                "size":300
            },
            {
                "information":106,
                "betweenness":108,
                "network":111,
                "degree":106,
                "lac":101,
                "subgragh":47,
                "closeness":74,
                "eigenvector":47,
                "size":400
            },
            {
                "information":136,
                "betweenness":142,
                "network":149,
                "degree":136,
                "lac":140,
                "subgragh":64,
                "closeness":89,
                "eigenvector":64,
                "size":500
            },
            {
                "information":171,
                "betweenness":167,
                "network":169,
                "degree":171,
                "lac":174,
                "subgragh":84,
                "closeness":100,
                "eigenvector":84,
                "size":600
            },
            {
                "information":194,
                "betweenness":199,
                "network":214,
                "degree":194,
                "lac":205,
                "subgragh":105,
                "closeness":125,
                "eigenvector":105,
                "size":700
            },
            {
                "information":217,
                "betweenness":218,
                "network":250,
                "degree":217,
                "lac":241,
                "subgragh":115,
                "closeness":151,
                "eigenvector":115,
                "size":800
            },
            {
                "information":247,
                "betweenness":250,
                "network":283,
                "degree":244,
                "lac":268,
                "subgragh":139,
                "closeness":173,
                "eigenvector":139,
                "size":900
            },
            {
                "information":278,
                "betweenness":274,
                "network":306,
                "degree":278,
                "lac":300,
                "subgragh":167,
                "closeness":196,
                "eigenvector":167,
                "size":1000
            }
        ]
        ```
    
- ### 使用示例
    ```python
    import test
    
    # 调用test模块提供的deal函数
    test.deal("./dip_all.txt", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    
    ```
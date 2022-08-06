# fairies

* 针对中文nlp任务中包含的噪音数据进行自动修正清洗(TODO)
- 利用算法合理划分训练集和验证集(TODO)
- txt,json,excel等文件的储存读取
* nlp常用工具

# 安装

pip install fairies

<!-- # 常用API -->

<!-- **label2id**
用于序列标注时标签和id相互转换  
**find_lcs**
查找公共子串  
**random_build_data**
按照比例切分数据集  
**removeLineFeed**
清洗数据中的去除换行 tab键  
**text_len_analysis**
分析数据中的文本长度  
**split_to_paragraph**
将文本切成句子  
**get_slide_window_text**
滑动窗口切割句子  
**find_co_occurrence_word**
通过统计词语的共现次数,寻找关键词  
**chs_2_cht**  
简体到繁体  
**strQ2B**
全角转半角  
**long_substr**
多个字符的公共子串   -->

# 更新

2022/8/6 使用orjson代替json作为json的读写
2022/4/29 新增write_csv 用于写入csv文件  
2021/12/23 新增random_split_data方法 用来快速划分数据集  
2021/11/26 整合read方法 优化读写速度
  



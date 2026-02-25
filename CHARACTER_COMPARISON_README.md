# 角色音对比展示功能说明

## 修改内容

根据用户要求，在 `index.html` 中重新设计了角色音对比展示功能，具体包括：

### 1. 功能模块调整
- **位置**: 用"2. 角色音对比展示"替换了原来的"2. 多播角色音生成"部分
- **功能**: 展示三个系统在三个角色音生成方面的对比

### 2. Prompt音频展示
展示三个角色的参考音频：
- **夏姝 Prompt**: `audios/duibai/prompt/xiashu.wav`
- **周奕 Prompt**: `audios/duibai/prompt/zhouyi.wav`
- **姜雪宁 Prompt**: `audios/duibai/prompt/jiangxuening.wav`

### 3. 三个角色对比展示
基于不同数据源，展示三个角色的音色对比：

#### 角色信息：
1. **夏姝（xiashu）** - 太平教道童，机灵活泼，对师兄充满好奇
   - 数据源: `audios/duibai/prompt/jcdt.json`
   - 音频文件: `audios/duibai/xiashu/`
   - 包含7个demo

2. **周奕（zhouyi）** - 太平教弟子，穿越者，聪明机智
   - 数据源: `audios/duibai/prompt/jcdt.json`
   - 音频文件: `audios/duibai/zhouyi/`
   - 包含5个demo

3. **姜雪宁（jiangxuening）** - 前皇后，性格强势，有威严
   - 数据源: `audios/duibai/prompt/kunning.json`
   - 音频文件: `audios/duibai/jiangxuening/`
   - 包含6个demo（已添加1003004）

#### 每个角色包含：
- **上文**: 从对应JSON文件中提取的对话上文
- **角色文本**: 角色说的完整内容
- **下文**: 从对应JSON文件中提取的对话下文
- **三个系统对比**（CosyVoice在前，Takin AudioLLM在中，MOSS-TTSD在后）:
  - CosyVoice: `{id}-cosyvoice.{wav|mp3}`
  - Takin AudioLLM: `{id}-context.{wav|mp3}`
  - MOSS-TTSD: `{id}-moss_ttsd.wav`

### 4. 技术实现
- **表格布局**: 使用HTML表格结构，分为3大块（3个角色），每块4列（文本、cosyvoice、takin、moss）
- **动态生成**: 使用JavaScript动态生成表格内容
- **音频播放**: 集成现有的音频占位框点击播放功能
- **响应式设计**: 支持移动端和桌面端的自适应显示
- **文件路径**: 自动匹配实际的文件名格式
- **显示顺序**: 角色排序 jiangxuening > zhouyi > xiashu，系统排序 cosyvoice > context > moss_ttsd
- **界面简洁**: 一目了然的表格设计，清晰的数据对比
- **紧凑布局**: 表格形式减少了空间占用，提高了信息密度
- **完整展示**: 展示目录中的所有音频文件（已修正上下文信息）
- **Prompt展示**: 每个角色的prompt音频显示在角色标题行中
- **三系统对比**: 支持CosyVoice、Takin AudioLLM、MOSS-TTSD三个系统的对比
- **视觉区分**: 不同系统使用不同的背景色进行视觉区分

### 5. 文件结构
```
audios/duibai/
├── prompt/
│   ├── jcdt.json          # 夏姝和周奕的上下文文本数据
│   ├── kunning.json       # 姜雪宁的上下文文本数据
│   ├── xiashu.wav         # 夏姝角色音参考音频
│   ├── zhouyi.wav         # 周奕角色音参考音频
│   └── jiangxuening.wav   # 姜雪宁角色音参考音频
├── xiashu/                # 夏姝角色音频文件
│   ├── 1000005-cosyvoice.wav
│   ├── 1000005-context.wav
│   ├── 1000005-moss_ttsd.wav
│   └── ...
├── zhouyi/                # 周奕角色音频文件
│   ├── 1000011-cosyvoice.wav
│   ├── 1000011-context.wav
│   ├── 1000011-moss_ttsd.wav
│   └── ...
└── jiangxuening/          # 姜雪宁角色音频文件
    ├── 1000067-cosyvoice.mp3
    ├── 1000067-context.mp3
    ├── 1000067-moss_ttsd.wav
    └── ...
```

## 表格结构说明

- **表头**: 文本内容 | 🎭 CosyVoice | 🎯 Takin | 🤖 MOSS
- **角色标题行**: 每个角色的名称、描述和Prompt音频（压缩到一行显示）
- **Demo行**: 每个demo的上下文文本和三个系统的音频对比
- **列宽分配**: 文本列50%，系统列各16.67%
- **视觉区分**: 
  - 姜雪宁角色：浅灰色背景 + 红色左边框
  - 周奕角色：浅蓝色背景 + 蓝色左边框
  - 夏姝角色：浅绿色背景 + 绿色左边框
- **表格增强**: 更明显的边框、阴影和渐变效果
- **紧凑设计**: 压缩的文本显示空间，更小的字体和行距

## 使用方法

1. 启动本地服务器：
   ```bash
   cd /pai/user/code/takin-demo-page
   python3 -m http.server 8080
   ```

2. 在浏览器中访问：`http://localhost:8080`

3. 滚动到"2. 角色音对比展示"部分

4. 在表格中点击音频占位框播放对应的音频文件

5. 每个角色的Prompt音频显示在角色标题行中

## 界面特点

- **表格布局**: 使用HTML表格结构，信息组织清晰有序
- **简洁明了**: 移除了冗余的角色列，每个角色独立展示，上下文信息清晰
- **对比直观**: 三个系统并排显示，便于对比
- **视觉区分**: 每个角色使用统一的背景色和彩色边框，易于识别
- **紧凑设计**: 角色介绍和Prompt音频压缩到一行，文本显示空间进一步压缩
- **增强视觉效果**: 更明显的表格边框、阴影和渐变效果
- **优化空间利用**: 减小字体大小、行距和内边距，提高信息密度
- **响应式设计**: 支持移动端和桌面端的自适应显示
- **响应式设计**: 适配不同屏幕尺寸
- **交互友好**: 点击播放，操作简单

## 注意事项

- 音频文件包含中文字符，在URL中会自动进行编码
- 姜雪宁角色的音频文件为MP3格式，其他角色为WAV格式
- 页面保持了原有的响应式设计和交互体验
- 音频播放功能与现有页面完全兼容

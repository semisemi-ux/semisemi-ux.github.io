# 角色音对比展示功能说明

## 修改内容

根据用户要求，在 `index.html` 中重新设计了角色音对比展示功能，具体包括：

### 1. 功能模块调整
- **位置**: 用"2. 角色音对比展示"替换了原来的"2. 多播角色音生成"部分
- **功能**: 展示三个系统在三个角色音生成方面的对比

### 2. Prompt音频展示
- **文件**: `audios/duibai/prompt/xiashu.wav`
- **角色**: 夏姝（女-少年）
- **描述**: 太平教道童，机灵活泼，对师兄充满好奇
- **功能**: 作为角色音参考音频展示

### 3. 角色音对比展示
基于 `audios/duibai/prompt/jcdt.json` 中的上下文文本，动态生成7个角色音对比demo：

#### 包含的音频文件：
1. **1000005-师父的符水** - "师父的符水真灵验，五日前师兄还是个活死人，现已生龙活虎。"
2. **1000014-是** - "是。"
3. **1000016-但通天神姥** - "但通天神姥乃是合一派前辈高人，你用灵媒婆子称呼太过不敬。再者师兄乃是中毒，自然是符水解了毒。"
4. **1000019-大病初愈后** - "大病初愈后，师兄变化好大，最近伤春悲秋，总发诗兴。"
5. **1000024-这是有心事** - "这是有心事？"
6. **1000026-方才师兄所** - "方才师兄所念，可是新作？"
7. **1000037-是。** - "是。"

#### 每个demo包含：
- **上文**: 从jcdt.json中提取的对话上文
- **角色信息**: 夏姝（女-少年）
- **完整文本**: 角色说的完整内容
- **下文**: 从jcdt.json中提取的对话下文
- **三个音频对比**（CosyVoice在前，Takin AudioLLM在中，MOSS-TTSD在后）:
  - CosyVoice: `{id}-{text}-cosyvoice.wav`
  - Takin AudioLLM (Context): `{id}-{text}-context.wav`
  - MOSS-TTSD: `{id}-moss_ttsd.wav`

### 4. 技术实现
- **动态生成**: 使用JavaScript动态生成对比内容
- **音频播放**: 集成现有的音频占位框点击播放功能
- **响应式设计**: 保持与现有页面风格一致
- **文件路径**: 自动匹配实际的文件名格式
- **显示顺序**: CosyVoice在前，Takin AudioLLM在中，MOSS-TTSD在后
- **上下文完整**: 每个demo显示上文、文本、下文三个部分，上下文文本已修正
- **界面简洁**: 移除了音频文件位置显示
- **三系统对比**: 支持CosyVoice、Takin AudioLLM、MOSS-TTSD三个系统的对比

### 5. 文件结构
```
audios/duibai/
├── prompt/
│   ├── jcdt.json          # 上下文文本数据
│   └── xiashu.wav         # 角色音参考音频
├── 1000005-师父的符水-context.wav
├── 1000005-师父的符水-cosyvoice.wav
├── 1000014-是-cosyvoice.wav
├── 1000014-是。-context.wav
├── 1000016-但通天神姥-context.wav
├── 1000016-但通天神姥-cosyvoice.wav
├── 1000019-大病初愈后-context.wav
├── 1000019-大病初愈后-cosyvoice.wav
├── 1000024-这是有心事-context.wav
├── 1000024-这是有心事-cosyvoice.wav
├── 1000026-方才师兄所-context.wav
├── 1000026-方才师兄所-cosyvoice.wav
├── 1000037-是。-context.wav
├── 1000037-是。-cosyvoice.wav
├── 1000005-moss_ttsd.wav
├── 1000014-moss_ttsd.wav
├── 1000016-moss_ttsd.wav
├── 1000019-moss_ttsd.wav
├── 1000024-moss_ttsd.wav
├── 1000026-moss_ttsd.wav
└── 1000037-moss_ttsd.wav
```

## 使用方法

1. 启动本地服务器：
   ```bash
   cd /pai/user/code/takin-demo-page
   python3 -m http.server 8080
   ```

2. 在浏览器中访问：`http://localhost:8080`

3. 滚动到"2. 角色音对比展示"部分

4. 点击音频占位框播放对应的音频文件

## 注意事项

- 音频文件包含中文字符，在URL中会自动进行编码
- 所有音频文件都是WAV格式
- 页面保持了原有的响应式设计和交互体验
- 音频播放功能与现有页面完全兼容

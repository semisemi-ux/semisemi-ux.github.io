# Takin AudioLLM 音频文件配置说明

## 目录结构

请将以下音频文件放置到对应的目录中：

```
audios/
├── audiobook/           # 长篇章旁白生成
├── multi_voice/         # 多播角色音生成
├── emotion_control/     # 多播角色音控制
└── audiobook_production/ # 有声书制作生成
```

## 音频文件配置

### 1. 长篇章旁白生成 (audios/audiobook/)

**目录**: `audios/audiobook/`

**需要的音频文件**:
- `takin_narration.mp3` - Takin AudioLLM 旁白示例
  - 原文件位置: `old/audios/audiobook/我的阿勒泰.mp3`
  - 描述: Takin 系统的长篇旁白内容

- `cosyvoice_narration.mp3` - CosyVoice 旁白示例
  - 描述: CosyVoice 系统的长篇旁白内容对比

- `moss_ttsd_narration.mp3` - MOSS-TTSD 旁白示例
  - 描述: MOSS-TTSD 系统的长篇旁白内容对比

### 2. 多播角色音生成 (audios/multi_voice/)

**目录**: `audios/multi_voice/`

**需要的音频文件**:
- `takin_female.mp3` - Takin 女性角色
  - 原文件位置: `old/audios/duobo_yinxiao/TTS-后期-绸缎 (1).mp3`
  - 描述: Takin 系统女性角色语音特征

- `takin_male.mp3` - Takin 男性角色
  - 原文件位置: `old/audios/duobo_yinxiao/TTS 30s-5 (1).mp3`
  - 描述: Takin 系统男性角色语音特征

- `cosyvoice_female.mp3` - CosyVoice 女性角色
  - 描述: CosyVoice 系统女性角色语音特征对比

- `cosyvoice_male.mp3` - CosyVoice 男性角色
  - 描述: CosyVoice 系统男性角色语音特征对比

- `moss_female.mp3` - MOSS-TTSD 女性角色
  - 描述: MOSS-TTSD 系统女性角色语音特征对比

- `moss_male.mp3` - MOSS-TTSD 男性角色
  - 描述: MOSS-TTSD 系统男性角色语音特征对比

### 3. 多播角色音控制 (audios/emotion_control/)

**目录**: `audios/emotion_control/`

**需要的音频文件**:

#### 开心情绪对比
- `takin_happy.mp3` - Takin 开心情绪
  - 原文件位置: `old/audios/csft/xiaoyi-demo1.mp3`
  - 描述: Takin 系统开心情绪控制

- `cosyvoice_happy.mp3` - CosyVoice 开心情绪
  - 描述: CosyVoice 系统开心情绪控制对比

- `moss_happy.mp3` - MOSS-TTSD 开心情绪
  - 描述: MOSS-TTSD 系统开心情绪控制对比

#### 愤怒情绪对比
- `takin_angry.mp3` - Takin 愤怒情绪
  - 原文件位置: `old/audios/csft/anger-demo1.mp3`
  - 描述: Takin 系统愤怒情绪控制

- `cosyvoice_angry.mp3` - CosyVoice 愤怒情绪
  - 描述: CosyVoice 系统愤怒情绪控制对比

- `moss_angry.mp3` - MOSS-TTSD 愤怒情绪
  - 描述: MOSS-TTSD 系统愤怒情绪控制对比

#### 悲伤情绪对比
- `takin_sad.mp3` - Takin 悲伤情绪
  - 原文件位置: `old/audios/csft/kuqiang-demo1.mp3`
  - 描述: Takin 系统悲伤情绪控制

- `cosyvoice_sad.mp3` - CosyVoice 悲伤情绪
  - 描述: CosyVoice 系统悲伤情绪控制对比

- `moss_sad.mp3` - MOSS-TTSD 悲伤情绪
  - 描述: MOSS-TTSD 系统悲伤情绪控制对比

### 4. 有声书制作生成 (audios/audiobook_production/)

**目录**: `audios/audiobook_production/`

**需要的音频文件**:

#### 悬疑风格对比
- `takin_mystery.mp3` - Takin 悬疑风格
  - 原文件位置: `old/audios/danbo_duofengge/悬疑_喜千辉.mp3`
  - 描述: Takin 系统悬疑风格有声书制作

- `cosyvoice_mystery.mp3` - CosyVoice 悬疑风格
  - 描述: CosyVoice 系统悬疑风格有声书制作对比

- `moss_mystery.mp3` - MOSS-TTSD 悬疑风格
  - 描述: MOSS-TTSD 系统悬疑风格有声书制作对比

#### 睡眠故事对比
- `takin_sleep.mp3` - Takin 睡眠故事
  - 原文件位置: `old/audios/danbo_duofengge/1-1睡眠之夜v1.3版本.mp3`
  - 描述: Takin 系统睡眠故事有声书制作

- `cosyvoice_sleep.mp3` - CosyVoice 睡眠故事
  - 描述: CosyVoice 系统睡眠故事有声书制作对比

- `moss_sleep.mp3` - MOSS-TTSD 睡眠故事
  - 描述: MOSS-TTSD 系统睡眠故事有声书制作对比

## 快速设置命令

```bash
# 创建目录结构
mkdir -p audios/{audiobook,multi_voice,emotion_control,audiobook_production}

# 复制 Takin 音频文件（从old目录）
cp "old/audios/audiobook/我的阿勒泰.mp3" "audios/audiobook/takin_narration.mp3"
cp "old/audios/duobo_yinxiao/TTS-后期-绸缎 (1).mp3" "audios/multi_voice/takin_female.mp3"
cp "old/audios/duobo_yinxiao/TTS 30s-5 (1).mp3" "audios/multi_voice/takin_male.mp3"
cp "old/audios/csft/xiaoyi-demo1.mp3" "audios/emotion_control/takin_happy.mp3"
cp "old/audios/csft/anger-demo1.mp3" "audios/emotion_control/takin_angry.mp3"
cp "old/audios/csft/kuqiang-demo1.mp3" "audios/emotion_control/takin_sad.mp3"
cp "old/audios/danbo_duofengge/悬疑_喜千辉.mp3" "audios/audiobook_production/takin_mystery.mp3"
cp "old/audios/danbo_duofengge/1-1睡眠之夜v1.3版本.mp3" "audios/audiobook_production/takin_sleep.mp3"

# 注意：CosyVoice 和 MOSS-TTSD 的音频文件需要您自己准备
# 请将对应的音频文件放置到相应的目录中
```

## 系统对比说明

### 对比系统
1. **Takin AudioLLM** - 我们的系统（蓝色标识）
2. **CosyVoice** - 对比系统1（绿色标识）
3. **MOSS-TTSD** - 对比系统2（红色标识）

### 对比维度
- **音质质量**：清晰度、自然度
- **情感表达**：情感控制的准确性
- **语音多样性**：不同角色的区分度
- **风格适应性**：不同场景的适应性

## 音频文件要求

- **格式**: MP3 或 WAV
- **质量**: 建议 44.1kHz, 16-bit 或更高
- **时长**: 建议 10-60 秒
- **大小**: 建议单个文件不超过 5MB
- **命名规范**: 系统名_功能_类型.mp3

## 注意事项

1. 所有音频文件都设置了 `preload="none"`，只有在用户点击播放时才会加载
2. 如果音频文件不存在，页面会显示占位框
3. 建议使用压缩后的音频文件以提升加载速度
4. 原音频文件已备份到 `old/audios/` 目录中
5. CosyVoice 和 MOSS-TTSD 的音频文件需要您自己准备

## 文件统计

- **总音频文件数**: 21个（每个系统7个文件）
- **Takin 系统**: 7个文件（从原文件复制）
- **CosyVoice 系统**: 7个文件（需要准备）
- **MOSS-TTSD 系统**: 7个文件（需要准备）
- **预计总大小**: < 50MB（所有系统）

## 页面功能

- **对比展示**: 三个系统并排对比
- **按需加载**: 点击占位框才加载音频
- **响应式设计**: 适配不同屏幕尺寸
- **交互友好**: 清晰的视觉标识和操作提示